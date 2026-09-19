"""Schemas Pydantic do DOM-ORC."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class PPACreateRequest(BaseModel):
    """Payload de criação de PPA."""

    ano_inicial: int = Field(..., ge=2000)
    ano_final: int = Field(..., ge=2000)
    descricao: str = ""
    created_by: str = ""


class PPAResponse(BaseModel):
    """Representação de PPA."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    ano_inicial: int
    ano_final: int
    descricao: str | None = None
    status: str
    created_at: datetime


class LDOCreateRequest(BaseModel):
    """Payload de criação de LDO."""

    exercicio: int = Field(..., ge=2000)
    ppa_id: str = Field(..., min_length=1)
    descricao: str = ""
    meta_receita: float = Field(default=0.0, ge=0)
    meta_despesa: float = Field(default=0.0, ge=0)
    created_by: str = ""


class LDOResponse(BaseModel):
    """Representação de LDO."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    exercicio: int
    ppa_id: str
    descricao: str | None = None
    status: str
    created_at: datetime


class LOACreateRequest(BaseModel):
    """Payload de criação de LOA."""

    exercicio: int = Field(..., ge=2000)
    ldo_id: str = Field(..., min_length=1)
    descricao: str = ""
    receita: float = Field(default=0.0, ge=0)
    despesa: float = Field(default=0.0, ge=0)
    created_by: str = ""


class LOAResponse(BaseModel):
    """Representação de LOA."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    exercicio: int
    ldo_id: str
    descricao: str | None = None
    status: str
    created_at: datetime


class DotacaoCreateRequest(BaseModel):
    """Payload de criação de dotação."""

    loa_id: str = Field(..., min_length=1)
    exercicio: int = Field(..., ge=2000)
    codigo: str = Field(..., min_length=1)
    valor_inicial: float = Field(..., gt=0)
    unidade_orcamentaria: str = ""
    natureza_despesa: str = ""
    fonte_recursos: str = ""
    created_by: str = ""


class DotacaoValorRequest(BaseModel):
    """Payload de movimentação de valor."""

    valor: float = Field(..., gt=0)


class DotacaoResponse(BaseModel):
    """Representação de dotação."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    exercicio: int
    codigo: str
    valor_inicial: float
    valor_atualizado: float
    saldo_disponivel: float
    status: str
    created_at: datetime


class ReservaCreateRequest(BaseModel):
    """Payload de reserva de saldo."""

    dotacao_id: str = Field(..., min_length=1)
    valor: float = Field(..., gt=0)
    finalidade: str = ""
    numero: str = ""
    created_by: str = ""


class ReservaResponse(BaseModel):
    """Representação de reserva."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    dotacao_id: str
    valor: float
    status: str
    created_at: datetime


__all__ = ["PPACreateRequest", "PPAResponse", "LDOCreateRequest", "LDOResponse",
           "LOACreateRequest", "LOAResponse", "DotacaoCreateRequest",
           "DotacaoValorRequest", "DotacaoResponse", "ReservaCreateRequest",
           "ReservaResponse"]
