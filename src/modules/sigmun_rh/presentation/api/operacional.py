"""Rotas de folha/ferias/frequencia (DOM-PES)."""

from __future__ import annotations

import logging
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_rh.application.interfaces import (
    RepositorioFerias,
    RepositorioFolha,
    RepositorioFrequencia,
    RepositorioServidor,
)
from src.modules.sigmun_rh.infrastructure.repositories.sqlalchemy_ferias_repository import (
    SQLAlchemyFeriasRepository,
)
from src.modules.sigmun_rh.infrastructure.repositories.sqlalchemy_folha_repository import (
    SQLAlchemyFolhaRepository,
)
from src.modules.sigmun_rh.infrastructure.repositories.sqlalchemy_frequencia_repository import (
    SQLAlchemyFrequenciaRepository,
)
from src.modules.sigmun_rh.infrastructure.repositories.sqlalchemy_servidor_repository import (
    SQLAlchemyServidorRepository,
)

logger = logging.getLogger(__name__)

router_operacional = APIRouter(prefix="/api/v1/pes", tags=["Gestao de Pessoas"])


def get_folha_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioFolha:
    """Fabrica de folhas."""
    return SQLAlchemyFolhaRepository(session)


def get_ferias_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioFerias:
    """Fabrica de ferias."""
    return SQLAlchemyFeriasRepository(session)


def get_freq_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioFrequencia:
    """Fabrica de frequencia."""
    return SQLAlchemyFrequenciaRepository(session)


def get_serv_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioServidor:
    """Fabrica auxiliar de servidores."""
    return SQLAlchemyServidorRepository(session)


__all__ = ["router_operacional"]
