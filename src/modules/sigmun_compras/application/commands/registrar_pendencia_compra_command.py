"""Command para registro/resolução de pendências impeditivas (RN-COMPRAS-027)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID


@dataclass
class RegistrarPendenciaCompraCommand:
    """Comando para marcar ou resolver pendências impeditivas da compra."""

    compra_id: UUID
    registrar: bool
    justificativa: Optional[str] = None
    usuario_id: UUID | None = field(default=None, kw_only=True)
