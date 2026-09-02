"""Schemas de apresentação (Pydantic) para Contratos.

Baseado em:
  - ENT-COMPRAS-009 – Contrato
  - RN-COMPRAS-035 a 039
"""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from src.modules.sigmun_compras.domain.entities.contrato import SituacaoContrato


class ContratoCreateRequest(BaseModel):
    """Payload de registro de contrato (POST)."""

    processo_documental_id: UUID = Field(
        ..., description="Processo contratado (RN-COMPRAS-038)"
    )
    fornecedor_id: UUID = Field(..., description="Fornecedor contratado (ativo)")
    unidade_id: UUID = Field(..., description="Unidade administrativa responsável")
    numero: str = Field(..., min_length=1, description="Número único do contrato")
    data_inicio: Optional[date] = Field(None, description="Início da vigência")
    data_fim: Optional[date] = Field(None, description="Fim da vigência (RN-037)")
    valor: Optional[Decimal] = Field(None, ge=0, description="Valor contratual")
    objeto: Optional[str] = Field(None, max_length=2000)
    licitacao_master_id: Optional[UUID] = None
    situacao: Optional[SituacaoContrato] = Field(
        None, description="Situação inicial (default: EM_ELABORACAO)"
    )


class ContratoUpdateRequest(BaseModel):
    """Payload de atualização cadastral (PATCH)."""

    numero: Optional[str] = Field(None, min_length=1)
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    valor: Optional[Decimal] = Field(None, ge=0)
    objeto: Optional[str] = Field(None, max_length=2000)


class ContratoSituacaoRequest(BaseModel):
    """Payload de transição de situação."""

    situacao: SituacaoContrato


class FormalizarContratacaoRequest(BaseModel):
    """Payload da Formalização da Contratação (Compra -> Contrato).

    Integração do domínio (UC-COMPRAS-022 / RN-COMPRAS-038). O contrato
    herda processo documental, fornecedor e unidade da compra referenciada
    e passa a rastrear a origem via ``compra_id``.
    """

    numero: str = Field(..., min_length=1, description="Número único do contrato")
    data_inicio: date = Field(..., description="Início da vigência")
    data_fim: Optional[date] = Field(None, description="Fim da vigência (RN-037)")
    valor: Optional[Decimal] = Field(None, ge=0, description="Valor contratual")
    objeto: Optional[str] = Field(None, max_length=2000)
    data_assinatura: Optional[date] = Field(
        None, description="Data de assinatura; avança a situação para ASSINADO"
    )


class ContratoResponse(BaseModel):
    """Representação de um contrato nas respostas da API."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    processo_documental_id: UUID
    fornecedor_id: UUID
    unidade_id: UUID
    licitacao_master_id: Optional[UUID] = None
    compra_id: Optional[UUID] = None
    numero: str
    data_inicio: date
    data_fim: Optional[date] = None
    valor: Optional[Decimal] = None
    objeto: Optional[str] = None
    situacao: SituacaoContrato
    created_at: datetime
    updated_at: datetime


class ContratoListResponse(BaseModel):
    """Envelope paginado da listagem de contratos."""

    total: int
    page: int
    page_size: int
    items: list[ContratoResponse]


__all__ = [
    "ContratoCreateRequest",
    "ContratoUpdateRequest",
    "ContratoSituacaoRequest",
    "FormalizarContratacaoRequest",
    "ContratoResponse",
    "ContratoListResponse",
]
