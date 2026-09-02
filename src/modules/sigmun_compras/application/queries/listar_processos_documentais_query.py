"""Query para listagem de processos documentais."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class ListarProcessosDocumentaisQuery:
    """Query para listar processos documentais com filtros e paginação."""

    unidade_id: UUID | None = None
    ano: int | None = None
    include_inativos: bool = False
    page: int = 0
    page_size: int = 50
