"""Eventos de domínio para Contrato.

Baseado em:
  - 007-Regras-de-Negocio (RN-COMPRAS-035 a 040)
  - 017-Modelo-de-Auditoria
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from uuid import UUID


@dataclass(frozen=True)
class ContratoCriadoEvent:
    """Evento disparado quando um contrato é registrado."""

    contrato_id: UUID
    numero: str
    processo_documental_id: UUID
    fornecedor_id: UUID
    unidade_id: UUID
    situacao: str
    created_at: datetime


@dataclass(frozen=True)
class ContratoAtualizadoEvent:
    """Evento disparado quando dados do contrato são atualizados."""

    contrato_id: UUID
    numero: str
    valor: Decimal | None
    updated_at: datetime


@dataclass(frozen=True)
class ContratoSituacaoAlteradaEvent:
    """Evento disparado quando a situação do contrato muda."""

    contrato_id: UUID
    situacao_anterior: str
    situacao_nova: str
    updated_at: datetime


__all__ = [
    "ContratoCriadoEvent",
    "ContratoAtualizadoEvent",
    "ContratoSituacaoAlteradaEvent",
]
