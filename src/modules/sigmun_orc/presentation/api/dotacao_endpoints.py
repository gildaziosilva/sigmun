"""Endpoints de dotação e reserva (DOM-ORC)."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.modules.sigmun_orc.application.interfaces import (
    RepositorioDotacao,
    RepositorioLOA,
    RepositorioReserva,
)
from src.modules.sigmun_orc.application.use_cases_dotacao import (
    AnularDotacaoUseCase,
    CancelarReservaUseCase,
    CriarDotacaoInput,
    CriarDotacaoUseCase,
    ReservarSaldoInput,
    ReservarSaldoUseCase,
    SuplementarDotacaoUseCase,
)
from src.modules.sigmun_orc.domain.exceptions import DomOrcDomainError
from src.modules.sigmun_orc.presentation.schemas.orc_schemas import (
    DotacaoCreateRequest,
    DotacaoResponse,
    DotacaoValorRequest,
    ReservaCreateRequest,
    ReservaResponse,
)

from .base import get_dotacao_repo, get_loa_repo, get_reserva_repo

router = APIRouter(prefix="/api/v1/orc", tags=["Orçamento Público"])


def _to_dotacao(dot) -> DotacaoResponse:  # type: ignore[no-untyped-def]
    return DotacaoResponse(id=dot.id, exercicio=dot.exercicio, codigo=dot.codigo,
                           valor_inicial=dot.valor_inicial,
                           valor_atualizado=dot.valor_atualizado,
                           saldo_disponivel=dot.saldo_disponivel,
                           status=dot.status.value, created_at=dot.created_at)


@router.post("/dotacoes", status_code=201)
def criar_dotacao(payload: DotacaoCreateRequest,
                  dots: Annotated[RepositorioDotacao, Depends(get_dotacao_repo)],
                  loas: Annotated[RepositorioLOA, Depends(get_loa_repo)]):
    """Cria dotação vinculada à LOA."""
    try:
        dot = CriarDotacaoUseCase(dots, loas).execute(
            CriarDotacaoInput(loa_id=payload.loa_id, exercicio=payload.exercicio,
                              codigo=payload.codigo,
                              valor_inicial=payload.valor_inicial,
                              unidade_orcamentaria=payload.unidade_orcamentaria,
                              natureza_despesa=payload.natureza_despesa,
                              fonte_recursos=payload.fonte_recursos,
                              autor_id=payload.created_by))
    except DomOrcDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_dotacao(dot)


@router.post("/dotacoes/{dotacao_id}/suplementar")
def suplementar(dotacao_id: str, payload: DotacaoValorRequest,
                repo: Annotated[RepositorioDotacao, Depends(get_dotacao_repo)]):
    """Suplementa dotação ativa."""
    try:
        dot = SuplementarDotacaoUseCase(repo).execute(dotacao_id, payload.valor)
    except DomOrcDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_dotacao(dot)


@router.post("/dotacoes/{dotacao_id}/anular")
def anular(dotacao_id: str, payload: DotacaoValorRequest,
           repo: Annotated[RepositorioDotacao, Depends(get_dotacao_repo)]):
    """Anula parcialmente dotação ativa."""
    try:
        dot = AnularDotacaoUseCase(repo).execute(dotacao_id, payload.valor)
    except DomOrcDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_dotacao(dot)


@router.get("/dotacoes/{dotacao_id}/saldo")
def saldo(dotacao_id: str, repo: Annotated[RepositorioDotacao, Depends(get_dotacao_repo)]):
    """Consulta saldo disponível da dotação."""
    dot = repo.get_by_id(dotacao_id)
    if dot is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Dotação não encontrada")
    return {"dotacao_id": dot.id, "valor_atualizado": dot.valor_atualizado,
            "saldo_disponivel": dot.saldo_disponivel}


@router.post("/reservas", status_code=201)
def reservar(payload: ReservaCreateRequest,
             res: Annotated[RepositorioReserva, Depends(get_reserva_repo)],
             dots: Annotated[RepositorioDotacao, Depends(get_dotacao_repo)]):
    """Reserva saldo da dotação."""
    try:
        r = ReservarSaldoUseCase(res, dots).execute(
            ReservarSaldoInput(dotacao_id=payload.dotacao_id, valor=payload.valor,
                               finalidade=payload.finalidade, numero=payload.numero,
                               autor_id=payload.created_by))
    except DomOrcDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return ReservaResponse(id=r.id, dotacao_id=r.dotacao_id, valor=r.valor,
                           status=r.status.value, created_at=r.created_at)


@router.post("/reservas/{reserva_id}/cancelar")
def cancelar_reserva(reserva_id: str,
                     res: Annotated[RepositorioReserva, Depends(get_reserva_repo)],
                     dots: Annotated[RepositorioDotacao, Depends(get_dotacao_repo)]):
    """Cancela reserva ativa (devolve saldo)."""
    try:
        r = CancelarReservaUseCase(res, dots).execute(reserva_id)
    except DomOrcDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return ReservaResponse(id=r.id, dotacao_id=r.dotacao_id, valor=r.valor,
                           status=r.status.value, created_at=r.created_at)


__all__ = ["router"]
