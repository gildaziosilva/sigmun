"""Casos de uso para gerenciamento de Políticas de Dados."""

import logging

from src.modules.sigmun_dad.application.interfaces import PoliticaRepositoryInterface
from src.modules.sigmun_dad.domain.entities import PoliticaDado
from src.modules.sigmun_dad.domain.exceptions import (
    PoliticaJaExisteError,
    PoliticaNaoEncontradaError,
)

logger = logging.getLogger(__name__)


class CriarPoliticaUseCase:
    """Caso de uso para criar uma nova política."""

    def __init__(self, repository: PoliticaRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        codigo: str,
        nome: str,
        descricao: str = "",
        tipo: str = "",
        regras: list[str] | None = None,
    ) -> PoliticaDado:
        """Cria uma nova política."""
        if not codigo or len(codigo.strip()) < 2:
            raise ValueError("Código da política deve ter pelo menos 2 caracteres")
        if not nome or len(nome.strip()) < 3:
            raise ValueError("Nome da política deve ter pelo menos 3 caracteres")

        if self._repo.exists_by_codigo(codigo):
            raise PoliticaJaExisteError(f"Política com código '{codigo}' já existe")

        politica = PoliticaDado(
            codigo=codigo,
            nome=nome,
            descricao=descricao,
            tipo=tipo,
            regras=regras or [],
        )
        return self._repo.save(politica)


class AtualizarPoliticaUseCase:
    """Caso de uso para atualizar uma política."""

    def __init__(self, repository: PoliticaRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        politica_id: str,
        nome: str | None = None,
        descricao: str | None = None,
        tipo: str | None = None,
    ) -> PoliticaDado:
        """Atualiza uma política."""
        politica = self._repo.get_by_id(politica_id)
        if politica is None:
            raise PoliticaNaoEncontradaError(f"Política '{politica_id}' não encontrada")

        if nome is not None:
            politica.nome = nome
        if descricao is not None:
            politica.descricao = descricao
        if tipo is not None:
            politica.tipo = tipo

        from datetime import datetime
        politica.updated_at = datetime.utcnow()
        return self._repo.save(politica)


class BuscarPoliticaUseCase:
    """Caso de uso para buscar políticas."""

    def __init__(self, repository: PoliticaRepositoryInterface):
        self._repo = repository

    def get_by_id(self, politica_id: str) -> PoliticaDado:
        """Busca política por ID."""
        politica = self._repo.get_by_id(politica_id)
        if politica is None:
            raise PoliticaNaoEncontradaError(f"Política '{politica_id}' não encontrada")
        return politica

    def get_by_codigo(self, codigo: str) -> PoliticaDado:
        """Busca política por código."""
        politica = self._repo.get_by_codigo(codigo)
        if politica is None:
            raise PoliticaNaoEncontradaError(f"Política com código '{codigo}' não encontrada")
        return politica

    def list_all(self, page: int = 0, page_size: int = 50) -> tuple:
        """Lista políticas com paginação."""
        return self._repo.list_all(page, page_size)


class DeletarPoliticaUseCase:
    """Caso de uso para deletar uma política."""

    def __init__(self, repository: PoliticaRepositoryInterface):
        self._repo = repository

    def execute(self, politica_id: str) -> bool:
        """Deleta uma política."""
        politica = self._repo.get_by_id(politica_id)
        if politica is None:
            raise PoliticaNaoEncontradaError(f"Política '{politica_id}' não encontrada")
        return self._repo.delete(politica_id)


class AdicionarRegraPoliticaUseCase:
    """Caso de uso para adicionar regra à política."""

    def __init__(self, repository: PoliticaRepositoryInterface):
        self._repo = repository

    def execute(self, politica_id: str, regra: str) -> PoliticaDado:
        """Adiciona regra à política."""
        politica = self._repo.get_by_id(politica_id)
        if politica is None:
            raise PoliticaNaoEncontradaError(f"Política '{politica_id}' não encontrada")

        politica.add_rule(regra)
        return self._repo.save(politica)


class RemoverRegraPoliticaUseCase:
    """Caso de uso para remover regra da política."""

    def __init__(self, repository: PoliticaRepositoryInterface):
        self._repo = repository

    def execute(self, politica_id: str, regra: str) -> PoliticaDado:
        """Remove regra da política."""
        politica = self._repo.get_by_id(politica_id)
        if politica is None:
            raise PoliticaNaoEncontradaError(f"Política '{politica_id}' não encontrada")

        politica.remove_rule(regra)
        return self._repo.save(politica)


__all__ = [
    "CriarPoliticaUseCase",
    "AtualizarPoliticaUseCase",
    "BuscarPoliticaUseCase",
    "DeletarPoliticaUseCase",
    "AdicionarRegraPoliticaUseCase",
    "RemoverRegraPoliticaUseCase",
]
