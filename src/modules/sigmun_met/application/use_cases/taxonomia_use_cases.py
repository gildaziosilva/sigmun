"""Casos de uso para gerenciamento de Taxonomias."""

import logging

from src.modules.sigmun_met.application.interfaces import TaxonomiaRepositoryInterface
from src.modules.sigmun_met.domain.entities import Taxonomia
from src.modules.sigmun_met.domain.exceptions import (
    CodigoInvalidoError,
    TaxonomiaJaExisteError,
    TaxonomiaNaoEncontradaError,
)
from src.modules.sigmun_met.domain.value_objects import CodigoMetadado, NomeEntidade

logger = logging.getLogger(__name__)


class CriarTaxonomiaUseCase:
    """Caso de uso para criar uma nova taxonomia."""

    def __init__(self, repository: TaxonomiaRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        codigo: str,
        nome: str,
        descricao: str = "",
    ) -> Taxonomia:
        """Cria uma nova taxonomia."""
        valido, msg = CodigoMetadado.validar(codigo)
        if not valido:
            raise CodigoInvalidoError(f"Código inválido: {msg}")

        valido, msg = NomeEntidade.validar(nome)
        if not valido:
            raise ValueError(f"Nome inválido: {msg}")

        if self._repo.exists_by_codigo(codigo):
            raise TaxonomiaJaExisteError(f"Taxonomia com código '{codigo}' já existe")

        taxonomia = Taxonomia(
            codigo=codigo,
            nome=nome,
            descricao=descricao,
        )
        logger.info("Taxonomia criada: %s", taxonomia.codigo)
        return self._repo.save(taxonomia)


class AtualizarTaxonomiaUseCase:
    """Caso de uso para atualizar uma taxonomia."""

    def __init__(self, repository: TaxonomiaRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        taxonomia_id: str,
        nome: str | None = None,
        descricao: str | None = None,
    ) -> Taxonomia:
        """Atualiza uma taxonomia existente."""
        taxonomia = self._repo.get_by_id(taxonomia_id)
        if taxonomia is None:
            raise TaxonomiaNaoEncontradaError(f"Taxonomia '{taxonomia_id}' não encontrada")

        if nome is not None:
            valido, msg = NomeEntidade.validar(nome)
            if not valido:
                raise ValueError(f"Nome inválido: {msg}")
            taxonomia.nome = nome
        if descricao is not None:
            taxonomia.descricao = descricao

        from datetime import datetime
        taxonomia.updated_at = datetime.utcnow()
        return self._repo.save(taxonomia)


class BuscarTaxonomiaUseCase:
    """Caso de uso para buscar taxonomias."""

    def __init__(self, repository: TaxonomiaRepositoryInterface):
        self._repo = repository

    def get_by_id(self, taxonomia_id: str) -> Taxonomia:
        """Busca taxonomia por ID."""
        taxonomia = self._repo.get_by_id(taxonomia_id)
        if taxonomia is None:
            raise TaxonomiaNaoEncontradaError(f"Taxonomia '{taxonomia_id}' não encontrada")
        return taxonomia

    def get_by_codigo(self, codigo: str) -> Taxonomia:
        """Busca taxonomia por código."""
        taxonomia = self._repo.get_by_codigo(codigo)
        if taxonomia is None:
            raise TaxonomiaNaoEncontradaError(
                f"Taxonomia com código '{codigo}' não encontrada"
            )
        return taxonomia

    def list_all(self, page: int = 0, page_size: int = 50) -> tuple:
        """Lista taxonomias com paginação."""
        return self._repo.list_all(page, page_size)


class DeletarTaxonomiaUseCase:
    """Caso de uso para deletar uma taxonomia."""

    def __init__(self, repository: TaxonomiaRepositoryInterface):
        self._repo = repository

    def execute(self, taxonomia_id: str) -> bool:
        """Deleta uma taxonomia."""
        taxonomia = self._repo.get_by_id(taxonomia_id)
        if taxonomia is None:
            raise TaxonomiaNaoEncontradaError(f"Taxonomia '{taxonomia_id}' não encontrada")
        return self._repo.delete(taxonomia_id)


__all__ = [
    "CriarTaxonomiaUseCase",
    "AtualizarTaxonomiaUseCase",
    "BuscarTaxonomiaUseCase",
    "DeletarTaxonomiaUseCase",
]
