"""Rotas de lotacoes (DOM-PES)."""

from __future__ import annotations

import logging
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_rh.application.interfaces import (
    RepositorioLotacao,
    RepositorioServidor,
)
from src.modules.sigmun_rh.infrastructure.repositories.sqlalchemy_lotacao_repository import (
    SQLAlchemyLotacaoRepository,
)
from src.modules.sigmun_rh.infrastructure.repositories.sqlalchemy_servidor_repository import (
    SQLAlchemyServidorRepository,
)
from src.modules.sigmun_rh.presentation.schemas.pes_operacionais_schemas import (
    LotacaoResponse,
)

logger = logging.getLogger(__name__)

router_lotacoes = APIRouter(prefix="/api/v1/pes", tags=["Gestao de Pessoas"])


def get_lotacao_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioLotacao:
    """Fabrica de lotacoes."""
    return SQLAlchemyLotacaoRepository(session)


def get_servidor_repo2(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioServidor:
    """Fabrica auxiliar de servidores."""
    return SQLAlchemyServidorRepository(session)


def lotacao_to_response(lotacao) -> LotacaoResponse:
    """Converte lotacao em resposta."""
    return LotacaoResponse(
        id=lotacao.id, servidor_id=lotacao.servidor_id,
        unidade_id=lotacao.unidade_id, cargo_id=lotacao.cargo_id,
        data_inicio=lotacao.data_inicio, data_fim=lotacao.data_fim,
        vigente=lotacao.vigente, motivo=lotacao.motivo,
        created_at=lotacao.created_at,
    )
