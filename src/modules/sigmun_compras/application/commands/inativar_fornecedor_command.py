"""Command para inativação de fornecedor.

Baseado em:
  - RN-COMPRAS-033 (Dados Cadastrais)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class InativarFornecedorCommand:
    """Commando para inativar (soft-delete) um fornecedor."""

    fornecedor_id: UUID
    usuario_id: UUID = field(kw_only=True)
