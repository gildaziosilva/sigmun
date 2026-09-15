"""Eventos de domínio do módulo de Segurança da Informação."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class EventoSeguranca:
    """Evento base do domínio de segurança."""

    occurred_at: datetime
    aggregate_id: str
    tipo: str = ""


@dataclass(frozen=True)
class ControleImplementadoEvent(EventoSeguranca):
    """Disparado quando um controle de segurança é implementado."""

    pass


@dataclass(frozen=True)
class PoliticaAprovadaEvent(EventoSeguranca):
    """Disparado quando uma política de segurança é aprovada."""

    pass


@dataclass(frozen=True)
class IncidenteRegistradoEvent(EventoSeguranca):
    """Disparado quando um incidente de segurança é registrado."""

    pass


@dataclass(frozen=True)
class IncidenteResolvidoEvent(EventoSeguranca):
    """Disparado quando um incidente é resolvido."""

    pass


@dataclass(frozen=True)
class ChaveRevogadaEvent(EventoSeguranca):
    """Disparado quando uma chave criptográfica é revogada."""

    pass


@dataclass(frozen=True)
class CredencialRevogadaEvent(EventoSeguranca):
    """Disparado quando uma credencial é revogada."""

    pass


__all__ = [
    "EventoSeguranca",
    "ControleImplementadoEvent",
    "PoliticaAprovadaEvent",
    "IncidenteRegistradoEvent",
    "IncidenteResolvidoEvent",
    "ChaveRevogadaEvent",
    "CredencialRevogadaEvent",
]
