"""Caso de uso: Remover Item de Compra (soft-delete).

O item é removido logicamente, preservando o histórico (auditoria).
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.remover_item_compra_command import (
    RemoverItemCompraCommand,
)
from src.modules.sigmun_compras.domain.entities.item_compra import ItemCompra
from src.modules.sigmun_compras.domain.events.item_compra_events import (
    ItemCompraRemovidoEvent,
)
from src.modules.sigmun_compras.domain.exceptions import ItemNaoEncontradoError
from src.modules.sigmun_compras.domain.repositories.item_compra_repository import (
    ItemCompraRepository,
)

logger = logging.getLogger(__name__)


class RemoverItemCompraUseCase:
    """Orquestra a remoção lógica de um item de compra."""

    def __init__(self, repository: ItemCompraRepository) -> None:
        self._repository = repository

    def execute(self, command: RemoverItemCompraCommand) -> ItemCompra:
        logger.info("Removendo item de compra – id=%s", command.item_id)

        item = self._repository.get_by_id(command.item_id)
        if item is None or item.foi_excluido():
            raise ItemNaoEncontradoError(f"Item {command.item_id} não encontrado")

        item.excluir(command.usuario_id)
        self._repository.delete(item.id, command.usuario_id)

        evento = ItemCompraRemovidoEvent(
            item_id=item.id,
            compra_id=item.compra_id,
            deleted_at=item.deleted_at,
        )
        logger.info("Item removido: %s", evento)

        return item
