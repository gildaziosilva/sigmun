"""Casos de uso para gerenciamento de Termos de Taxonomia."""

import logging

from src.modules.sigmun_met.application.interfaces import (
    TaxonomiaRepositoryInterface,
    TermoTaxonomiaRepositoryInterface,
)
from src.modules.sigmun_met.domain.entities import TermoTaxonomia
from src.modules.sigmun_met.domain.exceptions import (
    CodigoInvalidoError,
    TaxonomiaNaoEncontradaError,
    TermoNaoEncontradoError,
)
from src.modules.sigmun_met.domain.services import TaxonomiaService
from src.modules.sigmun_met.domain.value_objects import CodigoMetadado, NomeEntidade

logger = logging.getLogger(__name__)


class CriarTermoUseCase:
    """Caso de uso para criar um novo termo de taxonomia."""

    def __init__(
        self,
        termo_repo: TermoTaxonomiaRepositoryInterface,
        taxonomia_repo: TaxonomiaRepositoryInterface,
    ):
        self._termo_repo = termo_repo
        self._taxonomia_repo = taxonomia_repo

    def execute(
        self,
        taxonomia_id: str,
        codigo: str,
        nome: str,
        descricao: str = "",
        termo_pai_id: str = "",
        sinonimos: list[str] = None,
        ordem: int = 0,
    ) -> TermoTaxonomia:
        """Cria um novo termo dentro de uma taxonomia."""
        valido, msg = CodigoMetadado.validar(codigo)
        if not valido:
            raise CodigoInvalidoError(f"Código inválido: {msg}")

        valido, msg = NomeEntidade.validar(nome)
        if not valido:
            raise ValueError(f"Nome inválido: {msg}")

        taxonomia = self._taxonomia_repo.get_by_id(taxonomia_id)
        if taxonomia is None:
            raise TaxonomiaNaoEncontradaError(f"Taxonomia '{taxonomia_id}' não encontrada")

        # Valida unicidade do código dentro da taxonomia
        termos_existentes = self._termo_repo.get_by_taxonomia(taxonomia_id)
        TaxonomiaService.validar_codigo_unico_na_taxonomia(termos_existentes, taxonomia_id, codigo)

        termo = TermoTaxonomia(
            taxonomia_id=taxonomia_id,
            termo_pai_id=termo_pai_id,
            codigo=codigo,
            nome=nome,
            descricao=descricao,
            sinonimos=sinonimos or [],
            ordem=ordem,
        )
        logger.info("Termo criado: %s na taxonomia %s", termo.codigo, taxonomia.codigo)
        return self._termo_repo.save(termo)


class AtualizarTermoUseCase:
    """Caso de uso para atualizar um termo de taxonomia."""

    def __init__(self, repository: TermoTaxonomiaRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        termo_id: str,
        nome: str | None = None,
        descricao: str | None = None,
        sinonimos: list[str] | None = None,
        ordem: int | None = None,
    ) -> TermoTaxonomia:
        """Atualiza um termo existente (não permite mudar hierarquia por aqui)."""
        termo = self._repo.get_by_id(termo_id)
        if termo is None:
            raise TermoNaoEncontradoError(f"Termo '{termo_id}' não encontrado")

        if nome is not None:
            valido, msg = NomeEntidade.validar(nome)
            if not valido:
                raise ValueError(f"Nome inválido: {msg}")
            termo.nome = nome
        if descricao is not None:
            termo.descricao = descricao
        if sinonimos is not None:
            termo.sinonimos = sinonimos
        if ordem is not None:
            termo.ordem = ordem

        from datetime import datetime
        termo.updated_at = datetime.utcnow()
        return self._repo.save(termo)


class BuscarTermoUseCase:
    """Caso de uso para buscar termos de taxonomia."""

    def __init__(self, repository: TermoTaxonomiaRepositoryInterface):
        self._repo = repository

    def get_by_id(self, termo_id: str) -> TermoTaxonomia:
        """Busca termo por ID."""
        termo = self._repo.get_by_id(termo_id)
        if termo is None:
            raise TermoNaoEncontradoError(f"Termo '{termo_id}' não encontrado")
        return termo

    def get_by_taxonomia(self, taxonomia_id: str) -> list[TermoTaxonomia]:
        """Busca todos os termos de uma taxonomia."""
        return self._repo.get_by_taxonomia(taxonomia_id)

    def get_by_pai(self, termo_pai_id: str) -> list[TermoTaxonomia]:
        """Busca termos filhos diretos de um termo pai."""
        return self._repo.get_by_pai(termo_pai_id)

    def list_all(
        self, page: int = 0, page_size: int = 50, taxonomia_id: str | None = None,
    ) -> tuple:
        """Lista termos com paginação."""
        return self._repo.list_all(page, page_size, taxonomia_id)


class DeletarTermoUseCase:
    """Caso de uso para deletar um termo de taxonomia."""

    def __init__(self, repository: TermoTaxonomiaRepositoryInterface):
        self._repo = repository

    def execute(self, termo_id: str) -> bool:
        """Deleta um termo."""
        termo = self._repo.get_by_id(termo_id)
        if termo is None:
            raise TermoNaoEncontradoError(f"Termo '{termo_id}' não encontrado")
        logger.info("Termo deletado: %s", termo.codigo)
        return self._repo.delete(termo_id)


__all__ = [
    "CriarTermoUseCase",
    "AtualizarTermoUseCase",
    "BuscarTermoUseCase",
    "DeletarTermoUseCase",
]
