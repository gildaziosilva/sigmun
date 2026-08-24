"""Command para alteração de situação processual da compra.

Baseado em:
  - RN-COMPRAS-026 – Sequenciamento
  - RN-COMPRAS-027 – Pendências
  - RN-COMPRAS-028 – Responsabilidade
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID

from src.modules.sigmun_compras.domain.entities.compra import SituacaoCompra


@dataclass
class AlterarSituacaoCompraCommand:
    """Comando para transicionar a situação processual de uma compra."""

    compra_id: UUID
    nova_situacao: SituacaoCompra
    usuario_id: UUID | None = field(default=None, kw_only=True)
