"""Command para atualização de fornecedor.

Baseado em:
  - RN-COMPRAS-033 (Dados Cadastrais)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID

from src.modules.sigmun_compras.domain.entities.fornecedor import SituacaoFornecedor


@dataclass
class AtualizarFornecedorCommand:
    """Commando para atualizar os dados de um fornecedor."""

    fornecedor_id: UUID
    situacao_cadastro: SituacaoFornecedor
    usuario_id: UUID | None = field(default=None, kw_only=True)
