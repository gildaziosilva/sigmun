"""Command para atualização de contrato.

Baseado em:
  - RN-COMPRAS-036 – Identificação do Contrato
  - RN-COMPRAS-037 – Vigência
  - RN-COMPRAS-039 – Valor Contratual
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from uuid import UUID


@dataclass
class AtualizarContratoCommand:
    """Comando para atualizar campos de um contrato."""

    contrato_id: UUID
    numero: str | None = None
    data_inicio: date | None = None
    data_fim: date | None = None
    valor: Decimal | None = None
    objeto: str | None = None
    usuario_id: UUID | None = field(default=None, kw_only=True)
