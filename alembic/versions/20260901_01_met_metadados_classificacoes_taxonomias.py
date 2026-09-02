"""Create metadata governance (MET) tables.

Revision ID: 20260901_01
Revises: 20260831_04
Create Date: 2026-09-01

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision = "20260901_01"
down_revision = "20260831_04"
branch_labels = None
depends_on = None


def uuid_column() -> sa.Column:
    return sa.Column(
        "id",
        postgresql.UUID(as_uuid=True),
        primary_key=True,
        server_default=sa.text("gen_random_uuid()"),
    )


def audit_columns() -> list[sa.Column]:
    return [
        sa.Column(
            "created_at", sa.TIMESTAMP(timezone=True),
            nullable=False, server_default=sa.func.now(),
        ),
        sa.Column("created_by", postgresql.UUID(as_uuid=True)),
        sa.Column(
            "updated_at", sa.TIMESTAMP(timezone=True),
            nullable=False, server_default=sa.func.now(),
        ),
        sa.Column("updated_by", postgresql.UUID(as_uuid=True)),
        sa.Column("deleted_at", sa.TIMESTAMP(timezone=True)),
        sa.Column("deleted_by", postgresql.UUID(as_uuid=True)),
    ]


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS met")

    # Tabela de metadados (definições de campos de metadado)
    op.create_table(
        "metadados",
        uuid_column(),
        sa.Column("codigo", sa.Text(), nullable=False, unique=True),
        sa.Column("nome", sa.Text(), nullable=False),
        sa.Column("descricao", sa.Text()),
        sa.Column("tipo_dado", sa.Text(), nullable=False, default="texto"),
        sa.Column("obrigatorio", sa.Boolean(), nullable=False, default=False),
        sa.Column("multi_valor", sa.Boolean(), nullable=False, default=False),
        sa.Column("aplicavel_a", sa.Text(), nullable=False, default=""),
        sa.Column("valor_padrao", sa.Text()),
        sa.Column("status", sa.Text(), nullable=False, default="ativo"),
        sa.Column("config", sa.JSON()),
        *audit_columns(),
        sa.CheckConstraint(
            "tipo_dado IN ('texto', 'numero', 'data', 'booleano', 'lista', 'json')",
            name="ck_metadados_tipo_dado",
        ),
        sa.CheckConstraint("status IN ('ativo', 'inativo')", name="ck_metadados_status"),
        schema="met",
    )
    op.create_index("idx_metadados_codigo", "metadados", ["codigo"], schema="met")
    op.create_index("idx_metadados_status", "metadados", ["status"], schema="met")
    op.create_index("idx_metadados_tipo_dado", "metadados", ["tipo_dado"], schema="met")

    # Tabela de valores de metadados (valores atribuídos às entidades)
    op.create_table(
        "valores_metadados",
        uuid_column(),
        sa.Column("metadado_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("entidade_tipo", sa.Text(), nullable=False),
        sa.Column("entidade_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("valor", sa.Text(), nullable=False),
        *audit_columns(),
        sa.ForeignKeyConstraint(
            ["metadado_id"], ["met.metadados.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        schema="met",
    )
    op.create_index(
        "idx_valores_metadados_metadado",
        "valores_metadados",
        ["metadado_id"],
        schema="met",
    )
    op.create_index(
        "idx_valores_metadados_entidade",
        "valores_metadados",
        ["entidade_tipo", "entidade_id"],
        schema="met",
    )

    # Tabela de classificações corporativas
    op.create_table(
        "classificacoes",
        uuid_column(),
        sa.Column("codigo", sa.Text(), nullable=False, unique=True),
        sa.Column("nome", sa.Text(), nullable=False),
        sa.Column("descricao", sa.Text()),
        sa.Column("tipo", sa.Text(), nullable=False, default="confidencialidade"),
        sa.Column("nivel", sa.Integer(), nullable=False, default=0),
        sa.Column("cor", sa.Text()),
        *audit_columns(),
        sa.CheckConstraint(
            "tipo IN ('confidencialidade', 'assunto', 'retencao', 'origem')",
            name="ck_classificacoes_tipo",
        ),
        schema="met",
    )
    op.create_index("idx_classificacoes_codigo", "classificacoes", ["codigo"], schema="met")
    op.create_index("idx_classificacoes_tipo", "classificacoes", ["tipo"], schema="met")

    # Tabela de taxonomias
    op.create_table(
        "taxonomias",
        uuid_column(),
        sa.Column("codigo", sa.Text(), nullable=False, unique=True),
        sa.Column("nome", sa.Text(), nullable=False),
        sa.Column("descricao", sa.Text()),
        sa.Column("termos_ids", sa.Text(), nullable=False, default=""),
        *audit_columns(),
        schema="met",
    )
    op.create_index("idx_taxonomias_codigo", "taxonomias", ["codigo"], schema="met")

    # Tabela de termos de taxonomia (hierarquia)
    op.create_table(
        "termos_taxonomias",
        uuid_column(),
        sa.Column("taxonomia_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("termo_pai_id", postgresql.UUID(as_uuid=True)),
        sa.Column("codigo", sa.Text(), nullable=False),
        sa.Column("nome", sa.Text(), nullable=False),
        sa.Column("descricao", sa.Text()),
        sa.Column("sinonimos", sa.Text(), nullable=False, default=""),
        sa.Column("ordem", sa.Integer(), nullable=False, default=0),
        *audit_columns(),
        sa.ForeignKeyConstraint(
            ["taxonomia_id"], ["met.taxonomias.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["termo_pai_id"], ["met.termos_taxonomias.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        schema="met",
    )
    op.create_index("idx_termos_taxonomia", "termos_taxonomias", ["taxonomia_id"], schema="met")
    op.create_index("idx_termos_pai", "termos_taxonomias", ["termo_pai_id"], schema="met")
    op.create_index("idx_termos_codigo", "termos_taxonomias", ["codigo"], schema="met")

    # Triggers
    tabelas = (
        "metadados",
        "valores_metadados",
        "classificacoes",
        "taxonomias",
        "termos_taxonomias",
    )
    for table in tabelas:
        op.execute(
            f"CREATE TRIGGER trg_{table}_updated_at "
            f"BEFORE UPDATE ON met.{table} "
            "FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp()"
        )


def downgrade() -> None:
    tabelas = (
        "metadados",
        "valores_metadados",
        "classificacoes",
        "taxonomias",
        "termos_taxonomias",
    )
    for table in tabelas:
        op.execute(f"DROP TRIGGER IF EXISTS trg_{table}_updated_at ON met.{table}")
    op.drop_table("termos_taxonomias", schema="met")
    op.drop_table("taxonomias", schema="met")
    op.drop_table("classificacoes", schema="met")
    op.drop_table("valores_metadados", schema="met")
    op.drop_table("metadados", schema="met")
    op.execute("DROP SCHEMA IF EXISTS met")
