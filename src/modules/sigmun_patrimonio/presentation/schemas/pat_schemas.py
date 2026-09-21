"""Schemas Pydantic do DOM-PAT — Gestão Patrimonial."""

from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field


class BemCreateRequest(BaseModel):
    """Payload de cadastro de bem."""

    codigo: str = Field(..., min_length=1)
    tipo: str = Field(default="movel", pattern="^(movel|imovel)$")
    descricao: str = Field(..., min_length=1)
    valor_aquisicao: float = Field(..., gt=0)
    categoria: str = ""
    data_aquisicao: date | None = None
    valor_residual: float = 0.0
    vida_util_anos: int = 0
    localizacao: str = ""
    responsavel_id: str = ""
    created_by: str = ""


class BemResponse(BaseModel):
    """Representação de bem."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    codigo: str
    tipo: str
    descricao: str
    categoria: str | None = None
    valor_aquisicao: float
    data_aquisicao: date | None = None
    valor_residual: float
    vida_util_anos: int
    valor_contabil: float
    status: str
    localizacao: str | None = None
    responsavel_id: str | None = None
    created_at: datetime


class DepreciacaoCreateRequest(BaseModel):
    """Payload de depreciação."""

    data: date | None = None


class DepreciacaoResponse(BaseModel):
    """Representação de depreciação."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    bem_id: str
    data: date | None = None
    valor_depreciado: float
    valor_acumulado: float
    valor_liquido: float
    created_at: datetime


class TransferenciaCreateRequest(BaseModel):
    """Payload de transferência de bem."""

    bem_id: str = Field(..., min_length=1)
    para_localizacao: str = Field(..., min_length=1)
    de_localizacao: str = ""
    de_responsavel_id: str = ""
    para_responsavel_id: str = ""
    motivo: str = ""
    created_by: str = ""


class TransferenciaResponse(BaseModel):
    """Representação de transferência."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    bem_id: str
    de_localizacao: str | None = None
    para_localizacao: str
    de_responsavel_id: str | None = None
    para_responsavel_id: str | None = None
    data_transferencia: date | None = None
    motivo: str | None = None
    status: str
    created_at: datetime


__all__ = [
    "BemCreateRequest",
    "BemResponse",
    "DepreciacaoCreateRequest",
    "DepreciacaoResponse",
    "TransferenciaCreateRequest",
    "TransferenciaResponse",
]