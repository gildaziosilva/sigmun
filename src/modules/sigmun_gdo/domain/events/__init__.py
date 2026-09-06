"""Eventos do domínio de Gestão Documental."""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class EventoDocumento:
    """Evento de domínio genérico para documentos."""
    evento_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)
    documento_id: str = ""
    usuario_id: str = ""
    payload: dict = field(default_factory=dict)

    @property
    def evento_nome(self) -> str:
        return self.__class__.__name__.replace("Evento", "")


class EventoDocumentoCriado(EventoDocumento):
    """Evento disparado quando um documento é criado."""
    pass


class EventoDocumentoCapturado(EventoDocumento):
    """Evento disparado quando um documento é capturado/armazenado."""
    pass


class EventoDocumentoClassificado(EventoDocumento):
    """Evento disparado quando um documento é classificado."""
    pass


class EventoDocumentoTramitado(EventoDocumento):
    """Evento disparado quando um documento é tramitado."""
    pass


class EventoDocumentoArquivado(EventoDocumento):
    """Evento disparado quando um documento é arquivado."""
    pass


class EventoDocumentoRejeitado(EventoDocumento):
    """Evento disparado quando um documento é rejeitado."""
    pass


class EventoDocumentoAssinado(EventoDocumento):
    """Evento disparado quando um documento é assinado."""
    pass


class EventoDocumentoEliminado(EventoDocumento):
    """Evento disparado quando um documento é eliminado."""
    pass


class EventoDocumentoDestinado(EventoDocumento):
    """Evento disparado quando um documento é destinado."""
    pass


__all__ = [
    "EventoDocumento",
    "EventoDocumentoCriado",
    "EventoDocumentoCapturado",
    "EventoDocumentoClassificado",
    "EventoDocumentoTramitado",
    "EventoDocumentoArquivado",
    "EventoDocumentoRejeitado",
    "EventoDocumentoAssinado",
    "EventoDocumentoEliminado",
    "EventoDocumentoDestinado",
]
