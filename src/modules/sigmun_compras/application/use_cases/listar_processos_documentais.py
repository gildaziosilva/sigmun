"""Caso de uso: Listar Processos Documentais."""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.queries.listar_processos_documentais_query import (
    ListarProcessosDocumentaisQuery,
)
from src.modules.sigmun_compras.domain.entities.processo_documental import (
    ProcessoDocumental,
)
from src.modules.sigmun_compras.domain.repositories.processo_documental_repository import (
    ProcessoDocumentalRepository,
)

logger = logging.getLogger(__name__)


class ListarProcessosDocumentaisUseCase:
    """Orquestra a listagem paginada de processos documentais."""

    def __init__(self, repository: ProcessoDocumentalRepository) -> None:
        self._repository = repository

    def execute(
        self, query: ListarProcessosDocumentaisQuery
    ) -> list[ProcessoDocumental]:
        logger.info(
            "Listando processos documentais – unidade=%s ano=%s",
            query.unidade_id,
            query.ano,
        )

        offset = query.page * query.page_size

        return self._repository.list(
            unidade_id=query.unidade_id,
            ano=query.ano,
            include_deleted=query.include_inativos,
            limit=query.page_size,
            offset=offset,
        )
