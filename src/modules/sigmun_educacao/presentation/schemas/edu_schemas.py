"""Schemas Pydantic do DOM-EDU - Educacao Publica."""
from __future__ import annotations
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field

class AlunoCreateRequest(BaseModel):
    nome: str = Field(..., min_length=1)
    cpf: str = ""
    data_nascimento: str = ""
    sexo: str = Field(default="ignorado", pattern="^(masculino|feminino|ignorado)$")
    nome_mae: str = ""
    telefone: str = ""
    endereco: str = ""
    created_by: str = ""

class AlunoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str; nome: str; cpf: str | None = None; data_nascimento: str | None = None
    sexo: str; nome_mae: str | None = None; telefone: str | None = None; endereco: str | None = None
    status: str; created_at: datetime; updated_at: datetime | None = None

class MatriculaCreateRequest(BaseModel):
    aluno_id: str = Field(..., min_length=1)
    escola: str = Field(..., min_length=1)
    serie: str = Field(..., min_length=1)
    turno: str = Field(default="manha", pattern="^(manha|tarde|noite)$")
    ano_letivo: int = 0
    created_by: str = ""

class MatriculaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str; aluno_id: str; escola: str; serie: str; turno: str; ano_letivo: int
    data_matricula: date | None = None; status: str; escola_destino: str | None = None
    motivo: str | None = None; created_at: datetime

class LancamentoDiarioCreateRequest(BaseModel):
    matricula_id: str = Field(..., min_length=1)
    data: date | None = None
    presente: bool = True
    nota: float | None = Field(default=None, ge=0, le=10)
    observacao: str = ""
    created_by: str = ""

class LancamentoDiarioResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str; matricula_id: str; data: date | None = None; presente: bool
    nota: float | None = None; observacao: str | None = None; created_at: datetime

class RotaTransporteCreateRequest(BaseModel):
    identificacao: str = Field(..., min_length=1)
    motorista: str = Field(..., min_length=1)
    veiculo: str = ""
    vagas: int = Field(..., ge=1)
    turno: str = Field(default="manha", pattern="^(manha|tarde|noite)$")
    created_by: str = ""

class RotaTransporteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str; identificacao: str; veiculo: str | None = None; motorista: str
    vagas: int; turno: str; status: str; created_at: datetime

class PassagemTransporteCreateRequest(BaseModel):
    rota_id: str = Field(..., min_length=1)
    matricula_id: str = Field(..., min_length=1)
    data: date | None = None
    created_by: str = ""

class PassagemTransporteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str; rota_id: str; matricula_id: str; data: date | None = None; created_at: datetime

class ItemMerendaCreateRequest(BaseModel):
    nome: str = Field(..., min_length=1)
    tipo: str = "refeicao"
    estoque: float = Field(default=0.0, ge=0)
    estoque_minimo: float = Field(default=0.0, ge=0)
    created_by: str = ""

class ItemMerendaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str; nome: str; tipo: str; estoque: float; estoque_minimo: float; created_at: datetime

class DistribuicaoMerendaCreateRequest(BaseModel):
    matricula_id: str = Field(..., min_length=1)
    item_id: str = Field(..., min_length=1)
    quantidade: float = Field(..., gt=0)
    refeicao: str = Field(default="almoco", pattern="^(almoco|lanche|jantar)$")
    data: date | None = None
    created_by: str = ""

class DistribuicaoMerendaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str; matricula_id: str; item_id: str; quantidade: float; data: date | None = None
    refeicao: str; created_at: datetime
