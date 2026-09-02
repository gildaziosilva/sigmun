"""Implementação SQLAlchemy do repositório de Valores de Metadados (DOM-MET)."""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.sigmun_met.application.interfaces import (
    ValorMetadadoRepositoryInterface,
)
from src.modules.sigmun_met.domain.entities import ValorMetadado
from src.modules.sigmun_met.infrastructure.database.models import ValorMetadadoModel

logger = logging.getLogger(__name__)


def _to_entity(model: ValorMetadadoModel) -> ValorMetadado:
    return ValorMetadado(
        id=str(model.id),
        metadado_id=str(model.metadado_id),
        entidade_tipo=model.entidade_tipo,
        entidade_id=str(model.entidade_id),
        valor=model.valor,
        created_at=model.created_at,
        updated_at=model.updated_at,
        is_deleted=model.deleted_at is not None,
    )


class SqlAlchemyValorMetadadoRepository(ValorMetadadoRepositoryInterface):
    """Repositório de valores de metadados persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, valor_id: str) -> ValorMetadado | None:
        model = self._session.get(ValorMetadadoModel, UUID(valor_id))
        if model is None or model.deleted_at is not None:
            return None
        return _to_entity(model)

    def get_by_entidade(
        self, entidade_tipo: str, entidade_id: str
    ) -> builtins.list[ValorMetadado]:
        stmt = select(ValorMetadadoModel).where(
            ValorMetadadoModel.entidade_tipo == entidade_tipo,
            ValorMetadadoModel.entidade_id == UUID(entidade_id),
            ValorMetadadoModel.deleted_at.is_(None),
        )
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models]

    def get_by_metadado_e_entidade(
        self, metadado_id: str, entidade_tipo: str, entidade_id: str
    ) -> ValorMetadado | None:
        stmt = select(ValorMetadadoModel).where(
            ValorMetadadoModel.metadado_id == UUID(metadado_id),
            ValorMetadadoModel.entidade_tipo == entidade_tipo,
            ValorMetadadoModel.entidade_id == UUID(entidade_id),
            ValorMetadadoModel.deleted_at.is_(None),
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        metadado_id: str | None = None,
        entidade_tipo: str | None = None,
    ) -> tuple[builtins.list[ValorMetadado], int]:
        stmt = select(ValorMetadadoModel).where(ValorMetadadoModel.deleted_at.is_(None))
        if metadado_id:
            stmt = stmt.where(ValorMetadadoModel.metadado_id == UUID(metadado_id))
        if entidade_tipo:
            stmt = stmt.where(ValorMetadadoModel.entidade_tipo == entidade_tipo)
        total = len(self._session.scalars(stmt).all())
        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def save(self, valor: ValorMetadado) -> ValorMetadado:
        model = self._session.get(ValorMetadadoModel, UUID(valor.id))
        if model is None:
            model = ValorMetadadoModel(
                id=UUID(valor.id),
                metadado_id=UUID(valor.metadado_id),
                entidade_tipo=valor.entidade_tipo,
                entidade_id=UUID(valor.entidade_id),
                valor=valor.valor,
                created_at=valor.created_at,
            )
            self._session.add(model)
            logger.info("Valor de metadado inserido: %s", valor.id)
        else:
            model.valor = valor.valor
            model.updated_at = valor.updated_at
            logger.info("Valor de metadado atualizado: %s", valor.id)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def delete(self, valor_id: str) -> bool:
        model = self._session.get(ValorMetadadoModel, UUID(valor_id))
        if model is None:
            return False
        if model.deleted_at is None:
            model.deleted_at = func.now()
        self._session.flush()
        return True


__all__ = ["SqlAlchemyValorMetadadoRepository"]
