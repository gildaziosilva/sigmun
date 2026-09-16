"""Repositório SQLAlchemy de entregas de mensagens a webhooks (retry/DLQ).

``list_pendentes_para_retry`` seleciona as entregas ``pendente`` já
habilitadas (``proximo_retry`` nula ou vencida) para que o despachador
aplique o backoff exponencial e mova para a fila de mensagens mortas ao
esgotar as tentativas.
"""

import logging
from datetime import datetime
from uuid import UUID

from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from src.modules.sigmun_int.application.interfaces import RepositorioEntregaWebhook
from src.modules.sigmun_int.domain.entities import EntregaWebhook, EstadoEntrega
from src.modules.sigmun_int.infrastructure.database.models import EntregaWebhookModel

logger = logging.getLogger(__name__)


def _to_entity(model: EntregaWebhookModel) -> EntregaWebhook:
    return EntregaWebhook(
        id=str(model.id),
        webhook_id=str(model.webhook_id),
        url_destino=model.url_destino,
        cabecalhos=dict(model.cabecalhos or {}),
        topico=model.topico,
        evento_nome=model.evento_nome,
        agregado_tipo=model.agregado_tipo,
        agregado_id=model.agregado_id,
        payload=model.payload or {},
        estado=EstadoEntrega(model.estado),
        tentativas=model.tentativas,
        max_tentativas=model.max_tentativas,
        backoff_base_seg=model.backoff_base_seg,
        ultimo_http_status=model.ultimo_http_status,
        ultimo_erro=model.ultimo_erro or "",
        proximo_retry=model.proximo_retry,
        criado_em=model.criado_em,
        entregue_em=model.entregue_em,
        atualizado_em=model.atualizado_em,
        is_deleted=model.is_deleted,
    )


class SqlAlchemyEntregaWebhookRepository(RepositorioEntregaWebhook):
    """Repositório de entregas de webhooks persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, entrega: EntregaWebhook) -> EntregaWebhook:
        model = self._session.get(EntregaWebhookModel, UUID(entrega.id))
        if model is None:
            model = EntregaWebhookModel(
                id=UUID(entrega.id),
                webhook_id=UUID(entrega.webhook_id),
                url_destino=entrega.url_destino,
                cabecalhos=entrega.cabecalhos,
                topico=entrega.topico,
                evento_nome=entrega.evento_nome,
                agregado_tipo=entrega.agregado_tipo,
                agregado_id=entrega.agregado_id,
                payload=entrega.payload,
                estado=entrega.estado.value,
                tentativas=entrega.tentativas,
                max_tentativas=entrega.max_tentativas,
                backoff_base_seg=entrega.backoff_base_seg,
                ultimo_http_status=entrega.ultimo_http_status,
                ultimo_erro=entrega.ultimo_erro or None,
                proximo_retry=entrega.proximo_retry,
                entregue_em=entrega.entregue_em,
                is_deleted=entrega.is_deleted,
            )
            self._session.add(model)
        else:
            self._atualizar_modelo(model, entrega)
        self._session.flush()
        return entrega

    @staticmethod
    def _atualizar_modelo(model: EntregaWebhookModel, entrega: EntregaWebhook) -> None:
        model.webhook_id = UUID(entrega.webhook_id)
        model.url_destino = entrega.url_destino
        model.cabecalhos = entrega.cabecalhos
        model.topico = entrega.topico
        model.evento_nome = entrega.evento_nome
        model.agregado_tipo = entrega.agregado_tipo
        model.agregado_id = entrega.agregado_id
        model.payload = entrega.payload
        model.estado = entrega.estado.value
        model.tentativas = entrega.tentativas
        model.max_tentativas = entrega.max_tentativas
        model.backoff_base_seg = entrega.backoff_base_seg
        model.ultimo_http_status = entrega.ultimo_http_status
        model.ultimo_erro = entrega.ultimo_erro or ""
        model.proximo_retry = entrega.proximo_retry
        model.entregue_em = entrega.entregue_em
        model.atualizado_em = func.now()

    def get_by_id(self, entrega_id: str) -> EntregaWebhook | None:
        model = self._session.get(EntregaWebhookModel, UUID(entrega_id))
        if model is None or model.is_deleted:
            return None
        return _to_entity(model)

    def list_pendentes_para_retry(self, lote: int, agora: datetime) -> list[EntregaWebhook]:
        stmt = (
            select(EntregaWebhookModel)
            .where(
                EntregaWebhookModel.is_deleted.is_(False),
                EntregaWebhookModel.estado == EstadoEntrega.PENDENTE.value,
                or_(
                    EntregaWebhookModel.proximo_retry.is_(None),
                    EntregaWebhookModel.proximo_retry <= agora,
                ),
            )
            .order_by(EntregaWebhookModel.criado_em)
            .limit(lote)
        )
        return [_to_entity(m) for m in self._session.scalars(stmt).all()]

    def list_by_webhook(
        self, webhook_id: str, page: int = 0, page_size: int = 50
    ) -> tuple[list[EntregaWebhook], int]:
        base = select(EntregaWebhookModel).where(
            EntregaWebhookModel.is_deleted.is_(False),
            EntregaWebhookModel.webhook_id == UUID(webhook_id),
        )
        total = len(self._session.scalars(base).all())
        stmt = (
            base.order_by(EntregaWebhookModel.criado_em).offset(page * page_size).limit(page_size)
        )
        return [_to_entity(m) for m in self._session.scalars(stmt).all()], total

    def list_all(
        self, page: int = 0, page_size: int = 50, estado: str | None = None
    ) -> tuple[list[EntregaWebhook], int]:
        base = select(EntregaWebhookModel).where(EntregaWebhookModel.is_deleted.is_(False))
        if estado:
            base = base.where(EntregaWebhookModel.estado == estado)
        total = len(self._session.scalars(base).all())
        stmt = (
            base.order_by(EntregaWebhookModel.criado_em).offset(page * page_size).limit(page_size)
        )
        return [_to_entity(m) for m in self._session.scalars(stmt).all()], total

    def delete(self, entrega_id: str) -> bool:
        model = self._session.get(EntregaWebhookModel, UUID(entrega_id))
        if model is None:
            return False
        if not model.is_deleted:
            model.is_deleted = True
            model.atualizado_em = func.now()
        self._session.flush()
        return True
