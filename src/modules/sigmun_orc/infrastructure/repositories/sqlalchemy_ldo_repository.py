"""Repositório SQLAlchemy de LDOs (DOM-ORC)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioLDO
from ...domain.entities.ldo import LDO, StatusLDO
from ..database.models import LDOModel


class SQLAlchemyLDORepository(RepositorioLDO):
    """Persistência de LDOs."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, ldo: LDO) -> LDO:
        """Insere ou atualiza LDO."""
        ex = self._session.get(LDOModel, uuid.UUID(ldo.id))
        if ex is not None:
            ex.status = ldo.status.value
            ex.meta_fiscal_receita = ldo.meta_fiscal_receita
            ex.meta_fiscal_despesa = ldo.meta_fiscal_despesa
            ex.data_aprovacao = ldo.data_aprovacao
            ex.data_sancao = ldo.data_sancao
            ex.updated_at = ldo.updated_at
            ex.updated_by = ldo.updated_by
            ex.is_deleted = ldo.is_deleted
        else:
            self._session.add(LDOModel(
                id=uuid.UUID(ldo.id), exercicio=ldo.exercicio,
                ppa_id=uuid.UUID(ldo.ppa_id),
                descricao=ldo.descricao, status=ldo.status.value,
                meta_fiscal_receita=ldo.meta_fiscal_receita,
                meta_fiscal_despesa=ldo.meta_fiscal_despesa,
                created_at=ldo.created_at, created_by=ldo.created_by,
                is_deleted=ldo.is_deleted))
        self._session.flush()
        return ldo

    def get_by_id(self, ldo_id: str) -> LDO | None:
        """Busca LDO por id."""
        m = self._session.get(LDOModel, uuid.UUID(ldo_id))
        if m is None or m.is_deleted:
            return None
        return self._to_entity(m)

    def get_by_exercicio(self, exercicio: int) -> LDO | None:
        """Busca LDO pelo exercício."""
        m = (self._session.query(LDOModel).filter(
            LDOModel.exercicio == exercicio,
            LDOModel.is_deleted == False).first())  # noqa: E712
        return self._to_entity(m) if m else None

    def _to_entity(self, m: LDOModel) -> LDO:
        return LDO(id=str(m.id), exercicio=int(m.exercicio or 0),
                   ppa_id=str(m.ppa_id) if m.ppa_id else "", descricao=m.descricao or "",
                   status=StatusLDO(m.status or "elaboracao"),
                   meta_fiscal_receita=float(m.meta_fiscal_receita or 0),
                   meta_fiscal_despesa=float(m.meta_fiscal_despesa or 0),
                   data_aprovacao=m.data_aprovacao, data_sancao=m.data_sancao,
                   created_at=m.created_at, updated_at=m.updated_at,
                   created_by=m.created_by or "", updated_by=m.updated_by or "",
                   is_deleted=bool(m.is_deleted))


__all__ = ["SQLAlchemyLDORepository"]
