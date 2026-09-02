"""Command para abertura de processo documental.

Baseado em:
  - UC-COMPRAS-013 – Abrir Processo de Contratação
  - RN-COMPRAS-025 – Processo Único
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class CriarProcessoDocumentalCommand:
    """Comando para abrir um novo processo documental."""

    unidade_id: UUID
    numero: str
    ano: int
    assunto: str
    descricao: str | None = None
    usuario_id: UUID | None = field(default=None, kw_only=True)
