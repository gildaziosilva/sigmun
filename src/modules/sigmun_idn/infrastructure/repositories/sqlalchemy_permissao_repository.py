"""Implementação SQLAlchemy do repositório de Permissões (DOM-IDN)."""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.modules.sigmun_idn.domain.entities import Permissao, PermissaoEscopo
from src.modules.sigmun_idn.application.interfaces import PermissaoRepositoryInterface
from src.modules.sigmun_idn.infrastructure.database.models import PermissaoModel

logger = logging.getLogger(__name__)


def _to_entity(model: PermissaoModel) -> Permissao:
    """Converte um registro ORM em entidade de domínio."""
    return Permissao(
        id=str(model.id),
        codigo=model.codigo,
        nome=model.nome,
        descricao=model.descricao or "",
        escopo=PermissaoEscopo(model.escopo),
        modulo=model.modulo,
        created_at=model.created_at,
        is_deleted=model.deleted_at is not None,
    )


class SqlAlchemyPermissaoRepository(PermissaoRepositoryInterface):
    """Repositório de permissões persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, permissao_id: str) -> Permissao | None:
        model = self._session.get(PermissaoModel, UUID(permissao_id))
        if model is None or model.deleted_at is not None:
            return None
        return _to_entity(model)

    def get_by_codigo(self, codigo: str) -> Permissao | None:
        stmt = select(PermissaoModel).where(
            PermissaoModel.codigo == codigo,
            PermissaoModel.deleted_at.is_(None),
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        modulo: str | None = None,
    ) -> tuple[builtins.list[Permissao], int]:
        stmt = select(PermissaoModel).where(PermissaoModel.deleted_at.is_(None))
        if modulo is not None:
            stmt = stmt.where(PermissaoModel.modulo == modulo)
        total = len(self._session.scalars(stmt).all())
        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def save(self, permissao: Permissao) -> Permissao:
        model = self._session.get(PermissaoModel, UUID(permissao.id))
        if model is None:
            model = PermissaoModel(
                id=UUID(permissao.id),
                codigo=permissao.codigo,
                nome=permissao.nome,
                descricao=permissao.descricao,
                escopo=permissao.escopo.value,
                modulo=permissao.modulo,
                created_at=permissao.created_at,
            )
            self._session.add(model)
            logger.info("Permissão inserida: %s", permissao.id)
        else:
            model.codigo = permissao.codigo
            model.nome = permissao.nome
            model.descricao = permissao.descricao
            model.escopo = permissao.escopo.value
            model.modulo = permissao.modulo
            model.updated_at = permissao.updated_at
            model.deleted_at = None
            logger.info("Permissão atualizada: %s", permissao.id)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def delete(self, permissao_id: str) -> bool:
        """Soft-delete: preserva histórico."""
        from sqlalchemy import func
        model = self._session.get(PermissaoModel, UUID(permissao_id))
        if model is None:
            return False
        if model.deleted_at is None:
            model.deleted_at = func.now()
        self._session.flush()
        return True

    def exists_by_codigo(self, codigo: str) -> bool:
        stmt = select(PermissaoModel.id).where(
            PermissaoModel.codigo == codigo,
            PermissaoModel.deleted_at.is_(None),
        ).limit(1)
        return self._session.scalars(stmt).first() is not None


__all__ = ["SqlAlchemyPermissaoRepository"]
