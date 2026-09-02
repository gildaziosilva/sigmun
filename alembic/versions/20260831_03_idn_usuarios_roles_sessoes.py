"""Create identity and access (IDN) tables.

Revision ID: 20260831_03
Revises: 20260831_02
Create Date: 2026-08-31

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision = "20260831_03"
down_revision = "20260831_02"
branch_labels = None
depends_on = None


def uuid_column() -> sa.Column:
    return sa.Column(
        "id",
        postgresql.UUID(as_uuid=True),
        primary_key=True,
        server_default=sa.text("gen_random_uuid()"),
    )


def audit_columns(include_updated: bool = True) -> list[sa.Column]:
    columns = [
        sa.Column(
            "created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.func.now()
        ),
        sa.Column("created_by", postgresql.UUID(as_uuid=True)),
    ]
    if include_updated:
        columns.extend(
            [
                sa.Column(
                    "updated_at",
                    sa.TIMESTAMP(timezone=True),
                    nullable=False,
                    server_default=sa.func.now(),
                ),
                sa.Column("updated_by", postgresql.UUID(as_uuid=True)),
                sa.Column("deleted_at", sa.TIMESTAMP(timezone=True)),
                sa.Column("deleted_by", postgresql.UUID(as_uuid=True)),
            ]
        )
    return columns


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS idn")

    # Tabela de usuários
    op.create_table(
        "usuarios",
        uuid_column(),
        sa.Column("login", sa.Text(), nullable=False, unique=True),
        sa.Column("email", sa.Text(), nullable=False, unique=True),
        sa.Column("nome", sa.Text(), nullable=False),
        sa.Column("status", sa.Text(), nullable=False, default="PENDENTE"),
        sa.Column("senha_hash", sa.Text(), nullable=False),
        sa.Column("unidades_ids", sa.Text(), nullable=False, default=""),
        sa.Column("roles_ids", sa.Text(), nullable=False, default=""),
        sa.Column("last_login", sa.TIMESTAMP(timezone=True)),
        *audit_columns(),
        sa.CheckConstraint(
            "status IN ('ATIVO', 'INATIVO', 'BLOQUEADO', 'PENDENTE')",
            name="ck_usuarios_status",
        ),
        sa.CheckConstraint("deleted_at IS NULL OR deleted_at <= NOW()", name="ck_usuarios_deleted"),
        schema="idn",
    )
    op.create_index("idx_usuarios_login", "usuarios", ["login"], schema="idn")
    op.create_index("idx_usuarios_email", "usuarios", ["email"], schema="idn")
    op.create_index("idx_usuarios_status", "usuarios", ["status"], schema="idn")

    # Tabela de roles (papéis)
    op.create_table(
        "roles",
        uuid_column(),
        sa.Column("codigo", sa.Text(), nullable=False, unique=True),
        sa.Column("nome", sa.Text(), nullable=False),
        sa.Column("descricao", sa.Text()),
        *audit_columns(),
        sa.CheckConstraint("deleted_at IS NULL OR deleted_at <= NOW()", name="ck_roles_deleted"),
        schema="idn",
    )
    op.create_index("idx_roles_codigo", "roles", ["codigo"], schema="idn")

    # Tabela de permissões
    op.create_table(
        "permissoes",
        uuid_column(),
        sa.Column("codigo", sa.Text(), nullable=False, unique=True),
        sa.Column("nome", sa.Text(), nullable=False),
        sa.Column("descricao", sa.Text()),
        sa.Column("escopo", sa.Text(), nullable=False, default="DOMINIO"),
        sa.Column("modulo", sa.Text(), nullable=False, default=""),
        *audit_columns(),
        sa.CheckConstraint(
            "escopo IN ('GLOBAL', 'DOMINIO', 'UNIDADE', 'PROPRIO')",
            name="ck_permissoes_escopo",
        ),
        sa.CheckConstraint("deleted_at IS NULL OR deleted_at <= NOW()", name="ck_permissoes_deleted"),
        schema="idn",
    )
    op.create_index("idx_permissoes_codigo", "permissoes", ["codigo"], schema="idn")
    op.create_index("idx_permissoes_modulo", "permissoes", ["modulo"], schema="idn")

    # Tabela de relacionamento N:N entre usuários e roles
    op.create_table(
        "usuario_roles",
        uuid_column(),
        sa.Column("usuario_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("role_id", postgresql.UUID(as_uuid=True), nullable=False),
        *audit_columns(include_updated=False),
        sa.ForeignKeyConstraint(
            ["usuario_id"], ["idn.usuarios.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["role_id"], ["idn.roles.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        schema="idn",
    )
    op.create_index("idx_usuario_roles_usuario_id", "usuario_roles", ["usuario_id"], schema="idn")
    op.create_index("idx_usuario_roles_role_id", "usuario_roles", ["role_id"], schema="idn")

    # Tabela de relacionamento N:N entre roles e permissões
    op.create_table(
        "role_permissoes",
        uuid_column(),
        sa.Column("role_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("permissao_id", postgresql.UUID(as_uuid=True), nullable=False),
        *audit_columns(include_updated=False),
        sa.ForeignKeyConstraint(
            ["role_id"], ["idn.roles.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["permissao_id"], ["idn.permissoes.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        schema="idn",
    )
    op.create_index("idx_role_permissoes_role_id", "role_permissoes", ["role_id"], schema="idn")
    op.create_index("idx_role_permissoes_permissao_id", "role_permissoes", ["permissao_id"], schema="idn")

    # Tabela de sessões
    op.create_table(
        "sessoes",
        uuid_column(),
        sa.Column("usuario_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("token", sa.Text(), nullable=False, unique=True),
        sa.Column("ip_origem", sa.Text()),
        sa.Column("user_agent", sa.Text()),
        sa.Column("is_active", sa.Boolean(), nullable=False, default=True),
        sa.Column("expires_at", sa.TIMESTAMP(timezone=True)),
        *audit_columns(),
        sa.ForeignKeyConstraint(
            ["usuario_id"], ["idn.usuarios.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        schema="idn",
    )
    op.create_index("idx_sessoes_token", "sessoes", ["token"], schema="idn")
    op.create_index("idx_sessoes_usuario_id", "sessoes", ["usuario_id"], schema="idn")
    op.create_index("idx_sessoes_is_active", "sessoes", ["is_active"], schema="idn")

    # Tabela de auditoria de login
    op.create_table(
        "auditoria_logins",
        uuid_column(),
        sa.Column("usuario_id", postgresql.UUID(as_uuid=True)),
        sa.Column("login", sa.Text(), nullable=False),
        sa.Column("ip_origem", sa.Text()),
        sa.Column("user_agent", sa.Text()),
        sa.Column("sucesso", sa.Boolean(), nullable=False, default=False),
        sa.Column("motivo_falha", sa.Text()),
        sa.Column(
            "created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.func.now()
        ),
        schema="idn",
    )
    op.create_index("idx_auditoria_logins_usuario_id", "auditoria_logins", ["usuario_id"], schema="idn")
    op.create_index("idx_auditoria_logins_login", "auditoria_logins", ["login"], schema="idn")
    op.create_index("idx_auditoria_logins_created_at", "auditoria_logins", ["created_at"], schema="idn")

    # Triggers de updated_at
    for table in ("usuarios", "roles", "permissoes", "sessoes"):
        op.execute(
            f"CREATE TRIGGER trg_{table}_updated_at "
            f"BEFORE UPDATE ON idn.{table} "
            "FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp()"
        )


def downgrade() -> None:
    for index_name, table, schema in (
        ("idx_auditoria_logins_created_at", "auditoria_logins", "idn"),
        ("idx_auditoria_logins_login", "auditoria_logins", "idn"),
        ("idx_auditoria_logins_usuario_id", "auditoria_logins", "idn"),
        ("idx_sessoes_is_active", "sessoes", "idn"),
        ("idx_sessoes_usuario_id", "sessoes", "idn"),
        ("idx_sessoes_token", "sessoes", "idn"),
        ("idx_role_permissoes_permissao_id", "role_permissoes", "idn"),
        ("idx_role_permissoes_role_id", "role_permissoes", "idn"),
        ("idx_usuario_roles_role_id", "usuario_roles", "idn"),
        ("idx_usuario_roles_usuario_id", "usuario_roles", "idn"),
        ("idx_permissoes_modulo", "permissoes", "idn"),
        ("idx_permissoes_codigo", "permissoes", "idn"),
        ("idx_roles_codigo", "roles", "idn"),
        ("idx_usuarios_status", "usuarios", "idn"),
        ("idx_usuarios_email", "usuarios", "idn"),
        ("idx_usuarios_login", "usuarios", "idn"),
    ):
        op.drop_index(index_name, table_name=table, schema=schema)

    for table in ("sessoes", "roles", "permissoes", "usuarios"):
        op.execute(f"DROP TRIGGER IF EXISTS trg_{table}_updated_at ON idn.{table}")

    op.drop_table("auditoria_logins", schema="idn")
    op.drop_table("sessoes", schema="idn")
    op.drop_table("role_permissoes", schema="idn")
    op.drop_table("usuario_roles", schema="idn")
    op.drop_table("permissoes", schema="idn")
    op.drop_table("roles", schema="idn")
    op.drop_table("usuarios", schema="idn")
    op.execute("DROP SCHEMA IF EXISTS idn")
