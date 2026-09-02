"""Caso de uso: Listar Fornecedores.

Baseado em:
  - SRV-COMPRAS-007 – Gestão de Fornecedores
  - Operação: buscarFornecedores()
  - UC-COMPRAS-020 – Consultar Fornecedor
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.queries.listar_fornecedores_query import (
    ListarFornecedoresQuery,
)
from src.modules.sigmun_compras.domain.entities.fornecedor import Fornecedor
from src.modules.sigmun_compras.domain.repositories.fornecedor_repository import (
    FornecedorRepository,
)

logger = logging.getLogger(__name__)


class ListarFornecedoresUseCase:
    """Orquestra a listagem de fornecedores com filtros."""

    def __init__(self, repository: FornecedorRepository) -> None:
        self._repository = repository

    def execute(self, query: ListarFornecedoresQuery) -> list[Fornecedor]:
        logger.info(
            "Listando fornecedores – situacao=%s, include_inativos=%s",
            query.situacao,
            query.include_inativos,
        )

        offset = query.page * query.page_size

        return self._repository.list(
            situacao=query.situacao,
            include_deleted=query.include_inativos,
            limit=query.page_size,
            offset=offset,
        )
