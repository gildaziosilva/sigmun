"""Repositório SQLAlchemy de webhooks inscritos no barramento (DOM-INT).

Segue o padrão do DOM-SEG: ``flush`` sem ``commit`` (a transação é
controlada pela sessão da requisição) e exclusão lógica por ``is_deleted``.
"""

import logging
from uuid import UUID

from sqlalchemy import func, select

from src.modules.sigmun_int.application.interfaces import RepositorioWebhook
from src.modules.sigmun_int.domain.entities import EstadoInscricao, Webhook
from src.modules.sigmun_int.infrastructure.database.models import WebhookModel

logger = logging.getLogger(__name__)


def _para_entidade(model: WebhookModel) -> Webhook:
    return Webhook(
        id=str(model.id),
        nome=model.nome,
        url_destino=model.url_destino,
        segredo_ref=model.segredo_ref or "",
        topicos=list(model.topicos or []),
        cabecalhos=dict(model.cabecalhos or {}),
        estado=EstadoInscricao(model.estado),
        max_tentativas=model.max_tentativas,
        backoff_base_seg=model.backoff_base_seg,
        criado_em=model.criado_em,
        atualizado_em=model.atualizado_em,
        is_deleted=model.is_deleted,
    )


class SqlAlchemyWebhookRepository(RepositorioWebhook):
    """Repositório de webhooks persistido via SQLAlchemy."""

    def __init__(self, session) -> None:
        self._session = session

    def save(self, webhook: Webhook) -> Webhook:
        model = self._session.get(WebhookModel, UUID(webhook.id))
        if model is None:
            model = WebhookModel(
                id=UUID(webhook.id),
                nome=webhook.nome,
                url_destino=webhook.url_destino,
                segredo_ref=webhook.segredo_ref or None,
                topicos=webhook.topicos,
                cabecalhos=webhook.cabecalhos,
                estado=webhook.estado.value,
                max_tentativas=webhook.max_tentativas,
                backoff_base_seg=webhook.backoff_base_seg,
                is_deleted=webhook.is_deleted,
            )
            self._session.add(model)
        else:
            model.nome = webhook.nome
            model.url_destino = webhook.url_destino
            model.segredo_ref = webhook.segredo_ref or None
            model.topicos = webhook.topicos
            model.cabecalhos = webhook.cabecalhos
            model.estado = webhook.estado.value
            model.max_tentativas = webhook.max_tentativas
            model.backoff_base_seg = webhook.backoff_base_seg
            model.atualizado_em = func.now()
        self._session.flush()
        return webhook

    def get_by_id(self, webhook_id: str) -> Webhook | None:
        model = self._session.get(WebhookModel, UUID(webhook_id))
        if model is None or model.is_deleted:
            return None
        return _para_entidade(model)

    def get_by_nome(self, nome: str) -> Webhook | None:
        stmt = select(WebhookModel).where(
            WebhookModel.nome == nome, WebhookModel.is_deleted.is_(False)
        )
        model = self._session.scalars(stmt).first()
        return _para_entidade(model) if model else None

    def exists_by_nome(self, nome: str) -> bool:
        stmt = (
            select(WebhookModel.id)
            .where(WebhookModel.nome == nome, WebhookModel.is_deleted.is_(False))
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None

    def list_all(
        self, page: int = 0, page_size: int = 50, estado: str | None = None
    ) -> tuple[list[Webhook], int]:
        base = select(WebhookModel).where(WebhookModel.is_deleted.is_(False))
        if estado:
            base = base.where(WebhookModel.estado == estado)
        total = len(self._session.scalars(base).all())
        stmt = base.order_by(WebhookModel.nome).offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_para_entidade(m) for m in models], total

    def find_ativos(self) -> list[Webhook]:
        stmt = select(WebhookModel).where(
            WebhookModel.is_deleted.is_(False),
            WebhookModel.estado == EstadoInscricao.ATIVA.value,
        )
        return [_para_entidade(m) for m in self._session.scalars(stmt).all()]

    def delete(self, webhook_id: str) -> bool:
        model = self._session.get(WebhookModel, UUID(webhook_id))
        if model is None:
            return False
        if not model.is_deleted:
            model.is_deleted = True
            model.atualizado_em = func.now()
        self._session.flush()
        return True
