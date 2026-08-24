"""Command para exclusão (soft-delete) de processo documental."""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class ExcluirProcessoDocumentalCommand:
    """Comando para excluir logicamente um processo documental."""

    processo_id: UUID
    usuario_id: UUID | None = field(default=None, kw_only=True)
