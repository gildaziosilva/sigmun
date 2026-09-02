"""Caso de uso: Atualizar Unidade Administrativa (DOM-CUM).

PATCH parcial: nome, sigla, códigos e hierarquia (RN-CUM-007/008/009).
"""

from __future__ import annotations

import logging
from uuid import uuid4

from src.modules.sigmun_cadastro.application.commands.unidade_commands import (
    AtualizarUnidadeCommand,
)
from src.modules.sigmun_cadastro.domain.entities.unidade_administrativa import (
    UnidadeAdministrativa,
)
from src.modules.sigmun_cadastro.domain.events.unidade_events import (
    UnidadeAtualizadaEvent,
)
from src.modules.sigmun_cadastro.domain.exceptions import (
    CadastroDomainError,
    UnidadeJaExistenteError,
    UnidadeNaoEncontradaError,
)
from src.modules.sigmun_cadastro.domain.repositories.unidade_administrativa_repository import (
    UnidadeAdministrativaRepository,
)

logger = logging.getLogger(__name__)


class AtualizarUnidadeUseCase:
    """Atualiza dados de uma unidade administrativa (PATCH parcial)."""

    def __init__(self, repository: UnidadeAdministrativaRepository) -> None:
        self._repository = repository

    def execute(self, command: AtualizarUnidadeCommand) -> UnidadeAdministrativa:
        unidade = self._repository.get_by_id(command.unidade_id)
        if unidade is None:
            raise UnidadeNaoEncontradaError(
                f"Unidade administrativa {command.unidade_id} não encontrada"
            )

        # RN-CUM-009: unicidade (desconsiderando a própria unidade)
        if (
            command.sigla
            and command.sigla != unidade.sigla
            and self._repository.exists_sigla(command.sigla, exclude_id=unidade.id)
        ):
            raise UnidadeJaExistenteError(
                f"Já existe unidade administrativa com a sigla {command.sigla} (RN-CUM-009)"
            )
        if (
            command.codigo_ibge
            and command.codigo_ibge != unidade.codigo_ibge
            and self._repository.exists_codigo_ibge(command.codigo_ibge, exclude_id=unidade.id)
        ):
            raise UnidadeJaExistenteError(
                f"Já existe unidade administrativa com o código IBGE "
                f"{command.codigo_ibge} (RN-CUM-009)"
            )
        if (
            command.codigo_siafi
            and command.codigo_siafi != unidade.codigo_siafi
            and self._repository.exists_codigo_siafi(command.codigo_siafi, exclude_id=unidade.id)
        ):
            raise UnidadeJaExistenteError(
                f"Já existe unidade administrativa com o código SIAFI "
                f"{command.codigo_siafi} (RN-CUM-009)"
            )

        try:
            unidade.atualizar(
                nome=command.nome,
                sigla=command.sigla,
                codigo_ibge=command.codigo_ibge,
                codigo_siafi=command.codigo_siafi,
                unidade_pai_id=command.unidade_pai_id,
                usuario_id=command.usuario_id,
            )
        except ValueError as exc:
            raise CadastroDomainError(str(exc)) from exc

        # RN-CUM-008: o repositório valida ciclos profundos no save
        salvo = self._repository.save(unidade)

        logger.info(
            "Unidade administrativa atualizada: %s",
            UnidadeAtualizadaEvent(
                event_id=uuid4(), unidade_id=salvo.id, occurred_at=salvo.updated_at
            ),
        )
        return salvo


__all__ = ["AtualizarUnidadeUseCase"]
