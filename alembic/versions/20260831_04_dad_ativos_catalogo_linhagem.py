"""Create data governance (DAD) tables.

Revision ID: 20260831_04
Revises: 20260831_03
Create Date: 2026-08-31

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision = "20260831_04"
down_revision = "20260831_03"
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
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("created_by", postgresql.UUID(as_uuid=True)),
    ]
    if include_updated:
        columns.extend([
            sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.func.now()),
            sa.Column("updated_by", postgresql.UUID(as_uuid=True)),
            sa.Column("deleted_at", sa.TIMESTAMP(timezone=True)),
            sa.Column("deleted_by", postgresql.UUID(as_uuid=True)),
        ])
    return columns


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS dad")

    # Tabela de ativos de dados
    op.create_table(
        "ativos_dados",
        uuid_column(),
        sa.Column("nome", sa.Text(), nullable=False, unique=True),
        sa.Column("descricao", sa.Text()),
        sa.Column("tipo", sa.Text(), nullable=False, default="tabela"),
        sa.Column("status", sa.Text(), nullable=False, default="PENDENTE"),
        sa.Column("qualidade", sa.Text(), nullable=False, default="MEDIO"),
        sa.Column("dono_id", sa.Text()),
        sa.Column("steward_id", sa.Text()),
        sa.Column("schema_origem", sa.Text()),
        sa.Column("tabela_origem", sa.Text()),
        sa.Column("classificacao", sa.Text()),
        sa.Column("tags", sa.Text(), nullable=False, default=""),
        sa.Column("metadata", sa.JSON()),
        *audit_columns(),
        sa.CheckConstraint("tipo IN ('tabela', 'campo', 'relatorio', 'api', 'arquivo')", name="ck_ativos_tipo"),
        sa.CheckConstraint("status IN ('ativo', 'inativo', 'pendente', 'arquivado')", name="ck_ativos_status"),
        sa.CheckConstraint("qualidade IN ('alto', 'medio', 'baixo', 'critico')", name="ck_ativos_qualidade"),
        schema="dad",
    )
    op.create_index("idx_ativos_dados_nome", "ativos_dados", ["nome"], schema="dad")
    op.create_index("idx_ativos_dados_tipo", "ativos_dados", ["tipo"], schema="dad")
    op.create_index("idx_ativos_dados_status", "ativos_dados", ["status"], schema="dad")

    # Tabela de catálogos
    op.create_table(
        "catalogos",
        uuid_column(),
        sa.Column("nome", sa.Text(), nullable=False, unique=True),
        sa.Column("descricao", sa.Text()),
        sa.Column("dominio", sa.Text()),
        sa.Column("ativos_ids", sa.Text(), nullable=False, default=""),
        *audit_columns(),
        schema="dad",
    )
    op.create_index("idx_catalogos_nome", "catalogos", ["nome"], schema="dad")

    # Tabela de linhagens
    op.create_table(
        "linhagens",
        uuid_column(),
        sa.Column("ativo_origem_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("ativo_destino_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("tipo_transformacao", sa.Text()),
        sa.Column("descricao", sa.Text()),
        sa.Column("regras", sa.Text()),
        *audit_columns(),
        sa.ForeignKeyConstraint(["ativo_origem_id"], ["dad.ativos_dados.id"], onupdate="CASCADE", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["ativo_destino_id"], ["dad.ativos_dados.id"], onupdate="CASCADE", ondelete="CASCADE"),
        schema="dad",
    )
    op.create_index("idx_linhagens_origem", "linhagens", ["ativo_origem_id"], schema="dad")
    op.create_index("idx_linhagens_destino", "linhagens", ["ativo_destino_id"], schema="dad")

    # Tabela de políticas
    op.create_table(
        "politicas",
        uuid_column(),
        sa.Column("codigo", sa.Text(), nullable=False, unique=True),
        sa.Column("nome", sa.Text(), nullable=False),
        sa.Column("descricao", sa.Text()),
        sa.Column("tipo", sa.Text()),
        sa.Column("regras", sa.Text(), nullable=False, default=""),
        *audit_columns(),
        schema="dad",
    )
    op.create_index("idx_politicas_codigo", "politicas", ["codigo"], schema="dad")

    # Tabela de qualidade de dados
    op.create_table(
        "qualidade_dados",
        uuid_column(),
        sa.Column("ativo_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("nivel", sa.Text(), nullable=False, default="MEDIO"),
        sa.Column("score", sa.Float(), nullable=False, default=0.0),
        sa.Column("criterios", sa.Text(), nullable=False, default=""),
        sa.Column("observacao", sa.Text()),
        *audit_columns(),
        sa.ForeignKeyConstraint(["ativo_id"], ["dad.ativos_dados.id"], onupdate="CASCADE", ondelete="CASCADE"),
        schema="dad",
    )
    op.create_index("idx_qualidade_dados_ativo_id", "qualidade_dados", ["ativo_id"], schema="dad")

    # Triggers
    for table in ("ativos_dados", "catalogos", "politicas", "qualidade_dados"):
        op.execute(
            f"CREATE TRIGGER trg_{table}_updated_at "
            f"BEFORE UPDATE ON dad.{table} "
            "FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp()"
        )


def downgrade() -> None:
    for table in ("ativos_dados", "catalogos", "politicas", "qualidade_dados"):
        op.execute(f"DROP TRIGGER IF EXISTS trg_{table}_updated_at ON dad.{table}")
    op.drop_table("qualidade_dados", schema="dad")
    op.drop_table("politicas", schema="dad")
    op.drop_table("linhagens", schema="dad")
    op.drop_table("catalogos", schema="dad")
    op.drop_table("ativos_dados", schema="dad")
    op.execute("DROP SCHEMA IF EXISTS dad")
