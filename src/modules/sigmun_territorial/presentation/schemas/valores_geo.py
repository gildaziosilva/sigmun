"""Schemas Pydantic do DOM-TEL - planta de valores e georreferenciamento."""

from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field

from .territoriais import (
    DATUM,
    GEOMETRIA,
    OCUPACAO,
)


class VerticeGeometria(BaseModel):
    """Vértice de uma geometria territorial."""

    latitude: float = Field(..., ge=-90.0, le=90.0)
    longitude: float = Field(..., ge=-180.0, le=180.0)


class PlantaValoresCreateRequest(BaseModel):
    ano: int = Field(..., ge=1900, le=2200)
    bairro_id: str = Field(..., min_length=1)
    ocupacao: str = Field(default="residencial", pattern=OCUPACAO)
    valor_terreno_m2: float = Field(default=0.0, ge=0)
    valor_construcao_m2: float = Field(default=0.0, ge=0)
    aliquota_percent: float = Field(default=0.0, ge=0, le=100)
    legislacao: str = ""
    ativar: bool = False
    created_by: str = ""


class PlantaValoresUpdateRequest(BaseModel):
    """Campos atualizáveis da planta genérica de valores (todos opcionais)."""

    ano: int | None = Field(None, ge=1900, le=2200)
    valor_terreno_m2: float | None = Field(None, ge=0)
    valor_construcao_m2: float | None = Field(None, ge=0)
    aliquota_percent: float | None = Field(None, ge=0, le=100)
    legislacao: str | None = None
    created_by: str = ""


class PlantaValoresResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    ano: int
    bairro_id: str
    ocupacao: str
    valor_terreno_m2: float
    valor_construcao_m2: float
    aliquota_percent: float
    situacao: str
    legislacao: str | None = None
    created_at: datetime
    updated_at: datetime | None = None


class PlantaValoresRevogarRequest(BaseModel):
    """Justificativa obrigatória para revogação (RN-TEL-004)."""

    motivo: str = Field(..., min_length=1)
    created_by: str = ""


class GeorreferenciaCreateRequest(BaseModel):
    bairro_id: str = ""
    logradouro_id: str = ""
    geometria: str = Field(default="ponto", pattern=GEOMETRIA)
    latitude: float = Field(default=0.0, ge=-90.0, le=90.0)
    longitude: float = Field(default=0.0, ge=-180.0, le=180.0)
    altitude_m: float | None = None
    vertices: list[VerticeGeometria] = Field(default_factory=list)
    datum: str = Field(default="sirgas2000", pattern=DATUM)
    precisao_m: float = Field(default=0.0, ge=0)
    data_levantamento: date | None = None
    created_by: str = ""


class GeorreferenciaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    bairro_id: str
    logradouro_id: str
    geometria: str
    latitude: float
    longitude: float
    altitude_m: float | None = None
    vertices: list[VerticeGeometria] = Field(default_factory=list)
    datum: str
    precisao_m: float
    data_levantamento: date
    created_at: datetime
