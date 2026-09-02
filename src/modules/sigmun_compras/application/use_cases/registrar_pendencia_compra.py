"""Caso de uso: Registrar/Resolver Pendências Impeditivas (RN-COMPRAS-027).

Enquanto existirem pendências impeditivas, a compra não poderá avançar
para etapas incompatíveis; o cancelamento permanece permitido.
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.registrar_pendencia_compra_command import (
    RegistrarPendenciaCompraCommand,
)
from src.modules.sigmun_compras.domain.entities.compra import Compra
from src.modules.sigmun_compras.domain.exceptions import CompraNaoEncontradaError
from src.modules.sigmun_compras.domain.repositories.compra_repository import (
    CompraRepository,
)

logger = logging.getLogger(__name__)


class RegistrarPendenciaCompraUseCase:
    """Orquestra o registro e a resolução de pendências impeditivas."""

    def __init__(self, repository: CompraRepository) -> None:
        self._repository = repository

    def execute(self, command: RegistrarPendenciaCompraCommand) -> Compra:
        logger.info(
            "Atualizando pendências – compra=%s registrar=%s",
            command.compra_id,
            command.registrar,
        )

        compra = self._repository.get_by_id(command.compra_id)
        if compra is None or compra.foi_excluido():
            raise CompraNaoEncontradaError(
                f"Compra {command.compra_id} não encontrada"
            )

        if command.registrar:
            compra.registrar_pendencia(command.usuario_id)
        else:
            compra.resolver_pendencias(command.usuario_id)

        return self._repository.update(compra)