"""Caso de uso: Listar Itens de uma Compra.

Baseado em:
  - ENT-COMPRAS-004 – Item da Contratação
  - SRV-COMPRAS – Gestão de Compras
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.queries.listar_itens_compra_query import (
    ListarItensCompraQuery,
)
from src.modules.sigmun_compras.domain.entities.item_compra import ItemCompra
from src.modules.sigmun_compras.domain.exceptions import CompraNaoEncontradaError
from src.modules.sigmun_compras.domain.repositories.item_compra_repository import (
    ItemCompraRepository,
)

logger = logging.getLogger(__name__)


class ListarItensCompraUseCase:
    """Orquestra a listagem paginada dos itens de uma compra."""

    def __init__(self, repository: ItemCompraRepository) -> None:
        self._repository = repository

    def execute(self, query: ListarItensCompraQuery) -> list[ItemCompra]:
        logger.info("Listando itens da compra=%s", query.compra_id)

        if not self._repository.exists_compra(query.compra_id):
            raise CompraNaoEncontradaError(
                f"Compra {query.compra_id} não encontrada"
            )

        offset = query.page * query.page_size

        return self._repository.list_by_compra(
            compra_id=query.compra_id,
            include_deleted=query.include_inativos,
            limit=query.page_size,
            offset=offset,
        )
