"""Command para registro de compra (processo de compras).

Baseado em:
  - UC-COMPRAS-022 – Formalizar Contratação
  - RN-COMPRAS-025 – Processo Único
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from uuid import UUID

from src.modules.sigmun_compras.domain.entities.compra import SituacaoCompra


@dataclass
class CriarCompraCommand:
    """Comando para registrar uma nova compra."""

    processo_documental_id: UUID
    fornecedor_id: UUID
    unidade_id: UUID
    numero: str
    data: date | None = None
    valor_total: Decimal | None = None
    situacao: SituacaoCompra = SituacaoCompra.RASCUNHO
    usuario_id: UUID | None = field(default=None, kw_only=True)
