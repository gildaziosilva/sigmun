"""Eventos de domínio para ProcessoDocumental.

Baseado em:
  - 007-Regras-de-Negocio (RN-COMPRAS-004, 025, 028, 029)
  - 017-Modelo-de-Auditoria
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class ProcessoDocumentalAbertoEvent:
    """Evento disparado quando um processo documental é aberto."""

    processo_id: UUID
    numero: str
    ano: int
    unidade_id: UUID
    created_at: datetime


@dataclass(frozen=True)
class ProcessoDocumentalAtualizadoEvent:
    """Evento disparado quando um processo documental é atualizado."""

    processo_id: UUID
    numero: str
    ano: int
    updated_at: datetime


__all__ = ["ProcessoDocumentalAbertoEvent", "ProcessoDocumentalAtualizadoEvent"]
