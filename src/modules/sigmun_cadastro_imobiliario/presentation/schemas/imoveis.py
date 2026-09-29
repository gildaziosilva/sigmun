"""Schemas Pydantic do DOM-IMO - Cadastro Imobiliário (imóveis e proprietários)."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

TIPO_IMOVEL = "^(lote|casa|apartamento|loja|galpao|terreno|outro)$"
SITUACAO_IMOVEL = "^(ativo|inativo|em_obra|desocupado|demolido)$"
TIPO_PROPRIEDADE = "^(proprio|alugado|cedido|invencionado)$"
TIPO_VINCULO = "^(titular|comodato|arrendamento|usufruto|parceiro)$"
SITUACAO_AVALIACAO = "^(rascunho|concluida|cancelada)$"
GEOMETRIA = "^(ponto|linha|poligono)$"
DATUM = "^(sirgas2000|sad69|wgs84)$"
TIPO_OBRA = "^(residencial|comercial|industrial|institucional|mista|nao_aplicavel)$"


class ImovelCreateRequest(BaseModel):
    inscricao_imobiliaria: str = Field(..., min_length=1)
    logradouro_id: str = Field(..., min_length=1)
    bairro_id: str = Field(..., min_length=1)
    numero: str = ""
    complemento: str = ""
    tipo: str = Field(default="lote", pattern=TIPO_IMOVEL)
    tipo_propriedade: str = Field(default="proprio", pattern=TIPO_PROPRIEDADE)
    area_terreno_m2: float = Field(default=0.0, ge=0)
    area_construida_m2: float = Field(default=0.0, ge=0)
    ano_construcao: int | None = Field(None, ge=1800, le=2200)
    created_by: str = ""


class ImovelUpdateRequest(BaseModel):
    """Campos atualizáveis do imóvel (todos opcionais)."""

    numero: str | None = None
    complemento: str | None = None
    tipo: str | None = Field(None, pattern=TIPO_IMOVEL)
    tipo_propriedade: str | None = Field(None, pattern=TIPO_PROPRIEDADE)
    area_terreno_m2: float | None = Field(None, ge=0)
    area_construida_m2: float | None = Field(None, ge=0)
    ano_construcao: int | None = Field(None, ge=1800, le=2200)
    created_by: str = ""


class ImovelSituacaoRequest(BaseModel):
    """Nova situação do imóvel (RN-IMO-004)."""

    situacao: str = Field(..., pattern=SITUACAO_IMOVEL)
    created_by: str = ""


class ImovelResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    inscricao_imobiliaria: str
    logradouro_id: str
    bairro_id: str
    numero: str | None = None
    complemento: str | None = None
    tipo: str
    situacao: str
    tipo_propriedade: str
    area_terreno_m2: float
    area_construida_m2: float
    ano_construcao: int | None = None
    created_at: datetime
    updated_at: datetime | None = None


class ProprietarioCreateRequest(BaseModel):
    imovel_id: str = Field(..., min_length=1)
    nome: str = Field(..., min_length=1)
    # CPF (11 dígitos) para pessoa física ou CNPJ (14 dígitos) para jurídica.
    cpf: str = Field(..., min_length=11, max_length=14, pattern=r"^\d{11,14}$")
    pessoa_id: str = ""
    vinculo: str = Field(default="titular", pattern=TIPO_VINCULO)
    principal: bool = False
    created_by: str = ""


class ProprietarioResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    imovel_id: str
    pessoa_id: str
    nome: str
    cpf: str
    vinculo: str
    principal: bool
    created_at: datetime
    updated_at: datetime | None = None
