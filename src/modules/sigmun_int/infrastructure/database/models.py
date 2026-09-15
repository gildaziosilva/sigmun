"""Modelos ORM (SQLAlchemy) da persistência do domínio de Integração e Interoperabilidade.

Mapeiam as tabelas do schema ``integracao``:
  - ``apis_externas``: catálogo de APIs externas.
  - ``contratos_integracao``: contratos de integração.
  - ``conectores``: conectores oficiais (GOV.BR, e-Social, SIAFIC, PNCP).
  - ``webhooks``: inscritos do barramento.
  - ``entregas_webhook``: entregas de mensagens (retry/DLQ).
  - ``eventos_processados``: inbox do barramento (idempotência do outbox).

Segue o padrão do DOM-SEG (exclusão lógica ``is_deleted``, timestamps com
``server_default`` do PostgreSQL e base declarativa própria) usado nas
migrações Alembic do SIGMUN.
"""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import JSON, Boolean, DateTime, Integer, Text, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class IntegracaoBase(DeclarativeBase):
    """Base declarativa dos modelos ORM do domínio DOM-INT."""


class ApiExternaModel(IntegracaoBase):
    """Modelo ORM da tabela ``integracao.apis_externas``."""

    __tablename__ = "apis_externas"
    __table_args__ = {"schema": "integracao"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str] = mapped_column(Text, nullable=True)
    provedor: Mapped[str] = mapped_column(Text, nullable=True)
    url_base: Mapped[str] = mapped_column(Text, nullable=True)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, default="rest")
    autenticacao: Mapped[str] = mapped_column(Text, nullable=False, default="oauth2")
    estado: Mapped[str] = mapped_column(Text, nullable=False, default="rascunho")
    versao: Mapped[str] = mapped_column(Text, nullable=False, default="1.0")
    limite_por_minuto: Mapped[int] = mapped_column(Integer, nullable=False, default=300)
    timeout_seg: Mapped[int] = mapped_column(Integer, nullable=False, default=30)
    criado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    atualizado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<ApiExternaModel id={self.id} codigo={self.codigo}>"


class ContratoIntegracaoModel(IntegracaoBase):
    """Modelo ORM da tabela ``integracao.contratos_integracao``."""

    __tablename__ = "contratos_integracao"
    __table_args__ = {"schema": "integracao"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str] = mapped_column(Text, nullable=True)
    versao_formato: Mapped[str] = mapped_column(Text, nullable=False, default="1.0")
    esquema_ref: Mapped[str] = mapped_column(Text, nullable=True)
    api_externa_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True)
    estado: Mapped[str] = mapped_column(Text, nullable=False, default="rascunho")
    criado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    atualizado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<ContratoIntegracaoModel id={self.id} codigo={self.codigo}>"


class ConectorModel(IntegracaoBase):
    """Modelo ORM da tabela ``integracao.conectores``."""

    __tablename__ = "conectores"
    __table_args__ = {"schema": "integracao"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str] = mapped_column(Text, nullable=True)
    provedor: Mapped[str] = mapped_column(Text, nullable=True)
    url_base: Mapped[str] = mapped_column(Text, nullable=True)
    autenticacao_tipo: Mapped[str] = mapped_column(Text, nullable=False, default="oauth2")
    estado: Mapped[str] = mapped_column(Text, nullable=False, default="sem_configuracao")
    config: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    criado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    atualizado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<ConectorModel id={self.id} codigo={self.codigo}>"


class WebhookModel(IntegracaoBase):
    """Modelo ORM da tabela ``integracao.webhooks``."""

    __tablename__ = "webhooks"
    __table_args__ = {"schema": "integracao"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    url_destino: Mapped[str] = mapped_column(Text, nullable=False)
    segredo_ref: Mapped[str] = mapped_column(Text, nullable=True)
    topicos: Mapped[list] = mapped_column(JSON, nullable=False, default=list)
    cabecalhos: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    estado: Mapped[str] = mapped_column(Text, nullable=False, default="ativa")
    max_tentativas: Mapped[int] = mapped_column(Integer, nullable=False, default=5)
    backoff_base_seg: Mapped[int] = mapped_column(Integer, nullable=False, default=60)
    criado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    atualizado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<WebhookModel id={self.id} nome={self.nome}>"


class EntregaWebhookModel(IntegracaoBase):
    """Modelo ORM da tabela ``integracao.entregas_webhook`` (retry/DLQ)."""

    __tablename__ = "entregas_webhook"
    __table_args__ = {"schema": "integracao"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    webhook_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    url_destino: Mapped[str] = mapped_column(Text, nullable=False)
    cabecalhos: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    topico: Mapped[str] = mapped_column(Text, nullable=False)
    evento_nome: Mapped[str] = mapped_column(Text, nullable=False)
    agregado_tipo: Mapped[str] = mapped_column(Text, nullable=False)
    agregado_id: Mapped[str] = mapped_column(Text, nullable=False)
    payload: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    estado: Mapped[str] = mapped_column(Text, nullable=False, default="pendente")
    tentativas: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    max_tentativas: Mapped[int] = mapped_column(Integer, nullable=False, default=5)
    backoff_base_seg: Mapped[int] = mapped_column(Integer, nullable=False, default=60)
    ultimo_http_status: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ultimo_erro: Mapped[str] = mapped_column(Text, nullable=True)
    proximo_retry: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    criado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    entregue_em: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    atualizado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<EntregaWebhookModel id={self.id} topico={self.topico} estado={self.estado}>"


class EventoProcessadoModel(IntegracaoBase):
    """Modelo ORM da tabela ``integracao.eventos_processados`` (inbox do barramento).

    A restrição única ``(fonte, evento_outbox_id)`` garante a idempotência do
    consumo do Transactional Outbox dos produtores.
    """

    __tablename__ = "eventos_processados"
    __table_args__ = (
        UniqueConstraint("fonte", "evento_outbox_id", name="uq_eventos_processados_fonte_evento"),
        {"schema": "integracao"},
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    fonte: Mapped[str] = mapped_column(Text, nullable=False)
    evento_outbox_id: Mapped[str] = mapped_column(Text, nullable=False)
    topico: Mapped[str] = mapped_column(Text, nullable=False)
    evento_nome: Mapped[str] = mapped_column(Text, nullable=False)
    agregado_tipo: Mapped[str] = mapped_column(Text, nullable=False)
    agregado_id: Mapped[str] = mapped_column(Text, nullable=False)
    payload: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    recebido_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<EventoProcessadoModel id={self.id} fonte={self.fonte}>"


__all__ = [
    "IntegracaoBase",
    "ApiExternaModel",
    "ContratoIntegracaoModel",
    "ConectorModel",
    "WebhookModel",
    "EntregaWebhookModel",
    "EventoProcessadoModel",
]
