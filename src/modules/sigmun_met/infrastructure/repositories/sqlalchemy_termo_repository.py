"""Implementação SQLAlchemy do repositório de Termos de Taxonomia (DOM-MET)."""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.sigmun_met.application.interfaces import (
    TermoTaxonomiaRepositoryInterface,
)
from src.modules.sigmun_met.domain.entities import TermoTaxonomia
from src.modules.sigmun_met.infrastructure.database.models import TermoTaxonomiaModel

logger = logging.getLogger(__name__)


def _parse_list(value: str | None) -> list[str]:
    if not value:
        return []
    return [v.strip() for v in value.split(",") if v.strip()]


def _format_list(values: list[str]) -> str:
    return ",".join(values)


def _termo_to_entity(model: TermoTaxonomiaModel) -> TermoTaxonomia:
    return TermoTaxonomia(
        id=str(model.id),
        taxonomia_id=str(model.taxonomia_id),
        termo_pai_id=str(model.termo_pai_id) if model.termo_pai_id else "",
        codigo=model.codigo,
        nome=model.nome,
        descricao=model.descricao or "",
        sinonimos=_parse_list(model.sinonimos),
        ordem=model.ordem,
        created_at=model.created_at,
        updated_at=model.updated_at,
        is_deleted=model.deleted_at is not None,
    )


class SqlAlchemyTermoTaxonomiaRepository(TermoTaxonomiaRepositoryInterface):
    """Repositório de termos de taxonomia persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, termo_id: str) -> TermoTaxonomia | None:
        model = self._session.get(TermoTaxonomiaModel, UUID(termo_id))
        if model is None or model.deleted_at is not None:
            return None
        return _termo_to_entity(model)

    def get_by_taxonomia(self, taxonomia_id: str) -> builtins.list[TermoTaxonomia]:
        stmt = select(TermoTaxonomiaModel).where(
            TermoTaxonomiaModel.taxonomia_id == UUID(taxonomia_id),
            TermoTaxonomiaModel.deleted_at.is_(None),
        )
        models = self._session.scalars(stmt).all()
        return [_termo_to_entity(m) for m in models]

    def get_by_pai(self, termo_pai_id: str) -> builtins.list[TermoTaxonomia]:
        stmt = select(TermoTaxonomiaModel).where(
            TermoTaxonomiaModel.termo_pai_id == UUID(termo_pai_id),
            TermoTaxonomiaModel.deleted_at.is_(None),
        )
        models = self._session.scalars(stmt).all()
        return [_termo_to_entity(m) for m in models]

    def list_all(
        self, page: int = 0, page_size: int = 50, taxonomia_id: str | None = None,
    ) -> tuple[builtins.list[TermoTaxonomia], int]:
        stmt = select(TermoTaxonomiaModel).where(TermoTaxonomiaModel.deleted_at.is_(None))
        if taxonomia_id:
            stmt = stmt.where(TermoTaxonomiaModel.taxonomia_id == UUID(taxonomia_id))
        total = len(self._session.scalars(stmt).all())
        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_termo_to_entity(m) for m in models], total

    def save(self, termo: TermoTaxonomia) -> TermoTaxonomia:
        model = self._session.get(TermoTaxonomiaModel, UUID(termo.id))
        if model is None:
            model = TermoTaxonomiaModel(
                id=UUID(termo.id),
                taxonomia_id=UUID(termo.taxonomia_id),
                termo_pai_id=UUID(termo.termo_pai_id) if termo.termo_pai_id else None,
                codigo=termo.codigo,
                nome=termo.nome,
                descricao=termo.descricao,
                sinonimos=_format_list(termo.sinonimos),
                ordem=termo.ordem,
                created_at=termo.created_at,
            )
            self._session.add(model)
            logger.info("Termo inserido: %s", termo.id)
        else:
            model.nome = termo.nome
            model.descricao = termo.descricao
            model.sinonimos = _format_list(termo.sinonimos)
            model.ordem = termo.ordem
            model.updated_at = termo.updated_at
            logger.info("Termo atualizado: %s", termo.id)
        self._session.flush()
        self._session.refresh(model)
        return _termo_to_entity(model)

    def delete(self, termo_id: str) -> bool:
        model = self._session.get(TermoTaxonomiaModel, UUID(termo_id))
        if model is None:
            return False
        if model.deleted_at is None:
            model.deleted_at = func.now()
        self._session.flush()
        return True


__all__ = ["SqlAlchemyTermoTaxonomiaRepository"]
