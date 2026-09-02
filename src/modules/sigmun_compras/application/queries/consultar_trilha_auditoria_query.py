"""Query para consulta da trilha de auditoria."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.modules.sigmun_compras.domain.entities.registro_auditoria import (
    CategoriaEventoAuditoria,
)


@dataclass(frozen=True)
class ConsultarTrilhaAuditoriaQuery:
    """Filtros de consulta da trilha (017-Modelo-de-Auditoria, seção 42)."""

    data_inicio: datetime | None = None
    data_fim: datetime | None = None
    usuario_id: UUID | None = None
    categoria: CategoriaEventoAuditoria | None = None
    recurso_tipo: str | None = None
    recurso_id: UUID | None = None
    correlation_id: UUID | None = None
    page: int = 0
    page_size: int = 50


__all__ = ["ConsultarTrilhaAuditoriaQuery"]
