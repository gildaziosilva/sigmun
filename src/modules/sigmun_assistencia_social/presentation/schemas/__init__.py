"""Schemas Pydantic do DOM-ASS - Assistência Social."""
from __future__ import annotations
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field


class FamiliaCreateRequest(BaseModel):
    nis: str = Field(..., min_length=11, max_length=11)
    responsavel_nome: str = Field(..., min_length=1)
    responsavel_cpf: str = ""
    endereco: str = ""
    telefone: str = ""
    renda_per_capita: float = Field(default=0.0, ge=0)
    quantidade_pessoas: int = Field(default=0, ge=0)
    created_by: str = ""


class FamiliaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    nis: str
    responsavel_nome: str
    responsavel_cpf: str | None = None
    endereco: str | None = None
    telefone: str | None = None
    renda_per_capita: float
    quantidade_pessoas: int
    status: str
    created_at: datetime
    updated_at: datetime | None = None


class PessoaCreateRequest(BaseModel):
    familia_id: str = Field(..., min_length=1)
    nome: str = Field(..., min_length=1)
    cpf: str = Field(..., min_length=11, max_length=11)
    data_nascimento: str = ""
    sexo: str = Field(default="ignorado", pattern="^(masculino|feminino|ignorado)$")
    nome_mae: str = ""
    parentesco: str = ""
    escolaridade: str = ""
    ocupacao: str = ""
    renda: float = Field(default=0.0, ge=0)
    created_by: str = ""


class PessoaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    familia_id: str
    nome: str
    cpf: str
    data_nascimento: str | None = None
    sexo: str
    nome_mae: str | None = None
    parentesco: str | None = None
    escolaridade: str | None = None
    ocupacao: str | None = None
    renda: float
    created_at: datetime
    updated_at: datetime | None = None


class UnidadeCreateRequest(BaseModel):
    codigo: str = Field(..., min_length=1)
    nome: str = Field(..., min_length=1)
    tipo: str = Field(default="cras", pattern="^(cras|creas|centro_pop|abrigo|outro)$")
    endereco: str = ""
    telefone: str = ""
    email: str = ""
    responsavel: str = ""
    created_by: str = ""


class UnidadeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    codigo: str
    nome: str
    tipo: str
    endereco: str | None = None
    telefone: str | None = None
    email: str | None = None
    responsavel: str | None = None
    status: str
    created_at: datetime
    updated_at: datetime | None = None


class BeneficioCreateRequest(BaseModel):
    familia_id: str = Field(..., min_length=1)
    tipo: str = Field(default="alimentacao", pattern="^(alimentacao|aluguel|medicamento|funeral|natalidade|calamidade|outro)$")
    descricao: str = ""
    valor: float = Field(default=0.0, ge=0)
    quantidade: int = Field(default=1, ge=1)
    unidade_id: str = ""
    observacao: str = ""
    created_by: str = ""


class BeneficioResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    familia_id: str
    tipo: str
    descricao: str | None = None
    valor: float
    quantidade: int
    data_solicitacao: datetime
    data_aprovacao: datetime | None = None
    data_entrega: datetime | None = None
    status: str
    unidade_id: str | None = None
    observacao: str | None = None
    created_at: datetime
    updated_at: datetime | None = None


class AtendimentoCreateRequest(BaseModel):
    pessoa_id: str = Field(..., min_length=1)
    unidade_id: str = Field(..., min_length=1)
    tipo: str = Field(default="acolhimento", pattern="^(acolhimento|orientacao|encaminhamento|visita_domiciliar|grupo_convivencia|beneficio_eventual|outro)$")
    data: date | None = None
    descricao: str = ""
    encaminhamento: str = ""
    profissional: str = Field(..., min_length=1)
    created_by: str = ""


class AtendimentoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    pessoa_id: str
    unidade_id: str
    tipo: str
    data: date | None = None
    descricao: str | None = None
    encaminhamento: str | None = None
    profissional: str
    created_at: datetime


class FamiliaUpdateRequest(BaseModel):
    """Campos atualizáveis da família (todos opcionais)."""

    nis: str | None = Field(None, min_length=11, max_length=11)
    responsavel_nome: str | None = Field(None, min_length=1)
    responsavel_cpf: str | None = None
    endereco: str | None = None
    telefone: str | None = None
    renda_per_capita: float | None = Field(None, ge=0)
    quantidade_pessoas: int | None = Field(None, ge=0)
    status: str | None = Field(None, pattern="^(ativa|inativa)$")
    created_by: str = ""


class PessoaUpdateRequest(BaseModel):
    """Campos atualizáveis da pessoa (todos opcionais)."""

    familia_id: str | None = None
    nome: str | None = Field(None, min_length=1)
    cpf: str | None = Field(None, min_length=11, max_length=11)
    data_nascimento: str | None = None
    sexo: str | None = Field(None, pattern="^(masculino|feminino|ignorado)$")
    nome_mae: str | None = None
    parentesco: str | None = None
    escolaridade: str | None = None
    ocupacao: str | None = None
    renda: float | None = Field(None, ge=0)
    created_by: str = ""


class UnidadeUpdateRequest(BaseModel):
    """Campos atualizáveis da unidade (todos opcionais)."""

    codigo: str | None = Field(None, min_length=1)
    nome: str | None = Field(None, min_length=1)
    tipo: str | None = Field(None, pattern="^(cras|creas|centro_pop|abrigo|outro)$")
    endereco: str | None = None
    telefone: str | None = None
    email: str | None = None
    responsavel: str | None = None
    status: str | None = Field(None, pattern="^(ativa|inativa|manutencao)$")
    created_by: str = ""


