"""Casos de uso para gerenciamento de Linhagens de Dados."""

import logging

from src.modules.sigmun_dad.application.interfaces import LinhagemRepositoryInterface
from src.modules.sigmun_dad.domain.entities import LinhagemDado
from src.modules.sigmun_dad.domain.exceptions import (
    LinhagemJaExisteError,
    LinhagemNaoEncontradaError,
)

logger = logging.getLogger(__name__)


class CriarLinhagemUseCase:
    """Caso de uso para criar uma nova linhagem."""

    def __init__(self, repository: LinhagemRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        ativo_origem_id: str,
        ativo_destino_id: str,
        tipo_transformacao: str = "",
        descricao: str = "",
        regras: str = "",
    ) -> LinhagemDado:
        """Cria uma nova linhagem."""
        if not ativo_origem_id:
            raise ValueError("ID do ativo de origem é obrigatório")
        if not ativo_destino_id:
            raise ValueError("ID do ativo de destino é obrigatório")
        if ativo_origem_id == ativo_destino_id:
            raise ValueError("Ativo de origem e destino devem ser diferentes")

        if self._repo.exists_linhagem(ativo_origem_id, ativo_destino_id):
            raise LinhagemJaExisteError(
                f"Já existe linhagem entre '{ativo_origem_id}' e '{ativo_destino_id}'"
            )

        linhagem = LinhagemDado(
            ativo_origem_id=ativo_origem_id,
            ativo_destino_id=ativo_destino_id,
            tipo_transformacao=tipo_transformacao,
            descricao=descricao,
            regras=regras,
        )
        return self._repo.save(linhagem)


class AtualizarLinhagemUseCase:
    """Caso de uso para atualizar uma linhagem."""

    def __init__(self, repository: LinhagemRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        linhagem_id: str,
        tipo_transformacao: str | None = None,
        descricao: str | None = None,
        regras: str | None = None,
    ) -> LinhagemDado:
        """Atualiza uma linhagem."""
        linhagem = self._repo.get_by_id(linhagem_id)
        if linhagem is None:
            raise LinhagemNaoEncontradaError(f"Linhagem '{linhagem_id}' não encontrada")

        if tipo_transformacao is not None:
            linhagem.tipo_transformacao = tipo_transformacao
        if descricao is not None:
            linhagem.descricao = descricao
        if regras is not None:
            linhagem.regras = regras

        return self._repo.save(linhagem)


class BuscarLinhagemUseCase:
    """Caso de uso para buscar linhagens."""

    def __init__(self, repository: LinhagemRepositoryInterface):
        self._repo = repository

    def get_by_id(self, linhagem_id: str) -> LinhagemDado:
        """Busca linhagem por ID."""
        linhagem = self._repo.get_by_id(linhagem_id)
        if linhagem is None:
            raise LinhagemNaoEncontradaError(f"Linhagem '{linhagem_id}' não encontrada")
        return linhagem

    def get_by_origem(self, ativo_origem_id: str) -> list:
        """Busca linhagens por ativo de origem."""
        return self._repo.get_by_origem(ativo_origem_id)

    def get_by_destino(self, ativo_destino_id: str) -> list:
        """Busca linhagens por ativo de destino."""
        return self._repo.get_by_destino(ativo_destino_id)

    def list_all(self, page: int = 0, page_size: int = 50) -> tuple:
        """Lista linhagens com paginação."""
        return self._repo.list_all(page, page_size)


class DeletarLinhagemUseCase:
    """Caso de uso para deletar uma linhagem."""

    def __init__(self, repository: LinhagemRepositoryInterface):
        self._repo = repository

    def execute(self, linhagem_id: str) -> bool:
        """Deleta uma linhagem."""
        linhagem = self._repo.get_by_id(linhagem_id)
        if linhagem is None:
            raise LinhagemNaoEncontradaError(f"Linhagem '{linhagem_id}' não encontrada")
        return self._repo.delete(linhagem_id)


__all__ = [
    "CriarLinhagemUseCase",
    "AtualizarLinhagemUseCase",
    "BuscarLinhagemUseCase",
    "DeletarLinhagemUseCase",
]
