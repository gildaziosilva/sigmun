"""Fábricas de repositórios e routers base (DOM-CON)."""

from __future__ import annotations

import logging
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_con.application.interfaces import (
    RepositorioConciliacao,
    RepositorioContaContabil,
    RepositorioEmpenho,
    RepositorioLancamento,
    RepositorioLiquidacao,
    RepositorioPagamento,
)
from src.modules.sigmun_con.infrastructure.repositories.sqlalchemy_conta_repository import (
    SQLAlchemyContaRepository,
)
from src.modules.sigmun_con.infrastructure.repositories.sqlalchemy_empenho_repository import (
    SQLAlchemyEmpenhoRepository,
)
from src.modules.sigmun_con.infrastructure.repositories.sqlalchemy_lanc_conc_repository import (
    SQLAlchemyConciliacaoRepository,
    SQLAlchemyLancamentoRepository,
)
from src.modules.sigmun_con.infrastructure.repositories.sqlalchemy_liq_pag_repository import (
    SQLAlchemyLiquidacaoRepository,
    SQLAlchemyPagamentoRepository,
)
from src.modules.sigmun_orc.infrastructure.repositories.sqlalchemy_dotacao_repository import (
    SQLAlchemyDotacaoRepository,
)

logger = logging.getLogger(__name__)

router_con = APIRouter(prefix="/api/v1/con", tags=["Contabilidade Pública"])


def get_empenho_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioEmpenho:
    """Fábrica de empenhos."""
    return SQLAlchemyEmpenhoRepository(session)


def get_liquidacao_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioLiquidacao:
    """Fábrica de liquidações."""
    return SQLAlchemyLiquidacaoRepository(session)


def get_pagamento_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioPagamento:
    """Fábrica de pagamentos."""
    return SQLAlchemyPagamentoRepository(session)


def get_conta_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioContaContabil:
    """Fábrica de contas PCASP."""
    return SQLAlchemyContaRepository(session)


def get_lancamento_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioLancamento:
    """Fábrica de lançamentos."""
    return SQLAlchemyLancamentoRepository(session)


def get_conciliacao_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioConciliacao:
    """Fábrica de conciliações."""
    return SQLAlchemyConciliacaoRepository(session)


def get_dotacao_repo_con(session: Annotated[Session, Depends(get_db)]):  # type: ignore[no-untyped-def]
    """Fábrica de dotações (integração DOM-ORC → DOM-CON)."""
    return SQLAlchemyDotacaoRepository(session)


__all__ = ["router_con", "get_empenho_repo", "get_liquidacao_repo", "get_pagamento_repo",
           "get_conta_repo", "get_lancamento_repo", "get_conciliacao_repo",
           "get_dotacao_repo_con"]
