"""Caso de uso: Atualizar dados cadastrais de uma Compra.

Baseado em:
  - RN-COMPRAS-028 – Responsabilidade
  - RN-COMPRAS-029 – Registro de Data e Hora
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.atualizar_compra_command import (
    AtualizarCompraCommand,
)
from src.modules.sigmun_compras.domain.entities.compra import Compra
from src.modules.sigmun_compras.domain.events.compra_events import (
    CompraAtualizadaEvent,
)
from src.modules.sigmun_compras.domain.exceptions import CompraNaoEncontradaError
from src.modules.sigmun_compras.domain.repositories.compra_repository import (
    CompraRepository,
)

logger = logging.getLogger(__name__)


class AtualizarCompraUseCase:
    """Orquestra a atualização cadastral de uma compra."""

    def __init__(self, repository: CompraRepository) -> None:
        self._repository = repository

    def execute(self, command: AtualizarCompraCommand) -> Compra:
        logger.info("Atualizando compra – id=%s", command.compra_id)

        if (
            command.numero is None
            and command.data is None
            and command.valor_total is None
        ):
            raise ValueError("Informe ao menos um campo para atualização")

        compra = self._repository.get_by_id(command.compra_id)
        if compra is None or compra.foi_excluido():
            raise CompraNaoEncontradaError(
                f"Compra {command.compra_id} não encontrada"
            )

        compra.atualizar_dados(
            numero=command.numero,
            data=command.data,
            valor_total=command.valor_total,
            usuario_id=command.usuario_id,
        )

        compra_atualizada = self._repository.update(compra)

        evento = CompraAtualizadaEvent(
            compra_id=compra_atualizada.id,
            numero=compra_atualizada.numero,
            valor_total=compra_atualizada.valor_total,
            updated_at=compra_atualizada.updated_at,
        )
        logger.info("Compra atualizada: %s", evento)

        return compra_atualizada
