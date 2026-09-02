"""Interface de repositório para Contrato.

Baseado em:
  - 025-Estrutura-Tecnica
  - Modelo Físico (Tabela: compras.contratos)
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from src.modules.sigmun_compras.domain.entities.contrato import (
    Contrato,
    SituacaoContrato,
)


class ContratoRepository(ABC):
    """Abstração de repositório para a entidade Contrato."""

    @abstractmethod
    def save(self, contrato: Contrato) -> Contrato:
        """Persiste (cria ou atualiza) um contrato."""

    @abstractmethod
    def get_by_id(self, contrato_id: UUID) -> Optional[Contrato]:
        """Retorna um contrato pelo ID ou None se não existir."""

    @abstractmethod
    def list(
        self,
        situacao: Optional[SituacaoContrato] = None,
        fornecedor_id: Optional[UUID] = None,
        unidade_id: Optional[UUID] = None,
        include_deleted: bool = False,
        limit: Optional[int] = None,
        offset: int = 0,
    ) -> List[Contrato]:
        """Lista contratos com filtros opcionais e paginação."""

    @abstractmethod
    def update(self, contrato: Contrato) -> Contrato:
        """Atualiza os dados de um contrato existente."""

    @abstractmethod
    def delete(self, contrato_id: UUID, usuario_id: UUID) -> None:
        """Exclui logicamente (soft-delete) um contrato."""

    @abstractmethod
    def exists_processo_documental(self, processo_documental_id: UUID) -> bool:
        """Verifica se o processo documental existe (RN-COMPRAS-038)."""

    @abstractmethod
    def exists_fornecedor_ativo(self, fornecedor_id: UUID) -> bool:
        """Verifica se o fornecedor existe e está ativo."""

    @abstractmethod
    def exists_unidade(self, unidade_id: UUID) -> bool:
        """Verifica se a unidade administrativa existe."""

    @abstractmethod
    def exists_numero(self, numero: str, excluir_id: Optional[UUID] = None) -> bool:
        """Verifica unicidade do numero do contrato (RN-COMPRAS-036)."""

    @abstractmethod
    def exists_compra(self, compra_id: UUID) -> bool:
        """Verifica se a compra (processo de compras) existe (RN-COMPRAS-025)."""


__all__ = ["ContratoRepository"]
