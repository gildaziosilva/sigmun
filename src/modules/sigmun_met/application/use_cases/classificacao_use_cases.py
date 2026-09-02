"""Casos de uso para gerenciamento de Classificações."""

import logging

from src.modules.sigmun_met.application.interfaces import (
    ClassificacaoRepositoryInterface,
)
from src.modules.sigmun_met.domain.entities import (
    Classificacao,
    TipoClassificacao,
)
from src.modules.sigmun_met.domain.exceptions import (
    ClassificacaoJaExisteError,
    ClassificacaoNaoEncontradaError,
    CodigoInvalidoError,
)
from src.modules.sigmun_met.domain.value_objects import CodigoMetadado, NomeEntidade

logger = logging.getLogger(__name__)


class CriarClassificacaoUseCase:
    """Caso de uso para criar uma nova classificação."""

    def __init__(self, repository: ClassificacaoRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        codigo: str,
        nome: str,
        descricao: str = "",
        tipo: str = "confidencialidade",
        nivel: int = 0,
        cor: str = "",
    ) -> Classificacao:
        """Cria uma nova classificação."""
        valido, msg = CodigoMetadado.validar(codigo)
        if not valido:
            raise CodigoInvalidoError(f"Código inválido: {msg}")

        valido, msg = NomeEntidade.validar(nome)
        if not valido:
            raise ValueError(f"Nome inválido: {msg}")

        if self._repo.exists_by_codigo(codigo):
            raise ClassificacaoJaExisteError(f"Classificação com código '{codigo}' já existe")

        classificacao = Classificacao(
            codigo=codigo,
            nome=nome,
            descricao=descricao,
            tipo=TipoClassificacao(tipo),
            nivel=nivel,
            cor=cor,
        )
        logger.info("Classificação criada: %s", classificacao.codigo)
        return self._repo.save(classificacao)


class AtualizarClassificacaoUseCase:
    """Caso de uso para atualizar uma classificação."""

    def __init__(self, repository: ClassificacaoRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        classificacao_id: str,
        nome: str | None = None,
        descricao: str | None = None,
        tipo: str | None = None,
        nivel: int | None = None,
        cor: str | None = None,
    ) -> Classificacao:
        """Atualiza uma classificação existente."""
        classificacao = self._repo.get_by_id(classificacao_id)
        if classificacao is None:
            raise ClassificacaoNaoEncontradaError(
                f"Classificação '{classificacao_id}' não encontrada"
            )

        if nome is not None:
            valido, msg = NomeEntidade.validar(nome)
            if not valido:
                raise ValueError(f"Nome inválido: {msg}")
            classificacao.nome = nome
        if descricao is not None:
            classificacao.descricao = descricao
        if tipo is not None:
            classificacao.tipo = TipoClassificacao(tipo)
        if nivel is not None:
            classificacao.nivel = nivel
        if cor is not None:
            classificacao.cor = cor

        from datetime import datetime
        classificacao.updated_at = datetime.utcnow()
        return self._repo.save(classificacao)


class BuscarClassificacaoUseCase:
    """Caso de uso para buscar classificações."""

    def __init__(self, repository: ClassificacaoRepositoryInterface):
        self._repo = repository

    def get_by_id(self, classificacao_id: str) -> Classificacao:
        """Busca classificação por ID."""
        classificacao = self._repo.get_by_id(classificacao_id)
        if classificacao is None:
            raise ClassificacaoNaoEncontradaError(
                f"Classificação '{classificacao_id}' não encontrada"
            )
        return classificacao

    def get_by_codigo(self, codigo: str) -> Classificacao:
        """Busca classificação por código."""
        classificacao = self._repo.get_by_codigo(codigo)
        if classificacao is None:
            raise ClassificacaoNaoEncontradaError(
                f"Classificação com código '{codigo}' não encontrada"
            )
        return classificacao

    def list_all(self, page: int = 0, page_size: int = 50, tipo: str | None = None) -> tuple:
        """Lista classificações com paginação."""
        return self._repo.list_all(page, page_size, tipo)


class DeletarClassificacaoUseCase:
    """Caso de uso para deletar uma classificação."""

    def __init__(self, repository: ClassificacaoRepositoryInterface):
        self._repo = repository

    def execute(self, classificacao_id: str) -> bool:
        """Deleta uma classificação."""
        classificacao = self._repo.get_by_id(classificacao_id)
        if classificacao is None:
            raise ClassificacaoNaoEncontradaError(
                f"Classificação '{classificacao_id}' não encontrada"
            )
        return self._repo.delete(classificacao_id)


__all__ = [
    "CriarClassificacaoUseCase",
    "AtualizarClassificacaoUseCase",
    "BuscarClassificacaoUseCase",
    "DeletarClassificacaoUseCase",
]
