"""Schemas Pydantic do DOM-CON."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class EmpenhoCreateRequest(BaseModel):
    """Payload de emissão de empenho."""

    exercicio: int = Field(..., ge=2000)
    numero: str = Field(..., min_length=1)
    dotacao_id: str = Field(..., min_length=1)
    valor: float = Field(..., gt=0)
    favorecido_nome: str = ""
    descricao: str = ""
    tipo: str = "ordinario"
    created_by: str = ""


class EmpenhoResponse(BaseModel):
    """Representação de empenho."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    exercicio: int
    numero: str
    valor_empenhado: float
    valor_liquidado: float
    valor_pago: float
    status: str
    created_at: datetime


class EmpenhoValorRequest(BaseModel):
    """Payload de valor (liquidação/anulação)."""

    valor: float = Field(..., gt=0)
    documento: str = ""


class LiquidacaoResponse(BaseModel):
    """Representação de liquidação."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    empenho_id: str
    valor: float
    status: str
    created_at: datetime


class PagamentoCreateRequest(BaseModel):
    """Payload de pagamento."""

    liquidacao_id: str = Field(..., min_length=1)
    valor: float = Field(..., gt=0)
    conta_bancaria: str = ""
    created_by: str = ""


class PagamentoResponse(BaseModel):
    """Representação de pagamento."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    liquidacao_id: str
    empenho_id: str
    valor: float
    status: str
    created_at: datetime


class ContaCreateRequest(BaseModel):
    """Payload de conta PCASP."""

    codigo: str = Field(..., min_length=1)
    nome: str = Field(..., min_length=1)
    classe: str = ""
    tipo: str = "analitica"
    natureza: str = "devedora"
    created_by: str = ""


class ContaResponse(BaseModel):
    """Representação de conta."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    codigo: str
    nome: str
    tipo: str
    created_at: datetime


class PartidaRequest(BaseModel):
    """Partida dobrada."""

    conta_id: str = Field(..., min_length=1)
    codigo_conta: str = ""
    tipo: str = Field(..., pattern="^(debito|credito)$")
    valor: float = Field(..., gt=0)


class LancamentoCreateRequest(BaseModel):
    """Payload de lançamento."""

    exercicio: int = Field(..., ge=2000)
    historico: str = Field(..., min_length=1)
    partidas: list[PartidaRequest] = Field(..., min_length=2)
    origem: str = ""
    origem_id: str = ""
    created_by: str = ""


class LancamentoResponse(BaseModel):
    """Representação de lançamento."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    exercicio: int
    historico: str
    total_debito: float
    total_credito: float
    status: str


class ConciliacaoCreateRequest(BaseModel):
    """Payload de conciliação."""

    conta_id: str = Field(..., min_length=1)
    codigo_conta: str = ""
    ano: int = Field(..., ge=2000)
    mes: int = Field(..., ge=1, le=12)
    saldo_contabil: float = 0.0
    saldo_extrato: float = 0.0
    justificativa: str = ""
    created_by: str = ""


class ConciliacaoResponse(BaseModel):
    """Representação de conciliação."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    conta_id: str
    competencia_ano: int
    competencia_mes: int
    saldo_contabil: float
    saldo_extrato: float
    diferenca: float
    status: str


__all__ = ["EmpenhoCreateRequest", "EmpenhoResponse", "EmpenhoValorRequest",
           "LiquidacaoResponse", "PagamentoCreateRequest", "PagamentoResponse",
           "ContaCreateRequest", "ContaResponse", "PartidaRequest",
           "LancamentoCreateRequest", "LancamentoResponse",
           "ConciliacaoCreateRequest", "ConciliacaoResponse"]
