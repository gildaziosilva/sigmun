"""Implementação SQLAlchemy do repositório de Taxonomias (DOM-MET)."""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.sigmun_met.application.interfaces import TaxonomiaRepositoryInterface
from src.modules.sigmun_met.domain.entities import Taxonomia
from src.modules.sigmun_met.infrastructure.database.models import TaxonomiaModel

logger = logging.getLogger(__name__)


def _parse_list(value: str | None) -> list[str]:
    if not value:
        return []
    return [v.strip() for v in value.split(",") if v.strip()]


def _format_list(values: list[str]) -> str:
    return ",".join(values)


def _taxonomia_to_entity(model: TaxonomiaModel) -> Taxonomia:
    return Taxonomia(
        id=str(model.id),
        codigo=model.codigo,
        nome=model.nome,
        descricao=model.descricao or "",
        termos_ids=_parse_list(model.termos_ids),
        created_at=model.created_at,
        updated_at=model.updated_at,
        is_deleted=model.deleted_at is not None,
    )


class SqlAlchemyTaxonomiaRepository(TaxonomiaRepositoryInterface):
    """Repositório de taxonomias persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, taxonomia_id: str) -> Taxonomia | None:
        model = self._session.get(TaxonomiaModel, UUID(taxonomia_id))
        if model is None or model.deleted_at is not None:
            return None
        return _taxonomia_to_entity(model)

    def get_by_codigo(self, codigo: str) -> Taxonomia | None:
        stmt = select(TaxonomiaModel).where(
            TaxonomiaModel.codigo == codigo,
            TaxonomiaModel.deleted_at.is_(None),
        )
        model = self._session.scalars(stmt).first()
        return _taxonomia_to_entity(model) if model else None

    def list_all(self, page: int = 0, page_size: int = 50) -> tuple[builtins.list[Taxonomia], int]:
        stmt = select(TaxonomiaModel).where(TaxonomiaModel.deleted_at.is_(None))
        total = len(self._session.scalars(stmt).all())
        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_taxonomia_to_entity(m) for m in models], total

    def save(self, taxonomia: Taxonomia) -> Taxonomia:
        model = self._session.get(TaxonomiaModel, UUID(taxonomia.id))
        if model is None:
            model = TaxonomiaModel(
                id=UUID(taxonomia.id),
                codigo=taxonomia.codigo,
                nome=taxonomia.nome,
                descricao=taxonomia.descricao,
                termos_ids=_format_list(taxonomia.termos_ids),
                created_at=taxonomia.created_at,
            )
            self._session.add(model)
            logger.info("Taxonomia inserida: %s", taxonomia.id)
        else:
            model.nome = taxonomia.nome
            model.descricao = taxonomia.descricao
            model.termos_ids = _format_list(taxonomia.termos_ids)
            model.updated_at = taxonomia.updated_at
            logger.info("Taxonomia atualizada: %s", taxonomia.id)
        self._session.flush()
        self._session.refresh(model)
        return _taxonomia_to_entity(model)

    def delete(self, taxonomia_id: str) -> bool:
        model = self._session.get(TaxonomiaModel, UUID(taxonomia_id))
        if model is None:
            return False
        if model.deleted_at is None:
            model.deleted_at = func.now()
        self._session.flush()
        return True

    def exists_by_codigo(self, codigo: str) -> bool:
        stmt = select(TaxonomiaModel.id).where(
            TaxonomiaModel.codigo == codigo,
            TaxonomiaModel.deleted_at.is_(None),
        ).limit(1)
        return self._session.scalars(stmt).first() is not None


__all__ = ["SqlAlchemyTaxonomiaRepository"]
