"""Command para atualização de processo documental."""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class AtualizarProcessoDocumentalCommand:
    """Comando para atualizar campos de um processo documental."""

    processo_id: UUID
    numero: str | None = None
    ano: int | None = None
    assunto: str | None = None
    descricao: str | None = None
    usuario_id: UUID | None = field(default=None, kw_only=True)
