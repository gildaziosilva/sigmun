"""Eventos do domínio de Integração e Interoperabilidade (DOM-INT).

Eventos de domínio emitidos pelo próprio DOM-INT ao barramento corporativo
(tópicos ``int.*``), documentando a atividade do catálogo, os webhooks e
o ciclo de vida das entregas (014-Modelo-de-Integracao).
"""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

__all__ = [
    "EventoIntegracao",
    "EventoApiRegistrada",
    "EventoContratoCriado",
    "EventoConectorConfigurado",
    "EventoWebhookRegistrado",
    "EventoEntregaCriada",
    "EventoEntregaSucesso",
    "EventoEntregaFalha",
    "EventoFilaMorta",
    "EventoOutboxConsumido",
]


@dataclass
class EventoIntegracao:
    """Evento de domínio genérico do DOM-INT."""

    evento_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)
    agregado_tipo: str = ""
    agregado_id: str = ""
    payload: dict = field(default_factory=dict)

    @property
    def evento_nome(self) -> str:
        return self.__class__.__name__.replace("Evento", "")


class EventoApiRegistrada(EventoIntegracao):
    """Emitido quando se registra (ou atualiza) uma API no catálogo."""


class EventoContratoCriado(EventoIntegracao):
    """Emitido quando se cria um contrato de integração."""


class EventoConectorConfigurado(EventoIntegracao):
    """Emitido quando se configura/ativa um conector oficial."""


class EventoWebhookRegistrado(EventoIntegracao):
    """Emitido quando se registra ou atualiza um webhook inscrito."""


class EventoEntregaCriada(EventoIntegracao):
    """Emitido quando o barramento enfileira uma entrega a um webhook."""


class EventoEntregaSucesso(EventoIntegracao):
    """Emitido quando uma entrega a webhook é concluída com sucesso."""


class EventoEntregaFalha(EventoIntegracao):
    """Emitido quando uma entrega a webhook falha (retry programado)."""


class EventoFilaMorta(EventoIntegracao):
    """Emitido quando uma entrega esgota os retries e entra na DLQ."""


class EventoOutboxConsumido(EventoIntegracao):
    """Emitido quando o barramento consome um evento do outbox produtor."""
