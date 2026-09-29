"""Schemas Pydantic do DOM-TEL - Gestão Territorial (bairros e logradouros)."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

TIPO_BAIRRO = "^(bairro|distrito|setor|zona_rural)$"
TIPO_LOGRADOURO = "^(rua|avenida|travessa|praca|rodovia|estrada|alameda|parque|outro)$"
SITUACAO_BAIRRO = "^(ativo|inativo)$"
SITUACAO_LOGRADOURO = "^(ativo|inativo|em_obra)$"
OCUPACAO = "^(residencial|comercial|industrial|institucional|misto|terreno)$"
SITUACAO_PLANTA = "^(rascunho|vigente|revogada)$"
GEOMETRIA = "^(ponto|linha|poligono)$"
DATUM = "^(sirgas2000|sad69|wgs84)$"


class BairroCreateRequest(BaseModel):
    codigo: str = Field(..., min_length=1)
    nome: str = Field(..., min_length=1)
    tipo: str = Field(default="bairro", pattern=TIPO_BAIRRO)
    populacao_estimada: int = Field(default=0, ge=0)
    area_km2: float = Field(default=0.0, ge=0)
    created_by: str = ""


class BairroUpdateRequest(BaseModel):
    """Campos atualizáveis do bairro (todos opcionais)."""

    codigo: str | None = Field(None, min_length=1)
    nome: str | None = Field(None, min_length=1)
    tipo: str | None = Field(None, pattern=TIPO_BAIRRO)
    populacao_estimada: int | None = Field(None, ge=0)
    area_km2: float | None = Field(None, ge=0)
    situacao: str | None = Field(None, pattern=SITUACAO_BAIRRO)
    created_by: str = ""


class BairroResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    codigo: str
    nome: str
    tipo: str
    populacao_estimada: int
    area_km2: float
    situacao: str
    created_at: datetime
    updated_at: datetime | None = None


class LogradouroCreateRequest(BaseModel):
    codigo: str = Field(..., min_length=1)
    nome: str = Field(..., min_length=1)
    bairro_id: str = Field(..., min_length=1)
    tipo: str = Field(default="rua", pattern=TIPO_LOGRADOURO)
    cep: str = ""
    numero_inicial: int = Field(default=0, ge=0)
    numero_final: int = Field(default=0, ge=0)
    created_by: str = ""


class LogradouroUpdateRequest(BaseModel):
    """Campos atualizáveis do logradouro (todos opcionais)."""

    codigo: str | None = Field(None, min_length=1)
    nome: str | None = Field(None, min_length=1)
    tipo: str | None = Field(None, pattern=TIPO_LOGRADOURO)
    bairro_id: str | None = Field(None, min_length=1)
    cep: str | None = None
    numero_inicial: int | None = Field(None, ge=0)
    numero_final: int | None = Field(None, ge=0)
    situacao: str | None = Field(None, pattern=SITUACAO_LOGRADOURO)
    created_by: str = ""


class LogradouroResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    codigo: str
    nome: str
    tipo: str
    bairro_id: str
    cep: str | None = None
    numero_inicial: int
    numero_final: int
    situacao: str
    created_at: datetime
    updated_at: datetime | None = None
