"""Create core and compras foundation tables.

Revision ID: 20260820_01
Revises:
Create Date: 2026-08-20

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision = "20260820_01"
down_revision = None
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
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")
    op.execute("CREATE SCHEMA IF NOT EXISTS core")
    op.execute("CREATE SCHEMA IF NOT EXISTS compras")
    op.execute(
        """
        CREATE OR REPLACE FUNCTION core.fn_update_timestamp()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = NOW();
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql
        """
    )

    op.create_table(
        "unidades_administrativas",
        uuid_column(),
        sa.Column("unidade_pai_id", postgresql.UUID(as_uuid=True)),
        sa.Column("codigo_ibge", sa.Text(), unique=True),
        sa.Column("codigo_siafi", sa.Text(), unique=True),
        sa.Column("nome", sa.Text(), nullable=False),
        sa.Column("sigla", sa.Text(), unique=True),
        *audit_columns(),
        sa.CheckConstraint(
            "deleted_at IS NULL OR deleted_at <= NOW()", name="ck_unidades_administrativas_deleted"
        ),
        schema="core",
    )
    op.create_foreign_key(
        "unidades_pai_id_fkey",
        "unidades_administrativas",
        "unidades_administrativas",
        ["unidade_pai_id"],
        ["id"],
        source_schema="core",
        referent_schema="core",
        onupdate="CASCADE",
        ondelete="RESTRICT",
    )

    op.create_table(
        "pessoas",
        uuid_column(),
        sa.Column("tipo", sa.Text(), nullable=False),
        sa.Column("categoria", sa.Text(), nullable=False),
        sa.Column("unidade_id", postgresql.UUID(as_uuid=True)),
        *audit_columns(),
        sa.CheckConstraint("tipo IN ('FISICA', 'JURIDICA')", name="ck_pessoas_tipo"),
        sa.CheckConstraint(
            "categoria IN ('CIDADAO', 'SERVIDOR', 'FORNECEDOR', 'AGENTE_EXTERNO')",
            name="ck_pessoas_categoria",
        ),
        sa.CheckConstraint("deleted_at IS NULL OR deleted_at <= NOW()", name="ck_pessoas_deleted"),
        schema="core",
    )
    op.create_foreign_key(
        "pessoas_unidade_id_fkey",
        "pessoas",
        "unidades_administrativas",
        ["unidade_id"],
        ["id"],
        source_schema="core",
        referent_schema="core",
        onupdate="CASCADE",
        ondelete="RESTRICT",
    )

    op.create_table(
        "pessoas_juridicas",
        uuid_column(),
        sa.Column("pessoa_id", postgresql.UUID(as_uuid=True), nullable=False, unique=True),
        sa.Column("razao_social", sa.Text(), nullable=False),
        sa.Column("nome_fantasia", sa.Text()),
        sa.Column("cnae_principal", sa.Text()),
        sa.Column("capital", sa.Numeric(15, 2)),
        *audit_columns(),
        sa.ForeignKeyConstraint(
            ["pessoa_id"], ["core.pessoas.id"], onupdate="CASCADE", ondelete="RESTRICT"
        ),
        sa.CheckConstraint(
            "deleted_at IS NULL OR deleted_at <= NOW()", name="ck_pessoas_juridicas_deleted"
        ),
        schema="core",
    )

    op.create_table(
        "pessoas_fisicas",
        uuid_column(),
        sa.Column("pessoa_id", postgresql.UUID(as_uuid=True), nullable=False, unique=True),
        sa.Column("data_nascimento", sa.Date()),
        sa.Column("sexo", sa.Text()),
        sa.Column("estado_civil", sa.Text()),
        sa.Column("mae", sa.Text()),
        sa.Column("pai", sa.Text()),
        *audit_columns(),
        sa.ForeignKeyConstraint(
            ["pessoa_id"], ["core.pessoas.id"], onupdate="CASCADE", ondelete="RESTRICT"
        ),
        sa.CheckConstraint(
            "sexo IS NULL OR sexo IN ('M', 'F', 'OUTRO')", name="ck_pessoas_fisicas_sexo"
        ),
        sa.CheckConstraint(
            "deleted_at IS NULL OR deleted_at <= NOW()", name="ck_pessoas_fisicas_deleted"
        ),
        schema="core",
    )

    op.create_table(
        "fornecedores",
        uuid_column(),
        sa.Column("pessoa_juridica_id", postgresql.UUID(as_uuid=True), nullable=False, unique=True),
        sa.Column("situacao_cadastro", sa.Text(), nullable=False),
        sa.Column("macro_categoria", sa.Text()),
        *audit_columns(),
        sa.ForeignKeyConstraint(
            ["pessoa_juridica_id"],
            ["core.pessoas_juridicas.id"],
            onupdate="CASCADE",
            ondelete="RESTRICT",
        ),
        sa.CheckConstraint(
            "situacao_cadastro IN ('ATIVO', 'INATIVO', 'SUSPENSO')",
            name="ck_fornecedores_situacao",
        ),
        sa.CheckConstraint(
            "deleted_at IS NULL OR deleted_at <= NOW()", name="ck_fornecedores_deleted"
        ),
        schema="core",
    )

    op.create_table(
        "processos_documentais",
        uuid_column(),
        sa.Column("unidade_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("numero", sa.Text(), nullable=False),
        sa.Column("ano", sa.Integer(), nullable=False),
        sa.Column("assunto", sa.Text(), nullable=False),
        sa.Column("descricao", sa.Text()),
        *audit_columns(),
        sa.ForeignKeyConstraint(
            ["unidade_id"],
            ["core.unidades_administrativas.id"],
            onupdate="CASCADE",
            ondelete="RESTRICT",
        ),
        sa.UniqueConstraint("numero", "ano", name="uq_processos_documentais_numero_ano"),
        sa.CheckConstraint(
            "deleted_at IS NULL OR deleted_at <= NOW()", name="ck_processos_documentais_deleted"
        ),
        schema="core",
    )

    op.create_table(
        "compras",
        uuid_column(),
        sa.Column("processo_documental_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("fornecedor_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("unidade_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("numero", sa.Text(), nullable=False),
        sa.Column("data", sa.Date(), nullable=False),
        sa.Column("valor_total", sa.Numeric(15, 2)),
        sa.Column("situacao", sa.Text(), nullable=False),
        *audit_columns(),
        sa.ForeignKeyConstraint(
            ["processo_documental_id"],
            ["core.processos_documentais.id"],
            onupdate="CASCADE",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["fornecedor_id"], ["core.fornecedores.id"], onupdate="CASCADE", ondelete="RESTRICT"
        ),
        sa.ForeignKeyConstraint(
            ["unidade_id"],
            ["core.unidades_administrativas.id"],
            onupdate="CASCADE",
            ondelete="RESTRICT",
        ),
        sa.CheckConstraint("deleted_at IS NULL OR deleted_at <= NOW()", name="ck_compras_deleted"),
        schema="compras",
    )

    op.create_table(
        "itens_compras",
        uuid_column(),
        sa.Column("compra_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("descricao", sa.Text(), nullable=False),
        sa.Column("quantidade", sa.Numeric(15, 2), nullable=False),
        sa.Column("valor_unitario", sa.Numeric(15, 2), nullable=False),
        sa.Column("valor_total", sa.Numeric(15, 2), nullable=False),
        *audit_columns(),
        sa.ForeignKeyConstraint(
            ["compra_id"], ["compras.compras.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        sa.CheckConstraint(
            "deleted_at IS NULL OR deleted_at <= NOW()", name="ck_itens_compras_deleted"
        ),
        schema="compras",
    )

    op.create_table(
        "contratos",
        uuid_column(),
        sa.Column("processo_documental_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("fornecedor_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("unidade_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("licitacao_master_id", postgresql.UUID(as_uuid=True)),
        sa.Column("numero", sa.Text(), nullable=False),
        sa.Column("data_inicio", sa.Date(), nullable=False),
        sa.Column("data_fim", sa.Date()),
        sa.Column("valor", sa.Numeric(15, 2)),
        sa.Column("objeto", sa.Text()),
        *audit_columns(),
        sa.ForeignKeyConstraint(
            ["processo_documental_id"],
            ["core.processos_documentais.id"],
            onupdate="CASCADE",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["fornecedor_id"], ["core.fornecedores.id"], onupdate="CASCADE", ondelete="RESTRICT"
        ),
        sa.ForeignKeyConstraint(
            ["unidade_id"],
            ["core.unidades_administrativas.id"],
            onupdate="CASCADE",
            ondelete="RESTRICT",
        ),
        sa.CheckConstraint(
            "deleted_at IS NULL OR deleted_at <= NOW()", name="ck_contratos_deleted"
        ),
        schema="compras",
    )

    for table in (
        "unidades_administrativas",
        "pessoas",
        "pessoas_fisicas",
        "pessoas_juridicas",
        "fornecedores",
        "processos_documentais",
    ):
        op.execute(
            f"CREATE TRIGGER trg_{table}_updated_at "
            f"BEFORE UPDATE ON core.{table} "
            "FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp()"
        )

    for table in ("compras", "itens_compras", "contratos"):
        op.execute(
            f"CREATE TRIGGER trg_{table}_updated_at "
            f"BEFORE UPDATE ON compras.{table} "
            "FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp()"
        )

    op.create_index("idx_pessoas_tipo_categoria", "pessoas", ["tipo", "categoria"], schema="core")
    op.create_index(
        "idx_fornecedores_situacao", "fornecedores", ["situacao_cadastro"], schema="core"
    )
    op.create_index(
        "idx_processos_documentais_unidade_id",
        "processos_documentais",
        ["unidade_id"],
        schema="core",
    )
    op.create_index("idx_compras_fornecedor_id", "compras", ["fornecedor_id"], schema="compras")
    op.create_index("idx_compras_unidade_id", "compras", ["unidade_id"], schema="compras")
    op.create_index("idx_itens_compras_compra_id", "itens_compras", ["compra_id"], schema="compras")
    op.create_index("idx_contratos_fornecedor_id", "contratos", ["fornecedor_id"], schema="compras")


def downgrade() -> None:
    for index_name, table, schema in (
        ("idx_contratos_fornecedor_id", "contratos", "compras"),
        ("idx_itens_compras_compra_id", "itens_compras", "compras"),
        ("idx_compras_unidade_id", "compras", "compras"),
        ("idx_compras_fornecedor_id", "compras", "compras"),
        ("idx_processos_documentais_unidade_id", "processos_documentais", "core"),
        ("idx_fornecedores_situacao", "fornecedores", "core"),
        ("idx_pessoas_tipo_categoria", "pessoas", "core"),
    ):
        op.drop_index(index_name, table_name=table, schema=schema)

    op.drop_table("contratos", schema="compras")
    op.drop_table("itens_compras", schema="compras")
    op.drop_table("compras", schema="compras")
    op.drop_table("processos_documentais", schema="core")
    op.drop_table("fornecedores", schema="core")
    op.drop_table("pessoas_fisicas", schema="core")
    op.drop_table("pessoas_juridicas", schema="core")
    op.drop_constraint("pessoas_unidade_id_fkey", "pessoas", schema="core", type_="foreignkey")
    op.drop_table("pessoas", schema="core")
    op.drop_constraint(
        "unidades_pai_id_fkey", "unidades_administrativas", schema="core", type_="foreignkey"
    )
    op.drop_table("unidades_administrativas", schema="core")
    op.execute("DROP SCHEMA IF EXISTS compras")
    op.execute("DROP FUNCTION IF EXISTS core.fn_update_timestamp()")
    op.execute("DROP SCHEMA IF EXISTS core")
