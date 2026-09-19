"""Endpoints de PCASP/lançamentos/conciliação (DOM-CON)."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.modules.sigmun_con.application.interfaces import (
    RepositorioConciliacao,
    RepositorioContaContabil,
    RepositorioLancamento,
)
from src.modules.sigmun_con.application.use_cases_contabil import (
    ConciliarContaUseCase,
    ConciliarInput,
    CriarContaInput,
    CriarContaUseCase,
    LancarContabilUseCase,
    LancarInput,
    PartidaInput,
)
from src.modules.sigmun_con.domain.exceptions import DomConDomainError
from src.modules.sigmun_con.presentation.schemas.con_schemas import (
    ConciliacaoCreateRequest,
    ConciliacaoResponse,
    ContaCreateRequest,
    ContaResponse,
    LancamentoCreateRequest,
    LancamentoResponse,
)

from .base import (
    get_conciliacao_repo,
    get_conta_repo,
    get_lancamento_repo,
)

router = APIRouter(prefix="/api/v1/con", tags=["Contabilidade Pública"])


@router.post("/contas", status_code=201)
def criar_conta(payload: ContaCreateRequest,
                repo: Annotated[RepositorioContaContabil, Depends(get_conta_repo)]):
    """Cria conta PCASP."""
    try:
        conta = CriarContaUseCase(repo).execute(
            CriarContaInput(codigo=payload.codigo, nome=payload.nome,
                            classe=payload.classe, tipo=payload.tipo,
                            natureza=payload.natureza,
                            autor_id=payload.created_by))
    except DomConDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return ContaResponse(id=conta.id, codigo=conta.codigo, nome=conta.nome,
                         tipo=conta.tipo, created_at=conta.created_at)


@router.post("/lancamentos", status_code=201)
def lancar(payload: LancamentoCreateRequest,
           lancs: Annotated[RepositorioLancamento, Depends(get_lancamento_repo)],
           contas: Annotated[RepositorioContaContabil, Depends(get_conta_repo)]):
    """Registra lançamento por partidas dobradas."""
    try:
        lanc = LancarContabilUseCase(lancs, contas).execute(
            LancarInput(exercicio=payload.exercicio, historico=payload.historico,
                        partidas=[PartidaInput(conta_id=p.conta_id,
                                               codigo_conta=p.codigo_conta,
                                               tipo=p.tipo, valor=p.valor)
                                  for p in payload.partidas],
                        origem=payload.origem, origem_id=payload.origem_id,
                        autor_id=payload.created_by))
    except DomConDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return LancamentoResponse(id=lanc.id, exercicio=lanc.exercicio,
                              historico=lanc.historico,
                              total_debito=lanc.total_debito,
                              total_credito=lanc.total_credito,
                              status=lanc.status.value)


@router.post("/conciliacoes", status_code=201)
def conciliar(payload: ConciliacaoCreateRequest,
              repo: Annotated[RepositorioConciliacao, Depends(get_conciliacao_repo)]):
    """Concilia conta (saldo contábil × extrato)."""
    try:
        conc = ConciliarContaUseCase(repo).execute(
            ConciliarInput(conta_id=payload.conta_id,
                           codigo_conta=payload.codigo_conta, ano=payload.ano,
                           mes=payload.mes, saldo_contabil=payload.saldo_contabil,
                           saldo_extrato=payload.saldo_extrato,
                           autor_id=payload.created_by),
            payload.justificativa)
    except DomConDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return ConciliacaoResponse(id=conc.id, conta_id=conc.conta_id,
                               competencia_ano=conc.competencia_ano,
                               competencia_mes=conc.competencia_mes,
                               saldo_contabil=conc.saldo_contabil,
                               saldo_extrato=conc.saldo_extrato,
                               diferenca=conc.diferenca,
                               status=conc.status.value)


__all__ = ["router"]
