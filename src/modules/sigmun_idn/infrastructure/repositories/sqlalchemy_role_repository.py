"""Implementação SQLAlchemy do repositório de Roles (DOM-IDN)."""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.modules.sigmun_idn.domain.entities import Role, Permissao, PermissaoEscopo
from src.modules.sigmun_idn.application.interfaces import RoleRepositoryInterface
from src.modules.sigmun_idn.infrastructure.database.models import (
    RoleModel,
    RolePermissaoModel,
    PermissaoModel,
)

logger = logging.getLogger(__name__)


def _to_role_entity(model: RoleModel) -> Role:
    """Converte um registro ORM em entidade de domínio."""
    entity = Role(
        id=str(model.id),
        codigo=model.codigo,
        nome=model.nome,
        descricao=model.descricao or "",
        created_at=model.created_at,
        updated_at=model.updated_at,
        is_deleted=model.deleted_at is not None,
    )
    # Load permissoes associadas
    stmt = select(PermissaoModel).where(
        RolePermissaoModel.role_id == model.id,
        PermissaoModel.id == RolePermissaoModel.permissao_id,
        PermissaoModel.deleted_at.is_(None),
    )
    for perm_model in self._session.scalars(stmt).all():
        entity.permissoes.append(Permissao(
            id=str(perm_model.id),
            codigo=perm_model.codigo,
            nome=perm_model.nome,
            descricao=perm_model.descricao or "",
            escopo=PermissaoEscopo(perm_model.escopo),
            modulo=perm_model.modulo,
            created_at=perm_model.created_at,
            is_deleted=perm_model.deleted_at is not None,
        ))
    return entity


class SqlAlchemyRoleRepository(RoleRepositoryInterface):
    """Repositório de roles persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, role_id: str) -> Role | None:
        model = self._session.get(RoleModel, UUID(role_id))
        if model is None or model.deleted_at is not None:
            return None
        return self._to_entity(model)

    def get_by_codigo(self, codigo: str) -> Role | None:
        stmt = select(RoleModel).where(
            RoleModel.codigo == codigo,
            RoleModel.deleted_at.is_(None),
        )
        model = self._session.scalars(stmt).first()
        return self._to_entity(model) if model else None

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
    ) -> tuple[builtins.list[Role], int]:
        stmt = select(RoleModel).where(RoleModel.deleted_at.is_(None))
        total = len(self._session.scalars(stmt).all())
        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [self._to_entity(m) for m in models], total

    def save(self, role: Role) -> Role:
        model = self._session.get(RoleModel, UUID(role.id))
        if model is None:
            model = RoleModel(
                id=UUID(role.id),
                codigo=role.codigo,
                nome=role.nome,
                descricao=role.descricao,
                created_at=role.created_at,
            )
            self._session.add(model)
            self._session.flush()
        else:
            model.codigo = role.codigo
            model.nome = role.nome
            model.descricao = role.descricao
            model.updated_at = role.updated_at
            model.deleted_at = None
        # Sync permissoes
        self._sync_permissoes(role)
        self._session.flush()
        self._session.refresh(model)
        return self._to_entity(model)

    def _sync_permissoes(self, role: Role) -> None:
        """Sincroniza as permissões associadas à role."""
        existentes = self._session.scalars(
            select(RolePermissaoModel).where(RolePermissaoModel.role_id == UUID(role.id))
        ).all()
        existentes_ids = {str(rp.permissao_id) for rp in existentes}
        atuais_ids = {p.id for p in role.permissoes}

        # Adicionar novas
        for perm in role.permissoes:
            if perm.id not in existentes_ids:
                self._session.add(RolePermissaoModel(
                    role_id=UUID(role.id),
                    permissao_id=UUID(perm.id),
                ))

        # Remover antigas
        for rp in existentes:
            if str(rp.permissao_id) not in atuais_ids:
                self._session.delete(rp)

    def delete(self, role_id: str) -> bool:
        """Soft-delete: preserva histórico."""
        from sqlalchemy import func
        model = self._session.get(RoleModel, UUID(role_id))
        if model is None:
            return False
        if model.deleted_at is None:
            model.deleted_at = func.now()
        self._session.flush()
        return True

    def exists_by_codigo(self, codigo: str) -> bool:
        stmt = select(RoleModel.id).where(
            RoleModel.codigo == codigo,
            RoleModel.deleted_at.is_(None),
        ).limit(1)
        return self._session.scalars(stmt).first() is not None

    def _to_entity(self, model: RoleModel) -> Role:
        """Converte um registro ORM em entidade de domínio."""
        entity = Role(
            id=str(model.id),
            codigo=model.codigo,
            nome=model.nome,
            descricao=model.descricao or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            is_deleted=model.deleted_at is not None,
        )
        # Load permissoes associadas
        stmt = (
            select(PermissaoModel)
            .join(RolePermissaoModel, PermissaoModel.id == RolePermissaoModel.permissao_id)
            .where(
                RolePermissaoModel.role_id == model.id,
                PermissaoModel.deleted_at.is_(None),
            )
        )
        for perm_model in self._session.scalars(stmt).all():
            entity.permissoes.append(Permissao(
                id=str(perm_model.id),
                codigo=perm_model.codigo,
                nome=perm_model.nome,
                descricao=perm_model.descricao or "",
                escopo=PermissaoEscopo(perm_model.escopo),
                modulo=perm_model.modulo,
                created_at=perm_model.created_at,
                is_deleted=perm_model.deleted_at is not None,
            ))
        return entity


__all__ = ["SqlAlchemyRoleRepository"]
