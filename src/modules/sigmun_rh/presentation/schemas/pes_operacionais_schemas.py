"""Schemas Pydantic de lotacao/folha/ferias/frequencia."""

from __future__ import annotations

from datetime import date, datetime, time

from pydantic import BaseModel, ConfigDict, Field


class LotacaoCreateRequest(BaseModel):
    """Payload de lotacao."""

    servidor_id: str = Field(..., min_length=1)
    unidade_id: str = Field(..., min_length=1)
    cargo_id: str = ""
    data_inicio: date | None = None
    motivo: str = ""
    created_by: str = ""


class LotacaoResponse(BaseModel):
    """Representacao de lotacao."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    servidor_id: str
    unidade_id: str
    cargo_id: str | None = None
    data_inicio: date | None = None
    data_fim: date | None = None
    vigente: bool
    motivo: str | None = None
    created_at: datetime


class FolhaCreateRequest(BaseModel):
    """Payload de abertura de folha."""

    competencia_ano: int = Field(..., ge=2000)
    competencia_mes: int = Field(..., ge=1, le=12)
    descricao: str = ""
    created_by: str = ""


class FolhaConsolidarRequest(BaseModel):
    """Payload de consolidacao."""

    proventos: float = Field(..., ge=0)
    descontos: float = Field(..., ge=0)
    quantidade_servidores: int = Field(..., ge=1)


class FolhaResponse(BaseModel):
    """Representacao de folha."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    competencia_ano: int
    competencia_mes: int
    descricao: str | None = None
    status: str
    total_proventos: float
    total_descontos: float
    total_liquido: float
    quantidade_servidores: int
    created_at: datetime


class FeriasCreateRequest(BaseModel):
    """Payload de planejamento de ferias."""

    servidor_id: str = Field(..., min_length=1)
    periodo_aquisitivo_inicio: date | None = None
    periodo_aquisitivo_fim: date | None = None
    data_inicio_gozo: date | None = None
    data_fim_gozo: date | None = None
    dias: int = Field(default=30, ge=10)
    parcela: int = Field(default=1, ge=1, le=3)
    created_by: str = ""


class FeriasResponse(BaseModel):
    """Representacao de ferias."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    servidor_id: str
    data_inicio_gozo: date | None = None
    data_fim_gozo: date | None = None
    dias: int
    parcela: int
    status: str
    created_at: datetime


class FrequenciaCreateRequest(BaseModel):
    """Payload de frequencia."""

    servidor_id: str = Field(..., min_length=1)
    data: date
    tipo: str = "presenca"
    hora_entrada: time | None = None
    hora_saida: time | None = None
    minutos_atraso: int = Field(default=0, ge=0)
    created_by: str = ""


class FrequenciaResponse(BaseModel):
    """Representacao de frequencia."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    servidor_id: str
    data: date
    tipo: str
    minutos_atraso: int
    desconto_folha: bool
    created_at: datetime


__all__ = [
    "LotacaoCreateRequest",
    "LotacaoResponse",
    "FolhaCreateRequest",
    "FolhaConsolidarRequest",
    "FolhaResponse",
    "FeriasCreateRequest",
    "FeriasResponse",
    "FrequenciaCreateRequest",
    "FrequenciaResponse",
]
