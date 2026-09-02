"""Caso de uso: Consultar Contrato."""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.queries.consultar_contrato_query import (
    ConsultarContratoQuery,
)
from src.modules.sigmun_compras.domain.entities.contrato import Contrato
from src.modules.sigmun_compras.domain.exceptions import (
    ContratoNaoEncontradoError,
)
from src.modules.sigmun_compras.domain.repositories.contrato_repository import (
    ContratoRepository,
)

logger = logging.getLogger(__name__)


class ConsultarContratoUseCase:
    """Orquestra a consulta de um contrato."""

    def __init__(self, repository: ContratoRepository) -> None:
        self._repository = repository

    def execute(self, query: ConsultarContratoQuery) -> Contrato:
        logger.info("Consultando contrato – id=%s", query.contrato_id)

        contrato = self._repository.get_by_id(query.contrato_id)
        if contrato is None or contrato.foi_excluido():
            raise ContratoNaoEncontradoError(
                f"Contrato {query.contrato_id} não encontrado"
            )

        return contrato
