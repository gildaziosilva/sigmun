"""Command para alteração de situação do contrato."""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID

from src.modules.sigmun_compras.domain.entities.contrato import SituacaoContrato


@dataclass
class AlterarSituacaoContratoCommand:
    """Comando para transicionar a situação de um contrato."""

    contrato_id: UUID
    nova_situacao: SituacaoContrato
    usuario_id: UUID | None = field(default=None, kw_only=True)
