"""Repositorio SQLAlchemy do inbox do barramento (eventos processados).

Garante a idempotência do consumo do Transactional Outbox: a existência
de ``(fonte, evento_outbox_id)`` (constraint única) evita reprocesar um
evento já consumido.
"""

import logging
from uuid import UUID

from sqlalchemy import func, select

from src.modules.sigmun_int.application.interfaces import RepositorioEventoProcessado
from src.modules.sigmun_int.domain.entities import EventoProcessado
from src.modules.sigmun_int.infrastructure.database.models import EventoProcessadoModel

logger = logging.getLogger(__name__)


def _to_entity(model: EventoProcessadoModel) -> EventoProcessado:
    return EventoProcessado(
        id=str(model.id),
        fonte=model.fonte,
        evento_outbox_id=model.evento_outbox_id,
        topico=model.topico,
        evento_nome=model.evento_nome,
        agregado_tipo=model.agregado_tipo,
        agregado_id=model.agregado_id,
        payload=model.payload or {},
        recebido_em=model.recebido_em,
        is_deleted=model.is_deleted,
    )


class SqlAlchemyEventoProcessadoRepository(RepositorioEventoProcessado):
    """Repositorio de eventos processados persistido via SQLAlchemy."""

    def __init__(self, session) -> None:
        self._session = session

    def save(self, evento: EventoProcessado) -> EventoProcessado:
        model = EventoProcessadoModel(
            id=UUID(evento.id),
            fonte=evento.fonte,
            evento_outbox_id=evento.evento_outbox_id,
            topico=evento.topico,
            evento_nome=evento.evento_nome,
            agregado_tipo=evento.agregado_tipo,
            agregado_id=evento.agregado_id,
            payload=evento.payload,
            is_deleted=evento.is_deleted,
        )
        self._session.add(model)
        self._session.flush()
        return evento

    def get_by_evento_outbox(self, fonte: str, evento_outbox_id: str) -> EventoProcessado | None:
        stmt = select(EventoProcessadoModel).where(
            EventoProcessadoModel.fonte == fonte,
            EventoProcessadoModel.evento_outbox_id == evento_outbox_id,
            EventoProcessadoModel.is_deleted.is_(False),
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def exists(self, fonte: str, evento_outbox_id: str) -> bool:
        stmt = (
            select(EventoProcessadoModel.id)
            .where(
                EventoProcessadoModel.fonte == fonte,
                EventoProcessadoModel.evento_outbox_id == evento_outbox_id,
                EventoProcessadoModel.is_deleted.is_(False),
            )
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None

    def list_all(
        self, page: int = 0, page_size: int = 50, fonte: str | None = None
    ) -> tuple[list[EventoProcessado], int]:
        base = select(EventoProcessadoModel).where(EventoProcessadoModel.is_deleted.is_(False))
        if fonte:
            base = base.where(EventoProcessadoModel.fonte == fonte)
        total = len(self._session.scalars(base).all())
        stmt = base.order_by(EventoProcessadoModel.recebido_em).offset(page * page_size).limit(page_size)
        return [_to_entity(m) for m in self._session.scalars(stmt).all()], total

    def delete(self, evento_id: str) -> bool:
        model = self._session.get(EventoProcessadoModel, UUID(evento_id))
        if model is None:
            return False
        if not model.is_deleted:
            model.is_deleted = True
        self._session.flush()
        return True