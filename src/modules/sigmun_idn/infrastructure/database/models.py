"""Modelos ORM (SQLAlchemy) da persistência do domínio Identidade e Acesso.

Mapeiam as tabelas criadas pela migração 20260831_03 (alembic).
A criação de schema é responsabilidade exclusiva das migrações; estes
modelos servem para leitura e escrita.
"""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class IdnBase(DeclarativeBase):
    """Base declarativa dos modelos ORM do domínio Identidade e Acesso."""


class UsuarioModel(IdnBase):
    """Modelo ORM da tabela ``idn.usuarios``."""

    __tablename__ = "usuarios"
    __table_args__ = {"schema": "idn"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    login: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    email: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(Text, nullable=False, default="PENDENTE")
    senha_hash: Mapped[str] = mapped_column(Text, nullable=False)
    unidades_ids: Mapped[str] = mapped_column(Text, nullable=False, default="")
    roles_ids: Mapped[str] = mapped_column(Text, nullable=False, default="")
    last_login: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    # Colunas de auditoria
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))

    def __repr__(self) -> str:  # pragma: no cover
        return f"<UsuarioModel id={self.id} login={self.login}>"


class RoleModel(IdnBase):
    """Modelo ORM da tabela ``idn.roles``."""

    __tablename__ = "roles"
    __table_args__ = {"schema": "idn"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)

    # Colunas de auditoria
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))

    def __repr__(self) -> str:  # pragma: no cover
        return f"<RoleModel id={self.id} codigo={self.codigo}>"


class PermissaoModel(IdnBase):
    """Modelo ORM da tabela ``idn.permissoes``."""

    __tablename__ = "permissoes"
    __table_args__ = {"schema": "idn"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    escopo: Mapped[str] = mapped_column(Text, nullable=False, default="DOMINIO")
    modulo: Mapped[str] = mapped_column(Text, nullable=False, default="")

    # Colunas de auditoria
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))

    def __repr__(self) -> str:  # pragma: no cover
        return f"<PermissaoModel id={self.id} codigo={self.codigo}>"


class UsuarioRoleModel(IdnBase):
    """Modelo ORM da tabela ``idn.usuario_roles`` (relação N:N)."""

    __tablename__ = "usuario_roles"
    __table_args__ = {"schema": "idn"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    usuario_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    role_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)

    # Colunas de auditoria
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))

    def __repr__(self) -> str:  # pragma: no cover
        return f"<UsuarioRoleModel usuario_id={self.usuario_id} role_id={self.role_id}>"


class RolePermissaoModel(IdnBase):
    """Modelo ORM da tabela ``idn.role_permissoes`` (relação N:N)."""

    __tablename__ = "role_permissoes"
    __table_args__ = {"schema": "idn"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    role_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    permissao_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)

    # Colunas de auditoria
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))

    def __repr__(self) -> str:  # pragma: no cover
        return f"<RolePermissaoModel role_id={self.role_id} permissao_id={self.permissao_id}>"


class SessaoModel(IdnBase):
    """Modelo ORM da tabela ``idn.sessoes``."""

    __tablename__ = "sessoes"
    __table_args__ = {"schema": "idn"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    usuario_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    token: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    ip_origem: Mapped[str | None] = mapped_column(Text)
    user_agent: Mapped[str | None] = mapped_column(Text)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    # Colunas de auditoria
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    def __repr__(self) -> str:  # pragma: no cover
        return f"<SessaoModel id={self.id} usuario_id={self.usuario_id}>"


class AuditoriaLoginModel(IdnBase):
    """Modelo ORM da tabela ``idn.auditoria_logins``."""

    __tablename__ = "auditoria_logins"
    __table_args__ = {"schema": "idn"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    usuario_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    login: Mapped[str] = mapped_column(Text, nullable=False)
    ip_origem: Mapped[str | None] = mapped_column(Text)
    user_agent: Mapped[str | None] = mapped_column(Text)
    sucesso: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    motivo_falha: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    def __repr__(self) -> str:  # pragma: no cover
        return f"<AuditoriaLoginModel id={self.id} login={self.login} sucesso={self.sucesso}>"


__all__ = [
    "IdnBase",
    "UsuarioModel",
    "RoleModel",
    "PermissaoModel",
    "UsuarioRoleModel",
    "RolePermissaoModel",
    "SessaoModel",
    "AuditoriaLoginModel",
]
