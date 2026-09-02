"""Caso de uso: Listar Pessoas (DOM-CUM)."""

from __future__ import annotations

import logging

from src.modules.sigmun_cadastro.application.queries.pessoa_queries import (
    ListarPessoasQuery,
)
from src.modules.sigmun_cadastro.domain.entities.pessoa import Pessoa
from src.modules.sigmun_cadastro.domain.repositories.pessoa_repository import (
    PessoaRepository,
)

logger = logging.getLogger(__name__)


class ListarPessoasUseCase:
    """Lista pessoas com filtros e paginação."""

    def __init__(self, repository: PessoaRepository) -> None:
        self._repository = repository

    def execute(self, query: ListarPessoasQuery) -> list[Pessoa]:
        return self._repository.list(
            tipo=query.tipo,
            categoria=query.categoria,
            include_deleted=query.include_deleted,
            limit=query.limit,
            offset=query.offset,
        )


__all__ = ["ListarPessoasUseCase"]
