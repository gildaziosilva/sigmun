"""Query para consulta de compra (processo de compras)."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class ConsultarCompraQuery:
    """Query para obter os dados de uma compra."""

    compra_id: UUID
