"""Command para exclusão (soft-delete) de contrato."""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class ExcluirContratoCommand:
    """Comando para excluir logicamente um contrato."""

    contrato_id: UUID
    usuario_id: UUID | None = field(default=None, kw_only=True)
