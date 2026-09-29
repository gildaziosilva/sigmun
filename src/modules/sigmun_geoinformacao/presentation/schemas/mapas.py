"""Schemas Pydantic do DOM-GEO — mapas SIG e composição de camadas."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from .camadas import DATUM, ZOOM_MAXIMO, ZOOM_MINIMO

TIPO_MAPA = "^(tematico|cadastral|basemap|infraestrutura|ambiental|outro)$"
SITUACAO_MAPA = "^(rascunho|publicado|arquivado)$"


class MapaCreateRequest(BaseModel):
    codigo: str = Field(..., min_length=1)
    nome: str = Field(..., min_length=1)
    descricao: str = ""
    tipo: str = Field(default="tematico", pattern=TIPO_MAPA)
    datum: str = Field(default="sirgas2000", pattern=DATUM)
    srid: int = Field(default=4326, ge=2000, le=99999)
    escala_denominador: int = Field(default=0, ge=0)
    zoom_inicial: int = Field(default=13, ge=ZOOM_MINIMO, le=ZOOM_MAXIMO)
    zoom_minimo: int = Field(default=0, ge=ZOOM_MINIMO, le=ZOOM_MAXIMO)
    zoom_maximo: int = Field(default=24, ge=ZOOM_MINIMO, le=ZOOM_MAXIMO)
    lat_min: float | None = Field(None, ge=-90.0, le=90.0)
    lon_min: float | None = Field(None, ge=-180.0, le=180.0)
    lat_max: float | None = Field(None, ge=-90.0, le=90.0)
    lon_max: float | None = Field(None, ge=-180.0, le=180.0)
    created_by: str = ""


class MapaUpdateRequest(BaseModel):
    """Campos atualizáveis do mapa SIG (todos opcionais)."""

    codigo: str | None = Field(None, min_length=1)
    nome: str | None = Field(None, min_length=1)
    descricao: str | None = None
    tipo: str | None = Field(None, pattern=TIPO_MAPA)
    datum: str | None = Field(None, pattern=DATUM)
    srid: int | None = Field(None, ge=2000, le=99999)
    escala_denominador: int | None = Field(None, ge=0)
    zoom_inicial: int | None = Field(None, ge=ZOOM_MINIMO, le=ZOOM_MAXIMO)
    zoom_minimo: int | None = Field(None, ge=ZOOM_MINIMO, le=ZOOM_MAXIMO)
    zoom_maximo: int | None = Field(None, ge=ZOOM_MINIMO, le=ZOOM_MAXIMO)
    lat_min: float | None = Field(None, ge=-90.0, le=90.0)
    lon_min: float | None = Field(None, ge=-180.0, le=180.0)
    lat_max: float | None = Field(None, ge=-90.0, le=90.0)
    lon_max: float | None = Field(None, ge=-180.0, le=180.0)
    created_by: str = ""


class MapaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    codigo: str
    nome: str
    descricao: str | None = None
    tipo: str
    situacao: str
    datum: str
    srid: int
    escala_denominador: int
    zoom_inicial: int
    zoom_minimo: int
    zoom_maximo: int
    lat_min: float | None = None
    lon_min: float | None = None
    lat_max: float | None = None
    lon_max: float | None = None
    publicado_em: datetime | None = None
    criado_por: str | None = None
    created_at: datetime
    updated_at: datetime | None = None


class MapaComposicaoRequest(BaseModel):
    """DTO de composição de camada em um mapa (RN-GEO-004)."""

    camada_id: str = Field(..., min_length=1)
    ordem: int = Field(default=0, ge=0)
    opacidade: float = Field(default=100.0, ge=0.0, le=100.0)
    visivel: bool = True
    rotulo: str = ""
    created_by: str = ""


class MapaCamadaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    mapa_id: str
    camada_id: str
    ordem: int
    opacidade: float
    visivel: bool
    rotulo: str | None = None
    created_at: datetime


class MapaComposicaoResponse(BaseModel):
    """Composição de um mapa com os dados de cada camada composta."""

    mapa: MapaResponse
    camadas: list[MapaCamadaResponse]
