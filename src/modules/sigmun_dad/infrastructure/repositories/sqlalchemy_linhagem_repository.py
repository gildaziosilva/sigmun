"""Implementação SQLAlchemy do repositório de Linhagens (DOM-DAD)."""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.modules.sigmun_dad.application.interfaces import LinhagemRepositoryInterface
from src.modules.sigmun_dad.domain.entities import LinhagemDado
from src.modules.sigmun_dad.infrastructure.database.models import LinhagemDadoModel

logger = logging.getLogger(__name__)


def _to_entity(model: LinhagemDadoModel) -> LinhagemDado:
    return LinhagemDado(
        id=str(model.id),
        ativo_origem_id=str(model.ativo_origem_id),
        ativo_destino_id=str(model.ativo_destino_id),
        tipo_transformacao=model.tipo_transformacao or "",
        descricao=model.descricao or "",
        regras=model.regras or "",
        created_at=model.created_at,
        is_deleted=model.deleted_at is not None,
    )


class SqlAlchemyLinhagemRepository(LinhagemRepositoryInterface):
    """Repositório de linhagens persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, linhagem_id: str) -> LinhagemDado | None:
        model = self._session.get(LinhagemDadoModel, UUID(linhagem_id))
        if model is None or model.deleted_at is not None:
            return None
        return _to_entity(model)

    def get_by_origem(self, ativo_origem_id: str) -> builtins.list[LinhagemDado]:
        stmt = select(LinhagemDadoModel).where(
            LinhagemDadoModel.ativo_origem_id == UUID(ativo_origem_id),
            LinhagemDadoModel.deleted_at.is_(None),
        )
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models]

    def get_by_destino(self, ativo_destino_id: str) -> builtins.list[LinhagemDado]:
        stmt = select(LinhagemDadoModel).where(
            LinhagemDadoModel.ativo_destino_id == UUID(ativo_destino_id),
            LinhagemDadoModel.deleted_at.is_(None),
        )
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models]

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
    ) -> tuple[builtins.list[LinhagemDado], int]:
        stmt = select(LinhagemDadoModel).where(LinhagemDadoModel.deleted_at.is_(None))
        total = len(self._session.scalars(stmt).all())
        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def save(self, linhagem: LinhagemDado) -> LinhagemDado:
        model = self._session.get(LinhagemDadoModel, UUID(linhagem.id))
        if model is None:
            model = LinhagemDadoModel(
                id=UUID(linhagem.id),
                ativo_origem_id=UUID(linhagem.ativo_origem_id),
                ativo_destino_id=UUID(linhagem.ativo_destino_id),
                tipo_transformacao=linhagem.tipo_transformacao,
                descricao=linhagem.descricao,
                regras=linhagem.regras,
                created_at=linhagem.created_at,
            )
            self._session.add(model)
            logger.info("Linhagem inserida: %s", linhagem.id)
        else:
            model.ativo_origem_id = UUID(linhagem.ativo_origem_id)
            model.ativo_destino_id = UUID(linhagem.ativo_destino_id)
            model.tipo_transformacao = linhagem.tipo_transformacao
            model.descricao = linhagem.descricao
            model.regras = linhagem.regras
            logger.info("Linhagem atualizada: %s", linhagem.id)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def delete(self, linhagem_id: str) -> bool:
        from sqlalchemy import func
        model = self._session.get(LinhagemDadoModel, UUID(linhagem_id))
        if model is None:
            return False
        if model.deleted_at is None:
            model.deleted_at = func.now()
        self._session.flush()
        return True

    def exists_linhagem(self, origem_id: str, destino_id: str) -> bool:
        stmt = select(LinhagemDadoModel.id).where(
            LinhagemDadoModel.ativo_origem_id == UUID(origem_id),
            LinhagemDadoModel.ativo_destino_id == UUID(destino_id),
            LinhagemDadoModel.deleted_at.is_(None),
        ).limit(1)
        return self._session.scalars(stmt).first() is not None


__all__ = ["SqlAlchemyLinhagemRepository"]
