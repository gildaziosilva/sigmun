"""Query para consulta de processo documental."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class ConsultarProcessoDocumentalQuery:
    """Query para obter os dados de um processo documental."""

    processo_id: UUID
