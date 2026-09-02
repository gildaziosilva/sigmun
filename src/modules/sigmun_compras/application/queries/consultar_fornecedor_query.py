"""Query para consulta de fornecedor.

Baseado em:
  - HU-COMPRAS-020 (Consultar Fornecedor)
  - UC-COMPRAS-020 (Consultar Fornecedor)
  - RF-COMPRAS-034 (Consultar Fornecedor)
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class ConsultarFornecedorQuery:
    """Query para obter os dados cadastrais de um fornecedor."""

    fornecedor_id: UUID


@dataclass(frozen=True)
class ConsultarFornecedorPorPessoaJuridicaQuery:
    """Query para obter um fornecedor pela pessoa jurídica referenciada."""

    pessoa_juridica_id: UUID
