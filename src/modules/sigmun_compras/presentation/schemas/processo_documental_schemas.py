"""Schemas de apresentação (Pydantic) para Processos Documentais.

Baseado em:
  - UC-COMPRAS-013 – Abrir Processo de Contratação
  - Modelo Físico: core.processos_documentais
"""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ProcessoDocumentalCreateRequest(BaseModel):
    """Payload de abertura de processo documental (POST)."""

    unidade_id: UUID = Field(..., description="Unidade responsável (RN-COMPRAS-028)")
    numero: str = Field(..., min_length=1, description="Número do processo")
    ano: int = Field(..., ge=1900, le=2100, description="Ano do processo")
    assunto: str = Field(..., min_length=3, description="Assunto do processo")
    descricao: str | None = None


class ProcessoDocumentalUpdateRequest(BaseModel):
    """Payload de atualização (PATCH)."""

    numero: str | None = Field(None, min_length=1)
    ano: int | None = Field(None, ge=1900, le=2100)
    assunto: str | None = Field(None, min_length=3)
    descricao: str | None = None


class ProcessoDocumentalResponse(BaseModel):
    """Representação de um processo documental nas respostas da API."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    unidade_id: UUID
    numero: str
    ano: int
    assunto: str
    descricao: str | None = None
    created_at: datetime
    updated_at: datetime


class ProcessoDocumentalListResponse(BaseModel):
    """Envelope paginado da listagem de processos documentais."""

    total: int
    page: int
    page_size: int
    items: list[ProcessoDocumentalResponse]


__all__ = [
    "ProcessoDocumentalCreateRequest",
    "ProcessoDocumentalUpdateRequest",
    "ProcessoDocumentalResponse",
    "ProcessoDocumentalListResponse",
]
