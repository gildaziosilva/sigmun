"""Endpoints de PPA/LDO/LOA (DOM-ORC)."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.modules.sigmun_orc.application.interfaces import (
    RepositorioLDO,
    RepositorioLOA,
    RepositorioPPA,
)
from src.modules.sigmun_orc.application.use_cases_planejamento import (
    CriarLDOInput,
    CriarLDOUseCase,
    CriarLOAInput,
    CriarLOAUseCase,
    CriarPPAInput,
    CriarPPAUseCase,
    PublicarLOAUseCase,
    PublicarPPAUseCase,
    SancionarLDOUseCase,
)
from src.modules.sigmun_orc.domain.exceptions import DomOrcDomainError
from src.modules.sigmun_orc.presentation.schemas.orc_schemas import (
    LDOCreateRequest,
    LDOResponse,
    LOACreateRequest,
    LOAResponse,
    PPACreateRequest,
    PPAResponse,
)

from .base import get_ldo_repo, get_loa_repo, get_ppa_repo

router = APIRouter(prefix="/api/v1/orc", tags=["Orçamento Público"])


@router.post("/ppas", status_code=201)
def criar_ppa(payload: PPACreateRequest,
              repo: Annotated[RepositorioPPA, Depends(get_ppa_repo)]):
    """Cria PPA do quadriênio."""
    try:
        ppa = CriarPPAUseCase(repo).execute(
            CriarPPAInput(ano_inicial=payload.ano_inicial,
                          ano_final=payload.ano_final,
                          descricao=payload.descricao,
                          autor_id=payload.created_by))
    except DomOrcDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return PPAResponse(id=ppa.id, ano_inicial=ppa.ano_inicial,
                       ano_final=ppa.ano_final, descricao=ppa.descricao,
                       status=ppa.status.value, created_at=ppa.created_at)


@router.post("/ppas/{ppa_id}/publicar")
def publicar_ppa(ppa_id: str, repo: Annotated[RepositorioPPA, Depends(get_ppa_repo)]):
    """Publica PPA em elaboração."""
    try:
        ppa = PublicarPPAUseCase(repo).execute(ppa_id)
    except DomOrcDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return PPAResponse(id=ppa.id, ano_inicial=ppa.ano_inicial,
                       ano_final=ppa.ano_final, descricao=ppa.descricao,
                       status=ppa.status.value, created_at=ppa.created_at)


@router.post("/ldos", status_code=201)
def criar_ldo(payload: LDOCreateRequest,
              ldos: Annotated[RepositorioLDO, Depends(get_ldo_repo)],
              ppas: Annotated[RepositorioPPA, Depends(get_ppa_repo)]):
    """Cria LDO vinculada a PPA vigente."""
    try:
        ldo = CriarLDOUseCase(ldos, ppas).execute(
            CriarLDOInput(exercicio=payload.exercicio, ppa_id=payload.ppa_id,
                          descricao=payload.descricao,
                          meta_receita=payload.meta_receita,
                          meta_despesa=payload.meta_despesa,
                          autor_id=payload.created_by))
    except DomOrcDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return LDOResponse(id=ldo.id, exercicio=ldo.exercicio, ppa_id=ldo.ppa_id,
                       descricao=ldo.descricao, status=ldo.status.value,
                       created_at=ldo.created_at)


@router.post("/ldos/{ldo_id}/sancionar")
def sancionar_ldo(ldo_id: str, repo: Annotated[RepositorioLDO, Depends(get_ldo_repo)]):
    """Aprova e sanciona LDO."""
    try:
        ldo = SancionarLDOUseCase(repo).execute(ldo_id, sancionar=True)
    except DomOrcDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return LDOResponse(id=ldo.id, exercicio=ldo.exercicio, ppa_id=ldo.ppa_id,
                       descricao=ldo.descricao, status=ldo.status.value,
                       created_at=ldo.created_at)


@router.post("/loas", status_code=201)
def criar_loa(payload: LOACreateRequest,
              loas: Annotated[RepositorioLOA, Depends(get_loa_repo)],
              ldos: Annotated[RepositorioLDO, Depends(get_ldo_repo)]):
    """Cria LOA vinculada a LDO sancionada."""
    try:
        loa = CriarLOAUseCase(loas, ldos).execute(
            CriarLOAInput(exercicio=payload.exercicio, ldo_id=payload.ldo_id,
                          descricao=payload.descricao, receita=payload.receita,
                          despesa=payload.despesa, autor_id=payload.created_by))
    except DomOrcDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return LOAResponse(id=loa.id, exercicio=loa.exercicio, ldo_id=loa.ldo_id,
                       descricao=loa.descricao, status=loa.status.value,
                       created_at=loa.created_at)


@router.post("/loas/{loa_id}/publicar")
def publicar_loa(loa_id: str, repo: Annotated[RepositorioLOA, Depends(get_loa_repo)]):
    """Aprova e publica LOA."""
    try:
        loa = PublicarLOAUseCase(repo).execute(loa_id, publicar=True)
    except DomOrcDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return LOAResponse(id=loa.id, exercicio=loa.exercicio, ldo_id=loa.ldo_id,
                       descricao=loa.descricao, status=loa.status.value,
                       created_at=loa.created_at)


__all__ = ["router"]
