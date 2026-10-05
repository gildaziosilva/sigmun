"""Comandos CQRS de Atendimento ao Cidadão (DOM-ATE)."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import uuid4


@dataclass
class RealizarTriagemCommand:
    """Comando: Realizar triagem de atendimento."""

    servico_id: str
    observacao: str = ""
    prioridade: int = 2


@dataclass
class AbrirFilaCommand:
    """Comando: Abrir fila de atendimento."""

    unidade_id: str
    servico_id: str


@dataclass
class FecharFilaCommand:
    """Comando: Fechar fila de atendimento."""

    fila_id: str


@dataclass
class EmitirSenhaCommand:
    """Comando: Emitir senha de atendimento."""

    fila_id: str
    servico_id: str
    triagem_id: str


@dataclass
class ChamarSenhaCommand:
    """Comando: Chamar senha para atendimento."""

    senha_id: str
    guiche_id: str
    unidade_id: str
    operador: str


@dataclass
class RechamarSenhaCommand:
    """Comando: Rechamar senha."""

    senha_id: str


@dataclass
class MarcarSenhaAtendidaCommand:
    """Comando: Marcar senha como atendida."""

    senha_id: str


@dataclass
class IniciarAtendimentoCommand:
    """Comando: Iniciar atendimento."""

    chamada_id: str
    canal_id: str


@dataclass
class ConcluirAtendimentoCommand:
    """Comando: Concluir atendimento."""

    atendimento_id: str
    descricao: str


@dataclass
class CancelarAtendimentoCommand:
    """Comando: Cancelar atendimento."""

    atendimento_id: str
    motivo: str


@dataclass
class RegistrarAvaliacaoCommand:
    """Comando: Registrar avaliação de atendimento."""

    atendimento_id: str
    nota: int
    comentario: str = ""


@dataclass
class CriarEncaminhamentoCommand:
    """Comando: Criar encaminhamento."""

    atendimento_id: str
    destino: str
    motivo: str


@dataclass
class ConcluirEncaminhamentoCommand:
    """Comando: Concluir encaminhamento."""

    encaminhamento_id: str


__all__ = [
    "RealizarTriagemCommand",
    "AbrirFilaCommand",
    "FecharFilaCommand",
    "EmitirSenhaCommand",
    "ChamarSenhaCommand",
    "RechamarSenhaCommand",
    "MarcarSenhaAtendidaCommand",
    "IniciarAtendimentoCommand",
    "ConcluirAtendimentoCommand",
    "CancelarAtendimentoCommand",
    "RegistrarAvaliacaoCommand",
    "CriarEncaminhamentoCommand",
    "ConcluirEncaminhamentoCommand",
]