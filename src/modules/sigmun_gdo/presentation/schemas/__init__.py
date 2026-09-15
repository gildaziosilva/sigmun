"""Schemas de apresentação (Pydantic) para Gestão Documental (DOM-GDO)."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from src.modules.sigmun_gdo.domain.entities import (
    TipoDestinacao,
    TipoTramitacao,
)

# =============================================================================
# Schemas de Documento
# =============================================================================


class DocumentoCreateRequest(BaseModel):
    """Payload de criação de documento."""

    codigo: str = Field(..., min_length=3, max_length=100)
    numero: str = Field(..., min_length=1, max_length=50)
    ano: int = Field(..., ge=1900, le=2100)
    tipo_documental_id: str = Field(..., min_length=1)
    titulo: str = Field(..., min_length=3, max_length=200)
    descricao: str | None = None
    unidade_autor_id: str = Field(..., min_length=1)
    unidade_arquivo_id: str | None = None
    processo_id: str | None = None
    is_sigiloso: bool = False
    conteudo_ref: str | None = None
    hash_integridade: str | None = None


class DocumentoResponse(BaseModel):
    """Representação de um documento."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    codigo: str
    numero: str
    ano: int
    tipo_documental_id: str
    titulo: str
    descricao: str | None = None
    data_criacao: datetime | None = None
    data_recebimento: datetime | None = None
    data_arquivamento: datetime | None = None
    data_encerramento: datetime | None = None
    data_eliminacao: datetime | None = None
    unidade_autor_id: str
    unidade_arquivo_id: str | None = None
    processo_id: str | None = None
    status: str
    is_sigiloso: bool
    conteudo_ref: str | None = None
    hash_integridade: str | None = None
    created_at: datetime
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None


class DocumentoListResponse(BaseModel):
    """Envelope de listagem de documentos."""

    total: int
    page: int
    page_size: int
    items: list[DocumentoResponse]


class DocumentoCapturaRequest(BaseModel):
    """Payload para captura de documento via upload."""

    codigo: str = Field(..., min_length=3, max_length=100)
    numero: str = Field(..., min_length=1, max_length=50)
    ano: int = Field(..., ge=1900, le=2100)
    tipo_documental_id: str = Field(..., min_length=1)
    titulo: str = Field(..., min_length=3, max_length=200)
    descricao: str | None = None
    unidade_autor_id: str = Field(..., min_length=1)
    unidade_arquivo_id: str | None = None
    processo_id: str | None = None
    is_sigiloso: bool = False
    hash_integridade: str | None = None


# =============================================================================
# Schemas de Tramitação
# =============================================================================


class TramitacaoCreateRequest(BaseModel):
    """Payload de criação de tramitação."""

    documento_id: str | None = None
    unidade_origem_id: str
    unidade_destino_id: str
    tipo: TipoTramitacao
    motivo: str | None = None
    observacao: str | None = None


class TramitacaoResponse(BaseModel):
    """Representação de uma tramitação."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    documento_id: str
    unidade_origem_id: str
    unidade_destino_id: str
    tipo: str
    data_envio: datetime | None = None
    data_recebimento: datetime | None = None
    data_devolucao: datetime | None = None
    motivo: str | None = None
    observacao: str | None = None
    created_at: datetime


# =============================================================================
# Schemas de Classificação
# =============================================================================


class ClassificacaoCreateRequest(BaseModel):
    """Payload de criação de classificação."""

    codigo: str = Field(..., min_length=1, max_length=100)
    nome: str = Field(..., min_length=3, max_length=200)
    descricao: str | None = None
    nivel: int = Field(..., ge=0)
    classificacao_pai_id: str | None = None
    prazo_retencao: int = Field(..., ge=0)
    unidade_destino_id: str | None = None


class ClassificacaoResponse(BaseModel):
    """Representação de uma classificação."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    codigo: str
    nome: str
    descricao: str | None = None
    nivel: int
    classificacao_pai_id: str | None = None
    prazo_retencao: int
    unidade_destino_id: str | None = None
    created_at: datetime
    is_active: bool


class ClassificacaoListResponse(BaseModel):
    """Envelope de listagem de classificações."""

    total: int
    page: int
    page_size: int
    items: list[ClassificacaoResponse]


# =============================================================================
# Schemas de Processo
# =============================================================================


class ProcessoDocumentoCreateRequest(BaseModel):
    """Payload de criação de processo."""

    numero: str = Field(..., min_length=1, max_length=50)
    ano: int = Field(..., ge=1900, le=2100)
    tipo_processo_id: str = Field(..., min_length=1)
    titulo: str = Field(..., min_length=3, max_length=200)
    descricao: str | None = None
    unidade_autor_id: str = Field(..., min_length=1)


