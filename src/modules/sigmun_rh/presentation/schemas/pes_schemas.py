"""Schemas Pydantic do DOM-PES (cargos e servidores)."""

from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field


class CargoCreateRequest(BaseModel):
    """Payload de criacao de cargo."""

    codigo: str = Field(..., min_length=1)
    nome: str = Field(..., min_length=1)
    descricao: str = ""
    nivel: str = "basico"
    salario_base: float = Field(..., gt=0)
    carga_horaria_semanal: int = 40
    created_by: str = ""


class CargoResponse(BaseModel):
    """Representacao de cargo."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    codigo: str
    nome: str
    descricao: str | None = None
    nivel: str
    salario_base: float
    carga_horaria_semanal: int
    ativo: bool
    created_at: datetime
    updated_at: datetime | None = None


class ServidorCreateRequest(BaseModel):
    """Payload de admissao de servidor."""

    matricula: str = Field(..., min_length=1)
    cpf: str = Field(..., min_length=11, max_length=11)
    nome: str = Field(..., min_length=1)
    cargo_id: str = Field(..., min_length=1)
    tipo_vinculo: str = "efetivo"
    salario: float = Field(default=0.0, ge=0)
    data_admissao: date | None = None
    email: str = ""
    telefone: str = ""
    created_by: str = ""


class ServidorResponse(BaseModel):
    """Representacao de servidor."""

    model_config = ConfigDict(from_attributes=True)
    id: str
    matricula: str
    cpf: str
    nome: str
    cargo_id: str
    tipo_vinculo: str
    status: str
    data_admissao: date | None = None
    data_desligamento: date | None = None
    salario: float
    email: str | None = None
    telefone: str | None = None
    created_at: datetime
    updated_at: datetime | None = None


__all__ = [
    "CargoCreateRequest",
    "CargoResponse",
    "ServidorCreateRequest",
    "ServidorResponse",
]
