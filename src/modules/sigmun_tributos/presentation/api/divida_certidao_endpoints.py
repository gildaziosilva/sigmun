"""Endpoints de dívida ativa e certidões (DOM-TRI)."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_tributos.application.interfaces import (
    RepositorioCertidao,
    RepositorioContribuinte,
    RepositorioDividaAtiva,
    RepositorioLancamento,
)
from src.modules.sigmun_tributos.application.use_cases import (
    BaixarDividaAtivaUseCase,
    EmitirCertidaoUseCase,
    InscreverDividaAtivaUseCase,
)
from src.modules.sigmun_tributos.domain.exceptions import (
    ContribuinteNaoEncontradoError,
    DividaAtivaNaoEncontradaError,
    DomTriDomainError,
    LancamentoNaoEncontradoError,
)
from src.modules.sigmun_tributos.infrastructure.repositories.sqlalchemy_certidao_repository import (
    SQLAlchemyCertidaoRepository,
)
from src.modules.sigmun_tributos.infrastructure.repositories.sqlalchemy_contribuinte_repository import (
    SQLAlchemyContribuinteRepository,
)
from src.modules.sigmun_tributos.infrastructure.repositories.sqlalchemy_divida_ativa_repository import (
    SQLAlchemyDividaAtivaRepository,
)
from src.modules.sigmun_tributos.infrastructure.repositories.sqlalchemy_lancamento_repository import (
    SQLAlchemyLancamentoRepository,
)
from src.modules.sigmun_tributos.presentation.schemas.tri_schemas import (
    CertidaoResponse,
    DividaAtivaResponse,
)

router = APIRouter(prefix="/api/v1/tri", tags=["Administracao Tributaria"])


def get_divida_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioDividaAtiva:
    """Fabrica de repositório de dívida ativa."""
    return SQLAlchemyDividaAtivaRepository(session)


def get_lancamento_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioLancamento:
    """Fabrica de repositório de lançamentos."""
    return SQLAlchemyLancamentoRepository(session)


def get_certidao_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioCertidao:
    """Fabrica de repositório de certidões."""
    return SQLAlchemyCertidaoRepository(session)


def get_contribuinte_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioContribuinte:
    """Fabrica de repositório de contribuintes."""
    return SQLAlchemyContribuinteRepository(session)


def _to_divida(inscricao) -> DividaAtivaResponse:
    return DividaAtivaResponse(
        id=inscricao.id, lancamento_id=inscricao.lancamento_id,
        numero_inscricao=inscricao.numero_inscricao,
        data_inscricao=inscricao.data_inscricao,
        valor_original=inscricao.valor_original,
        valor_atualizado=inscricao.valor_atualizado,
        status=inscricao.status.value, created_at=inscricao.created_at,
    )


def _to_certidao(certidao) -> CertidaoResponse:
    return CertidaoResponse(
        id=certidao.id, contribuinte_id=certidao.contribuinte_id,
        tipo=certidao.tipo.value, numero=certidao.numero,
        data_emissao=certidao.data_emissao, valido_ate=certidao.valido_ate,
        observacao=certidao.observacao, status=certidao.status.value,
        created_at=certidao.created_at,
    )


@router.post("/lancamentos/{lancamento_id}/inscrever-divida-ativa", status_code=201)
def inscrever_divida_ativa(
    lancamento_id: str,
    repo: Annotated[RepositorioDividaAtiva, Depends(get_divida_repo)],
    lancamentos: Annotated[RepositorioLancamento, Depends(get_lancamento_repo)],
):
    """Inscreve crédito vencido em dívida ativa."""
    try:
        inscricao = InscreverDividaAtivaUseCase(repo, lancamentos).execute(
            lancamento_id
        )
    except (LancamentoNaoEncontradoError, DividaAtivaNaoEncontradaError) as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomTriDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_divida(inscricao)


@router.get("/divida-ativa")
def listar_divida_ativa(
    repo: Annotated[RepositorioDividaAtiva, Depends(get_divida_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    """Lista inscrições em dívida ativa."""
    itens = repo.list_all(page=page, page_size=page_size)
    return [_to_divida(d) for d in itens]


@router.get("/divida-ativa/{inscricao_id}")
def obter_divida_ativa(
    inscricao_id: str,
    repo: Annotated[RepositorioDividaAtiva, Depends(get_divida_repo)],
):
    """Obtém uma inscrição por id."""
    inscricao = repo.get_by_id(inscricao_id)
    if inscricao is None:
        raise HTTPException(status_code=404, detail="Inscrição não encontrada")
    return _to_divida(inscricao)


@router.post("/divida-ativa/{inscricao_id}/baixar")
def baixar_divida_ativa(
    inscricao_id: str,
    repo: Annotated[RepositorioDividaAtiva, Depends(get_divida_repo)],
):
    """Baixa uma inscrição de dívida ativa."""
    try:
        inscricao = BaixarDividaAtivaUseCase(repo).execute(inscricao_id)
    except DividaAtivaNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomTriDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_divida(inscricao)


@router.post("/certidoes", status_code=201)
def emitir_certidao(
    contribuinte_id: str,
    repo: Annotated[RepositorioCertidao, Depends(get_certidao_repo)],
    lancamentos: Annotated[RepositorioLancamento, Depends(get_lancamento_repo)],
    contribuintes: Annotated[RepositorioContribuinte, Depends(get_contribuinte_repo)],
):
    """Emite certidão de regularidade fiscal."""
    try:
        certidao = EmitirCertidaoUseCase(repo, lancamentos, contribuintes).execute(
            contribuinte_id
        )
    except ContribuinteNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomTriDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_certidao(certidao)


@router.get("/certidoes/{certidao_id}")
def obter_certidao(
    certidao_id: str,
    repo: Annotated[RepositorioCertidao, Depends(get_certidao_repo)],
):
    """Obtém uma certidão por id."""
    certidao = repo.get_by_id(certidao_id)
    if certidao is None:
        raise HTTPException(status_code=404, detail="Certidão não encontrada")
    return _to_certidao(certidao)


__all__ = ["router"]