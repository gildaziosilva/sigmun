"""Schemas de apresentação (Pydantic) para Unidades Administrativas (DOM-CUM).

Baseado em:
  - 010-Especificacoes-Cadastro-Unico-Municipal.md (serviços de unidade)
  - RN-CUM-008 (hierarquia sem ciclos) e RN-CUM-009 (unicidade)
"""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class UnidadeCreateRequest(BaseModel):
    """Payload de registro de unidade administrativa (POST)."""

    nome: str = Field(..., min_length=1)
    unidade_pai_id: UUID | None = None
    sigla: str | None = None
    codigo_ibge: str | None = None
    codigo_siafi: str | None = None


class UnidadeUpdateRequest(BaseModel):
    """Payload de atualização de unidade administrativa (PATCH parcial).

    Limitação documentada: ``unidade_pai_id`` não pode ser removido
    (definido como null) — apenas substituído por outro pai.
    """

    nome: str | None = None
    sigla: str | None = None
    codigo_ibge: str | None = None
    codigo_siafi: str | None = None
    unidade_pai_id: UUID | None = None


class UnidadeResponse(BaseModel):
    """Representação de uma unidade administrativa nas respostas."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    nome: str
    unidade_pai_id: UUID | None = None
    sigla: str | None = None
    codigo_ibge: str | None = None
    codigo_siafi: str | None = None
    created_at: datetime
    updated_at: datetime


class UnidadeListResponse(BaseModel):
    """Envelope paginado de listagem de unidades administrativas."""

    total: int
    page: int
    page_size: int
    items: list[UnidadeResponse]


class ErrorResponse(BaseModel):
    """Erro padronizado da API."""

    detail: str


__all__ = [
    "UnidadeCreateRequest",
    "UnidadeUpdateRequest",
    "UnidadeResponse",
    "UnidadeListResponse",
    "ErrorResponse",
]
