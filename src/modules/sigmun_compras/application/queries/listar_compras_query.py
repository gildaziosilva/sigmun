"""Query para listagem de compras (processos de compras)."""

from __future__ import annotations

from dataclasses import dataclass

from src.modules.sigmun_compras.domain.entities.compra import SituacaoCompra


@dataclass(frozen=True)
class ListarComprasQuery:
    """Query para listar compras com filtros opcionais e paginação."""

    situacao: SituacaoCompra | None = None
    include_inativos: bool = False
    page: int = 0
    page_size: int = 50
