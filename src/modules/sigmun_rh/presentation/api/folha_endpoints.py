"""Endpoints de folha (DOM-PES)."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, HTTPException, status

from src.modules.sigmun_rh.application.interfaces import RepositorioFolha
from src.modules.sigmun_rh.application.use_cases_folha import (
    AbrirFolhaInput,
    AbrirFolhaUseCase,
    ConsolidarFolhaInput,
    ConsolidarFolhaUseCase,
    FecharFolhaUseCase,
    HomologarFolhaUseCase,
    PagarFolhaUseCase,
    ReabrirFolhaUseCase,
)
from src.modules.sigmun_rh.domain.exceptions import DomPesDomainError
from src.modules.sigmun_rh.presentation.schemas.pes_operacionais_schemas import (
    FolhaConsolidarRequest,
    FolhaCreateRequest,
    FolhaResponse,
)

from .operacional import get_folha_repo, router_operacional

router = router_operacional


def _to_response(folha) -> FolhaResponse:
    return FolhaResponse(
        id=folha.id, competencia_ano=folha.competencia_ano,
        competencia_mes=folha.competencia_mes, descricao=folha.descricao,
        status=folha.status.value, total_proventos=folha.total_proventos,
        total_descontos=folha.total_descontos, total_liquido=folha.total_liquido,
        quantidade_servidores=folha.quantidade_servidores,
        created_at=folha.created_at,
    )


@router.post("/folhas", status_code=201)
def abrir_folha(
    payload: FolhaCreateRequest,
    repo: Annotated[RepositorioFolha, Depends(get_folha_repo)],
):
    """Abre folha da competencia."""
    try:
        folha = AbrirFolhaUseCase(repo).execute(
            AbrirFolhaInput(
                competencia_ano=payload.competencia_ano,
                competencia_mes=payload.competencia_mes,
                descricao=payload.descricao,
                autor_id=payload.created_by,
            )
        )
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_response(folha)


@router.post("/folhas/{folha_id}/consolidar")
def consolidar_folha(
    folha_id: str,
    payload: FolhaConsolidarRequest,
    repo: Annotated[RepositorioFolha, Depends(get_folha_repo)],
):
    """Consolida totais da folha."""
    try:
        folha = ConsolidarFolhaUseCase(repo).execute(
            ConsolidarFolhaInput(
                folha_id=folha_id, proventos=payload.proventos,
                descontos=payload.descontos,
                quantidade_servidores=payload.quantidade_servidores,
            )
        )
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_response(folha)


@router.post("/folhas/{folha_id}/fechar")
def fechar_folha(
    folha_id: str, repo: Annotated[RepositorioFolha, Depends(get_folha_repo)]
):
    """Fecha folha aberta."""
    try:
        folha = FecharFolhaUseCase(repo).execute(folha_id)
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_response(folha)


@router.post("/folhas/{folha_id}/reabrir")
def reabrir_folha(
    folha_id: str, repo: Annotated[RepositorioFolha, Depends(get_folha_repo)]
):
    """Reabre folha fechada."""
    try:
        folha = ReabrirFolhaUseCase(repo).execute(folha_id)
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_response(folha)


@router.post("/folhas/{folha_id}/homologar")
def homologar_folha(
    folha_id: str, repo: Annotated[RepositorioFolha, Depends(get_folha_repo)]
):
    """Homologa folha fechada."""
    try:
        folha = HomologarFolhaUseCase(repo).execute(folha_id)
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_response(folha)


@router.post("/folhas/{folha_id}/pagar")
def pagar_folha(
    folha_id: str, repo: Annotated[RepositorioFolha, Depends(get_folha_repo)]
):
    """Paga folha homologada."""
    try:
        folha = PagarFolhaUseCase(repo).execute(folha_id)
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_response(folha)


__all__ = ["router"]
