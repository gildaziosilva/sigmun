"""Command para atualização de item de compra.

Baseado em:
  - RN-COMPRAS-011 – Especificação do Objeto
  - RN-COMPRAS-012 – Quantificação
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from uuid import UUID


@dataclass
class AtualizarItemCompraCommand:
    """Comando para atualizar campos de um item de compra."""

    item_id: UUID
    descricao: str | None = None
    quantidade: Decimal | None = None
    valor_unitario: Decimal | None = None
    usuario_id: UUID | None = field(default=None, kw_only=True)
