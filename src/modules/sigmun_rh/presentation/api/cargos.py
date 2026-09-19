"""Rotas de cargos (DOM-PES) - parte 1."""

from __future__ import annotations

import logging
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_rh.application.interfaces import RepositorioCargo
from src.modules.sigmun_rh.infrastructure.repositories.sqlalchemy_cargo_repository import (
    SQLAlchemyCargoRepository,
)
from src.modules.sigmun_rh.presentation.schemas.pes_schemas import (
    CargoResponse,
)

logger = logging.getLogger(__name__)

router_cargos = APIRouter(prefix="/api/v1/pes", tags=["Gestao de Pessoas"])


def get_cargo_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioCargo:
    """Fabrica de repositorio de cargos."""
    return SQLAlchemyCargoRepository(session)


def cargo_to_response(cargo) -> CargoResponse:
    """Converte cargo em resposta."""
    return CargoResponse(
        id=cargo.id, codigo=cargo.codigo, nome=cargo.nome,
        descricao=cargo.descricao, nivel=cargo.nivel,
        salario_base=cargo.salario_base,
        carga_horaria_semanal=cargo.carga_horaria_semanal,
        ativo=cargo.ativo, created_at=cargo.created_at,
        updated_at=cargo.updated_at,
    )
