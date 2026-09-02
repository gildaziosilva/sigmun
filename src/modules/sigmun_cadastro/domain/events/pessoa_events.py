"""Eventos de domínio relacionados a Pessoas (DOM-CUM).

Padrão validado no DOM-COMPRAS-001: dataclasses congeladas carregando
os dados relevantes do fato ocorrido.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4


def _novo_id() -> UUID:
    return uuid4()


@dataclass(frozen=True)
class PessoaRegistradaEvent:
    """Emitido quando uma pessoa é registrada no cadastro."""

    event_id: UUID
    pessoa_id: UUID
    tipo: str
    categoria: str
    occurred_at: datetime


@dataclass(frozen=True)
class PessoaAtualizadaEvent:
    """Emitido quando dados cadastrais de uma pessoa são atualizados."""

    event_id: UUID
    pessoa_id: UUID
    occurred_at: datetime


@dataclass(frozen=True)
class PessoaExcluidaEvent:
    """Emitido quando a pessoa é logicamente excluída (RN-CUM-007)."""

    event_id: UUID
    pessoa_id: UUID
    occurred_at: datetime


@dataclass(frozen=True)
class EnderecoAdicionadoEvent:
    """Emitido quando um endereço é adicionado ao agregado (RN-CUM-005)."""

    event_id: UUID
    pessoa_id: UUID
    endereco_id: UUID
    tipo: str
    principal: bool
    occurred_at: datetime


@dataclass(frozen=True)
class DocumentoAdicionadoEvent:
    """Emitido quando um documento é adicionado ao agregado (RN-CUM-006)."""

    event_id: UUID
    pessoa_id: UUID
    documento_id: UUID
    tipo: str
    principal: bool
    occurred_at: datetime


@dataclass(frozen=True)
class ContatoAdicionadoEvent:
    """Emitido quando um contato é adicionado ao agregado."""

    event_id: UUID
    pessoa_id: UUID
    contato_id: UUID
    tipo: str
    principal: bool
    occurred_at: datetime


__all__ = [
    "PessoaRegistradaEvent",
    "PessoaAtualizadaEvent",
    "PessoaExcluidaEvent",
    "EnderecoAdicionadoEvent",
    "DocumentoAdicionadoEvent",
    "ContatoAdicionadoEvent",
]
