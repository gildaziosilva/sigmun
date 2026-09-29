"""Schemas Pydantic do DOM-GEO — elementos geoespaciais e serviços."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from .camadas import DATUM, ZOOM_MAXIMO, ZOOM_MINIMO

GEOMETRIA = "^(ponto|linha|poligono)$"
TIPO_SERVICO = "^(wms|wfs|wmts|xyz|rest)$"


class VerticeGeo(BaseModel):
    """Vértice de uma geometria geoespacial (RN-GEO-003)."""

    latitude: float = Field(..., ge=-90.0, le=90.0)
    longitude: float = Field(..., ge=-180.0, le=180.0)


class FeatureCreateRequest(BaseModel):
    codigo: str = Field(..., min_length=1)
    nome: str = Field(..., min_length=1)
    descricao: str = ""
    camada_id: str = Field(..., min_length=1)
    geometria: str = Field(default="ponto", pattern=GEOMETRIA)
    latitude: float = Field(default=0.0, ge=-90.0, le=90.0)
    longitude: float = Field(default=0.0, ge=-180.0, le=180.0)
    vertices: list[VerticeGeo] = Field(default_factory=list)
    datum: str = Field(default="sirgas2000", pattern=DATUM)
    atributos: dict[str, object] = Field(default_factory=dict)
    created_by: str = ""


class FeatureResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    codigo: str
    nome: str
    descricao: str | None = None
    camada_id: str
    geometria: str
    latitude: float
    longitude: float
    vertices: list[VerticeGeo] = Field(default_factory=list)
    datum: str
    atributos: dict[str, object] = Field(default_factory=dict)
    criado_por: str | None = None
    created_at: datetime
    updated_at: datetime | None = None


class ServicoCreateRequest(BaseModel):
    codigo: str = Field(..., min_length=1)
    nome: str = Field(..., min_length=1)
    descricao: str = ""
    tipo: str = Field(default="wms", pattern=TIPO_SERVICO)
    url: str = ""
    camada: str = ""
    datum: str = Field(default="sirgas2000", pattern=DATUM)
    srid: int = Field(default=4326, ge=2000, le=99999)
    zoom_minimo: int = Field(default=0, ge=ZOOM_MINIMO, le=ZOOM_MAXIMO)
    zoom_maximo: int = Field(default=24, ge=ZOOM_MINIMO, le=ZOOM_MAXIMO)
    publico: bool = False
    created_by: str = ""


class ServicoUpdateRequest(BaseModel):
    """Campos atualizáveis do serviço geoespacial (todos opcionais)."""

    codigo: str | None = Field(None, min_length=1)
    nome: str | None = Field(None, min_length=1)
    descricao: str | None = None
    tipo: str | None = Field(None, pattern=TIPO_SERVICO)
    url: str | None = None
    camada: str | None = None
    datum: str | None = Field(None, pattern=DATUM)
    srid: int | None = Field(None, ge=2000, le=99999)
    zoom_minimo: int | None = Field(None, ge=ZOOM_MINIMO, le=ZOOM_MAXIMO)
    zoom_maximo: int | None = Field(None, ge=ZOOM_MINIMO, le=ZOOM_MAXIMO)
    publico: bool | None = None
    created_by: str = ""


class ServicoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    codigo: str
    nome: str
    descricao: str | None = None
    tipo: str
    situacao: str
    url: str | None = None
    camada: str | None = None
    datum: str
    srid: int
    zoom_minimo: int
    zoom_maximo: int
    publico: bool
    created_at: datetime
    updated_at: datetime | None = None
