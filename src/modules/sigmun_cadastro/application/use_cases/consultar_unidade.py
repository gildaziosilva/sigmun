"""Caso de uso: Consultar Unidade Administrativa (DOM-CUM)."""

from __future__ import annotations

import logging

from src.modules.sigmun_cadastro.application.queries.unidade_queries import (
    ConsultarUnidadeQuery,
)
from src.modules.sigmun_cadastro.domain.entities.unidade_administrativa import (
    UnidadeAdministrativa,
)
from src.modules.sigmun_cadastro.domain.exceptions import UnidadeNaoEncontradaError
from src.modules.sigmun_cadastro.domain.repositories.unidade_administrativa_repository import (
    UnidadeAdministrativaRepository,
)

logger = logging.getLogger(__name__)


class ConsultarUnidadeUseCase:
    """Consulta uma unidade administrativa pelo ID."""

    def __init__(self, repository: UnidadeAdministrativaRepository) -> None:
        self._repository = repository

    def execute(self, query: ConsultarUnidadeQuery) -> UnidadeAdministrativa:
        unidade = self._repository.get_by_id(
            query.unidade_id, include_deleted=query.include_deleted
        )
        if unidade is None:
            raise UnidadeNaoEncontradaError(
                f"Unidade administrativa {query.unidade_id} não encontrada"
            )
        return unidade


__all__ = ["ConsultarUnidadeUseCase"]
