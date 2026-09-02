"""Caso de uso: Consultar Fornecedor.

Baseado em:
  - UC-COMPRAS-020 – Consultar Fornecedor
  - HU-COMPRAS-020 – Consultar Fornecedor
  - RF-COMPRAS-034 – Consultar Fornecedor (P1)
  - RN-COMPRAS-033 – Dados Cadastrais
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.queries.consultar_fornecedor_query import (
    ConsultarFornecedorPorPessoaJuridicaQuery,
    ConsultarFornecedorQuery,
)
from src.modules.sigmun_compras.domain.entities.fornecedor import Fornecedor
from src.modules.sigmun_compras.domain.exceptions import (
    FornecedorNaoEncontradoError,
)
from src.modules.sigmun_compras.domain.repositories.fornecedor_repository import (
    FornecedorRepository,
)

logger = logging.getLogger(__name__)


class ConsultarFornecedorUseCase:
    """Orquestra a consulta de dados cadastrais de um fornecedor."""

    def __init__(self, repository: FornecedorRepository) -> None:
        self._repository = repository

    def execute(self, query: ConsultarFornecedorQuery) -> Fornecedor:
        logger.info("Consultando fornecedor por ID – id=%s", query.fornecedor_id)

        fornecedor = self._repository.get_by_id(query.fornecedor_id)
        if fornecedor is None or fornecedor.foi_excluido():
            raise FornecedorNaoEncontradoError(
                f"Fornecedor {query.fornecedor_id} não encontrado"
            )

        return fornecedor

    def execute_por_pessoa_juridica(
        self, query: ConsultarFornecedorPorPessoaJuridicaQuery
    ) -> Fornecedor | None:
        """Retorna o fornecedor ou None se não existir."""
        logger.info(
            "Consultando fornecedor por pessoa_juridica_id – id=%s",
            query.pessoa_juridica_id,
        )

        fornecedor = self._repository.get_by_pessoa_juridica_id(
            query.pessoa_juridica_id
        )
        if fornecedor is None or fornecedor.foi_excluido():
            return None

        return fornecedor
