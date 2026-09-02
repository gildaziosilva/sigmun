"""Query para listagem de fornecedores.

Baseado em:
  - SRV-COMPRAS-007 – Gestão de Fornecedores
  - Operações: buscarFornecedores()
"""

from __future__ import annotations

from dataclasses import dataclass

from src.modules.sigmun_compras.domain.entities.fornecedor import SituacaoFornecedor


@dataclass(frozen=True)
class ListarFornecedoresQuery:
    """Query para listar fornecedores com filtros opcionais."""

    situacao: SituacaoFornecedor | None = None
    include_inativos: bool = True
    page: int = 0
    page_size: int = 50
