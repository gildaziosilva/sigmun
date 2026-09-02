"""Caso de uso: Registrar Item de Compra.

Baseado em:
  - ENT-COMPRAS-004 – Item da Contratação
  - RN-COMPRAS-011 – Especificação do Objeto
  - RN-COMPRAS-012 – Quantificação

O item representa um produto (material) ou serviço vinculado a uma
compra existente do domínio.
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.criar_item_compra_command import (
    CriarItemCompraCommand,
)
from src.modules.sigmun_compras.domain.entities.item_compra import ItemCompra
from src.modules.sigmun_compras.domain.events.item_compra_events import ItemCompraCriadoEvent
from src.modules.sigmun_compras.domain.exceptions import CompraNaoEncontradaError
from src.modules.sigmun_compras.domain.repositories.item_compra_repository import (
    ItemCompraRepository,
)

logger = logging.getLogger(__name__)


class RegistrarItemCompraUseCase:
    """Orquestra a inclusão de um item em uma compra."""

    def __init__(self, repository: ItemCompraRepository) -> None:
        self._repository = repository

    def execute(self, command: CriarItemCompraCommand) -> ItemCompra:
        logger.info("Registrando item para compra=%s", command.compra_id)

        # Integridade do vínculo: a compra precisa existir.
        if not self._repository.exists_compra(command.compra_id):
            raise CompraNaoEncontradaError(
                f"Compra {command.compra_id} não encontrada"
            )

        item = ItemCompra(
            compra_id=command.compra_id,
            descricao=command.descricao,
            quantidade=command.quantidade,
            valor_unitario=command.valor_unitario,
            created_by=command.usuario_id,
        )

        item_salvo = self._repository.save(item)

        evento = ItemCompraCriadoEvent(
            item_id=item_salvo.id,
            compra_id=item_salvo.compra_id,
            descricao=item_salvo.descricao,
            valor_total=item_salvo.valor_total,
            created_at=item_salvo.created_at,
        )
        logger.info("Item registrado: %s", evento)

        return item_salvo
