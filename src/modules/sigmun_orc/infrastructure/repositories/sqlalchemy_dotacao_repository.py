"""Repositório SQLAlchemy de dotações (DOM-ORC)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioDotacao
from ...domain.entities.dotacao import Dotacao, StatusDotacao
from ..database.models import DotacaoModel


class SQLAlchemyDotacaoRepository(RepositorioDotacao):
    """Persistência de dotações orçamentárias."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, dot: Dotacao) -> Dotacao:
        """Insere ou atualiza dotação."""
        ex = self._session.get(DotacaoModel, uuid.UUID(dot.id))
        if ex is not None:
            ex.valor_suplementado = dot.valor_suplementado
            ex.valor_anulado = dot.valor_anulado
            ex.valor_reservado = dot.valor_reservado
            ex.valor_empenhado = dot.valor_empenhado
            ex.status = dot.status.value
            ex.updated_at = dot.updated_at
            ex.updated_by = dot.updated_by
            ex.is_deleted = dot.is_deleted
        else:
            self._session.add(DotacaoModel(
                id=uuid.UUID(dot.id), loa_id=uuid.UUID(dot.loa_id),
                exercicio=dot.exercicio,
                codigo=dot.codigo, unidade_orcamentaria=dot.unidade_orcamentaria,
                natureza_despesa=dot.natureza_despesa,
                fonte_recursos=dot.fonte_recursos, valor_inicial=dot.valor_inicial,
                valor_suplementado=dot.valor_suplementado,
                valor_anulado=dot.valor_anulado, valor_reservado=dot.valor_reservado,
                valor_empenhado=dot.valor_empenhado, status=dot.status.value,
                created_at=dot.created_at, created_by=dot.created_by,
                is_deleted=dot.is_deleted))
        self._session.flush()
        return dot

    def get_by_id(self, dotacao_id: str) -> Dotacao | None:
        """Busca dotação por id."""
        m = self._session.get(DotacaoModel, uuid.UUID(dotacao_id))
        if m is None or m.is_deleted:
            return None
        return self._to_entity(m)

    def get_by_codigo_exercicio(self, codigo: str, exercicio: int) -> Dotacao | None:
        """Busca dotação por código/exercício."""
        m = (self._session.query(DotacaoModel).filter(
            DotacaoModel.codigo == codigo, DotacaoModel.exercicio == exercicio,
            DotacaoModel.is_deleted == False).first())  # noqa: E712
        return self._to_entity(m) if m else None

    def _to_entity(self, m: DotacaoModel) -> Dotacao:
        return Dotacao(id=str(m.id), loa_id=str(m.loa_id) if m.loa_id else "",
                       exercicio=int(m.exercicio or 0), codigo=m.codigo or "",
                       unidade_orcamentaria=m.unidade_orcamentaria or "",
                       natureza_despesa=m.natureza_despesa or "",
                       fonte_recursos=m.fonte_recursos or "",
                       valor_inicial=float(m.valor_inicial or 0),
                       valor_suplementado=float(m.valor_suplementado or 0),
                       valor_anulado=float(m.valor_anulado or 0),
                       valor_reservado=float(m.valor_reservado or 0),
                       valor_empenhado=float(m.valor_empenhado or 0),
                       status=StatusDotacao(m.status or "ativa"),
                       created_at=m.created_at, updated_at=m.updated_at,
                       created_by=m.created_by or "",
                       updated_by=m.updated_by or "",
                       is_deleted=bool(m.is_deleted))


__all__ = ["SQLAlchemyDotacaoRepository"]
