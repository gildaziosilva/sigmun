"""Schemas de apresentação (DTOs) de Atendimento ao Cidadão (DOM-ATE)."""

from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field, validator


# =============================================================================
# Triagem
# =============================================================================

class TriagemCreateRequest(BaseModel):
    servico_id: UUID
    observacao: str = ""
    prioridade: int = Field(default=2, ge=1, le=4)

    @validator('prioridade')
    def validar_prioridade(cls, v):
        if v < 1 or v > 4:
            raise ValueError("Prioridade deve estar entre 1 e 4")
        return v


class TriagemResponse(BaseModel):
    id: UUID
    servico_id: UUID
    data_hora: datetime
    classificacao: str
    prioridade: int
    observacao: str
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


# =============================================================================
# Fila
# =============================================================================

class FilaCreateRequest(BaseModel):
    unidade_id: UUID
    servico_id: UUID


class FilaResponse(BaseModel):
    id: UUID
    unidade_id: UUID
    servico_id: UUID
    data: datetime
    status: str
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


# =============================================================================
# Senha
# =============================================================================

class SenhaCreateRequest(BaseModel):
    fila_id: UUID
    servico_id: UUID
    triagem_id: UUID


class SenhaResponse(BaseModel):
    id: UUID
    fila_id: UUID
    servico_id: UUID
    triagem_id: UUID
    numero: str
    data_hora_emissao: datetime
    prioridade: int
    status: str
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


class SenhaChamadaRequest(BaseModel):
    senha_id: UUID
    guiche_id: UUID
    unidade_id: UUID
    operador: str


class SenhaChamadaResponse(BaseModel):
    chamada_id: UUID
    senha_id: UUID
    guiche_id: UUID
    ordem: int

    class Config:
        from_attributes = True


class RechamarSenhaRequest(BaseModel):
    senha_id: UUID


class RechamarSenhaResponse(BaseModel):
    senha_id: UUID
    guiche_id: UUID
    ordem: int

    class Config:
        from_attributes = True


class MarcarSenhaAtendidaRequest(BaseModel):
    senha_id: UUID


class MarcarSenhaAtendidaResponse(BaseModel):
    senha_id: UUID


# =============================================================================
# Atendimento
# =============================================================================

class AtendimentoIniciarRequest(BaseModel):
    chamada_id: UUID
    canal_id: UUID


class AtendimentoIniciarResponse(BaseModel):
    atendimento_id: UUID


class AtendimentoConcluirRequest(BaseModel):
    descricao: str


class AtendimentoConcluirResponse(BaseModel):
    atendimento_id: UUID
    duracao_segundos: int


class AtendimentoCancelarRequest(BaseModel):
    motivo: str


class AtendimentoCancelarResponse(BaseModel):
    atendimento_id: UUID


class AtendimentoResponse(BaseModel):
    id: UUID
    chamada_id: UUID
    canal_id: UUID
    inicio: Optional[datetime]
    fim: Optional[datetime]
    status: str
    descricao: str
    created_at: datetime
    updated_at: Optional[datetime]
    duracao_segundos: Optional[int]
    is_active: bool

    class Config:
        from_attributes = True


# =============================================================================
# Avaliação
# =============================================================================

class AvaliacaoCreateRequest(BaseModel):
    nota: int = Field(ge=1, le=5)
    comentario: str = ""

    @validator('nota')
    def validar_nota(cls, v):
        if v < 1 or v > 5:
            raise ValueError("Nota deve estar entre 1 e 5")
        return v


class AvaliacaoResponse(BaseModel):
    id: UUID
    atendimento_id: UUID
    nota: int
    comentario: str
    data_hora: datetime
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


# =============================================================================
# Encaminhamento
# =============================================================================

class EncaminhamentoCreateRequest(BaseModel):
    atendimento_id: UUID
    destino: str
    motivo: str


class EncaminhamentoResponse(BaseModel):
    id: UUID
    atendimento_id: UUID
    data_hora: datetime
    destino: str
    motivo: str
    status: str
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


class EncaminhamentoConcluirResponse(BaseModel):
    encaminhamento_id: UUID


# =============================================================================
# Guichê
# =============================================================================

class GuicheResponse(BaseModel):
    id: UUID
    unidade_id: UUID
    numero: str
    descricao: str
    ativo: bool
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


# =============================================================================
# Unidade de Atendimento
# =============================================================================

class UnidadeAtendimentoResponse(BaseModel):
    id: UUID
    codigo: str
    nome: str
    ativo: bool
    max_rechamadas: int
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


# =============================================================================
# Serviço de Atendimento
# =============================================================================

class ServicoAtendimentoResponse(BaseModel):
    id: UUID
    codigo: str
    nome: str
    prioridade: int
    ativo: bool
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


# =============================================================================
# Estatísticas
# =============================================================================

class EstatisticasFilaResponse(BaseModel):
    fila_id: UUID
    total_senhas_emitidas: int
    total_senhas_atendidas: int
    total_senhas_nao_compareceu: int
    tempo_medio_espera_minutos: int
    tempo_medio_atendimento_minutos: int


class EstatisticasUnidadeResponse(BaseModel):
    unidade_id: UUID
    total_filas_abertas: int
    total_atendimentos_hoje: int
    total_atendimentos_concluidos: int
    tempo_medio_espera_minutos: int
    nota_media_avaliacao: float


# =============================================================================
# Error Response
# =============================================================================

class ErrorResponse(BaseModel):
    error: str
    message: str
    detail: Optional[str] = None
    code: str = "ATE_ERROR"


__all__ = [
    "TriagemCreateRequest",
    "TriagemResponse",
    "FilaCreateRequest",
    "FilaResponse",
    "SenhaCreateRequest",
    "SenhaResponse",
    "SenhaChamadaRequest",
    "SenhaChamadaResponse",
    "RechamarSenhaResponse",
    "RechamarSenhaRequest",
    "MarcarSenhaAtendidaRequest",
    "MarcarSenhaAtendidaResponse",
    "AtendimentoIniciarRequest",
    "AtendimentoIniciarResponse",
    "AtendimentoConcluirRequest",
    "AtendimentoConcluirResponse",
    "AtendimentoCancelarRequest",
    "AtendimentoCancelarResponse",
    "AtendimentoResponse",
    "AvaliacaoCreateRequest",
    "AvaliacaoResponse",
    "EncaminhamentoCreateRequest",
    "EncaminhamentoResponse",
    "EncaminhamentoConcluirResponse",
    "GuicheResponse",
    "UnidadeAtendimentoResponse",
    "ServicoAtendimentoResponse",
    "ErrorResponse",
]
