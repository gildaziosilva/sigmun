"""Interfaces da camada de aplicação do DOM-INT.

Define os contratos (ABC) de repositórios que a camada de domínio/aplicação
exige e que a infraestrutura implementa, junto com as abstrações do
barramento de eventos: ``FonteOutbox`` (leitura dos outbox produtores) e
``TransporteWebhook`` (entrega HTTP aos inscritos com retry/DLQ).
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime

from ...domain.entities import (
    ApiExterna,
    Conector,
    ContratoIntegracao,
    EntregaWebhook,
    EventoProcessado,
    Webhook,
)

__all__ = [
    "EventoOutbox",
    "ResultadoEnvio",
    "RepositorioApiExterna",
    "RepositorioContratoIntegracao",
    "RepositorioConector",
    "RepositorioWebhook",
    "RepositorioEntregaWebhook",
    "RepositorioEventoProcessado",
    "FonteOutbox",
    "TransporteWebhook",
]


# ---------------------------------------------------------------------------
# Objetos de valor de transporte do barramento
# ---------------------------------------------------------------------------


@dataclass
class EventoOutbox:
    """Evento lido do Transactional Outbox de um domínio produtor."""

    id: str = ""
    topico: str = ""
    evento_nome: str = ""
    agregado_tipo: str = ""
    agregado_id: str = ""
    payload: dict = field(default_factory=dict)


@dataclass
class ResultadoEnvio:
    """Resultado de um envio HTTP para um webhook."""

    http_status: int | None = None
    ok: bool = False
    erro: str = ""
    duracao_seg: float = 0.0


# ---------------------------------------------------------------------------
# Catálogo de APIs externas
# ---------------------------------------------------------------------------


class RepositorioApiExterna(ABC):
    """Repositório do catálogo de APIs externas."""

    @abstractmethod
    def save(self, api: ApiExterna) -> ApiExterna:
        pass

    @abstractmethod
    def get_by_id(self, api_id: str) -> ApiExterna | None:
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str) -> ApiExterna | None:
        pass

    @abstractmethod
    def exists_by_codigo(self, codigo: str) -> bool:
        pass

    @abstractmethod
    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        estado: str | None = None,
        tipo: str | None = None,
    ) -> tuple[list[ApiExterna], int]:
        pass

    @abstractmethod
    def delete(self, api_id: str) -> bool:
        pass


class RepositorioConector(ABC):
    """Repositório de conectores oficiais de interoperabilidade."""

    @abstractmethod
    def save(self, conector: Conector) -> Conector:
        pass

    @abstractmethod
    def get_by_id(self, conector_id: str) -> Conector | None:
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str) -> Conector | None:
        pass

    @abstractmethod
    def exists_by_codigo(self, codigo: str) -> bool:
        pass

    @abstractmethod
    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        estado: str | None = None,
    ) -> tuple[list[Conector], int]:
        pass

    @abstractmethod
    def delete(self, conector_id: str) -> bool:
        pass


class RepositorioWebhook(ABC):
    """Repositório de webhooks inscritos no barramento."""

    @abstractmethod
    def save(self, webhook: Webhook) -> Webhook:
        pass

    @abstractmethod
    def get_by_id(self, webhook_id: str) -> Webhook | None:
        pass

    @abstractmethod
    def get_by_nome(self, nome: str) -> Webhook | None:
        pass

    @abstractmethod
    def exists_by_nome(self, nome: str) -> bool:
        pass

    @abstractmethod
    def find_ativos(self) -> list[Webhook]:
        pass

    @abstractmethod
    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        estado: str | None = None,
    ) -> tuple[list[Webhook], int]:
        pass

    @abstractmethod
    def delete(self, webhook_id: str) -> bool:
        pass


class RepositorioEntregaWebhook(ABC):
    """Repositório de entregas de mensagens (registro de tentativas/DLQ)."""

    @abstractmethod
    def save(self, entrega: EntregaWebhook) -> EntregaWebhook:
        pass

    @abstractmethod
    def get_by_id(self, entrega_id: str) -> EntregaWebhook | None:
        pass

    @abstractmethod
    def list_pendentes_para_retry(self, lote: int, agora: datetime) -> list[EntregaWebhook]:
        pass

    @abstractmethod
    def list_by_webhook(
        self, webhook_id: str, page: int = 0, page_size: int = 50
    ) -> tuple[list[EntregaWebhook], int]:
        pass

    @abstractmethod
    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        estado: str | None = None,
    ) -> tuple[list[EntregaWebhook], int]:
        pass

    @abstractmethod
    def delete(self, entrega_id: str) -> bool:
        pass


class RepositorioEventoProcessado(ABC):
    """Repositório de eventos consumidos do outbox (inbox do barramento)."""

    @abstractmethod
    def save(self, evento: EventoProcessado) -> EventoProcessado:
        pass

    @abstractmethod
    def get_by_evento_outbox(self, fonte: str, evento_outbox_id: str) -> EventoProcessado | None:
        pass

    @abstractmethod
    def exists(self, fonte: str, evento_outbox_id: str) -> bool:
        pass

    @abstractmethod
    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        fonte: str | None = None,
    ) -> tuple[list[EventoProcessado], int]:
        pass

    @abstractmethod
    def delete(self, evento_id: str) -> bool:
        pass


# ---------------------------------------------------------------------------
# Barramento de eventos
# ---------------------------------------------------------------------------


class FonteOutbox(ABC):
    """Fonte de leitura do Transactional Outbox de um domínio produtor.

    O DOM-INT consome os eventos publicados por outros domínios (GDO,
    Compras) em suas tabelas ``<schema>.eventos_outbox`` e os distribui aos
    inscritos do barramento (webhooks/conectores).
    """

    @abstractmethod
    def ler_pendentes(self, fonte: str, lote: int) -> list[EventoOutbox]:
        pass

    @abstractmethod
    def marcar_publicado(self, fonte: str, evento_outbox_id: str) -> None:
        pass


class TransporteWebhook(ABC):
    """Transporte HTTP de entrega de mensagens a webhooks."""

    @abstractmethod
    def enviar(
        self,
        url: str,
        payload: dict,
        cabecalhos: dict | None = None,
        timeout_seg: int = 30,
    ) -> ResultadoEnvio:
        pass


class RepositorioContratoIntegracao(ABC):
    """Repositório de contratos de integração."""

    @abstractmethod
    def save(self, contrato: ContratoIntegracao) -> ContratoIntegracao:
        pass

    @abstractmethod
    def get_by_id(self, contrato_id: str) -> ContratoIntegracao | None:
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str) -> ContratoIntegracao | None:
        pass

    @abstractmethod
    def exists_by_codigo(self, codigo: str) -> bool:
        pass

    @abstractmethod
    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        estado: str | None = None,
        api_externa_id: str | None = None,
    ) -> tuple[list[ContratoIntegracao], int]:
        pass

    @abstractmethod
    def delete(self, contrato_id: str) -> bool:
        pass
