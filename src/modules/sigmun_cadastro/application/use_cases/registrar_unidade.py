"""Caso de uso: Registrar Unidade Administrativa (DOM-CUM).

Baseado em:
  - 005-Casos-de-Uso-Cadastro-Unico-Municipal.md
  - RN-CUM-008 – hierarquia sem ciclos
  - RN-CUM-009 – unicidade de sigla/códigos IBGE/SIAFI
"""

from __future__ import annotations

import logging
from uuid import uuid4

from src.modules.sigmun_cadastro.application.commands.unidade_commands import (
    CriarUnidadeCommand,
)
from src.modules.sigmun_cadastro.domain.entities.unidade_administrativa import (
    UnidadeAdministrativa,
)
from src.modules.sigmun_cadastro.domain.events.unidade_events import (
    UnidadeRegistradaEvent,
)
from src.modules.sigmun_cadastro.domain.exceptions import UnidadeJaExistenteError
from src.modules.sigmun_cadastro.domain.repositories.unidade_administrativa_repository import (
    UnidadeAdministrativaRepository,
)

logger = logging.getLogger(__name__)


class RegistrarUnidadeUseCase:
    """Orquestra o registro de uma nova unidade administrativa."""

    def __init__(self, repository: UnidadeAdministrativaRepository) -> None:
        self._repository = repository

    def execute(self, command: CriarUnidadeCommand) -> UnidadeAdministrativa:
        logger.info("Registrando unidade administrativa – nome=%s", command.nome)

        # RN-CUM-009: unicidade de sigla e códigos
        if command.sigla and self._repository.exists_sigla(command.sigla):
            raise UnidadeJaExistenteError(
                f"Já existe unidade administrativa com a sigla {command.sigla} (RN-CUM-009)"
            )
        if command.codigo_ibge and self._repository.exists_codigo_ibge(command.codigo_ibge):
            raise UnidadeJaExistenteError(
                f"Já existe unidade administrativa com o código IBGE "
                f"{command.codigo_ibge} (RN-CUM-009)"
            )
        if command.codigo_siafi and self._repository.exists_codigo_siafi(command.codigo_siafi):
            raise UnidadeJaExistenteError(
                f"Já existe unidade administrativa com o código SIAFI "
                f"{command.codigo_siafi} (RN-CUM-009)"
            )

        unidade = UnidadeAdministrativa(
            nome=command.nome,
            unidade_pai_id=command.unidade_pai_id,
            sigla=command.sigla,
            codigo_ibge=command.codigo_ibge,
            codigo_siafi=command.codigo_siafi,
            created_by=command.usuario_id,
        )

        # RN-CUM-008: o repositório valida ciclos de hierarquia no save
        salvo = self._repository.save(unidade)

        evento = UnidadeRegistradaEvent(
            event_id=uuid4(),
            unidade_id=salvo.id,
            nome=salvo.nome,
            sigla=salvo.sigla,
            occurred_at=salvo.created_at,
        )
        logger.info("Unidade administrativa registrada: %s", evento)
        return salvo


__all__ = ["RegistrarUnidadeUseCase"]
