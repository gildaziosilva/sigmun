"""Schemas Pydantic de webhooks inscritos (DOM-INT)."""

from datetime import datetime

from pydantic import BaseModel, Field


class WebhookPayload(BaseModel):
    """Payload de registro/atualização de um webhook."""

    nome: str = Field(..., min_length=3, description="Nome único do webhook")
    url_destino: str = Field(..., description="URL destino (http/https) que recebe os eventos")
    segredo_ref: str = Field(
        default="", description="Referência ao segredo de assinatura (nunca o valor)"
    )
    topicos: list[str] = Field(default_factory=list, description="Tópicos inscritos (o ['*'])")
    cabecalhos: dict = Field(default_factory=dict, description="Cabeceras HTTP adicionales")
    max_tentativas: int = Field(default=5, ge=1, le=100, description="Máximo de tentativas")
    backoff_base_seg: int = Field(default=60, ge=0, description="Backoff base em segundos")


class WebhookEstadoPayload(BaseModel):
    """Payload de ativación/desativación de um webhook."""

    estado: str = Field(..., description="ativo o desativada")


class WebhookResponse(BaseModel):
    """Resposta de um webhook."""

    id: str
    nome: str
    url_destino: str
    segredo_ref: str = ""
    topicos: list[str] = []
    cabecalhos: dict = {}
    estado: str
    max_tentativas: int
    backoff_base_seg: int
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None
    is_deleted: bool = False
