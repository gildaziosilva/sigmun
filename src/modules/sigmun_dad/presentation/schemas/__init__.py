"""Schemas de apresentação (Pydantic) para Dados Corporativos (DOM-DAD)."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from src.modules.sigmun_dad.domain.entities import TipoAtivoDado

# =============================================================================
# Schemas de Ativos de Dados
# =============================================================================


class AtivoCreateRequest(BaseModel):
    """Payload de criação de ativo de dado."""
    nome: str = Field(..., min_length=3, max_length=200)
    descricao: str | None = None
    tipo: TipoAtivoDado = TipoAtivoDado.TABELA
    dono_id: str | None = None
    steward_id: str | None = None
    schema_origem: str | None = None
    tabela_origem: str | None = None
    classificacao: str | None = None
    tags: list[str] = Field(default_factory=list)


class AtivoResponse(BaseModel):
    """Representação de um ativo de dado."""
    model_config = ConfigDict(from_attributes=True)
    id: str
    nome: str
    descricao: str | None = None
    tipo: str
    status: str
    qualidade: str
    dono_id: str | None = None
    steward_id: str | None = None
    schema_origem: str | None = None
    tabela_origem: str | None = None
    classificacao: str | None = None
    tags: list[str] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime | None = None


class AtivoListResponse(BaseModel):
    """Envelope paginado de listagem de ativos."""
    total: int
    page: int
    page_size: int
    items: list[AtivoResponse]


# =============================================================================
# Schemas de Catálogos
# =============================================================================


class CatalogoCreateRequest(BaseModel):
    """Payload de criação de catálogo."""
    nome: str = Field(..., min_length=3, max_length=200)
    descricao: str | None = None
    dominio: str | None = None


class CatalogoUpdateRequest(BaseModel):
    """Payload de atualização de catálogo."""
    nome: str | None = None
    descricao: str | None = None
    dominio: str | None = None


class CatalogoResponse(BaseModel):
    """Representação de um catálogo."""
    model_config = ConfigDict(from_attributes=True)
    id: str
    nome: str
    descricao: str | None = None
    dominio: str | None = None
    ativos_ids: list[str] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime | None = None


class CatalogoListResponse(BaseModel):
    """Envelope paginado de listagem de catálogos."""
    total: int
    page: int
    page_size: int
    items: list[CatalogoResponse]


# =============================================================================
# Schemas de Linhagens
# =============================================================================


class LinhagemCreateRequest(BaseModel):
    """Payload de criação de linhagem."""
    ativo_origem_id: str
    ativo_destino_id: str
    tipo_transformacao: str | None = None
    descricao: str | None = None
    regras: str | None = None


class LinhagemUpdateRequest(BaseModel):
    """Payload de atualização de linhagem."""
    tipo_transformacao: str | None = None
    descricao: str | None = None
    regras: str | None = None


class LinhagemResponse(BaseModel):
    """Representação de uma linhagem."""
    model_config = ConfigDict(from_attributes=True)
    id: str
    ativo_origem_id: str
    ativo_destino_id: str
    tipo_transformacao: str | None = None
    descricao: str | None = None
    regras: str | None = None
    created_at: datetime


class LinhagemListResponse(BaseModel):
    """Envelope paginado de listagem de linhagens."""
    total: int
    page: int
    page_size: int
    items: list[LinhagemResponse]


# =============================================================================
# Schemas de Políticas
# =============================================================================


class PoliticaCreateRequest(BaseModel):
    """Payload de criação de política."""
    codigo: str = Field(..., min_length=2, max_length=50)
    nome: str = Field(..., min_length=3, max_length=200)
    descricao: str | None = None
    tipo: str | None = None
    regras: list[str] = Field(default_factory=list)


class PoliticaUpdateRequest(BaseModel):
    """Payload de atualização de política."""
    nome: str | None = None
    descricao: str | None = None
    tipo: str | None = None


class PoliticaResponse(BaseModel):
    """Representação de uma política."""
    model_config = ConfigDict(from_attributes=True)
    id: str
    codigo: str
    nome: str
    descricao: str | None = None
    tipo: str | None = None
    regras: list[str] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime | None = None


class PoliticaListResponse(BaseModel):
    """Envelope paginado de listagem de políticas."""
    total: int
    page: int
    page_size: int
    items: list[PoliticaResponse]


# =============================================================================
# Schemas de Qualidade de Dados
# =============================================================================


class QualidadeCreateRequest(BaseModel):
    """Payload de avaliação de qualidade."""
    ativo_id: str
    score: float = Field(..., ge=0, le=100)
    criterios: list[str] = Field(default_factory=list)
    observacao: str | None = None


class QualidadeUpdateRequest(BaseModel):
    """Payload de atualização de qualidade."""
    score: float | None = Field(None, ge=0, le=100)
    nivel: str | None = None
    criterios: list[str] | None = None
    observacao: str | None = None


class QualidadeResponse(BaseModel):
    """Representação de um registro de qualidade."""
    model_config = ConfigDict(from_attributes=True)
    id: str
    ativo_id: str
    nivel: str
    score: float
    criterios: list[str] = Field(default_factory=list)
    observacao: str | None = None
    created_at: datetime
    updated_at: datetime | None = None


class QualidadeListResponse(BaseModel):
    """Envelope paginado de listagem de registros de qualidade."""
    total: int
    page: int
    page_size: int
    items: list[QualidadeResponse]


# =============================================================================
# Schemas de Erro
# =============================================================================


class ErrorResponse(BaseModel):
    """Erro padronizado da API."""
    detail: str


__all__ = [
    # Ativos
    "AtivoCreateRequest",
    "AtivoResponse",
    "AtivoListResponse",
    # Catálogos
    "CatalogoCreateRequest",
    "CatalogoUpdateRequest",
    "CatalogoResponse",
    "CatalogoListResponse",
    # Linhagens
    "LinhagemCreateRequest",
    "LinhagemUpdateRequest",
    "LinhagemResponse",
    "LinhagemListResponse",
    # Políticas
    "PoliticaCreateRequest",
    "PoliticaUpdateRequest",
    "PoliticaResponse",
    "PoliticaListResponse",
    # Qualidade
    "QualidadeCreateRequest",
    "QualidadeUpdateRequest",
    "QualidadeResponse",
    "QualidadeListResponse",
    # Erro
    "ErrorResponse",
]
