"""Schemas Pydantic do DOM-FRO — Gestão de Frota."""

from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field


class VeiculoCreateRequest(BaseModel):
    """Payload de cadastro de veículo."""

    placa: str = Field(..., min_length=1)
    marca: str = Field(..., min_length=1)
    modelo: str = Field(..., min_length=1)
    chassi: str = ""
    renavam: str = ""
    ano_fabricacao: int = 0
    ano_modelo: int = 0
    tipo: str = Field(default="leve",
                      pattern="^(leve|pesado|motocicleta|onibus|trator)$")
    combustivel: str = Field(
        default="flex",
        pattern="^(gasolina|alcool|flex|diesel|eletrico|gas)$",
    )
    capacidade: float = 0.0
    odometro_atual: float = 0.0
    unidade_id: str = ""
    created_by: str = ""


class VeiculoResponse(BaseModel):
    """Representação de veículo."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    placa: str
    chassi: str | None = None
    renavam: str | None = None
    marca: str
    modelo: str
    ano_fabricacao: int
    ano_modelo: int
    tipo: str
    combustivel: str
    capacidade: float
    odometro_atual: float
    status: str
    unidade_id: str | None = None
    created_at: datetime


class AbastecimentoCreateRequest(BaseModel):
    """Payload de abastecimento."""

    quantidade_litros: float = Field(..., gt=0)
    valor_unitario: float = 0.0
    data: date | None = None
    odometro: float = 0.0
    posto: str = ""
    tipo_combustivel: str = Field(
        default="flex",
        pattern="^(gasolina|alcool|flex|diesel|eletrico|gas)$",
    )
    created_by: str = ""


class AbastecimentoResponse(BaseModel):
    """Representação de abastecimento."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    veiculo_id: str
    data: date | None = None
    quantidade_litros: float
    valor_unitario: float
    valor_total: float
    odometro: float
    posto: str | None = None
    tipo_combustivel: str
    created_at: datetime


class ManutencaoCreateRequest(BaseModel):
    """Payload de abertura de manutenção."""

    descricao: str = Field(..., min_length=1)
    tipo: str = Field(default="preventiva", pattern="^(preventiva|corretiva)$")
    oficina: str = ""
    valor: float = 0.0
    data_entrada: date | None = None
    created_by: str = ""


class ManutencaoResponse(BaseModel):
    """Representação de manutenção."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    veiculo_id: str
    data_entrada: date | None = None
    data_saida: date | None = None
    tipo: str
    descricao: str
    oficina: str | None = None
    valor: float
    status: str
    created_at: datetime


class RotaCreateRequest(BaseModel):
    """Payload de rota."""

    origem: str = Field(..., min_length=1)
    destino: str = Field(..., min_length=1)
    data: date | None = None
    km_inicio: float = 0.0
    km_fim: float = 0.0
    descricao: str = ""
    created_by: str = ""


class RotaResponse(BaseModel):
    """Representação de rota."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    veiculo_id: str
    data: date | None = None
    origem: str
    destino: str
    km_inicio: float
    km_fim: float
    distancia_km: float
    descricao: str | None = None
    status: str
    created_at: datetime


__all__ = [
    "VeiculoCreateRequest",
    "VeiculoResponse",
    "AbastecimentoCreateRequest",
    "AbastecimentoResponse",
    "ManutencaoCreateRequest",
    "ManutencaoResponse",
    "RotaCreateRequest",
    "RotaResponse",
]