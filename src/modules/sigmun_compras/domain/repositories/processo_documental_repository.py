"""Interface de repositório para ProcessoDocumental.

Baseado em:
  - 025-Estrutura-Tecnica
  - Modelo Físico (Tabela: core.processos_documentais)
"""

from __future__ import annotations

import builtins
from abc import ABC, abstractmethod
from uuid import UUID

from src.modules.sigmun_compras.domain.entities.processo_documental import (
    ProcessoDocumental,
)


class ProcessoDocumentalRepository(ABC):
    """Abstração de repositório para a entidade ProcessoDocumental."""

    @abstractmethod
    def save(self, processo: ProcessoDocumental) -> ProcessoDocumental:
        """Persiste (cria ou atualiza) um processo documental."""

    @abstractmethod
    def get_by_id(self, processo_id: UUID) -> ProcessoDocumental | None:
        """Retorna um processo pelo ID ou None se não existir."""

    @abstractmethod
    def list(
        self,
        unidade_id: UUID | None = None,
        ano: int | None = None,
        include_deleted: bool = False,
        limit: int | None = None,
        offset: int = 0,
    ) -> builtins.list[ProcessoDocumental]:
        """Lista processos com filtros opcionais e paginação."""

    @abstractmethod
    def update(self, processo: ProcessoDocumental) -> ProcessoDocumental:
        """Atualiza os dados de um processo existente."""

    @abstractmethod
    def delete(self, processo_id: UUID, usuario_id: UUID) -> None:
        """Exclui logicamente (soft-delete) um processo documental."""

    @abstractmethod
    def exists_unidade(self, unidade_id: UUID) -> bool:
        """Verifica se a unidade administrativa existe."""

    @abstractmethod
    def exists_numero_ano(
        self, numero: str, ano: int, excluir_id: UUID | None = None
    ) -> bool:
        """Verifica unicidade do par (numero, ano).

        ``excluir_id`` permite ignorar o próprio registro em atualizações.
        """


__all__ = ["ProcessoDocumentalRepository"]
