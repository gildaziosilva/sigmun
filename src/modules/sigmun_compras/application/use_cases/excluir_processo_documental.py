"""Caso de uso: Excluir Processo Documental (soft-delete)."""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.excluir_processo_documental_command import (
    ExcluirProcessoDocumentalCommand,
)
from src.modules.sigmun_compras.domain.entities.processo_documental import (
    ProcessoDocumental,
)
from src.modules.sigmun_compras.domain.exceptions import (
    ProcessoDocumentalNaoEncontradoError,
)
from src.modules.sigmun_compras.domain.repositories.processo_documental_repository import (
    ProcessoDocumentalRepository,
)

logger = logging.getLogger(__name__)


class ExcluirProcessoDocumentalUseCase:
    """Orquestra a exclusão lógica de um processo documental."""

    def __init__(self, repository: ProcessoDocumentalRepository) -> None:
        self._repository = repository

    def execute(
        self, command: ExcluirProcessoDocumentalCommand
    ) -> ProcessoDocumental:
        logger.info("Excluindo processo documental – id=%s", command.processo_id)

        processo = self._repository.get_by_id(command.processo_id)
        if processo is None or processo.foi_excluido():
            raise ProcessoDocumentalNaoEncontradoError(
                f"Processo documental {command.processo_id} não encontrado"
            )

        processo.excluir(command.usuario_id)
        self._repository.delete(processo.id, command.usuario_id)

        return processo
