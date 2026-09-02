"""Caso de uso: Listar Contratos."""

from __future__ import annotations

import logging
from typing import List

from src.modules.sigmun_compras.application.queries.listar_contratos_query import (
    ListarContratosQuery,
)
from src.modules.sigmun_compras.domain.entities.contrato import Contrato
from src.modules.sigmun_compras.domain.repositories.contrato_repository import (
    ContratoRepository,
)

logger = logging.getLogger(__name__)


class ListarContratosUseCase:
    """Orquestra a listagem paginada de contratos com filtros."""

    def __init__(self, repository: ContratoRepository) -> None:
        self._repository = repository

    def execute(self, query: ListarContratosQuery) -> List[Contrato]:
        logger.info(
            "Listando contratos – situacao=%s fornecedor=%s",
            query.situacao,
            query.fornecedor_id,
        )

        offset = query.page * query.page_size

        return self._repository.list(
            situacao=query.situacao,
            fornecedor_id=query.fornecedor_id,
            unidade_id=query.unidade_id,
            include_deleted=query.include_inativos,
            limit=query.page_size,
            offset=offset,
        )
