"""Schemas Pydantic do DOM-TRI — Administração Tributária."""

from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field


class ContribuinteCreateRequest(BaseModel):
    """Payload de cadastro de contribuinte."""

    tipo: str = Field(default="pf", pattern="^(pf|pj)$")
    nome: str = Field(..., min_length=1)
    cpf_cnpj: str = Field(..., min_length=11, max_length=14)
    inscricao_municipal: str = ""
    email: str = ""
    telefone: str = ""
    endereco: str = ""
    created_by: str = ""


class ContribuinteResponse(BaseModel):
    """Representação de contribuinte."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    tipo: str
    nome: str
    cpf_cnpj: str
    inscricao_municipal: str | None = None
    email: str | None = None
    telefone: str | None = None
    endereco: str | None = None
    status: str
    created_at: datetime
    updated_at: datetime | None = None


class ImovelCreateRequest(BaseModel):
    """Payload de cadastro de imóvel."""

    contribuinte_id: str = Field(..., min_length=1)
    inscricao_imobiliaria: str = Field(..., min_length=1)
    logradouro: str = ""
    numero: str = ""
    bairro: str = ""
    cidade: str = ""
    uf: str = ""
    cep: str = ""
    area_terreno: float = 0.0
    area_construida: float = 0.0
    valor_venal: float = Field(..., gt=0)
    aliquota: float = Field(default=0.0, ge=0)
    created_by: str = ""


class ImovelResponse(BaseModel):
    """Representação de imóvel."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    contribuinte_id: str
    inscricao_imobiliaria: str
    logradouro: str | None = None
    numero: str | None = None
    bairro: str | None = None
    cidade: str | None = None
    uf: str | None = None
    cep: str | None = None
    area_terreno: float
    area_construida: float
    valor_venal: float
    aliquota: float
    status: str
    created_at: datetime


class LancamentoCreateRequest(BaseModel):
    """Payload de lançamento de crédito tributário."""

    contribuinte_id: str = Field(..., min_length=1)
    tipo_tributo: str = Field(..., pattern="^(iptu|issqn|itbi|taxa)$")
    exercicio: int = Field(..., gt=0)
    base_calculo: float = Field(default=0.0, ge=0)
    aliquota: float = Field(default=0.0, ge=0)
    imovel_id: str = ""
    descricao: str = ""
    juros: float = 0.0
    multa: float = 0.0
    data_vencimento: date | None = None
    created_by: str = ""


class LancamentoResponse(BaseModel):
    """Representação de lançamento."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    contribuinte_id: str
    imovel_id: str | None = None
    tipo_tributo: str
    exercicio: int
    numero_lancamento: str
    descricao: str | None = None
    base_calculo: float
    aliquota: float
    valor_tributo: float
    juros: float
    multa: float
    valor_total: float
    data_vencimento: date | None = None
    status: str
    data_pagamento: date | None = None
    created_at: datetime


class PagarLancamentoRequest(BaseModel):
    """Payload de pagamento de lançamento."""

    data_pagamento: date | None = None


class DividaAtivaResponse(BaseModel):
    """Representação de inscrição de dívida ativa."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    lancamento_id: str
    numero_inscricao: str
    data_inscricao: date | None = None
    valor_original: float
    valor_atualizado: float
    status: str
    created_at: datetime


class CertidaoResponse(BaseModel):
    """Representação de certidão fiscal."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    contribuinte_id: str
    tipo: str
    numero: str
    data_emissao: date | None = None
    valido_ate: date | None = None
    observacao: str | None = None
    status: str
    created_at: datetime


__all__ = [
    "ContribuinteCreateRequest",
    "ContribuinteResponse",
    "ImovelCreateRequest",
    "ImovelResponse",
    "LancamentoCreateRequest",
    "LancamentoResponse",
    "PagarLancamentoRequest",
    "DividaAtivaResponse",
    "CertidaoResponse",
]