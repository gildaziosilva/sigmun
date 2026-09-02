"""Command da Formalização da Contratação (Compra -> Contrato).

Baseado em:
  - UC-COMPRAS-022 – Formalizar Contratação
  - RN-COMPRAS-036 – Identificação Única
  - RN-COMPRAS-038 – Objeto/Processo Contratual
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from uuid import UUID


@dataclass
class FormalizarContratacaoCommand:
    """Comando para formalizar o contrato a partir de uma compra."""

    compra_id: UUID
    numero: str
    data_inicio: date
    data_fim: date | None = None
    valor: Decimal | None = None
    objeto: str | None = None
    data_assinatura: date | None = None
    usuario_id: UUID | None = field(default=None, kw_only=True)
