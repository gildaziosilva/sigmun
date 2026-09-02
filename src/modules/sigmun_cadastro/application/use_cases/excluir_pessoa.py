"""Caso de uso: Excluir Pessoa (soft-delete, DOM-CUM RN-CUM-007)."""

from __future__ import annotations

import logging
from uuid import uuid4

from src.modules.sigmun_cadastro.application.commands.pessoa_commands import (
    ExcluirPessoaCommand,
)
from src.modules.sigmun_cadastro.domain.entities.pessoa import Pessoa
from src.modules.sigmun_cadastro.domain.events.pessoa_events import PessoaExcluidaEvent
from src.modules.sigmun_cadastro.domain.exceptions import PessoaNaoEncontradoError
from src.modules.sigmun_cadastro.domain.repositories.pessoa_repository import (
    PessoaRepository,
)

logger = logging.getLogger(__name__)


class ExcluirPessoaUseCase:
    """Exclui logicamente a pessoa e seus dados filhos (RN-CUM-007)."""

    def __init__(self, repository: PessoaRepository) -> None:
        self._repository = repository

    def execute(self, command: ExcluirPessoaCommand) -> Pessoa:
        pessoa = self._repository.get_by_id(command.pessoa_id)
        if pessoa is None:
            raise PessoaNaoEncontradoError(f"Pessoa {command.pessoa_id} não encontrada")
        self._repository.delete(command.pessoa_id, command.usuario_id)
        excluida = self._repository.get_by_id(command.pessoa_id, include_deleted=True)
        logger.info(
            "Pessoa excluída: %s",
            PessoaExcluidaEvent(
                event_id=uuid4(),
                pessoa_id=command.pessoa_id,
                occurred_at=excluida.deleted_at if excluida else pessoa.updated_at,
            ),
        )
        return excluida if excluida is not None else pessoa


__all__ = ["ExcluirPessoaUseCase"]
