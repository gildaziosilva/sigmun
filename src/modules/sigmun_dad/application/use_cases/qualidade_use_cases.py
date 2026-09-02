"""Casos de uso para gerenciamento de Qualidade de Dados."""

import logging

from src.modules.sigmun_dad.application.interfaces import QualidadeRepositoryInterface
from src.modules.sigmun_dad.domain.entities import QualidadeDado, QualidadeNivel
from src.modules.sigmun_dad.domain.exceptions import (
    QualidadeNaoEncontradaError,
)

logger = logging.getLogger(__name__)


class AvaliarQualidadeUseCase:
    """Caso de uso para avaliar qualidade de um ativo."""

    def __init__(self, repository: QualidadeRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        ativo_id: str,
        score: float,
        criterios: list[str] | None = None,
        observacao: str = "",
    ) -> QualidadeDado:
        """Avalia a qualidade de um ativo."""
        if not ativo_id:
            raise ValueError("ID do ativo é obrigatório")
        if score < 0 or score > 100:
            raise ValueError("Score deve estar entre 0 e 100")

        qualidade = self._repo.get_by_ativo(ativo_id)
        if qualidade is None:
            qualidade = QualidadeDado(ativo_id=ativo_id)

        qualidade.update_score(score)
        if criterios:
            qualidade.criterios = criterios
        if observacao:
            qualidade.observacao = observacao

        return self._repo.save(qualidade)


class AtualizarQualidadeDadosUseCase:
    """Caso de uso para atualizar qualidade de dados."""

    def __init__(self, repository: QualidadeRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        qualidade_id: str,
        score: float | None = None,
        nivel: str | None = None,
        criterios: list[str] | None = None,
        observacao: str | None = None,
    ) -> QualidadeDado:
        """Atualiza registro de qualidade."""
        qualidade = self._repo.get_by_id(qualidade_id)
        if qualidade is None:
            raise QualidadeNaoEncontradaError(
                f"Registro de qualidade '{qualidade_id}' não encontrado"
            )

        if score is not None:
            qualidade.update_score(score)
        if nivel is not None:
            qualidade.nivel = QualidadeNivel(nivel)
        if criterios is not None:
            qualidade.criterios = criterios
        if observacao is not None:
            qualidade.observacao = observacao

        from datetime import datetime
        qualidade.updated_at = datetime.utcnow()
        return self._repo.save(qualidade)


class BuscarQualidadeUseCase:
    """Caso de uso para buscar registros de qualidade."""

    def __init__(self, repository: QualidadeRepositoryInterface):
        self._repo = repository

    def get_by_id(self, qualidade_id: str) -> QualidadeDado:
        """Busca registro de qualidade por ID."""
        qualidade = self._repo.get_by_id(qualidade_id)
        if qualidade is None:
            raise QualidadeNaoEncontradaError(
                f"Registro de qualidade '{qualidade_id}' não encontrado"
            )
        return qualidade

    def get_by_ativo(self, ativo_id: str) -> QualidadeDado:
        """Busca qualidade por ativo."""
        qualidade = self._repo.get_by_ativo(ativo_id)
        if qualidade is None:
            raise QualidadeNaoEncontradaError(
                f"Qualidade do ativo '{ativo_id}' não encontrada"
            )
        return qualidade

    def list_all(self, page: int = 0, page_size: int = 50) -> tuple:
        """Lista registros de qualidade com paginação."""
        return self._repo.list_all(page, page_size)


class DeletarQualidadeUseCase:
    """Caso de uso para deletar registro de qualidade."""

    def __init__(self, repository: QualidadeRepositoryInterface):
        self._repo = repository

    def execute(self, qualidade_id: str) -> bool:
        """Deleta registro de qualidade."""
        qualidade = self._repo.get_by_id(qualidade_id)
        if qualidade is None:
            raise QualidadeNaoEncontradaError(
                f"Registro de qualidade '{qualidade_id}' não encontrado"
            )
        return self._repo.delete(qualidade_id)


__all__ = [
    "AvaliarQualidadeUseCase",
    "AtualizarQualidadeDadosUseCase",
    "BuscarQualidadeUseCase",
    "DeletarQualidadeUseCase",
]
