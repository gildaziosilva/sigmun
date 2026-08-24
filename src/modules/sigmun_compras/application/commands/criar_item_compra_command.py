"""Command para inclusão de item em uma compra.

Baseado em:
  - ENT-COMPRAS-004 – Item da Contratação
  - RN-COMPRAS-011 – Especificação do Objeto
  - RN-COMPRAS-012 – Quantificação
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from uuid import UUID


@dataclass
class CriarItemCompraCommand:
    """Comando para incluir um item (produto ou serviço) em uma compra."""

    compra_id: UUID
    descricao: str
    quantidade: Decimal
    valor_unitario: Decimal
    usuario_id: UUID | None = field(default=None, kw_only=True)
