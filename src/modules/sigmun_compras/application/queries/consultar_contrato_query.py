"""Query para consulta de contrato."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class ConsultarContratoQuery:
    """Query para obter os dados de um contrato."""

    contrato_id: UUID
