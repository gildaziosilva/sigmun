"""Caso de uso: Consultar Item de Compra.

Baseado em:
  - ENT-COMPRAS-004 – Item da Contratação
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.queries.consultar_item_compra_query import (
    ConsultarItemCompraQuery,
)
from src.modules.sigmun_compras.domain.entities.item_compra import ItemCompra
from src.modules.sigmun_compras.domain.exceptions import ItemNaoEncontradoError
from src.modules.sigmun_compras.domain.repositories.item_compra_repository import (
    ItemCompraRepository,
)

logger = logging.getLogger(__name__)


class ConsultarItemCompraUseCase:
    """Orquestra a consulta de um item de compra."""

    def __init__(self, repository: ItemCompraRepository) -> None:
        self._repository = repository

    def execute(self, query: ConsultarItemCompraQuery) -> ItemCompra:
        logger.info("Consultando item de compra – id=%s", query.item_id)

        item = self._repository.get_by_id(query.item_id)
        if item is None or item.foi_excluido():
            raise ItemNaoEncontradoError(f"Item {query.item_id} não encontrado")

        return item
