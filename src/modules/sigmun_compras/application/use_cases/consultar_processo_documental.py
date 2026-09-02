"""Caso de uso: Consultar Processo Documental."""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.queries.consultar_processo_documental_query import (
    ConsultarProcessoDocumentalQuery,
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


class ConsultarProcessoDocumentalUseCase:
    """Orquestra a consulta de um processo documental."""

    def __init__(self, repository: ProcessoDocumentalRepository) -> None:
        self._repository = repository

    def execute(
        self, query: ConsultarProcessoDocumentalQuery
    ) -> ProcessoDocumental:
        logger.info("Consultando processo documental – id=%s", query.processo_id)

        processo = self._repository.get_by_id(query.processo_id)
        if processo is None or processo.foi_excluido():
            raise ProcessoDocumentalNaoEncontradoError(
                f"Processo documental {query.processo_id} não encontrado"
            )

        return processo
