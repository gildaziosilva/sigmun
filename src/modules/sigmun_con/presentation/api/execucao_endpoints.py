"""Endpoints de empenho/liquidação/pagamento (DOM-CON)."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.modules.sigmun_con.application.interfaces import (
    RepositorioEmpenho,
    RepositorioLiquidacao,
    RepositorioPagamento,
)
from src.modules.sigmun_con.application.use_cases_execucao import (
    AnularEmpenhoUseCase,
    EmitirEmpenhoInput,
    EmitirEmpenhoUseCase,
    LiquidarEmpenhoUseCase,
    PagarLiquidacaoUseCase,
)
from src.modules.sigmun_con.domain.exceptions import DomConDomainError
from src.modules.sigmun_con.presentation.schemas.con_schemas import (
    EmpenhoCreateRequest,
    EmpenhoResponse,
    EmpenhoValorRequest,
    LiquidacaoResponse,
    PagamentoCreateRequest,
    PagamentoResponse,
)
from src.modules.sigmun_orc.application.interfaces import RepositorioDotacao
from src.modules.sigmun_orc.domain.exceptions import DomOrcDomainError

from .base import (
    get_dotacao_repo_con,
    get_empenho_repo,
    get_liquidacao_repo,
    get_pagamento_repo,
)

router = APIRouter(prefix="/api/v1/con", tags=["Contabilidade Pública"])


def _to_empenho(emp) -> EmpenhoResponse:  # type: ignore[no-untyped-def]
    return EmpenhoResponse(id=emp.id, exercicio=emp.exercicio, numero=emp.numero,
                           valor_empenhado=emp.valor_empenhado,
                           valor_liquidado=emp.valor_liquidado,
                           valor_pago=emp.valor_pago,
                           status=emp.status.value, created_at=emp.created_at)


@router.post("/empenhos", status_code=201)
def emitir_empenho(payload: EmpenhoCreateRequest,
                   emps: Annotated[RepositorioEmpenho, Depends(get_empenho_repo)],
                   dots: Annotated[RepositorioDotacao, Depends(get_dotacao_repo_con)]):
    """Emite empenho com baixa no saldo da dotação."""
    dot = dots.get_by_id(payload.dotacao_id)
    if dot is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Dotação não encontrada")
    try:
        emp = EmitirEmpenhoUseCase(emps).execute(
            EmitirEmpenhoInput(exercicio=payload.exercicio, numero=payload.numero,
                               valor=payload.valor,
                               favorecido_nome=payload.favorecido_nome,
                               descricao=payload.descricao, tipo=payload.tipo,
                               autor_id=payload.created_by), dot)
        dots.save(dot)
    except (DomConDomainError, DomOrcDomainError) as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_empenho(emp)


@router.post("/empenhos/{empenho_id}/liquidar")
def liquidar(empenho_id: str, payload: EmpenhoValorRequest,
             emps: Annotated[RepositorioEmpenho, Depends(get_empenho_repo)],
             liqs: Annotated[RepositorioLiquidacao, Depends(get_liquidacao_repo)]):
    """Registra liquidação do empenho."""
    try:
        liq = LiquidarEmpenhoUseCase(emps, liqs).execute(
            empenho_id, payload.valor, payload.documento)
    except DomConDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return LiquidacaoResponse(id=liq.id, empenho_id=liq.empenho_id, valor=liq.valor,
                              status=liq.status.value, created_at=liq.created_at)


@router.post("/empenhos/{empenho_id}/anular")
def anular_empenho(empenho_id: str, payload: EmpenhoValorRequest,
                   emps: Annotated[RepositorioEmpenho, Depends(get_empenho_repo)],
                   dots: Annotated[RepositorioDotacao, Depends(get_dotacao_repo_con)]):
    """Anula parcial/total do empenho (devolve saldo)."""
    emp = emps.get_by_id(empenho_id)
    if emp is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Empenho não encontrado")
    dot = dots.get_by_id(emp.dotacao_id)
    if dot is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Dotação não encontrada")
    try:
        emp2 = AnularEmpenhoUseCase(emps).execute(empenho_id, payload.valor, dot)
        dots.save(dot)
    except (DomConDomainError, DomOrcDomainError) as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_empenho(emp2)


@router.post("/pagamentos", status_code=201)
def pagar(payload: PagamentoCreateRequest,
          emps: Annotated[RepositorioEmpenho, Depends(get_empenho_repo)],
          liqs: Annotated[RepositorioLiquidacao, Depends(get_liquidacao_repo)],
          pags: Annotated[RepositorioPagamento, Depends(get_pagamento_repo)]):
    """Registra pagamento de liquidação confirmada."""
    try:
        pag = PagarLiquidacaoUseCase(emps, liqs, pags).execute(
            payload.liquidacao_id, payload.valor, payload.conta_bancaria,
            payload.created_by)
    except DomConDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return PagamentoResponse(id=pag.id, liquidacao_id=pag.liquidacao_id,
                             empenho_id=pag.empenho_id, valor=pag.valor,
                             status=pag.status.value, created_at=pag.created_at)


__all__ = ["router"]