class ProcessoDocumentoResponse(BaseModel):
    """Representação de um processo documental."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    numero: str
    ano: int
    tipo_processo_id: str
    titulo: str
    descricao: str | None = None
    unidade_autor_id: str
    data_abertura: datetime
    data_encerramento: datetime | None = None
    status: str
    created_at: datetime
    is_active: bool


# =============================================================================
# Schemas de Temporalidade
# =============================================================================


class TabelaTemporalidadeCreateRequest(BaseModel):
    """Payload de criação de tabela de temporalidade."""

    codigo: str = Field(..., min_length=1, max_length=100)
    nome: str = Field(..., min_length=3, max_length=200)
    prazo_tempo: int = Field(..., ge=0)
    unidade_tempo: str = Field(..., pattern="^(meses|anos|dias)$")
    evento_fim: str = Field(..., min_length=1)
    tipo_destinacao: TipoDestinacao = TipoDestinacao.ELIMINACAO


class TabelaTemporalidadeResponse(BaseModel):
    """Representação de uma tabela de temporalidade."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    codigo: str
    nome: str
    prazo_tempo: int
    unidade_tempo: str
    evento_fim: str
    tipo_destinacao: str
    is_ativo: bool
    created_at: datetime


# =============================================================================
# Schemas Comuns
# =============================================================================


class ErrorResponse(BaseModel):
    """Schema de erro padrão."""

    detail: str


# =============================================================================
# Schemas de Arquivamento
# =============================================================================


class ArquivamentoCreateRequest(BaseModel):
    """Payload de arquivamento de documento."""

    unidade_arquivo_id: str = Field(..., min_length=1)
    autor_id: str = Field(..., min_length=1)
    observacao: str | None = None


class ArquivamentoResponse(BaseModel):
    """Representação de um arquivamento."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    documento_id: str
    data_arquivamento: datetime
    data_restauracao: datetime | None = None
    created_by: str | None = None
    observacao: str | None = None
    is_restaurado: bool


# =============================================================================
# Schemas de Assinatura
# =============================================================================


class AssinaturaCreateRequest(BaseModel):
    """Payload de assinatura digital de documento."""

    signatario_id: str = Field(..., min_length=1)
    conteudo: str = Field(
        ...,
        min_length=1,
        description="Conteúdo a ser assinado (hash SHA-256 calculado pelo serviço)",
    )
    autor_id: str = Field(..., min_length=1)
    certificado_id: str | None = None


class AssinaturaResponse(BaseModel):
    """Representação de uma assinatura digital."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    documento_id: str
    signatario_id: str
    data_assinatura: datetime
    hash_assinatura: str
    certificado_id: str | None = None
    is_valida: bool
    is_revogada: bool


# =============================================================================
# Schemas de Versão
# =============================================================================


class VersaoCreateRequest(BaseModel):
    """Payload de criação de versão de documento."""

    conteudo_ref: str = Field(..., min_length=1)
    autor_id: str = Field(..., min_length=1)
    hash_integridade: str | None = None


class VersaoDocumentoResponse(BaseModel):
    """Representação de uma versão de documento."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    documento_id: str
    numero_versao: int
    conteudo_ref: str | None = None
    hash_integridade: str | None = None
    data_versao: datetime
    created_by: str | None = None


# =============================================================================
# Schemas de Destinação
# =============================================================================


class DestinacaoRequest(BaseModel):
    """Payload de aplicação de destinação final (RN-GDO-004/010/011)."""

    tipo_destinacao: str = Field(..., pattern="^(eliminacao|guarda_permanente)$")
    autor_id: str = Field(..., min_length=1)
    autoridade_homologadora_id: str | None = None
    justificativa: str | None = None


# =============================================================================
# Schemas de Tipo Documental
# =============================================================================


class TipoDocumentoCreateRequest(BaseModel):
    """Payload de criação de tipo documental."""

    codigo: str = Field(..., min_length=1, max_length=50)
    nome: str = Field(..., min_length=1, max_length=100)
    descricao: str | None = None


class TipoDocumentoResponse(BaseModel):
    """Representação de um tipo documental."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    codigo: str
    nome: str
    descricao: str | None = None
    is_ativo: bool
    created_at: datetime | None = None
    updated_at: datetime | None = None


__all__ = [
    "DocumentoCreateRequest",
    "DocumentoResponse",
    "DocumentoListResponse",
    "DocumentoCapturaRequest",
    "TramitacaoCreateRequest",
    "TramitacaoResponse",
    "ClassificacaoCreateRequest",
    "ClassificacaoResponse",
    "ClassificacaoListResponse",
    "ProcessoDocumentoCreateRequest",
    "ProcessoDocumentoResponse",
    "TabelaTemporalidadeCreateRequest",
    "TabelaTemporalidadeResponse",
    "ArquivamentoCreateRequest",
    "ArquivamentoResponse",
    "AssinaturaCreateRequest",
    "AssinaturaResponse",
    "VersaoCreateRequest",
    "VersaoDocumentoResponse",
    "DestinacaoRequest",
    "TipoDocumentoCreateRequest",
    "TipoDocumentoResponse",
    "ErrorResponse",
]
