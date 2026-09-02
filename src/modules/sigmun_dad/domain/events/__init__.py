"""Eventos de domínio do módulo de Dados Corporativos."""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class DomainEvent:
    """Base para eventos de domínio."""
    event_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)
    aggregate_id: str = ""


@dataclass
class AtivoCriadoEvent(DomainEvent):
    """Evento disparado quando um ativo é criado."""
    nome: str = ""
    tipo: str = ""


@dataclass
class AtivoAtualizadoEvent(DomainEvent):
    """Evento disparado quando um ativo é atualizado."""
    campos_alterados: list[str] = field(default_factory=list)


@dataclass
class AtivoAtivadoEvent(DomainEvent):
    """Evento disparado quando um ativo é ativado."""
    pass


@dataclass
class AtivoDesativadoEvent(DomainEvent):
    """Evento disparado quando um ativo é desativado."""
    pass


@dataclass
class AtivoArquivadoEvent(DomainEvent):
    """Evento disparado quando um ativo é arquivado."""
    pass


@dataclass
class CatalogoCriadoEvent(DomainEvent):
    """Evento disparado quando um catálogo é criado."""
    nome: str = ""


@dataclass
class CatalogoAtualizadoEvent(DomainEvent):
    """Evento disparado quando um catálogo é atualizado."""
    pass


@dataclass
class LinhagemCriadaEvent(DomainEvent):
    """Evento disparado quando uma linhagem é criada."""
    ativo_origem_id: str = ""
    ativo_destino_id: str = ""


@dataclass
class PoliticaCriadaEvent(DomainEvent):
    """Evento disparado quando uma política é criada."""
    codigo: str = ""
    nome: str = ""


@dataclass
class QualidadeAvaliadaEvent(DomainEvent):
    """Evento disparado quando a qualidade é avaliada."""
    ativo_id: str = ""
    score: float = 0.0
    nivel: str = ""


__all__ = [
    "DomainEvent",
    "AtivoCriadoEvent",
    "AtivoAtualizadoEvent",
    "AtivoAtivadoEvent",
    "AtivoDesativadoEvent",
    "AtivoArquivadoEvent",
    "CatalogoCriadoEvent",
    "CatalogoAtualizadoEvent",
    "LinhagemCriadaEvent",
    "PoliticaCriadaEvent",
    "QualidadeAvaliadaEvent",
]
