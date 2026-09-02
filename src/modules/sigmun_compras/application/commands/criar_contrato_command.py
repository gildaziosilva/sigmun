"""Command para registro de contrato.

Baseado em:
  - UC-COMPRAS-024 – Registrar Contrato
  - RN-COMPRAS-035 – Instrumento Contratual
  - RN-COMPRAS-038 – Objeto Contratual
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from typing import Optional
from uuid import UUID

from src.modules.sigmun_compras.domain.entities.contrato import SituacaoContrato


@dataclass
class CriarContratoCommand:
    """Comando para registrar um novo contrato."""

    processo_documental_id: UUID
    fornecedor_id: UUID
    unidade_id: UUID
    numero: str
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    valor: Optional[Decimal] = None
    objeto: Optional[str] = None
    licitacao_master_id: Optional[UUID] = None
    situacao: SituacaoContrato = SituacaoContrato.EM_ELABORACAO
    usuario_id: UUID | None = field(default=None, kw_only=True)
