"""Implementação SQLAlchemy do repositório de Catálogos (DOM-DAD)."""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.modules.sigmun_dad.application.interfaces import CatalogoRepositoryInterface
from src.modules.sigmun_dad.domain.entities import Catalogo
from src.modules.sigmun_dad.infrastructure.database.models import CatalogoModel

logger = logging.getLogger(__name__)


def _parse_list(value: str | None) -> list[str]:
    if not value:
        return []
    return [v.strip() for v in value.split(",") if v.strip()]


def _format_list(values: list[str]) -> str:
    return ",".join(values)


def _to_entity(model: CatalogoModel) -> Catalogo:
    return Catalogo(
        id=str(model.id),
        nome=model.nome,
        descricao=model.descricao or "",
        dominio=model.dominio or "",
        ativos_ids=_parse_list(model.ativos_ids),
        created_at=model.created_at,
        updated_at=model.updated_at,
        is_deleted=model.deleted_at is not None,
    )


class SqlAlchemyCatalogoRepository(CatalogoRepositoryInterface):
    """Repositório de catálogos persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, catalogo_id: str) -> Catalogo | None:
        model = self._session.get(CatalogoModel, UUID(catalogo_id))
        if model is None or model.deleted_at is not None:
            return None
        return _to_entity(model)

    def get_by_nome(self, nome: str) -> Catalogo | None:
        stmt = select(CatalogoModel).where(
            CatalogoModel.nome == nome,
            CatalogoModel.deleted_at.is_(None),
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
    ) -> tuple[builtins.list[Catalogo], int]:
        stmt = select(CatalogoModel).where(CatalogoModel.deleted_at.is_(None))
        total = len(self._session.scalars(stmt).all())
        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def save(self, catalogo: Catalogo) -> Catalogo:
        model = self._session.get(CatalogoModel, UUID(catalogo.id))
        if model is None:
            model = CatalogoModel(
                id=UUID(catalogo.id),
                nome=catalogo.nome,
                descricao=catalogo.descricao,
                dominio=catalogo.dominio,
                ativos_ids=_format_list(catalogo.ativos_ids),
                created_at=catalogo.created_at,
            )
            self._session.add(model)
            logger.info("Catálogo inserido: %s", catalogo.id)
        else:
            model.nome = catalogo.nome
            model.descricao = catalogo.descricao
            model.dominio = catalogo.dominio
            model.ativos_ids = _format_list(catalogo.ativos_ids)
            model.updated_at = catalogo.updated_at
            logger.info("Catálogo atualizado: %s", catalogo.id)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def delete(self, catalogo_id: str) -> bool:
        from sqlalchemy import func
        model = self._session.get(CatalogoModel, UUID(catalogo_id))
        if model is None:
            return False
        if model.deleted_at is None:
            model.deleted_at = func.now()
        self._session.flush()
        return True

    def exists_by_nome(self, nome: str) -> bool:
        stmt = select(CatalogoModel.id).where(
            CatalogoModel.nome == nome,
            CatalogoModel.deleted_at.is_(None),
        ).limit(1)
        return self._session.scalars(stmt).first() is not None


__all__ = ["SqlAlchemyCatalogoRepository"]
