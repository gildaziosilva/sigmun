"""Caso de uso: Listar Compras (processos de compras)."""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.queries.listar_compras_query import (
    ListarComprasQuery,
)
from src.modules.sigmun_compras.domain.entities.compra import Compra
from src.modules.sigmun_compras.domain.repositories.compra_repository import (
    CompraRepository,
)

logger = logging.getLogger(__name__)


class ListarComprasUseCase:
    """Orquestra a listagem paginada de compras com filtros."""

    def __init__(self, repository: CompraRepository) -> None:
        self._repository = repository

    def execute(self, query: ListarComprasQuery) -> list[Compra]:
        logger.info(
            "Listando compras – situacao=%s, include_inativos=%s",
            query.situacao,
            query.include_inativos,
        )

        offset = query.page * query.page_size

        return self._repository.list(
            situacao=query.situacao,
            include_deleted=query.include_inativos,
            limit=query.page_size,
            offset=offset,
        )
