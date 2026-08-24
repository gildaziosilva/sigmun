"""Command para atualização cadastral de compra.

Baseado em:
  - RN-COMPRAS-028 – Responsabilidade
  - RN-COMPRAS-029 – Registro de Data e Hora
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from uuid import UUID


@dataclass
class AtualizarCompraCommand:
    """Comando para atualizar campos cadastrais de uma compra."""

    compra_id: UUID
    numero: str | None = None
    data: date | None = None
    valor_total: Decimal | None = None
    usuario_id: UUID | None = field(default=None, kw_only=True)
