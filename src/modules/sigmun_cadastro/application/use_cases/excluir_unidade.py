"""Caso de uso: Excluir Unidade Administrativa (soft-delete, DOM-CUM)."""

from __future__ import annotations

import logging
from uuid import uuid4

from src.modules.sigmun_cadastro.application.commands.unidade_commands import (
    ExcluirUnidadeCommand,
)
from src.modules.sigmun_cadastro.domain.entities.unidade_administrativa import (
    UnidadeAdministrativa,
)
from src.modules.sigmun_cadastro.domain.events.unidade_events import (
    UnidadeExcluidaEvent,
)
from src.modules.sigmun_cadastro.domain.exceptions import (
    CadastroDomainError,
    UnidadeNaoEncontradaError,
)
from src.modules.sigmun_cadastro.domain.repositories.unidade_administrativa_repository import (
    UnidadeAdministrativaRepository,
)

logger = logging.getLogger(__name__)


class ExcluirUnidadeUseCase:
    """Exclui logicamente uma unidade administrativa (RN-CUM-007)."""

    def __init__(self, repository: UnidadeAdministrativaRepository) -> None:
        self._repository = repository

    def execute(self, command: ExcluirUnidadeCommand) -> UnidadeAdministrativa:
        unidade = self._repository.get_by_id(command.unidade_id)
        if unidade is None:
            raise UnidadeNaoEncontradaError(
                f"Unidade administrativa {command.unidade_id} não encontrada"
            )

        # Integridade hierárquica: não excluir unidade com filhas ativas
        if self._repository.tem_filhas_ativas(command.unidade_id):
            raise CadastroDomainError(
                "Unidade administrativa possui unidades filhas ativas e não "
                "pode ser excluída (RN-CUM-007)"
            )

        # Soft-delete com ``deleted_at`` do servidor (constraint ck_deleted)
        self._repository.delete(command.unidade_id, command.usuario_id)
        excluida = self._repository.get_by_id(command.unidade_id, include_deleted=True)
        logger.info(
            "Unidade administrativa excluída: %s",
            UnidadeExcluidaEvent(
                event_id=uuid4(),
                unidade_id=command.unidade_id,
                occurred_at=excluida.deleted_at if excluida else unidade.updated_at,
            ),
        )
        return excluida if excluida is not None else unidade


__all__ = ["ExcluirUnidadeUseCase"]
