"""Repositório SQLAlchemy de PPAs (DOM-ORC)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioPPA
from ...domain.entities.ppa import PPA, StatusPPA
from ..database.models import PPAModel


class SQLAlchemyPPARepository(RepositorioPPA):
    """Persistência de PPAs."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, ppa: PPA) -> PPA:
        """Insere ou atualiza PPA."""
        ex = self._session.get(PPAModel, uuid.UUID(ppa.id))
        if ex is not None:
            ex.descricao = ppa.descricao
            ex.status = ppa.status.value
            ex.data_publicacao = ppa.data_publicacao
            ex.data_encerramento = ppa.data_encerramento
            ex.updated_at = ppa.updated_at
            ex.updated_by = ppa.updated_by
            ex.is_deleted = ppa.is_deleted
        else:
            self._session.add(PPAModel(
                id=uuid.UUID(ppa.id), ano_inicial=ppa.ano_inicial,
                ano_final=ppa.ano_final, descricao=ppa.descricao,
                status=ppa.status.value, data_publicacao=ppa.data_publicacao,
                data_encerramento=ppa.data_encerramento, created_at=ppa.created_at,
                updated_at=ppa.updated_at, created_by=ppa.created_by,
                updated_by=ppa.updated_by, is_deleted=ppa.is_deleted))
        self._session.flush()
        return ppa

    def get_by_id(self, ppa_id: str) -> PPA | None:
        """Busca PPA por id."""
        m = self._session.get(PPAModel, uuid.UUID(ppa_id))
        if m is None or m.is_deleted:
            return None
        return self._to_entity(m)

    def get_by_quadrienio(self, ano_inicial: int, ano_final: int) -> PPA | None:
        """Busca PPA pelo quadriênio."""
        m = (self._session.query(PPAModel).filter(
            PPAModel.ano_inicial == ano_inicial, PPAModel.ano_final == ano_final,
            PPAModel.is_deleted == False).first())  # noqa: E712
        return self._to_entity(m) if m else None

    def _to_entity(self, m: PPAModel) -> PPA:
        return PPA(id=str(m.id), ano_inicial=int(m.ano_inicial or 0),
                   ano_final=int(m.ano_final or 0), descricao=m.descricao or "",
                   status=StatusPPA(m.status or "elaboracao"),
                   data_publicacao=m.data_publicacao,
                   data_encerramento=m.data_encerramento, created_at=m.created_at,
                   updated_at=m.updated_at, created_by=m.created_by or "",
                   updated_by=m.updated_by or "", is_deleted=bool(m.is_deleted))


__all__ = ["SQLAlchemyPPARepository"]
