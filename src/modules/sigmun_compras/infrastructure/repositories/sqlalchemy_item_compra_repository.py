"""Implementação SQLAlchemy do repositório de Itens de Compra.

Implementa o contrato ``ItemCompraRepository`` do domínio sobre a tabela
``compras.itens_compras`` (migration 20260820_01).

Observações de projeto:
  - O repositório executa ``flush`` (não ``commit``); a transação é
    controlada pela sessão da requisição (ver core get_db).
  - ``deleted_at`` é gerado pelo servidor do banco (constraint
    ``ck_itens_compras_deleted``).
"""

from __future__ import annotations

import logging
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.sigmun_compras.domain.entities.item_compra import ItemCompra
from src.modules.sigmun_compras.domain.repositories.item_compra_repository import (
    ItemCompraRepository,
)
from src.modules.sigmun_compras.infrastructure.database.models import (
    CompraModel,
    ItemCompraModel,
)

logger = logging.getLogger(__name__)


def _to_entity(model: ItemCompraModel) -> ItemCompra:
    """Converte um registro ORM em entidade de domínio."""
    return ItemCompra(
        id=model.id,
        compra_id=model.compra_id,
        descricao=model.descricao,
        quantidade=model.quantidade,
        valor_unitario=model.valor_unitario,
        valor_total=model.valor_total,
        created_at=model.created_at,
        created_by=model.created_by,
        updated_at=model.updated_at,
        updated_by=model.updated_by,
        deleted_at=model.deleted_at,
        deleted_by=model.deleted_by,
    )


class SqlAlchemyItemCompraRepository(ItemCompraRepository):
    """Repositório de itens de compra persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    # -- Contrato do domínio ---------------------------------------------------

    def save(self, item: ItemCompra) -> ItemCompra:
        model = self._session.get(ItemCompraModel, item.id)
        if model is None:
            model = ItemCompraModel(
                id=item.id,
                compra_id=item.compra_id,
                descricao=item.descricao,
                quantidade=item.quantidade,
                valor_unitario=item.valor_unitario,
                valor_total=item.valor_total,
                created_at=item.created_at,
                created_by=item.created_by,
                updated_at=item.updated_at,
                updated_by=item.updated_by,
            )
            self._session.add(model)
            logger.info("Item de compra inserido: %s", item.id)
        else:
            model.descricao = item.descricao
            model.quantidade = item.quantidade
            model.valor_unitario = item.valor_unitario
            model.valor_total = item.valor_total
            model.updated_at = item.updated_at
            model.updated_by = item.updated_by
            model.deleted_at = item.deleted_at
            model.deleted_by = item.deleted_by
            logger.info("Item de compra atualizado: %s", item.id)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def get_by_id(self, item_id: UUID) -> ItemCompra | None:
        model = self._session.get(ItemCompraModel, item_id)
        return _to_entity(model) if model else None

    def list_by_compra(
        self,
        compra_id: UUID,
        include_deleted: bool = False,
        limit: int | None = None,
        offset: int = 0,
    ) -> list[ItemCompra]:
        stmt = select(ItemCompraModel).where(ItemCompraModel.compra_id == compra_id)
        if not include_deleted:
            stmt = stmt.where(ItemCompraModel.deleted_at.is_(None))
        stmt = stmt.order_by(ItemCompraModel.created_at)
        if limit is not None:
            stmt = stmt.limit(limit)
        if offset:
            stmt = stmt.offset(offset)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models]

    def update(self, item: ItemCompra) -> ItemCompra:
        return self.save(item)

    def delete(self, item_id: UUID, usuario_id: UUID) -> None:
        """Soft-delete: preserva histórico (auditoria)."""
        model = self._session.get(ItemCompraModel, item_id)
        if model is None:
            return
        if model.deleted_at is None:
            model.deleted_at = func.now()
        model.deleted_by = usuario_id
        self._session.flush()
        logger.info("Item de compra marcado como excluído: %s", item_id)

    def exists_compra(self, compra_id: UUID) -> bool:
        stmt = select(CompraModel.id).where(CompraModel.id == compra_id).limit(1)
        return self._session.scalars(stmt).first() is not None


__all__ = ["SqlAlchemyItemCompraRepository"]
