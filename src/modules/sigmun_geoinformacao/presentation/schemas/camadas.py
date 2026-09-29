"""Schemas Pydantic do DOM-GEO — camadas de mapa."""

from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field

DATUM = "^(sirgas2000|sad69|wgs84)$"
TIPO_CAMADA = (
    "^(ortofoto|hipsometria|hipsografia|topografia|hidrografia|uso_solo|vegetacao"
    "|malha_urbana|infraestrutura|cadastro_territorial|outro)$"
)
FORMATO_CAMADA = (
    "^(geotiff|shapefile|geojson|kml|postgis|wms|wfs|wmts|xyz|vetorial)$"
)
SITUACAO_CAMADA = "^(rascunho|ativa|desativada)$"
ZOOM_MINIMO = 0
ZOOM_MAXIMO = 24


class CamadaCreateRequest(BaseModel):
    codigo: str = Field(..., min_length=1)
    nome: str = Field(..., min_length=1)
    descricao: str = ""
    tipo: str = Field(default="outro", pattern=TIPO_CAMADA)
    formato: str = Field(default="geojson", pattern=FORMATO_CAMADA)
    fonte: str = ""
    data_atualizacao: date | None = None
    datum: str = Field(default="sirgas2000", pattern=DATUM)
    srid: int = Field(default=4326, ge=2000, le=99999)
    url_servico: str = ""
    zoom_minimo: int = Field(default=0, ge=ZOOM_MINIMO, le=ZOOM_MAXIMO)
    zoom_maximo: int = Field(default=24, ge=ZOOM_MINIMO, le=ZOOM_MAXIMO)
    ativar: bool = False
    created_by: str = ""


class CamadaUpdateRequest(BaseModel):
    """Campos atualizáveis da camada de mapa (todos opcionais)."""

    codigo: str | None = Field(None, min_length=1)
    nome: str | None = Field(None, min_length=1)
    descricao: str | None = None
    tipo: str | None = Field(None, pattern=TIPO_CAMADA)
    formato: str | None = Field(None, pattern=FORMATO_CAMADA)
    fonte: str | None = None
    data_atualizacao: date | None = None
    datum: str | None = Field(None, pattern=DATUM)
    srid: int | None = Field(None, ge=2000, le=99999)
    url_servico: str | None = None
    zoom_minimo: int | None = Field(None, ge=ZOOM_MINIMO, le=ZOOM_MAXIMO)
    zoom_maximo: int | None = Field(None, ge=ZOOM_MINIMO, le=ZOOM_MAXIMO)
    visivel: bool | None = None
    created_by: str = ""


class CamadaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    codigo: str
    nome: str
    descricao: str | None = None
    tipo: str
    formato: str
    fonte: str | None = None
    data_atualizacao: date
    datum: str
    srid: int
    url_servico: str | None = None
    zoom_minimo: int
    zoom_maximo: int
    visivel: bool
    situacao: str
    created_at: datetime
    updated_at: datetime | None = None
