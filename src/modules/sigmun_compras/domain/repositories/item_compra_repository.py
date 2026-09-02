"""Interface de repositório para Item de Compra.

Define o contrato que a camada de infraestrutura deverá implementar.
Baseado em:
  - 025-Estrutura-Tecnica
  - 013-Modelo-de-Dados (Tabela: compras.itens_compras)
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from src.modules.sigmun_compras.domain.entities.item_compra import ItemCompra


class ItemCompraRepository(ABC):
    """Abstração de repositório para a entidade ItemCompra."""

    @abstractmethod
    def save(self, item: ItemCompra) -> ItemCompra:
        """Persiste (cria ou atualiza) um item de compra."""

    @abstractmethod
    def get_by_id(self, item_id: UUID) -> ItemCompra | None:
        """Retorna um item pelo ID ou None se não existir."""

    @abstractmethod
    def list_by_compra(
        self,
        compra_id: UUID,
        include_deleted: bool = False,
        limit: int | None = None,
        offset: int = 0,
    ) -> list[ItemCompra]:
        """Lista os itens de uma compra, opcionalmente com paginação."""

    @abstractmethod
    def update(self, item: ItemCompra) -> ItemCompra:
        """Atualiza os dados de um item existente."""

    @abstractmethod
    def delete(self, item_id: UUID, usuario_id: UUID) -> None:
        """Exclui logicamente (soft-delete) um item de compra."""

    @abstractmethod
    def exists_compra(self, compra_id: UUID) -> bool:
        """Verifica se a compra informada existe (integridade do vínculo)."""


__all__ = ["ItemCompraRepository"]
