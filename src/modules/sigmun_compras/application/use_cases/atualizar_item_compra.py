"""Caso de uso: Atualizar Item de Compra.

Baseado em:
  - ENT-COMPRAS-004 – Item da Contratação
  - RN-COMPRAS-011 – Especificação do Objeto
  - RN-COMPRAS-012 – Quantificação
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.atualizar_item_compra_command import (
    AtualizarItemCompraCommand,
)
from src.modules.sigmun_compras.domain.entities.item_compra import ItemCompra
from src.modules.sigmun_compras.domain.events.item_compra_events import (
    ItemCompraAtualizadoEvent,
)
from src.modules.sigmun_compras.domain.exceptions import ItemNaoEncontradoError
from src.modules.sigmun_compras.domain.repositories.item_compra_repository import (
    ItemCompraRepository,
)

logger = logging.getLogger(__name__)


class AtualizarItemCompraUseCase:
    """Orquestra a atualização de um item de compra."""

    def __init__(self, repository: ItemCompraRepository) -> None:
        self._repository = repository

    def execute(self, command: AtualizarItemCompraCommand) -> ItemCompra:
        logger.info("Atualizando item de compra – id=%s", command.item_id)

        if (
            command.descricao is None
            and command.quantidade is None
            and command.valor_unitario is None
        ):
            raise ValueError("Informe ao menos um campo para atualização")

        item = self._repository.get_by_id(command.item_id)
        if item is None or item.foi_excluido():
            raise ItemNaoEncontradoError(f"Item {command.item_id} não encontrado")

        item.atualizar_dados(
            descricao=command.descricao,
            quantidade=command.quantidade,
            valor_unitario=command.valor_unitario,
            usuario_id=command.usuario_id,
        )

        item_atualizado = self._repository.update(item)

        evento = ItemCompraAtualizadoEvent(
            item_id=item_atualizado.id,
            compra_id=item_atualizado.compra_id,
            valor_total=item_atualizado.valor_total,
            updated_at=item_atualizado.updated_at,
        )
        logger.info("Item atualizado: %s", evento)

        return item_atualizado
