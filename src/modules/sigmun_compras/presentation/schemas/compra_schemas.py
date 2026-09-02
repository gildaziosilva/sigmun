"""Schemas de apresentação (Pydantic) para Compras (processos de compras).

Baseado em:
  - ENT-COMPRAS-003 – Processo de Contratação
  - Estados: 013-Modelo-de-Dados, seção 30
"""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from src.modules.sigmun_compras.domain.entities.compra import SituacaoCompra


class CompraCreateRequest(BaseModel):
    """Payload de registro de uma compra (POST)."""

    processo_documental_id: UUID = Field(
        ..., description="Processo documental vinculado (RN-COMPRAS-025)"
    )
    fornecedor_id: UUID = Field(..., description="Fornecedor contratado (ativo)")
    unidade_id: UUID = Field(..., description="Unidade administrativa responsável")
    numero: str = Field(..., min_length=1, description="Número da compra")
    data: date | None = Field(None, description="Data da compra (default: hoje)")
    valor_total: Decimal | None = Field(None, ge=0)
    situacao: SituacaoCompra | None = Field(
        None, description="Situação inicial (default: RASCUNHO)"
    )


class CompraUpdateRequest(BaseModel):
    """Payload de atualização cadastral (PATCH)."""

    numero: str | None = Field(None, min_length=1)
    data: date | None = None
    valor_total: Decimal | None = Field(None, ge=0)


class CompraSituacaoRequest(BaseModel):
    """Payload de transição de situação processual."""

    situacao: SituacaoCompra


class CompraPendenciasRequest(BaseModel):
    """Payload de registro/resolução de pendências impeditivas (RN-027)."""

    pendencias_impeditivas: bool = Field(
        ...,
        description=(
            "true: registra pendência impeditiva (bloqueia avanço); "
            "false: resolve as pendências"
        ),
    )
    justificativa: str | None = Field(
        None, max_length=500, description="Justificativa do lançamento"
    )


class CompraResponse(BaseModel):
    """Representação de uma compra nas respostas da API."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    processo_documental_id: UUID
    fornecedor_id: UUID
    unidade_id: UUID
    numero: str
    data: date
    valor_total: Decimal | None = None
    situacao: SituacaoCompra
    pendencias_impeditivas: bool = False
    created_at: datetime
    updated_at: datetime


class CompraListResponse(BaseModel):
    """Envelope paginado da listagem de compras."""

    total: int
    page: int
    page_size: int
    items: list[CompraResponse]


__all__ = [
    "CompraCreateRequest",
    "CompraUpdateRequest",
    "CompraSituacaoRequest",
    "CompraPendenciasRequest",
    "CompraResponse",
    "CompraListResponse",
]
