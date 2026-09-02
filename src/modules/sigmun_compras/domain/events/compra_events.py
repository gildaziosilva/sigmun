"""Eventos de domínio para Compra (processo de compras).

Baseado em:
  - 007-Regras-de-Negocio (RN-COMPRAS-025 a 029)
  - 017-Modelo-de-Auditoria
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from uuid import UUID


@dataclass(frozen=True)
class CompraCriadaEvent:
    """Evento disparado quando uma compra é registrada."""

    compra_id: UUID
    numero: str
    processo_documental_id: UUID
    fornecedor_id: UUID
    unidade_id: UUID
    situacao: str
    data: date
    created_at: datetime


@dataclass(frozen=True)
class CompraAtualizadaEvent:
    """Evento disparado quando dados cadastrais da compra são atualizados."""

    compra_id: UUID
    numero: str
    valor_total: Decimal | None
    updated_at: datetime


@dataclass(frozen=True)
class CompraSituacaoAlteradaEvent:
    """Evento disparado quando a situação processual da compra muda."""

    compra_id: UUID
    situacao_anterior: str
    situacao_nova: str
    updated_at: datetime


__all__ = ["CompraCriadaEvent", "CompraAtualizadaEvent", "CompraSituacaoAlteradaEvent"]
