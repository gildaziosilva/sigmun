"""Caso de uso: Excluir Contrato (soft-delete, preserva histórico)."""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.excluir_contrato_command import (
    ExcluirContratoCommand,
)
from src.modules.sigmun_compras.domain.entities.contrato import Contrato
from src.modules.sigmun_compras.domain.exceptions import (
    ContratoNaoEncontradoError,
)
from src.modules.sigmun_compras.domain.repositories.contrato_repository import (
    ContratoRepository,
)

logger = logging.getLogger(__name__)


class ExcluirContratoUseCase:
    """Orquestra a exclusão lógica de um contrato."""

    def __init__(self, repository: ContratoRepository) -> None:
        self._repository = repository

    def execute(self, command: ExcluirContratoCommand) -> Contrato:
        logger.info("Excluindo contrato – id=%s", command.contrato_id)

        contrato = self._repository.get_by_id(command.contrato_id)
        if contrato is None or contrato.foi_excluido():
            raise ContratoNaoEncontradoError(
                f"Contrato {command.contrato_id} não encontrado"
            )

        contrato.excluir(command.usuario_id)
        self._repository.delete(contrato.id, command.usuario_id)

        return contrato
