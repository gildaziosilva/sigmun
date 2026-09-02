"""Query para consulta de item de compra.

Baseado em:
  - ENT-COMPRAS-004 – Item da Contratação
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class ConsultarItemCompraQuery:
    """Query para obter os dados de um item de compra."""

    item_id: UUID
