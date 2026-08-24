"""Command para remoção de item de compra.

O item é removido logicamente (soft-delete), preservando histórico.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class RemoverItemCompraCommand:
    """Comando para remover um item de compra."""

    item_id: UUID
    usuario_id: UUID | None = field(default=None, kw_only=True)
