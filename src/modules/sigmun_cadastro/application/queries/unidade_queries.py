"""Queries de aplicação de Unidades Administrativas (DOM-CUM)."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class ConsultarUnidadeQuery:
    """Consulta de uma unidade administrativa pelo ID."""

    unidade_id: UUID
    include_deleted: bool = False


@dataclass(frozen=True)
class ListarUnidadesQuery:
    """Listagem paginada de unidades administrativas."""

    include_deleted: bool = False
    limit: int | None = None
    offset: int = 0


__all__ = ["ConsultarUnidadeQuery", "ListarUnidadesQuery"]
