"""Caso de uso: Consultar Compra (processo de compras)."""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.queries.consultar_compra_query import (
    ConsultarCompraQuery,
)
from src.modules.sigmun_compras.domain.entities.compra import Compra
from src.modules.sigmun_compras.domain.exceptions import CompraNaoEncontradaError
from src.modules.sigmun_compras.domain.repositories.compra_repository import (
    CompraRepository,
)

logger = logging.getLogger(__name__)


class ConsultarCompraUseCase:
    """Orquestra a consulta de uma compra."""

    def __init__(self, repository: CompraRepository) -> None:
        self._repository = repository

    def execute(self, query: ConsultarCompraQuery) -> Compra:
        logger.info("Consultando compra – id=%s", query.compra_id)

        compra = self._repository.get_by_id(query.compra_id)
        if compra is None or compra.foi_excluido():
            raise CompraNaoEncontradaError(
                f"Compra {query.compra_id} não encontrada"
            )

        return compra
