"""Schemas Pydantic do DOM-OBR — obras públicas."""

from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field

TIPO_OBRA = (
    "^(pavimentacao|drenagem|construcao|reforma|iluminacao|saneamento|ponte|praca"
    "|quadra|outro)$"
)
SITUACAO_OBRA = (
    "^(planejada|em_licitacao|contratada|em_execucao|suspensa|concluida|cancelada)$"
)
TIPO_CONTRATACAO = "^(licitacao|dispensa|inexigibilidade|convenio|contrato_direto)$"
FONTE_RECURSO = (
    "^(orcamento_proprio|convenio|convenio_estadual|convenio_federal|transferencia"
    "|operacao_credito|outro)$"
)
PERCENTUAL_MIN = 0.0
PERCENTUAL_MAX = 100.0


class ObraCreateRequest(BaseModel):
    numero: str = Field(..., min_length=1)
    nome: str = Field(..., min_length=1)
    descricao: str = ""
    tipo: str = Field(default="outro", pattern=TIPO_OBRA)
    tipo_contratacao: str = Field(default="licitacao", pattern=TIPO_CONTRATACAO)
    fonte_recurso: str = Field(default="orcamento_proprio", pattern=FONTE_RECURSO)
    valor_orcado: float = Field(default=0.0, ge=0)
    valor_contratado: float = Field(default=0.0, ge=0)
    empresa_contratada: str = ""
    numero_contrato: str = ""
    responsavel_tecnico: str = ""
    endereco: str = ""
    bairro: str = ""
    data_inicio_prevista: date | None = None
    data_fim_prevista: date | None = None
    created_by: str = ""


class ObraUpdateRequest(BaseModel):
    """Campos atualizáveis da obra (todos opcionais)."""

    nome: str | None = Field(None, min_length=1)
    descricao: str | None = None
    tipo: str | None = Field(None, pattern=TIPO_OBRA)
    tipo_contratacao: str | None = Field(None, pattern=TIPO_CONTRATACAO)
    fonte_recurso: str | None = Field(None, pattern=FONTE_RECURSO)
    valor_orcado: float | None = Field(None, ge=0)
    valor_contratado: float | None = Field(None, ge=0)
    empresa_contratada: str | None = None
    numero_contrato: str | None = None
    responsavel_tecnico: str | None = None
    endereco: str | None = None
    bairro: str | None = None
    data_inicio_prevista: date | None = None
    data_fim_prevista: date | None = None
    observacao: str | None = None
    created_by: str = ""


class ObraResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    numero: str
    nome: str
    descricao: str | None = None
    tipo: str
    situacao: str
    tipo_contratacao: str
    fonte_recurso: str
    valor_orcado: float
    valor_contratado: float
    valor_mediado: float
    valor_pago: float
    percentual_fisico: float
    percentual_financeiro: float
    empresa_contratada: str | None = None
    numero_contrato: str | None = None
    responsavel_tecnico: str | None = None
    endereco: str | None = None
    bairro: str | None = None
    data_inicio_prevista: date | None = None
    data_fim_prevista: date | None = None
    data_inicio_real: date | None = None
    data_fim_real: date | None = None
    observacao: str | None = None
    created_at: datetime
    updated_at: datetime | None = None


class ObraAcaoRequest(BaseModel):
    """Ações de ciclo de vida da obra com justificativa opcional."""

    motivo: str = ""
    data: date | None = None
    created_by: str = ""
