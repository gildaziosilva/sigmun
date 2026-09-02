"""Query para listagem de contratos."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from src.modules.sigmun_compras.domain.entities.contrato import SituacaoContrato


@dataclass(frozen=True)
class ListarContratosQuery:
    """Query para listar contratos com filtros opcionais e paginação."""

    situacao: Optional[SituacaoContrato] = None
    fornecedor_id: Optional[UUID] = None
    unidade_id: Optional[UUID] = None
    include_inativos: bool = False
    page: int = 0
    page_size: int = 50
