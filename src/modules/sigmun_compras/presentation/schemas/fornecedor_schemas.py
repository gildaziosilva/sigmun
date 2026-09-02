"""Schemas de apresentação (Pydantic) para Fornecedores.

Baseado em:
  - RF-COMPRAS-033 – Cadastrar Fornecedor
  - RF-COMPRAS-034 – Consultar Fornecedor
  - ENT-COMPRAS-007 – Fornecedor
"""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from src.modules.sigmun_compras.domain.entities.fornecedor import SituacaoFornecedor


class FornecedorCreateRequest(BaseModel):
    """Payload de criação de fornecedor (POST)."""

    pessoa_juridica_id: UUID = Field(..., description="ID da pessoa jurídica corporativa")
    situacao_cadastro: SituacaoFornecedor = SituacaoFornecedor.ATIVO
    macro_categoria: str | None = None


class FornecedorUpdateRequest(BaseModel):
    """Payload de atualização cadastral (PATCH)."""

    situacao_cadastro: SituacaoFornecedor | None = None
    macro_categoria: str | None = None


class FornecedorResponse(BaseModel):
    """Representação de um fornecedor nas respostas da API."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    pessoa_juridica_id: UUID
    situacao_cadastro: SituacaoFornecedor
    macro_categoria: str | None = None
    created_at: datetime
    updated_at: datetime


class FornecedorListResponse(BaseModel):
    """Envelope paginado de listagem de fornecedores."""

    total: int
    page: int
    page_size: int
    items: list[FornecedorResponse]


class ErrorResponse(BaseModel):
    """Erro padronizado da API."""

    detail: str


__all__ = [
    "FornecedorCreateRequest",
    "FornecedorUpdateRequest",
    "FornecedorResponse",
    "FornecedorListResponse",
    "ErrorResponse",
]
