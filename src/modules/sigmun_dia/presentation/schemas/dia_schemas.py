"""Schemas de apresentação (Pydantic) para Diárias e Viagens (DOM-DIA)."""

from __future__ import annotations

from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


# =============================================================================
# Schemas de Viagem
# =============================================================================


class ViagemCreateRequest(BaseModel):
    """Payload de criação de viagem."""

    servidor_id: str = Field(..., min_length=1)
    dota_id: str = Field(..., min_length=1)
    motivo: str = Field(..., min_length=3, max_length=500)
    cargo_ocupado: str | None = None
    unidade_origem_id: str = Field(..., min_length=1)
    unidade_destino_id: str = Field(..., min_length=1)
    data_inicio: date | None = None
    data_fim: date | None = None
    destino: str = Field(..., min_length=3, max_length=200)
    is_antecipacao: bool = False
    created_by: str = ""


class ViagemResponse(BaseModel):
    """Representação de uma viagem."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    servidor_id: str
    dota_id: str
    motivo: str
    cargo_ocupado: str | None = None
    unidade_origem_id: str
    unidade_destino_id: str
    data_inicio: date | None = None
    data_fim: date | None = None
    destino: str
    is_antecipacao: bool
    created_at: datetime
    updated_at: datetime | None = None
    created_by: str | None = None


class ViagemListResponse(BaseModel):
    """Envelope de listagem de viagens."""

    total: int
    page: int
    page_size: int
    items: list[ViagemResponse]


# =============================================================================
# Schemas de Diária
# =============================================================================


class DiariaCreateRequest(BaseModel):
    """Payload de criação de diária."""

    viagem_id: str = Field(..., min_length=1)
    servidor_id: str = Field(..., min_length=1)
    dota_id: str = Field(..., min_length=1)
    categoria: str = Field(..., min_length=1)
    descricao: str = Field(..., min_length=3, max_length=1000)
    data_inicio: date | None = None
    data_fim: date | None = None
    valor_diaria: float = Field(..., ge=0)
    created_by: str = ""


class DiariaResponse(BaseModel):
    """Representação de uma diária."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    viagem_id: str
    servidor_id: str
    dota_id: str
    categoria: str
    descricao: str
    data_inicio: date | None = None
    data_fim: date | None = None
    valor_diaria: float
    valor_total: float
    status: str
    data_solicitacao: datetime | None = None
    data_autorizacao: datetime | None = None
    data_calculo: datetime | None = None
    data_concessao: datetime | None = None
    data_inicio_prestacao: datetime | None = None
    data_fim_prestacao: datetime | None = None
    data_pagamento: datetime | None = None
    data_aprovacao: datetime | None = None
    data_glosa: datetime | None = None
    data_restituicao: datetime | None = None
    data_cancelamento: datetime | None = None
    motivo_cancelamento: str | None = None
    motivo_glosa: str | None = None
    valor_glosado: float = 0.0
    documento_prestacao_id: str | None = None
    created_at: datetime
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None


class DiariaListResponse(BaseModel):
    """Envelope de listagem de diárias."""

    total: int
    page: int
    page_size: int
    items: list[DiariaResponse]


# =============================================================================
# Schemas de Transição de Status
# =============================================================================


class DiariaStatusTransitionRequest(BaseModel):
    """Payload para transição de status de diária."""

    documento_prestacao_id: str | None = None
    data_inicio_prestacao: date | None = None
    data_fim_prestacao: date | None = None
    created_by: str = ""


class DiariaPagamentoRequest(BaseModel):
    """Payload para pagamento de diária."""

    created_by: str = ""


class DiariaAprovacaoRequest(BaseModel):
    """Payload para aprovação de diária."""

    created_by: str = ""


class DiariaGlosaRequest(BaseModel):
    """Payload para glosa de diária."""

    motivo: str = Field(..., min_length=3)
    valor_glosado: float = Field(..., ge=0)
    created_by: str = ""


class DiariaRestituicaoRequest(BaseModel):
    """Payload para restituição de diária."""

    created_by: str = ""


class DiariaCancelamentoRequest(BaseModel):
    """Payload para cancelamento de diária."""

    motivo: str = Field(..., min_length=3)
    created_by: str = ""


# =============================================================================
# Schemas de Prestação de Contas
# =============================================================================


class PrestacaoContasCreateRequest(BaseModel):
    """Payload de criação de prestação de contas."""

    diaria_id: str = Field(..., min_length=1)
    servidor_id: str = Field(..., min_length=1)
    dota_id: str = Field(..., min_length=1)
    documento_id: str = Field(..., min_length=1)
    valor_previsto: float = Field(..., ge=0)
    valor_apresentado: float = Field(..., ge=0)
    data_vencimento: datetime | None = None
    created_by: str = ""


class PrestacaoContasResponse(BaseModel):
    """Representação de uma prestação de contas."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    diaria_id: str
    servidor_id: str
    dota_id: str
    data_emissao: datetime
    data_vencimento: datetime | None = None
    documento_id: str
    valor_previsto: float
    valor_apresentado: float
    valor_glosado: float
    valor_liquido: float
    status: str
    motivo_glosa: str | None = None
    created_at: datetime
    updated_at: datetime | None = None
    created_by: str | None = None


class PrestacaoContasListResponse(BaseModel):
    """Envelope de listagem de prestações."""

    total: int
    page: int
    page_size: int
    items: list[PrestacaoContasResponse]


class PrestacaoContasGlosaRequest(BaseModel):
    """Payload para glosa de prestação."""

    motivo: str = Field(..., min_length=3)
    valor_glosado: float = Field(..., ge=0)
    created_by: str = ""


class PrestacaoContasAprovacaoRequest(BaseModel):
    """Payload para aprovação de prestação."""

    created_by: str = ""


class PrestacaoContasRestituicaoRequest(BaseModel):
    """Payload para restituição de prestação."""

    created_by: str = ""


# =============================================================================
# Schemas de Evento/Auditoria
# =============================================================================


class EventoDiariaResponse(BaseModel):
    """Representação de um evento de auditoria de diária."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    diaria_id: str
    status_anterior: str
    status_posterior: str
    usuario_id: str
    motivo: str | None = None
    data_evento: datetime
    detalhes: str | None = None


__all__ = [
    # Schemas de Viagem
    "ViagemCreateRequest",
    "ViagemResponse",
    "ViagemListResponse",
    # Schemas de Diária
    "DiariaCreateRequest",
    "DiariaResponse",
    "DiariaListResponse",
    # Schemas de Transição
    "DiariaStatusTransitionRequest",
    "DiariaPagamentoRequest",
    "DiariaAprovacaoRequest",
    "DiariaGlosaRequest",
    "DiariaRestituicaoRequest",
    "DiariaCancelamentoRequest",
    # Schemas de Prestação de Contas
    "PrestacaoContasCreateRequest",
    "PrestacaoContasResponse",
    "PrestacaoContasListResponse",
    "PrestacaoContasGlosaRequest",
    "PrestacaoContasAprovacaoRequest",
    "PrestacaoContasRestituicaoRequest",
    # Schemas de Auditoria
    "EventoDiariaResponse",
]

