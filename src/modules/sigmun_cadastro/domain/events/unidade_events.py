"""Eventos de domínio relacionados a Unidades Administrativas (DOM-CUM)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4


def _novo_id() -> UUID:
    return uuid4()


@dataclass(frozen=True)
class UnidadeRegistradaEvent:
    """Emitido quando uma unidade administrativa é registrada."""

    event_id: UUID
    unidade_id: UUID
    nome: str
    sigla: str | None
    occurred_at: datetime


@dataclass(frozen=True)
class UnidadeAtualizadaEvent:
    """Emitido quando uma unidade administrativa é atualizada."""

    event_id: UUID
    unidade_id: UUID
    occurred_at: datetime


@dataclass(frozen=True)
class UnidadeExcluidaEvent:
    """Emitido quando uma unidade administrativa é logicamente excluída."""

    event_id: UUID
    unidade_id: UUID
    occurred_at: datetime


__all__ = [
    "UnidadeRegistradaEvent",
    "UnidadeAtualizadaEvent",
    "UnidadeExcluidaEvent",
]
