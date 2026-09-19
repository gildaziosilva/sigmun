"""Repositório SQLAlchemy de reservas de saldo (DOM-ORC)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioReserva
from ...domain.entities.reserva import ReservaSaldo, StatusReserva
from ..database.models import ReservaModel


class SQLAlchemyReservaRepository(RepositorioReserva):
    """Persistência de reservas de saldo."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, res: ReservaSaldo) -> ReservaSaldo:
        """Insere ou atualiza reserva."""
        ex = self._session.get(ReservaModel, uuid.UUID(res.id))
        if ex is not None:
            ex.status = res.status.value
            ex.data_conversao = res.data_conversao
            ex.data_cancelamento = res.data_cancelamento
            ex.motivo_cancelamento = res.motivo_cancelamento
            ex.empenho_id = res.empenho_id
            ex.updated_at = res.updated_at
            ex.updated_by = res.updated_by
            ex.is_deleted = res.is_deleted
        else:
            self._session.add(ReservaModel(
                id=uuid.UUID(res.id), dotacao_id=uuid.UUID(res.dotacao_id),
                numero=res.numero,
                valor=res.valor, finalidade=res.finalidade, status=res.status.value,
                data_reserva=res.data_reserva, created_at=res.created_at,
                created_by=res.created_by, is_deleted=res.is_deleted))
        self._session.flush()
        return res

    def get_by_id(self, reserva_id: str) -> ReservaSaldo | None:
        """Busca reserva por id."""
        m = self._session.get(ReservaModel, uuid.UUID(reserva_id))
        if m is None or m.is_deleted:
            return None
        return self._to_entity(m)

    def _to_entity(self, m: ReservaModel) -> ReservaSaldo:
        return ReservaSaldo(id=str(m.id),
                            dotacao_id=str(m.dotacao_id) if m.dotacao_id else "",
                            numero=m.numero or "", valor=float(m.valor or 0),
                            finalidade=m.finalidade or "",
                            status=StatusReserva(m.status or "ativa"),
                            data_reserva=m.data_reserva,
                            data_conversao=m.data_conversao,
                            data_cancelamento=m.data_cancelamento,
                            motivo_cancelamento=m.motivo_cancelamento or "",
                            empenho_id=m.empenho_id or "",
                            created_at=m.created_at, updated_at=m.updated_at,
                            created_by=m.created_by or "",
                            updated_by=m.updated_by or "",
                            is_deleted=bool(m.is_deleted))


__all__ = ["SQLAlchemyReservaRepository"]
