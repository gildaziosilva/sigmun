"""Query para listagem de contratos."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from src.modules.sigmun_compras.domain.entities.contrato import SituacaoContrato


@dataclass(frozen=True)
class ListarContratosQuery:
    """Query para listar contratos com filtros opcionais e paginação."""

    situacao: SituacaoContrato | None = None
    fornecedor_id: UUID | None = None
    unidade_id: UUID | None = None
    include_inativos: bool = False
    page: int = 0
    page_size: int = 50
