"""Command para cadastro de fornecedor.

Baseado em:
  - HU-COMPRAS-019 (Cadastrar Fornecedor)
  - UC-COMPRAS-019 (Cadastrar Fornecedor)
  - RF-COMPRAS-033 (Cadastrar Fornecedor)
  - RN-COMPRAS-030 (Identificação do Fornecedor)
  - RN-COMPRAS-031 (Unicidade Cadastral)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID

from src.modules.sigmun_compras.domain.entities.fornecedor import SituacaoFornecedor


@dataclass
class CriarFornecedorCommand:
    """Commando para registrar um novo fornecedor."""

    pessoa_juridica_id: UUID
    situacao_cadastro: SituacaoFornecedor = SituacaoFornecedor.ATIVO
    usuario_id: UUID | None = field(default=None, kw_only=True)
