"""Query para listagem dos itens de uma compra.

Baseado em:
  - ENT-COMPRAS-004 – Item da Contratação
  - SRV-COMPRAS – Gestão de Compras
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class ListarItensCompraQuery:
    """Query para listar os itens de uma compra com paginação."""

    compra_id: UUID
    include_inativos: bool = False
    page: int = 0
    page_size: int = 50
