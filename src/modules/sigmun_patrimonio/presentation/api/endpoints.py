"""Endpoints do DOM-PAT — Gestão Patrimonial."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_patrimonio.application.interfaces import (
    RepositorioBem,
    RepositorioDepreciacao,
    RepositorioTransferencia,
)
from src.modules.sigmun_patrimonio.application.use_cases import (
    BaixarBemUseCase,
    CadastrarBemInput,
    CadastrarBemUseCase,
    ConcluirTransferenciaUseCase,
    DepreciarBemUseCase,
    TransferirBemInput,
    TransferirBemUseCase,
)
from src.modules.sigmun_patrimonio.domain.exceptions import (
    BemNaoEncontradoError,
    DomPatDomainError,
    TransferenciaNaoEncontradaError,
)
from src.modules.sigmun_patrimonio.infrastructure.repositories.sqlalchemy_bem_repository import (
    SQLAlchemyBemRepository,
)
from src.modules.sigmun_patrimonio.infrastructure.repositories.sqlalchemy_depreciacao_transferencia_repository import (
    SQLAlchemyDepreciacaoRepository,
    SQLAlchemyTransferenciaRepository,
)
from src.modules.sigmun_patrimonio.presentation.schemas.pat_schemas import (
    BemCreateRequest,
    BemResponse,
    DepreciacaoCreateRequest,
    DepreciacaoResponse,
    TransferenciaCreateRequest,
    TransferenciaResponse,
)

router = APIRouter(prefix="/api/v1/pat", tags=["Gestao Patrimonial"])


def get_bem_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioBem:
    """Fabrica de repositório de bens."""
    return SQLAlchemyBemRepository(session)


def get_depreciacao_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioDepreciacao:
    """Fabrica de repositório de depreciações."""
    return SQLAlchemyDepreciacaoRepository(session)


def get_transferencia_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioTransferencia:
    """Fabrica de repositório de transferências."""
    return SQLAlchemyTransferenciaRepository(session)


def _to_bem(bem) -> BemResponse:
    return BemResponse(
        id=bem.id, codigo=bem.codigo, tipo=bem.tipo.value,
        descricao=bem.descricao, categoria=bem.categoria,
        valor_aquisicao=bem.valor_aquisicao, data_aquisicao=bem.data_aquisicao,
        valor_residual=bem.valor_residual, vida_util_anos=bem.vida_util_anos,
        valor_contabil=bem.valor_contabil, status=bem.status.value,
        localizacao=bem.localizacao, responsavel_id=bem.responsavel_id,
        created_at=bem.created_at,
    )


def _to_depreciacao(dep) -> DepreciacaoResponse:
    return DepreciacaoResponse(
        id=dep.id, bem_id=dep.bem_id, data=dep.data,
        valor_depreciado=dep.valor_depreciado,
        valor_acumulado=dep.valor_acumulado, valor_liquido=dep.valor_liquido,
        created_at=dep.created_at,
    )


def _to_transferencia(t) -> TransferenciaResponse:
    return TransferenciaResponse(
        id=t.id, bem_id=t.bem_id, de_localizacao=t.de_localizacao,
        para_localizacao=t.para_localizacao,
        de_responsavel_id=t.de_responsavel_id,
        para_responsavel_id=t.para_responsavel_id,
        data_transferencia=t.data_transferencia, motivo=t.motivo,
        status=t.status.value, created_at=t.created_at,
    )


@router.post("/bens", status_code=201)
def cadastrar_bem(
    payload: BemCreateRequest,
    repo: Annotated[RepositorioBem, Depends(get_bem_repo)],
):
    """Cadastra um bem patrimonial."""
    try:
        bem = CadastrarBemUseCase(repo).execute(
            CadastrarBemInput(
                codigo=payload.codigo, tipo=payload.tipo,
                descricao=payload.descricao, categoria=payload.categoria,
                valor_aquisicao=payload.valor_aquisicao,
                data_aquisicao=payload.data_aquisicao,
                valor_residual=payload.valor_residual,
                vida_util_anos=payload.vida_util_anos,
                localizacao=payload.localizacao,
                responsavel_id=payload.responsavel_id,
                autor_id=payload.created_by,
            )
        )
    except DomPatDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_bem(bem)


@router.get("/bens")
def listar_bens(
    repo: Annotated[RepositorioBem, Depends(get_bem_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    """Lista bens paginados."""
    itens = repo.list_all(page=page, page_size=page_size)
    return [_to_bem(b) for b in itens]


@router.get("/bens/{bem_id}")
def obter_bem(
    bem_id: str,
    repo: Annotated[RepositorioBem, Depends(get_bem_repo)],
):
    """Obtém um bem por id."""
    bem = repo.get_by_id(bem_id)
    if bem is None:
        raise HTTPException(status_code=404, detail="Bem não encontrado")
    return _to_bem(bem)


@router.post("/bens/{bem_id}/depreciar")
def depreciar_bem(
    bem_id: str,
    payload: DepreciacaoCreateRequest,
    bens: Annotated[RepositorioBem, Depends(get_bem_repo)],
    depreciacoes: Annotated[RepositorioDepreciacao, Depends(get_depreciacao_repo)],
):
    """Aplica depreciação linear a um bem."""
    try:
        dep = DepreciarBemUseCase(bens, depreciacoes).execute(bem_id, payload.data)
    except BemNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomPatDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_depreciacao(dep)


@router.get("/bens/{bem_id}/depreciacoes")
def listar_depreciacoes(
    bem_id: str,
    repo: Annotated[RepositorioDepreciacao, Depends(get_depreciacao_repo)],
):
    """Lista depreciações de um bem."""
    itens = repo.list_by_bem(bem_id)
    return [_to_depreciacao(d) for d in itens]


@router.post("/transferencias", status_code=201)
def transferir_bem(
    payload: TransferenciaCreateRequest,
    bens: Annotated[RepositorioBem, Depends(get_bem_repo)],
    transferencias: Annotated[RepositorioTransferencia, Depends(get_transferencia_repo)],
):
    """Registra transferência de bem."""
    try:
        t = TransferirBemUseCase(bens, transferencias).execute(
            TransferirBemInput(
                bem_id=payload.bem_id,
                para_localizacao=payload.para_localizacao,
                de_localizacao=payload.de_localizacao,
                de_responsavel_id=payload.de_responsavel_id,
                para_responsavel_id=payload.para_responsavel_id,
                motivo=payload.motivo, autor_id=payload.created_by,
            )
        )
    except BemNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomPatDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_transferencia(t)


@router.post("/transferencias/{transferencia_id}/concluir")
def concluir_transferencia(
    transferencia_id: str,
    transferencias: Annotated[RepositorioTransferencia, Depends(get_transferencia_repo)],
    bens: Annotated[RepositorioBem, Depends(get_bem_repo)],
):
    """Consolida uma transferência pendente."""
    try:
        t = ConcluirTransferenciaUseCase(transferencias, bens).execute(transferencia_id)
    except (TransferenciaNaoEncontradaError, BemNaoEncontradoError) as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomPatDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_transferencia(t)


@router.post("/bens/{bem_id}/baixar")
def baixar_bem(
    bem_id: str,
    repo: Annotated[RepositorioBem, Depends(get_bem_repo)],
):
    """Baixa definitiva de um bem."""
    try:
        bem = BaixarBemUseCase(repo).execute(bem_id)
    except BemNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomPatDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_bem(bem)


__all__ = ["router"]