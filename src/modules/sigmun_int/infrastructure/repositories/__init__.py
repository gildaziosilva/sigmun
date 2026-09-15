"""Repositórios do módulo de Integração e Interoperabilidade (DOM-INT)."""

from .sqlalchemy_api_externa_repository import SqlAlchemyApiExternaRepository
from .sqlalchemy_conector_repository import SqlAlchemyConectorRepository
from .sqlalchemy_contrato_repository import SqlAlchemyContratoIntegracaoRepository
from .sqlalchemy_entrega_repository import SqlAlchemyEntregaWebhookRepository
from .sqlalchemy_evento_processado_repository import SqlAlchemyEventoProcessadoRepository
from .sqlalchemy_webhook_repository import SqlAlchemyWebhookRepository

__all__ = [
    "SqlAlchemyApiExternaRepository",
    "SqlAlchemyContratoIntegracaoRepository",
    "SqlAlchemyConectorRepository",
    "SqlAlchemyWebhookRepository",
    "SqlAlchemyEntregaWebhookRepository",
    "SqlAlchemyEventoProcessadoRepository",
]