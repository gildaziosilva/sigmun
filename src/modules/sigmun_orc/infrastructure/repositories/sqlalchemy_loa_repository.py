"""Repositório SQLAlchemy de LOAs (DOM-ORC)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioLOA
from ...domain.entities.loa import LOA, StatusLOA
from ..database.models import LOAModel


class SQLAlchemyLOARepository(RepositorioLOA):
    """Persistência de LOAs."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, loa: LOA) -> LOA:
        """Insere ou atualiza LOA."""
        ex = self._session.get(LOAModel, uuid.UUID(loa.id))
        if ex is not None:
            ex.status = loa.status.value
            ex.valor_receita_prevista = loa.valor_receita_prevista
            ex.valor_despesa_fixada = loa.valor_despesa_fixada
            ex.data_aprovacao = loa.data_aprovacao
            ex.data_publicacao = loa.data_publicacao
            ex.updated_at = loa.updated_at
            ex.updated_by = loa.updated_by
            ex.is_deleted = loa.is_deleted
        else:
            self._session.add(LOAModel(
                id=uuid.UUID(loa.id), exercicio=loa.exercicio,
                ldo_id=uuid.UUID(loa.ldo_id),
                descricao=loa.descricao, status=loa.status.value,
                valor_receita_prevista=loa.valor_receita_prevista,
                valor_despesa_fixada=loa.valor_despesa_fixada,
                created_at=loa.created_at, created_by=loa.created_by,
                is_deleted=loa.is_deleted))
        self._session.flush()
        return loa

    def get_by_id(self, loa_id: str) -> LOA | None:
        """Busca LOA por id."""
        m = self._session.get(LOAModel, uuid.UUID(loa_id))
        if m is None or m.is_deleted:
            return None
        return self._to_entity(m)

    def get_by_exercicio(self, exercicio: int) -> LOA | None:
        """Busca LOA pelo exercício."""
        m = (self._session.query(LOAModel).filter(
            LOAModel.exercicio == exercicio,
            LOAModel.is_deleted == False).first())  # noqa: E712
        return self._to_entity(m) if m else None

    def _to_entity(self, m: LOAModel) -> LOA:
        return LOA(id=str(m.id), exercicio=int(m.exercicio or 0),
                   ldo_id=str(m.ldo_id) if m.ldo_id else "", descricao=m.descricao or "",
                   status=StatusLOA(m.status or "elaboracao"),
                   valor_receita_prevista=float(m.valor_receita_prevista or 0),
                   valor_despesa_fixada=float(m.valor_despesa_fixada or 0),
                   data_aprovacao=m.data_aprovacao, data_publicacao=m.data_publicacao,
                   created_at=m.created_at, updated_at=m.updated_at,
                   created_by=m.created_by or "", updated_by=m.updated_by or "",
                   is_deleted=bool(m.is_deleted))


__all__ = ["SQLAlchemyLOARepository"]
