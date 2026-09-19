"""Endpoints de cargos (DOM-PES)."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, HTTPException, status

from src.modules.sigmun_rh.application.interfaces import RepositorioCargo
from src.modules.sigmun_rh.application.use_cases_cargos_servidores import (
    CriarCargoInput,
    CriarCargoUseCase,
)
from src.modules.sigmun_rh.domain.exceptions import DomPesDomainError
from src.modules.sigmun_rh.presentation.schemas.pes_schemas import CargoCreateRequest

from .cargos import cargo_to_response, get_cargo_repo, router_cargos


@router_cargos.post("/cargos", status_code=201)
def criar_cargo(
    payload: CargoCreateRequest,
    repo: Annotated[RepositorioCargo, Depends(get_cargo_repo)],
):
    """Cria um cargo."""
    try:
        cargo = CriarCargoUseCase(repo).execute(
            CriarCargoInput(
                codigo=payload.codigo, nome=payload.nome,
                descricao=payload.descricao, nivel=payload.nivel,
                salario_base=payload.salario_base,
                carga_horaria_semanal=payload.carga_horaria_semanal,
                autor_id=payload.created_by,
            )
        )
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return cargo_to_response(cargo)


router = router_cargos
__all__ = ["router"]
