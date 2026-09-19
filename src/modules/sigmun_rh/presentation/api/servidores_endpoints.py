"""Endpoints de servidores (DOM-PES)."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, HTTPException, status

from src.modules.sigmun_rh.application.interfaces import (
    RepositorioCargo,
    RepositorioServidor,
)
from src.modules.sigmun_rh.application.use_cases_cargos_servidores import (
    AdmitirServidorInput,
    AdmitirServidorUseCase,
    AfastarServidorUseCase,
    DesligarServidorInput,
    DesligarServidorUseCase,
    ReativarServidorUseCase,
)
from src.modules.sigmun_rh.domain.exceptions import DomPesDomainError
from src.modules.sigmun_rh.presentation.schemas.pes_schemas import ServidorCreateRequest

from .servidores import get_cargo_repo2, get_servidor_repo, servidor_to_response
from .servidores import router_servidores

router = router_servidores


@router.post("/servidores", status_code=201)
def admitir_servidor(
    payload: ServidorCreateRequest,
    repo: Annotated[RepositorioServidor, Depends(get_servidor_repo)],
    cargos: Annotated[RepositorioCargo, Depends(get_cargo_repo2)],
):
    """Admite um servidor."""
    try:
        servidor = AdmitirServidorUseCase(repo, cargos).execute(
            AdmitirServidorInput(
                matricula=payload.matricula, cpf=payload.cpf,
                nome=payload.nome, cargo_id=payload.cargo_id,
                tipo_vinculo=payload.tipo_vinculo, salario=payload.salario,
                data_admissao=payload.data_admissao, email=payload.email,
                telefone=payload.telefone, autor_id=payload.created_by,
            )
        )
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return servidor_to_response(servidor)


@router.post("/servidores/{servidor_id}/afastar")
def afastar_servidor(
    servidor_id: str,
    repo: Annotated[RepositorioServidor, Depends(get_servidor_repo)],
):
    """Afastamento de servidor."""
    try:
        servidor = AfastarServidorUseCase(repo).execute(servidor_id)
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return servidor_to_response(servidor)


@router.post("/servidores/{servidor_id}/reativar")
def reativar_servidor(
    servidor_id: str,
    repo: Annotated[RepositorioServidor, Depends(get_servidor_repo)],
):
    """Reativa servidor afastado."""
    try:
        servidor = ReativarServidorUseCase(repo).execute(servidor_id)
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return servidor_to_response(servidor)


@router.post("/servidores/{servidor_id}/desligar")
def desligar_servidor(
    servidor_id: str,
    repo: Annotated[RepositorioServidor, Depends(get_servidor_repo)],
):
    """Desliga servidor."""
    try:
        servidor = DesligarServidorUseCase(repo).execute(
            DesligarServidorInput(servidor_id=servidor_id)
        )
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return servidor_to_response(servidor)


__all__ = ["router"]
