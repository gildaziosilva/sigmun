"""Implementação SQLAlchemy do repositório de Usuários (DOM-IDN).

Implementa o contrato ``UsuarioRepositoryInterface`` do domínio sobre a tabela
``idn.usuarios`` (migration 20260831_03).

Observações de projeto:
  - O repositório executa ``flush`` (não ``commit``); a transação é
    controlada pela sessão da requisição (ver core get_db).
"""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.modules.sigmun_idn.domain.entities import Usuario, UsuarioStatus
from src.modules.sigmun_idn.application.interfaces import UsuarioRepositoryInterface
from src.modules.sigmun_idn.infrastructure.database.models import UsuarioModel

logger = logging.getLogger(__name__)


def _parse_uuid_list(value: str | None) -> list[str]:
    """Converte string separada por vírgula em lista de UUIDs."""
    if not value:
        return []
    return [v.strip() for v in value.split(",") if v.strip()]


def _format_uuid_list(values: list[str]) -> str:
    """Converte lista de UUIDs em string separada por vírgula."""
    return ",".join(values)


def _to_entity(model: UsuarioModel) -> Usuario:
    """Converte um registro ORM em entidade de domínio."""
    return Usuario(
        id=str(model.id),
        login=model.login,
        email=model.email,
        nome=model.nome,
        status=UsuarioStatus(model.status),
        senha_hash=model.senha_hash,
        unidades_ids=_parse_uuid_list(model.unidades_ids),
        roles_ids=_parse_uuid_list(model.roles_ids),
        created_at=model.created_at,
        updated_at=model.updated_at,
        last_login=model.last_login,
        is_deleted=model.deleted_at is not None,
    )


class SqlAlchemyUsuarioRepository(UsuarioRepositoryInterface):
    """Repositório de usuários persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, usuario_id: str) -> Usuario | None:
        model = self._session.get(UsuarioModel, UUID(usuario_id))
        if model is None or model.deleted_at is not None:
            return None
        return _to_entity(model)

    def get_by_login(self, login: str) -> Usuario | None:
        stmt = select(UsuarioModel).where(
            UsuarioModel.login == login,
            UsuarioModel.deleted_at.is_(None),
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def get_by_email(self, email: str) -> Usuario | None:
        stmt = select(UsuarioModel).where(
            UsuarioModel.email == email,
            UsuarioModel.deleted_at.is_(None),
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        status: str | None = None,
    ) -> tuple[builtins.list[Usuario], int]:
        stmt = select(UsuarioModel).where(UsuarioModel.deleted_at.is_(None))
        count_stmt = select(UsuarioModel).where(UsuarioModel.deleted_at.is_(None))

        if status is not None:
            stmt = stmt.where(UsuarioModel.status == status)
            count_stmt = count_stmt.where(UsuarioModel.status == status)

        # Total count
        total = len(self._session.scalars(count_stmt).all())

        # Pagination
        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def save(self, usuario: Usuario) -> Usuario:
        model = self._session.get(UsuarioModel, UUID(usuario.id))
        if model is None:
            model = UsuarioModel(
                id=UUID(usuario.id),
                login=usuario.login,
                email=usuario.email,
                nome=usuario.nome,
                status=usuario.status.value,
                senha_hash=usuario.senha_hash,
                unidades_ids=_format_uuid_list(usuario.unidades_ids),
                roles_ids=_format_uuid_list(usuario.roles_ids),
                last_login=usuario.last_login,
                created_at=usuario.created_at,
                created_by=None,
                updated_at=usuario.updated_at,
                updated_by=None,
            )
            self._session.add(model)
            logger.info("Usuário inserido: %s", usuario.id)
        else:
            model.login = usuario.login
            model.email = usuario.email
            model.nome = usuario.nome
            model.status = usuario.status.value
            model.senha_hash = usuario.senha_hash
            model.unidades_ids = _format_uuid_list(usuario.unidades_ids)
            model.roles_ids = _format_uuid_list(usuario.roles_ids)
            model.last_login = usuario.last_login
            model.updated_at = usuario.updated_at
            model.deleted_at = None
            logger.info("Usuário atualizado: %s", usuario.id)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def delete(self, usuario_id: str) -> bool:
        """Soft-delete: preserva histórico."""
        from sqlalchemy import func
        model = self._session.get(UsuarioModel, UUID(usuario_id))
        if model is None:
            return False
        if model.deleted_at is None:
            model.deleted_at = func.now()
        self._session.flush()
        logger.info("Usuário marcado como excluído: %s", usuario_id)
        return True

    def exists_by_login(self, login: str) -> bool:
        stmt = select(UsuarioModel.id).where(
            UsuarioModel.login == login,
            UsuarioModel.deleted_at.is_(None),
        ).limit(1)
        return self._session.scalars(stmt).first() is not None

    def exists_by_email(self, email: str) -> bool:
        stmt = select(UsuarioModel.id).where(
            UsuarioModel.email == email,
            UsuarioModel.deleted_at.is_(None),
        ).limit(1)
        return self._session.scalars(stmt).first() is not None


__all__ = ["SqlAlchemyUsuarioRepository"]
