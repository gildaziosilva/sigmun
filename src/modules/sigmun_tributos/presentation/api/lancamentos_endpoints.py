"""Endpoints de lançamentos de créditos tributários (DOM-TRI)."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_tributos.application.interfaces import (
    RepositorioContribuinte,
    RepositorioImovel,
    RepositorioLancamento,
)
from src.modules.sigmun_tributos.application.use_cases import (
    LancarTributoInput,
    LancarTributoUseCase,
    PagarLancamentoUseCase,
)
from src.modules.sigmun_tributos.domain.exceptions import (
    ContribuinteNaoEncontradoError,
    DomTriDomainError,
    ImovelNaoEncontradoError,
    LancamentoNaoEncontradoError,
)
from src.modules.sigmun_tributos.infrastructure.repositories.sqlalchemy_contribuinte_repository import (
    SQLAlchemyContribuinteRepository,
)
from src.modules.sigmun_tributos.infrastructure.repositories.sqlalchemy_imovel_repository import (
    SQLAlchemyImovelRepository,
)
from src.modules.sigmun_tributos.infrastructure.repositories.sqlalchemy_lancamento_repository import (
    SQLAlchemyLancamentoRepository,
)
from src.modules.sigmun_tributos.presentation.schemas.tri_schemas import (
    LancamentoCreateRequest,
    LancamentoResponse,
    PagarLancamentoRequest,
)

router = APIRouter(prefix="/api/v1/tri", tags=["Administracao Tributaria"])


def get_lancamento_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioLancamento:
    """Fabrica de repositório de lançamentos."""
    return SQLAlchemyLancamentoRepository(session)


def get_contribuinte_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioContribuinte:
    """Fabrica de repositório de contribuintes."""
    return SQLAlchemyContribuinteRepository(session)


def get_imovel_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioImovel:
    """Fabrica de repositório de imóveis."""
    return SQLAlchemyImovelRepository(session)


def _to_lancamento(lancamento) -> LancamentoResponse:
    return LancamentoResponse(
        id=lancamento.id, contribuinte_id=lancamento.contribuinte_id,
        imovel_id=lancamento.imovel_id, tipo_tributo=lancamento.tipo_tributo.value,
        exercicio=lancamento.exercicio, numero_lancamento=lancamento.numero_lancamento,
        descricao=lancamento.descricao, base_calculo=lancamento.base_calculo,
        aliquota=lancamento.aliquota, valor_tributo=lancamento.valor_tributo,
        juros=lancamento.juros, multa=lancamento.multa,
        valor_total=lancamento.valor_total, data_vencimento=lancamento.data_vencimento,
        status=lancamento.status.value, data_pagamento=lancamento.data_pagamento,
        created_at=lancamento.created_at,
    )


@router.post("/lancamentos", status_code=201)
def lancar_tributo(
    payload: LancamentoCreateRequest,
    repo: Annotated[RepositorioLancamento, Depends(get_lancamento_repo)],
    contribuintes: Annotated[RepositorioContribuinte, Depends(get_contribuinte_repo)],
    imoveis: Annotated[RepositorioImovel, Depends(get_imovel_repo)],
):
    """Constitui um crédito tributário (IPTU/ISSQN/ITBI/Taxa)."""
    try:
        lance = LancarTributoUseCase(repo, contribuintes, imoveis).execute(
            LancarTributoInput(
                contribuinte_id=payload.contribuinte_id,
                tipo_tributo=payload.tipo_tributo,
                exercicio=payload.exercicio,
                base_calculo=payload.base_calculo,
                aliquota=payload.aliquota,
                imovel_id=payload.imovel_id,
                descricao=payload.descricao,
                juros=payload.juros, multa=payload.multa,
                data_vencimento=payload.data_vencimento,
                autor_id=payload.created_by,
            )
        )
    except (ContribuinteNaoEncontradoError, ImovelNaoEncontradoError) as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomTriDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_lancamento(lance)


@router.get("/lancamentos")
def listar_lancamentos(
    repo: Annotated[RepositorioLancamento, Depends(get_lancamento_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    """Lista lançamentos paginados."""
    itens = repo.list_all(page=page, page_size=page_size)
    return [_to_lancamento(l) for l in itens]


@router.get("/lancamentos/{lancamento_id}")
def obter_lancamento(
    lancamento_id: str,
    repo: Annotated[RepositorioLancamento, Depends(get_lancamento_repo)],
):
    """Obtém um lançamento por id."""
    lance = repo.get_by_id(lancamento_id)
    if lance is None:
        raise HTTPException(status_code=404, detail="Lançamento não encontrado")
    return _to_lancamento(lance)


@router.post("/lancamentos/{lancamento_id}/pagar")
def pagar_lancamento(
    lancamento_id: str,
    payload: PagarLancamentoRequest,
    repo: Annotated[RepositorioLancamento, Depends(get_lancamento_repo)],
):
    """Quita integralmente um lançamento."""
    try:
        lance = PagarLancamentoUseCase(repo).execute(
            lancamento_id, payload.data_pagamento
        )
    except LancamentoNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomTriDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_lancamento(lance)


__all__ = ["router"]