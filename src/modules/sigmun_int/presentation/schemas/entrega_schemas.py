"""Schemas Pydantic de entregas de mensagens e eventos processados (DOM-INT)."""

from datetime import datetime

from pydantic import BaseModel, Field


class EntregaResponse(BaseModel):
    """Representação de uma entrega de mensagem a um webhook."""

    id: str
    webhook_id: str
    url_destino: str = ""
    topico: str
    evento_nome: str
    agregado_tipo: str
    agregado_id: str
    payload: dict = {}
    estado: str
    tentativas: int
    max_tentativas: int
    ultimo_http_status: int | None = None
    ultimo_erro: str = ""
    proximo_retry: datetime | None = None
    criado_em: datetime | None = None
    entregue_em: datetime | None = None
    is_deleted: bool = False


class ReenfileirarPayload(BaseModel):
    """Payload para reenfileirar uma entrega da fila de mensagens mortas."""

    motivo: str = Field(default="", description="Motivo do reenfileirado (auditoría)")


class ConsumirOutboxPayload(BaseModel):
    """Payload de consumo do outbox de um dominio productor."""

    fonte: str = Field(default="gdo", description="Dominio productor: gdo o compras")
    lote: int = Field(default=100, ge=1, le=1000, description="Lote máximo de eventos")


class DespacharPayload(BaseModel):
    """Payload de despacho de entregas pendentes a webhooks."""

    lote: int = Field(default=100, ge=1, le=1000, description="Lote máximo de entregas")


class EventoProcessadoResponse(BaseModel):
    """Representação de um evento consumido do outbox (inbox do barramento)."""

    id: str
    fonte: str
    evento_outbox_id: str
    topico: str
    evento_nome: str
    agregado_tipo: str
    agregado_id: str
    payload: dict = {}
    recebido_em: datetime | None = None
    is_deleted: bool = False


class ResumoBarramento(BaseModel):
    """Resumo de uma execução do barramento."""

    processados: int = 0
    sucessos: int = 0
    falhas: int = 0
    fila_morta: int = 0