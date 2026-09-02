"""Caso de uso: Consultar Pessoa (DOM-CUM)."""

from __future__ import annotations

import logging

from src.modules.sigmun_cadastro.application.queries.pessoa_queries import (
    ConsultarPessoaQuery,
)
from src.modules.sigmun_cadastro.domain.entities.pessoa import Pessoa
from src.modules.sigmun_cadastro.domain.exceptions import PessoaNaoEncontradoError
from src.modules.sigmun_cadastro.domain.repositories.pessoa_repository import (
    PessoaRepository,
)

logger = logging.getLogger(__name__)


class ConsultarPessoaUseCase:
    """Consulta o agregado Pessoa hidratado (endereços/documentos/contatos)."""

    def __init__(self, repository: PessoaRepository) -> None:
        self._repository = repository

    def execute(self, query: ConsultarPessoaQuery) -> Pessoa:
        pessoa = self._repository.get_by_id(
            query.pessoa_id, include_deleted=query.include_deleted
        )
        if pessoa is None:
            raise PessoaNaoEncontradoError(
                f"Pessoa {query.pessoa_id} não encontrada"
            )
        return pessoa


__all__ = ["ConsultarPessoaUseCase"]
