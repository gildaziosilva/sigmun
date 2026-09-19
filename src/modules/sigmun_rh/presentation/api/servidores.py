"""Rotas de servidores (DOM-PES)."""

from __future__ import annotations

import logging
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_rh.application.interfaces import (
    RepositorioCargo,
    RepositorioServidor,
)
from src.modules.sigmun_rh.infrastructure.repositories.sqlalchemy_cargo_repository import (
    SQLAlchemyCargoRepository,
)
from src.modules.sigmun_rh.infrastructure.repositories.sqlalchemy_servidor_repository import (
    SQLAlchemyServidorRepository,
)
from src.modules.sigmun_rh.presentation.schemas.pes_schemas import (
    ServidorResponse,
)

logger = logging.getLogger(__name__)

router_servidores = APIRouter(prefix="/api/v1/pes", tags=["Gestao de Pessoas"])


def get_servidor_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioServidor:
    """Fabrica de repositorio de servidores."""
    return SQLAlchemyServidorRepository(session)


def get_cargo_repo2(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioCargo:
    """Fabrica auxiliar de cargos."""
    return SQLAlchemyCargoRepository(session)


def servidor_to_response(servidor) -> ServidorResponse:
    """Converte servidor em resposta."""
    return ServidorResponse(
        id=servidor.id, matricula=servidor.matricula, cpf=servidor.cpf,
        nome=servidor.nome, cargo_id=servidor.cargo_id,
        tipo_vinculo=servidor.tipo_vinculo.value,
        status=servidor.status.value,
        data_admissao=servidor.data_admissao,
        data_desligamento=servidor.data_desligamento,
        salario=servidor.salario, email=servidor.email,
        telefone=servidor.telefone, created_at=servidor.created_at,
        updated_at=servidor.updated_at,
    )
