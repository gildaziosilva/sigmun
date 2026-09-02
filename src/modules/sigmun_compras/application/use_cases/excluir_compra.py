"""Caso de uso: Excluir Compra (soft-delete, preserva histórico)."""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.excluir_compra_command import (
    ExcluirCompraCommand,
)
from src.modules.sigmun_compras.domain.entities.compra import Compra
from src.modules.sigmun_compras.domain.exceptions import CompraNaoEncontradaError
from src.modules.sigmun_compras.domain.repositories.compra_repository import (
    CompraRepository,
)

logger = logging.getLogger(__name__)


class ExcluirCompraUseCase:
    """Orquestra a exclusão lógica de uma compra."""

    def __init__(self, repository: CompraRepository) -> None:
        self._repository = repository

    def execute(self, command: ExcluirCompraCommand) -> Compra:
        logger.info("Excluindo compra – id=%s", command.compra_id)

        compra = self._repository.get_by_id(command.compra_id)
        if compra is None or compra.foi_excluido():
            raise CompraNaoEncontradaError(
                f"Compra {command.compra_id} não encontrada"
            )

        compra.excluir(command.usuario_id)
        self._repository.delete(compra.id, command.usuario_id)

        return compra
