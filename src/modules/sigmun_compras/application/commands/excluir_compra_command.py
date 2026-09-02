"""Command para exclusão (soft-delete) de compra."""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class ExcluirCompraCommand:
    """Comando para excluir logicamente uma compra."""

    compra_id: UUID
    usuario_id: UUID | None = field(default=None, kw_only=True)
