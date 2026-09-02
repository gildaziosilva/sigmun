"""Schemas de apresentação (Pydantic) para Metadados Corporativos (DOM-MET)."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from src.modules.sigmun_met.domain.entities import (
    StatusMetadado,
    TipoClassificacao,
    TipoDadoMetadado,
)

# =============================================================================
# Schemas de Metadados
# =============================================================================


class MetadadoCreateRequest(BaseModel):
    """Payload de criação de metadado."""
    codigo: str = Field(..., min_length=2, max_length=50, pattern=r"^[a-zA-Z][a-zA-Z0-9_]+$")
    nome: str = Field(..., min_length=3, max_length=200)
    descricao: str | None = None
    tipo_dado: TipoDadoMetadado = TipoDadoMetadado.TEXTO
    obrigatorio: bool = False
    multi_valor: bool = False
    aplicavel_a: list[str] = Field(default_factory=list)
    valor_padrao: str | None = None


class MetadadoUpdateRequest(BaseModel):
    """Payload de atualização de metadado."""
    nome: str | None = Field(None, min_length=3, max_length=200)
    descricao: str | None = None
    tipo_dado: TipoDadoMetadado | None = None
    obrigatorio: bool | None = None
    multi_valor: bool | None = None
    aplicavel_a: list[str] | None = None
    valor_padrao: str | None = None
    status: StatusMetadado | None = None


class MetadadoResponse(BaseModel):
    """Representação de um metadado."""
    model_config = ConfigDict(from_attributes=True)
    id: str
    codigo: str
    nome: str
    descricao: str | None = None
    tipo_dado: str
    obrigatorio: bool
    multi_valor: bool
    aplicavel_a: list[str] = Field(default_factory=list)
    valor_padrao: str | None = None
    status: str
    created_at: datetime
    updated_at: datetime | None = None


class MetadadoListResponse(BaseModel):
    """Envelope paginado de listagem de metadados."""
    total: int
    page: int
    page_size: int
    items: list[MetadadoResponse]


# =============================================================================
# Schemas de Valores de Metadados
# =============================================================================


class ValorMetadadoCreateRequest(BaseModel):
    """Payload de atribuição de valor de metadado."""
    metadado_id: str
    entidade_tipo: str = Field(..., min_length=1, max_length=100, pattern=r"^[a-z][a-z0-9_]+$")
    entidade_id: str
    valor: str = Field(..., min_length=1, max_length=1000)


class ValorMetadadoUpdateRequest(BaseModel):
    """Payload de atualização de valor de metadado."""
    valor: str = Field(..., min_length=1, max_length=1000)


class ValorMetadadoResponse(BaseModel):
    """Representação de um valor de metadado."""
    model_config = ConfigDict(from_attributes=True)
    id: str
    metadado_id: str
    entidade_tipo: str
    entidade_id: str
    valor: str
    created_at: datetime
    updated_at: datetime | None = None


class ValorMetadadoListResponse(BaseModel):
    """Envelope paginado de listagem de valores de metadados."""
    total: int
    page: int
    page_size: int
    items: list[ValorMetadadoResponse]


# =============================================================================
# Schemas de Classificações
# =============================================================================


class ClassificacaoCreateRequest(BaseModel):
    """Payload de criação de classificação."""
    codigo: str = Field(..., min_length=2, max_length=50, pattern=r"^[a-zA-Z][a-zA-Z0-9_]+$")
    nome: str = Field(..., min_length=3, max_length=200)
    descricao: str | None = None
    tipo: TipoClassificacao = TipoClassificacao.CONFIDENCIALIDADE
    nivel: int = Field(0, ge=0, le=100)
    cor: str | None = Field(None, max_length=20)


class ClassificacaoUpdateRequest(BaseModel):
    """Payload de atualização de classificação."""
    nome: str | None = Field(None, min_length=3, max_length=200)
    descricao: str | None = None
    tipo: TipoClassificacao | None = None
    nivel: int | None = Field(None, ge=0, le=100)
    cor: str | None = Field(None, max_length=20)


class ClassificacaoResponse(BaseModel):
    """Representação de uma classificação."""
    model_config = ConfigDict(from_attributes=True)
    id: str
    codigo: str
    nome: str
    descricao: str | None = None
    tipo: str
    nivel: int
    cor: str | None = None
    created_at: datetime
    updated_at: datetime | None = None


class ClassificacaoListResponse(BaseModel):
    """Envelope paginado de listagem de classificações."""
    total: int
    page: int
    page_size: int
    items: list[ClassificacaoResponse]


# =============================================================================
# Schemas de Taxonomias
# =============================================================================


class TaxonomiaCreateRequest(BaseModel):
    """Payload de criação de taxonomia."""
    codigo: str = Field(..., min_length=2, max_length=50, pattern=r"^[a-zA-Z][a-zA-Z0-9_]+$")
    nome: str = Field(..., min_length=3, max_length=200)
    descricao: str | None = None


class TaxonomiaUpdateRequest(BaseModel):
    """Payload de atualização de taxonomia."""
    nome: str | None = Field(None, min_length=3, max_length=200)
    descricao: str | None = None


class TaxonomiaResponse(BaseModel):
    """Representação de uma taxonomia."""
    model_config = ConfigDict(from_attributes=True)
    id: str
    codigo: str
    nome: str
    descricao: str | None = None
    termos_ids: list[str] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime | None = None


class TaxonomiaListResponse(BaseModel):
    """Envelope paginado de listagem de taxonomias."""
    total: int
    page: int
    page_size: int
    items: list[TaxonomiaResponse]


# =============================================================================
# Schemas de Termos de Taxonomia
# =============================================================================


class TermoCreateRequest(BaseModel):
    """Payload de criação de termo de taxonomia."""
    taxonomia_id: str
    codigo: str = Field(..., min_length=2, max_length=50, pattern=r"^[a-zA-Z][a-zA-Z0-9_]+$")
    nome: str = Field(..., min_length=3, max_length=200)
    descricao: str | None = None
    termo_pai_id: str | None = None
    sinonimos: list[str] = Field(default_factory=list)
    ordem: int = Field(0, ge=0)


class TermoUpdateRequest(BaseModel):
    """Payload de atualização de termo de taxonomia."""
    nome: str | None = Field(None, min_length=3, max_length=200)
    descricao: str | None = None
    sinonimos: list[str] | None = None
    ordem: int | None = Field(None, ge=0)


class TermoResponse(BaseModel):
    """Representação de um termo de taxonomia."""
    model_config = ConfigDict(from_attributes=True)
    id: str
    taxonomia_id: str
    termo_pai_id: str | None = None
    codigo: str
    nome: str
    descricao: str | None = None
    sinonimos: list[str] = Field(default_factory=list)
    ordem: int
    created_at: datetime
    updated_at: datetime | None = None


class TermoListResponse(BaseModel):
    """Envelope paginado de listagem de termos de taxonomia."""
    total: int
    page: int
    page_size: int
    items: list[TermoResponse]


# =============================================================================
# Schemas comuns
# =============================================================================


class ErrorResponse(BaseModel):
    """Resposta de erro padrão da API."""
    detail: str
