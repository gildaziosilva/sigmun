"""Fábricas de repositórios e routers base (DOM-ORC)."""

from __future__ import annotations

import logging
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_orc.application.interfaces import (
    RepositorioDotacao,
    RepositorioLDO,
    RepositorioLOA,
    RepositorioPPA,
    RepositorioReserva,
)
from src.modules.sigmun_orc.infrastructure.repositories.sqlalchemy_dotacao_repository import (
    SQLAlchemyDotacaoRepository,
)
from src.modules.sigmun_orc.infrastructure.repositories.sqlalchemy_ldo_repository import (
    SQLAlchemyLDORepository,
)
from src.modules.sigmun_orc.infrastructure.repositories.sqlalchemy_loa_repository import (
    SQLAlchemyLOARepository,
)
from src.modules.sigmun_orc.infrastructure.repositories.sqlalchemy_ppa_repository import (
    SQLAlchemyPPARepository,
)
from src.modules.sigmun_orc.infrastructure.repositories.sqlalchemy_reserva_repository import (
    SQLAlchemyReservaRepository,
)

logger = logging.getLogger(__name__)

router_orc = APIRouter(prefix="/api/v1/orc", tags=["Orçamento Público"])


def get_ppa_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioPPA:
    """Fábrica de PPAs."""
    return SQLAlchemyPPARepository(session)


def get_ldo_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioLDO:
    """Fábrica de LDOs."""
    return SQLAlchemyLDORepository(session)


def get_loa_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioLOA:
    """Fábrica de LOAs."""
    return SQLAlchemyLOARepository(session)


def get_dotacao_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioDotacao:
    """Fábrica de dotações."""
    return SQLAlchemyDotacaoRepository(session)


def get_reserva_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioReserva:
    """Fábrica de reservas."""
    return SQLAlchemyReservaRepository(session)


__all__ = ["router_orc", "get_ppa_repo", "get_ldo_repo", "get_loa_repo",
           "get_dotacao_repo", "get_reserva_repo"]
