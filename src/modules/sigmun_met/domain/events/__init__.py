"""Eventos de domínio do módulo de Metadados Corporativos."""

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
class MetadadoCriadoEvent(DomainEvent):
    """Evento disparado quando um metadado é criado."""
    codigo: str = ""
    nome: str = ""


@dataclass
class MetadadoAtualizadoEvent(DomainEvent):
    """Evento disparado quando um metadado é atualizado."""
    campos_alterados: list[str] = field(default_factory=list)


@dataclass
class MetadadoAtivadoEvent(DomainEvent):
    """Evento disparado quando um metadado é ativado."""
    pass


@dataclass
class MetadadoDesativadoEvent(DomainEvent):
    """Evento disparado quando um metadado é desativado."""
    pass


@dataclass
class ValorMetadadoAtribuidoEvent(DomainEvent):
    """Evento disparado quando um valor de metadado é atribuído."""
    metadado_id: str = ""
    entidade_tipo: str = ""
    entidade_id: str = ""


@dataclass
class ValorMetadadoRemovidoEvent(DomainEvent):
    """Evento disparado quando um valor de metadado é removido."""
    metadado_id: str = ""
    entidade_id: str = ""


@dataclass
class ClassificacaoCriadaEvent(DomainEvent):
    """Evento disparado quando uma classificação é criada."""
    codigo: str = ""
    tipo: str = ""


@dataclass
class TaxonomiaCriadaEvent(DomainEvent):
    """Evento disparado quando uma taxonomia é criada."""
    codigo: str = ""
    nome: str = ""


@dataclass
class TermoCriadoEvent(DomainEvent):
    """Evento disparado quando um termo de taxonomia é criado."""
    taxonomia_id: str = ""
    codigo: str = ""
    termo_pai_id: str = ""


__all__ = [
    "DomainEvent",
    "MetadadoCriadoEvent",
    "MetadadoAtualizadoEvent",
    "MetadadoAtivadoEvent",
    "MetadadoDesativadoEvent",
    "ValorMetadadoAtribuidoEvent",
    "ValorMetadadoRemovidoEvent",
    "ClassificacaoCriadaEvent",
    "TaxonomiaCriadaEvent",
    "TermoCriadoEvent",
]
