"""Schemas de apresentação (Pydantic) para Itens de Compra.

Baseado em:
  - ENT-COMPRAS-004 – Item da Contratação
  - RN-COMPRAS-011/012
"""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ItemCompraCreateRequest(BaseModel):
    """Payload de inclusão de item em uma compra (POST)."""

    descricao: str = Field(..., min_length=3, description="Descrição clara do objeto")
    quantidade: Decimal = Field(..., gt=0, description="Quantidade necessária")
    valor_unitario: Decimal = Field(..., ge=0, description="Valor unitário estimado")


class ItemCompraUpdateRequest(BaseModel):
    """Payload de atualização de item (PATCH)."""

    descricao: str | None = Field(None, min_length=3)
    quantidade: Decimal | None = Field(None, gt=0)
    valor_unitario: Decimal | None = Field(None, ge=0)


class ItemCompraResponse(BaseModel):
    """Representação de um item de compra nas respostas da API."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    compra_id: UUID
    descricao: str
    quantidade: Decimal
    valor_unitario: Decimal
    valor_total: Decimal
    created_at: datetime
    updated_at: datetime


class ItemCompraListResponse(BaseModel):
    """Envelope paginado da listagem de itens de uma compra."""

    total: int
    page: int
    page_size: int
    items: list[ItemCompraResponse]


__all__ = [
    "ItemCompraCreateRequest",
    "ItemCompraUpdateRequest",
    "ItemCompraResponse",
    "ItemCompraListResponse",
]
