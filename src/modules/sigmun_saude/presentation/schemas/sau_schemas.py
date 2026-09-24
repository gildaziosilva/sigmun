"""Schemas Pydantic do DOM-SAU - Saude Municipal."""
from __future__ import annotations
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field

class PacienteCreateRequest(BaseModel):
    nome: str = Field(..., min_length=1)
    cns: str = Field(..., min_length=15, max_length=15)
    cpf: str = ""
    data_nascimento: str = ""
    sexo: str = Field(default="ignorado", pattern="^(masculino|feminino|ignorado)$")
    nome_mae: str = ""
    telefone: str = ""
    endereco: str = ""
    ubs_referencia: str = ""
    created_by: str = ""

class PacienteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str; nome: str; cns: str; cpf: str | None = None; data_nascimento: str | None = None
    sexo: str; nome_mae: str | None = None; telefone: str | None = None; endereco: str | None = None
    ubs_referencia: str | None = None; status: str; created_at: datetime; updated_at: datetime | None = None

class AtendimentoCreateRequest(BaseModel):
    paciente_id: str = Field(..., min_length=1)
    profissional: str = Field(..., min_length=1)
    estabelecimento: str = Field(..., min_length=1)
    tipo: str = Field(default="consulta", pattern="^(consulta|retorno|urgencia|visita_domiciliar|teleatendimento)$")
    data: date | None = None; queixa: str = ""; conduta: str = ""; cid10: str = ""; created_by: str = ""

class AtendimentoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str; paciente_id: str; data: date | None = None; tipo: str; profissional: str; estabelecimento: str
    queixa: str | None = None; conduta: str | None = None; cid10: str | None = None; created_at: datetime

class AgendamentoCreateRequest(BaseModel):
    paciente_id: str = Field(..., min_length=1)
    especialidade: str = Field(..., min_length=1)
    data: date | None = None; hora: str = ""; estabelecimento: str = ""; created_by: str = ""

class AgendamentoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str; paciente_id: str; especialidade: str; data: date | None = None; hora: str | None = None
    estabelecimento: str | None = None; status: str; created_at: datetime

class RegulacaoCreateRequest(BaseModel):
    paciente_id: str = Field(..., min_length=1)
    procedimento: str = Field(..., min_length=1)
    prioridade: str = Field(default="rotina", pattern="^(rotina|prioritaria|urgencia)$")
    solicitante: str = ""; created_by: str = ""

class RegulacaoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str; paciente_id: str; procedimento: str; prioridade: str; solicitante: str | None = None
    data_solicitacao: date | None = None; status: str; justificativa: str | None = None; created_at: datetime

class MedicamentoCreateRequest(BaseModel):
    nome: str = Field(..., min_length=1)
    apresentacao: str = ""; estoque: float = Field(default=0.0, ge=0); estoque_minimo: float = Field(default=0.0, ge=0); created_by: str = ""

class MedicamentoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str; nome: str; apresentacao: str | None = None; estoque: float; estoque_minimo: float; created_at: datetime

class DispensacaoCreateRequest(BaseModel):
    paciente_id: str = Field(..., min_length=1)
    medicamento_id: str = Field(..., min_length=1)
    quantidade: float = Field(..., gt=0); receita: str = ""; created_by: str = ""

class DispensacaoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str; paciente_id: str; medicamento_id: str; quantidade: float; data: date | None = None; receita: str | None = None; created_at: datetime
