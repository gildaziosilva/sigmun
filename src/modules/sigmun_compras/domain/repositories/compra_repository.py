"""Interface de repositório para Compra (processo de compras).

Baseado em:
  - 025-Estrutura-Tecnica
  - 013-Modelo-de-Dados (Tabela: compras.compras)
"""

from __future__ import annotations

import builtins
from abc import ABC, abstractmethod
from uuid import UUID

from src.modules.sigmun_compras.domain.entities.compra import Compra, SituacaoCompra


class CompraRepository(ABC):
    """Abstração de repositório para a entidade Compra."""

    @abstractmethod
    def save(self, compra: Compra) -> Compra:
        """Persiste (cria ou atualiza) uma compra."""

    @abstractmethod
    def get_by_id(self, compra_id: UUID) -> Compra | None:
        """Retorna uma compra pelo ID ou None se não existir."""

    @abstractmethod
    def list(
        self,
        situacao: SituacaoCompra | None = None,
        include_deleted: bool = False,
        limit: int | None = None,
        offset: int = 0,
    ) -> builtins.list[Compra]:
        """Lista compras, opcionalmente filtrando por situação."""

    @abstractmethod
    def update(self, compra: Compra) -> Compra:
        """Atualiza os dados de uma compra existente."""

    @abstractmethod
    def delete(self, compra_id: UUID, usuario_id: UUID) -> None:
        """Exclui logicamente (soft-delete) uma compra."""

    @abstractmethod
    def exists_processo_documental(self, processo_documental_id: UUID) -> bool:
        """Verifica se o processo documental existe (RN-COMPRAS-025)."""

    @abstractmethod
    def exists_fornecedor_ativo(self, fornecedor_id: UUID) -> bool:
        """Verifica se o fornecedor existe e está ativo."""

    @abstractmethod
    def exists_unidade(self, unidade_id: UUID) -> bool:
        """Verifica se a unidade administrativa existe."""


__all__ = ["CompraRepository"]
