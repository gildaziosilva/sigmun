"""Caso de uso: Listar Unidades Administrativas (DOM-CUM)."""

from __future__ import annotations

import logging

from src.modules.sigmun_cadastro.application.queries.unidade_queries import (
    ListarUnidadesQuery,
)
from src.modules.sigmun_cadastro.domain.entities.unidade_administrativa import (
    UnidadeAdministrativa,
)
from src.modules.sigmun_cadastro.domain.repositories.unidade_administrativa_repository import (
    UnidadeAdministrativaRepository,
)

logger = logging.getLogger(__name__)


class ListarUnidadesUseCase:
    """Lista unidades administrativas com paginação."""

    def __init__(self, repository: UnidadeAdministrativaRepository) -> None:
        self._repository = repository

    def execute(self, query: ListarUnidadesQuery) -> list[UnidadeAdministrativa]:
        return self._repository.list(
            include_deleted=query.include_deleted,
            limit=query.limit,
            offset=query.offset,
        )


__all__ = ["ListarUnidadesUseCase"]
