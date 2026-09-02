"""Casos de uso para gerenciamento de Catálogos de Dados."""

import logging

from src.modules.sigmun_dad.application.interfaces import CatalogoRepositoryInterface
from src.modules.sigmun_dad.domain.entities import Catalogo
from src.modules.sigmun_dad.domain.exceptions import (
    CatalogoJaExisteError,
    CatalogoNaoEncontradoError,
)

logger = logging.getLogger(__name__)


class CriarCatalogoUseCase:
    """Caso de uso para criar um novo catálogo."""

    def __init__(self, repository: CatalogoRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        nome: str,
        descricao: str = "",
        dominio: str = "",
    ) -> Catalogo:
        """Cria um novo catálogo."""
        if not nome or len(nome.strip()) < 3:
            raise ValueError("Nome do catálogo deve ter pelo menos 3 caracteres")

        if self._repo.exists_by_nome(nome):
            raise CatalogoJaExisteError(f"Catálogo com nome '{nome}' já existe")

        catalogo = Catalogo(
            nome=nome,
            descricao=descricao,
            dominio=dominio,
        )
        return self._repo.save(catalogo)


class AtualizarCatalogoUseCase:
    """Caso de uso para atualizar um catálogo."""

    def __init__(self, repository: CatalogoRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        catalogo_id: str,
        nome: str | None = None,
        descricao: str | None = None,
        dominio: str | None = None,
    ) -> Catalogo:
        """Atualiza um catálogo."""
        catalogo = self._repo.get_by_id(catalogo_id)
        if catalogo is None:
            raise CatalogoNaoEncontradoError(f"Catálogo '{catalogo_id}' não encontrado")

        if nome is not None:
            catalogo.nome = nome
        if descricao is not None:
            catalogo.descricao = descricao
        if dominio is not None:
            catalogo.dominio = dominio

        from datetime import datetime
        catalogo.updated_at = datetime.utcnow()
        return self._repo.save(catalogo)


class BuscarCatalogoUseCase:
    """Caso de uso para buscar catálogos."""

    def __init__(self, repository: CatalogoRepositoryInterface):
        self._repo = repository

    def get_by_id(self, catalogo_id: str) -> Catalogo:
        """Busca catálogo por ID."""
        catalogo = self._repo.get_by_id(catalogo_id)
        if catalogo is None:
            raise CatalogoNaoEncontradoError(f"Catálogo '{catalogo_id}' não encontrado")
        return catalogo

    def get_by_nome(self, nome: str) -> Catalogo:
        """Busca catálogo por nome."""
        catalogo = self._repo.get_by_nome(nome)
        if catalogo is None:
            raise CatalogoNaoEncontradoError(f"Catálogo com nome '{nome}' não encontrado")
        return catalogo

    def list_all(self, page: int = 0, page_size: int = 50) -> tuple:
        """Lista catálogos com paginação."""
        return self._repo.list_all(page, page_size)


class DeletarCatalogoUseCase:
    """Caso de uso para deletar um catálogo."""

    def __init__(self, repository: CatalogoRepositoryInterface):
        self._repo = repository

    def execute(self, catalogo_id: str) -> bool:
        """Deleta um catálogo."""
        catalogo = self._repo.get_by_id(catalogo_id)
        if catalogo is None:
            raise CatalogoNaoEncontradoError(f"Catálogo '{catalogo_id}' não encontrado")
        return self._repo.delete(catalogo_id)


class AdicionarAtivoCatalogoUseCase:
    """Caso de uso para adicionar ativo ao catálogo."""

    def __init__(
        self,
        catalogo_repo: CatalogoRepositoryInterface,
        ativo_repo,
    ):
        self._catalogo_repo = catalogo_repo
        self._ativo_repo = ativo_repo

    def execute(self, catalogo_id: str, ativo_id: str) -> Catalogo:
        """Adiciona ativo ao catálogo."""
        catalogo = self._catalogo_repo.get_by_id(catalogo_id)
        if catalogo is None:
            raise CatalogoNaoEncontradoError(f"Catálogo '{catalogo_id}' não encontrado")

        ativo = self._ativo_repo.get_by_id(ativo_id)
        if ativo is None:
            from src.modules.sigmun_dad.domain.exceptions import AtivoNaoEncontradoError
            raise AtivoNaoEncontradoError(f"Ativo '{ativo_id}' não encontrado")

        catalogo.add_ativo(ativo_id)
        return self._catalogo_repo.save(catalogo)


class RemoverAtivoCatalogoUseCase:
    """Caso de uso para remover ativo do catálogo."""

    def __init__(self, repository: CatalogoRepositoryInterface):
        self._repo = repository

    def execute(self, catalogo_id: str, ativo_id: str) -> Catalogo:
        """Remove ativo do catálogo."""
        catalogo = self._repo.get_by_id(catalogo_id)
        if catalogo is None:
            raise CatalogoNaoEncontradoError(f"Catálogo '{catalogo_id}' não encontrado")

        catalogo.remove_ativo(ativo_id)
        return self._repo.save(catalogo)


__all__ = [
    "CriarCatalogoUseCase",
    "AtualizarCatalogoUseCase",
    "BuscarCatalogoUseCase",
    "DeletarCatalogoUseCase",
    "AdicionarAtivoCatalogoUseCase",
    "RemoverAtivoCatalogoUseCase",
]
