"""Schemas Pydantic do DOM-OBR — medições, despesas, etapas e vistorias."""

from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field

from .obras import ObraResponse

TIPO_MEDICAO = "^(avanco|etapa|final|revisional)$"
SITUACAO_MEDICAO = "^(registrada|conferida|aprovada|glosada|cancelada)$"
TIPO_DESPESA = "^(medicao|repasse|material|mao_de_obra|tributos|custos|outro)$"
TIPO_ETAPA = (
    "^(projeto|terraplanagem|fundacao|estrutura|acabamento|instalacao|pavimentacao"
    "|paisagismo|recepcao)$"
)
SITUACAO_ETAPA = "^(pendente|em_execucao|concluida|atrasada|cancelada)$"
TIPO_VISTORIA = "^(periodica|parcial|final|recepcao)$"
PARECER_VISTORIA = "^(aprovado|aprovado_com_ressalvas|reprovado)$"


class MedicaoCreateRequest(BaseModel):
    obra_id: str = Field(..., min_length=1)
    numero: str = Field(..., min_length=1)
    tipo: str = Field(default="avanco", pattern=TIPO_MEDICAO)
    data: date | None = None
    percentual_fisico: float = Field(default=0.0, ge=0, le=100)
    valor_medido: float = Field(default=0.0, ge=0)
    responsavel_tecnico: str = Field(..., min_length=1)
    observacao: str = ""
    created_by: str = ""


class MedicaoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    obra_id: str
    numero: str
    tipo: str
    situacao: str
    data: date
    percentual_fisico: float
    valor_medido: float
    responsavel_tecnico: str
    observacao: str | None = None
    created_at: datetime
    updated_at: datetime | None = None


class MedicaoGlosaRequest(BaseModel):
    """Justificativa obrigatória para a glosa (RN-OBR-005)."""

    motivo: str = Field(..., min_length=1)
    created_by: str = ""


class DespesaCreateRequest(BaseModel):
    obra_id: str = Field(..., min_length=1)
    medicao_id: str = ""
    descricao: str = Field(..., min_length=1)
    tipo: str = Field(default="medicao", pattern=TIPO_DESPESA)
    valor: float = Field(..., gt=0)
    data: date | None = None
    documento: str = ""
    credor: str = ""
    observacao: str = ""
    created_by: str = ""


class DespesaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    obra_id: str
    medicao_id: str | None = None
    descricao: str
    tipo: str
    valor: float
    data: date
    documento: str | None = None
    credor: str | None = None
    observacao: str | None = None
    created_at: datetime


class EtapaCreateRequest(BaseModel):
    obra_id: str = Field(..., min_length=1)
    numero: str = Field(..., min_length=1)
    descricao: str = Field(..., min_length=1)
    tipo: str = Field(default="estrutura", pattern=TIPO_ETAPA)
    percentual_previsto: float = Field(default=0.0, ge=0, le=100)
    data_inicio_prevista: date | None = None
    data_fim_prevista: date | None = None
    responsavel: str = Field(..., min_length=1)
    created_by: str = ""


class EtapaUpdateRequest(BaseModel):
    """Avanço físico da etapa (RN-OBR-007)."""

    percentual_realizado: float | None = Field(None, ge=0, le=100)
    situacao: str | None = Field(None, pattern=SITUACAO_ETAPA)
    created_by: str = ""


class EtapaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    obra_id: str
    numero: str
    descricao: str
    tipo: str
    situacao: str
    percentual_previsto: float
    percentual_realizado: float
    data_inicio_prevista: date | None = None
    data_fim_prevista: date | None = None
    data_conclusao: date | None = None
    responsavel: str
    created_at: datetime
    updated_at: datetime | None = None


class VistoriaCreateRequest(BaseModel):
    obra_id: str = Field(..., min_length=1)
    data: date | None = None
    tipo: str = Field(default="periodica", pattern=TIPO_VISTORIA)
    parecer: str = Field(default="aprovado", pattern=PARECER_VISTORIA)
    percentual_fisico_verificado: float = Field(default=0.0, ge=0, le=100)
    fiscal: str = Field(..., min_length=1)
    observacao: str = ""
    created_by: str = ""


class VistoriaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    obra_id: str
    data: date
    tipo: str
    parecer: str
    percentual_fisico_verificado: float
    fiscal: str
    observacao: str | None = None
    created_at: datetime


class ObraDetalheResponse(BaseModel):
    """Visão consolidada do acompanhamento físico-financeiro da obra."""

    obra: ObraResponse
    medicoes: list[MedicaoResponse]
    despesas: list[DespesaResponse]
    etapas: list[EtapaResponse]
    vistorias: list[VistoriaResponse]
