"""Eventos de domínio de Atendimento ao Cidadão (DOM-ATE)."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import uuid4

from src.modules.sigmun_ate.domain.entities import (
    StatusAtendimento,
    StatusSenha,
)


@dataclass
class EventoDominio:
    """Classe base para eventos de domínio."""

    id: str = field(default_factory=lambda: str(uuid4()))
    occurred_at: datetime = field(default_factory=datetime.utcnow)
    aggregate_id: str = ""
    aggregate_type: str = ""


@dataclass
class TriagemRealizada(EventoDominio):
    """Evento: Triagem realizada."""

    servico_id: str = ""
    prioridade: int = 0
    observacao: str = ""

    def __post_init__(self):
        self.aggregate_type = "Triagem"


@dataclass
class FilaAberta(EventoDominio):
    """Evento: Fila de atendimento aberta."""

    unidade_id: str = ""
    servico_id: str = ""
    data: str = ""

    def __post_init__(self):
        self.aggregate_type = "FilaAtendimento"


@dataclass
class FilaFechada(EventoDominio):
    """Evento: Fila de atendimento fechada."""

    def __post_init__(self):
        self.aggregate_type = "FilaAtendimento"


@dataclass
class SenhaEmitida(EventoDominio):
    """Evento: Senha emitida."""

    fila_id: str = ""
    servico_id: str = ""
    triagem_id: str = ""
    numero: str = ""
    prioridade: int = 0

    def __post_init__(self):
        self.aggregate_type = "Senha"


@dataclass
class SenhaChamada(EventoDominio):
    """Evento: Senha chamada para atendimento."""

    guiche_id: str = ""
    unidade_id: str = ""
    operador: str = ""
    ordem: int = 0
    tentativa: int = 1

    def __post_init__(self):
        self.aggregate_type = "Senha"


@dataclass
class SenhaRechamada(EventoDominio):
    """Evento: Senha rechamada."""

    guiche_id: str = ""
    unidade_id: str = ""
    operador: str = ""
    ordem: int = 0
    tentativa: int = 1

    def __post_init__(self):
        self.aggregate_type = "Senha"


@dataclass
class SenhaAtendida(EventoDominio):
    """Evento: Senha atendida."""

    def __post_init__(self):
        self.aggregate_type = "Senha"


@dataclass
class SenhaNaoCompareceu(EventoDominio):
    """Evento: Senha não compareceu."""

    def __post_init__(self):
        self.aggregate_type = "Senha"


@dataclass
class SenhaCancelada(EventoDominio):
    """Evento: Senha cancelada."""

    def __post_init__(self):
        self.aggregate_type = "Senha"


@dataclass
class AtendimentoIniciado(EventoDominio):
    """Evento: Atendimento iniciado."""

    chamada_id: str = ""
    canal_id: str = ""

    def __post_init__(self):
        self.aggregate_type = "Atendimento"


@dataclass
class AtendimentoConcluido(EventoDominio):
    """Evento: Atendimento concluído."""

    descricao: str = ""
    duracao_segundos: int = 0

    def __post_init__(self):
        self.aggregate_type = "Atendimento"


@dataclass
class AtendimentoCancelado(EventoDominio):
    """Evento: Atendimento cancelado."""

    motivo: str = ""

    def __post_init__(self):
        self.aggregate_type = "Atendimento"


@dataclass
class AvaliacaoRegistrada(EventoDominio):
    """Evento: Avaliação de atendimento registrada."""

    nota: int = 0
    comentario: str = ""

    def __post_init__(self):
        self.aggregate_type = "AvaliacaoAtendimento"


@dataclass
class EncaminhamentoCriado(EventoDominio):
    """Evento: Encaminhamento criado."""

    destino: str = ""
    motivo: str = ""

    def __post_init__(self):
        self.aggregate_type = "Encaminhamento"


@dataclass
class EncaminhamentoConcluido(EventoDominio):
    """Evento: Encaminhamento concluído."""

    def __post_init__(self):
        self.aggregate_type = "Encaminhamento"


__all__ = [
    "EventoDominio",
    "TriagemRealizada",
    "FilaAberta",
    "FilaFechada",
    "SenhaEmitida",
    "SenhaChamada",
    "SenhaRechamada",
    "SenhaAtendida",
    "SenhaNaoCompareceu",
    "SenhaCancelada",
    "AtendimentoIniciado",
    "AtendimentoConcluido",
    "AtendimentoCancelado",
    "AvaliacaoRegistrada",
    "EncaminhamentoCriado",
    "EncaminhamentoConcluido",
]
