"""Eventos de domínio para Item de Compra.

Baseado em:
  - 007-Regras-de-Negocio (RN-COMPRAS-011 a 013)
  - 017-Modelo-de-Auditoria
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID


@dataclass(frozen=True)
class ItemCompraCriadoEvent:
    """Evento disparado quando um item é incluído em uma compra."""

    item_id: UUID
    compra_id: UUID
    descricao: str
    valor_total: Decimal
    created_at: datetime


@dataclass(frozen=True)
class ItemCompraAtualizadoEvent:
    """Evento disparado quando os dados de um item são atualizados."""

    item_id: UUID
    compra_id: UUID
    valor_total: Decimal
    updated_at: datetime


@dataclass(frozen=True)
class ItemCompraRemovidoEvent:
    """Evento disparado quando um item é removido (soft-delete) da compra."""

    item_id: UUID
    compra_id: UUID
    deleted_at: datetime


__all__ = [
    "ItemCompraCriadoEvent",
    "ItemCompraAtualizadoEvent",
    "ItemCompraRemovidoEvent",
]
