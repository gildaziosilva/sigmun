"""Schemas Pydantic do DOM-IMO - avaliação, características e geometria do lote."""

from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field

from .imoveis import DATUM, GEOMETRIA, TIPO_OBRA


class AvaliacaoCreateRequest(BaseModel):
    """Avaliação de valor venal (RN-IMO-005).

    `valor_terreno_m2_unitario` e `valor_construcao_m2_unitario` provêm do
    contrato de integração com o DOM-TEL
    (`GET /api/v1/tel/plantas-valores/vigente`).
    """

    imovel_id: str = Field(..., min_length=1)
    ano: int = Field(..., ge=1900, le=2200)
    valor_terreno_m2_unitario: float = Field(..., ge=0)
    valor_construcao_m2_unitario: float = Field(..., ge=0)
    aliquota_percent: float = Field(default=0.0, ge=0, le=100)
    data_avaliacao: date | None = None
    concluir: bool = True
    created_by: str = ""


class AvaliacaoCancelarRequest(BaseModel):
    """Justificativa do cancelamento da avaliação (RN-IMO-005)."""

    motivo: str = Field(..., min_length=1)
    created_by: str = ""


class AvaliacaoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    imovel_id: str
    ano: int
    valor_terreno_m2_unitario: float
    valor_construcao_m2_unitario: float
    aliquota_percent: float
    area_terreno_m2: float
    area_construida_m2: float
    valor_terreno: float
    valor_construcao: float
    valor_venal: float
    valor_lancamento: float
    situacao: str
    data_avaliacao: date
    created_at: datetime
    updated_at: datetime | None = None


class CaracteristicaCreateRequest(BaseModel):
    imovel_id: str = Field(..., min_length=1)
    obra: str = Field(default="residencial", pattern=TIPO_OBRA)
    numero_pavimentos: int = Field(default=1, ge=1)
    ano_renovacao: int | None = Field(None, ge=1800, le=2200)
    observacao: str = ""
    created_by: str = ""


class CaracteristicaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    imovel_id: str
    obra: str
    numero_pavimentos: int
    ano_renovacao: int | None = None
    observacao: str | None = None
    created_at: datetime
    updated_at: datetime | None = None


class VerticeGeometria(BaseModel):
    """Vértice da geometria do lote (RN-IMO-007)."""

    latitude: float = Field(..., ge=-90.0, le=90.0)
    longitude: float = Field(..., ge=-180.0, le=180.0)


class GeometriaCreateRequest(BaseModel):
    imovel_id: str = Field(..., min_length=1)
    geometria: str = Field(default="ponto", pattern=GEOMETRIA)
    latitude: float = Field(default=0.0, ge=-90.0, le=90.0)
    longitude: float = Field(default=0.0, ge=-180.0, le=180.0)
    vertices: list[VerticeGeometria] = Field(default_factory=list)
    datum: str = Field(default="sirgas2000", pattern=DATUM)
    precisao_m: float = Field(default=0.0, ge=0)
    data_levantamento: date | None = None
    created_by: str = ""


class GeometriaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    imovel_id: str
    geometria: str
    latitude: float
    longitude: float
    vertices: list[VerticeGeometria] = Field(default_factory=list)
    datum: str
    precisao_m: float
    data_levantamento: date
    created_at: datetime
