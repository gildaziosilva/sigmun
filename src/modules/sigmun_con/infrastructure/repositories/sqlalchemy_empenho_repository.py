"""Repositório SQLAlchemy de empenhos (DOM-CON)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioEmpenho
from ...domain.entities.empenho import Empenho, StatusEmpenho, TipoEmpenho
from ..database.models import EmpenhoModel


class SQLAlchemyEmpenhoRepository(RepositorioEmpenho):
    """Persistência de empenhos."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, emp: Empenho) -> Empenho:
        """Insere ou atualiza empenho."""
        ex = self._session.get(EmpenhoModel, uuid.UUID(emp.id))
        if ex is not None:
            ex.valor_anulado = emp.valor_anulado
            ex.valor_liquidado = emp.valor_liquidado
            ex.valor_pago = emp.valor_pago
            ex.status = emp.status.value
            ex.motivo_anulacao = emp.motivo_anulacao
            ex.updated_at = emp.updated_at
            ex.updated_by = emp.updated_by
            ex.is_deleted = emp.is_deleted
        else:
            self._session.add(EmpenhoModel(
                id=uuid.UUID(emp.id), exercicio=emp.exercicio, numero=emp.numero,
                dotacao_id=emp.dotacao_id, reserva_id=emp.reserva_id,
                favorecido_nome=emp.favorecido_nome, tipo=emp.tipo.value,
                descricao=emp.descricao, valor_empenhado=emp.valor_empenhado,
                valor_anulado=emp.valor_anulado, valor_liquidado=emp.valor_liquidado,
                valor_pago=emp.valor_pago, status=emp.status.value,
                data_emissao=emp.data_emissao, created_at=emp.created_at,
                created_by=emp.created_by, is_deleted=emp.is_deleted))
        self._session.flush()
        return emp

    def get_by_id(self, empenho_id: str) -> Empenho | None:
        """Busca empenho por id."""
        m = self._session.get(EmpenhoModel, uuid.UUID(empenho_id))
        if m is None or m.is_deleted:
            return None
        return self._to_entity(m)

    def get_by_numero_exercicio(self, numero: str, exercicio: int) -> Empenho | None:
        """Busca empenho por número/exercício."""
        m = (self._session.query(EmpenhoModel).filter(
            EmpenhoModel.numero == numero, EmpenhoModel.exercicio == exercicio,
            EmpenhoModel.is_deleted == False).first())  # noqa: E712
        return self._to_entity(m) if m else None

    def _to_entity(self, m: EmpenhoModel) -> Empenho:
        return Empenho(id=str(m.id), exercicio=int(m.exercicio or 0),
                       numero=m.numero or "", dotacao_id=m.dotacao_id or "",
                       reserva_id=m.reserva_id or "",
                       favorecido_nome=m.favorecido_nome or "",
                       tipo=TipoEmpenho(m.tipo or "ordinario"),
                       descricao=m.descricao or "",
                       valor_empenhado=float(m.valor_empenhado or 0),
                       valor_anulado=float(m.valor_anulado or 0),
                       valor_liquidado=float(m.valor_liquidado or 0),
                       valor_pago=float(m.valor_pago or 0),
                       status=StatusEmpenho(m.status or "emitido"),
                       data_emissao=m.data_emissao,
                       motivo_anulacao=m.motivo_anulacao or "",
                       created_at=m.created_at, updated_at=m.updated_at,
                       created_by=m.created_by or "",
                       updated_by=m.updated_by or "",
                       is_deleted=bool(m.is_deleted))


__all__ = ["SQLAlchemyEmpenhoRepository"]
