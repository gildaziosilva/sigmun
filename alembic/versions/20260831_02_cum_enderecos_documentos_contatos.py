"""Cria as tabelas mestras de enderecos, documentos e contatos (DOM-CUM).

Onda 2 – Domínios Mestres e Transversais, slice 1: Cadastro Único
Municipal (DOM-CUM). Implementa o DDL do Modelo-Fisico.md §4.1
(``core.enderecos``, ``core.documentos``, ``core.contatos``), ausente da
migration fundacional 20260820_01.

Complemento documentado (desvio do Modelo-Físico): adiciona a coluna
``nome`` a ``core.pessoas_fisicas`` — sem ela o cadastro de pessoa física
não possui identificação mínima (a razão social da pessoa jurídica já
existe). O Modelo-Físico/Modelo-Logico serão atualizados na próxima
revisão dos artefatos DOM-CUM.

Revision ID: 20260831_02
Revises: 20260831_01
Create Date: 2026-08-30
"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision = "20260831_02"
down_revision = "20260831_01"
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
            "created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.func.now()
        ),
        sa.Column("created_by", postgresql.UUID(as_uuid=True)),
        sa.Column(
            "updated_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.func.now()
        ),
        sa.Column("updated_by", postgresql.UUID(as_uuid=True)),
        sa.Column("deleted_at", sa.TIMESTAMP(timezone=True)),
        sa.Column("deleted_by", postgresql.UUID(as_uuid=True)),
    ]


_NOVAS_TABELAS = ("enderecos", "documentos", "contatos")


def upgrade() -> None:
    # -- Coluna ``nome`` em pessoas_fisicas (identificação mínima) ----------
    op.add_column(
        "pessoas_fisicas",
        sa.Column("nome", sa.Text(), nullable=False, server_default=""),
        schema="core",
    )

    # -- core.enderecos (histórico de vigência) ------------------------------
    op.create_table(
        "enderecos",
        uuid_column(),
        sa.Column("pessoa_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("tipo", sa.Text(), nullable=False),
        sa.Column("logradouro", sa.Text(), nullable=False),
        sa.Column("numero", sa.Text(), nullable=False),
        sa.Column("complemento", sa.Text()),
        sa.Column("bairro", sa.Text()),
        sa.Column("cep", sa.Text()),
        sa.Column("cidade", sa.Text()),
        sa.Column("estado", sa.Text()),
        sa.Column("pais", sa.Text()),
        sa.Column("principal", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column(
            "vigencia_inicio",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column("vigencia_fim", sa.TIMESTAMP(timezone=True)),
        sa.Column("motivo_alteracao", sa.Text()),
        *audit_columns(),
        sa.ForeignKeyConstraint(
            ["pessoa_id"], ["core.pessoas.id"], onupdate="CASCADE", ondelete="RESTRICT"
        ),
        sa.CheckConstraint(
            "deleted_at IS NULL OR deleted_at <= NOW()", name="ck_enderecos_deleted"
        ),
        schema="core",
    )
    op.execute(
        "COMMENT ON COLUMN core.enderecos.vigencia_fim IS 'NULL = endereço vigente (histórico).'"
    )

    # -- core.documentos ------------------------------------------------------
    op.create_table(
        "documentos",
        uuid_column(),
        sa.Column("pessoa_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("tipo", sa.Text(), nullable=False),
        sa.Column("numero", sa.Text(), nullable=False),
        sa.Column("orgao_emissor", sa.Text()),
        sa.Column("data_emissao", sa.Date()),
        sa.Column("data_validade", sa.Date()),
        sa.Column("principal", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        *audit_columns(),
        sa.ForeignKeyConstraint(
            ["pessoa_id"], ["core.pessoas.id"], onupdate="CASCADE", ondelete="RESTRICT"
        ),
        sa.CheckConstraint(
            "deleted_at IS NULL OR deleted_at <= NOW()", name="ck_documentos_deleted"
        ),
        schema="core",
    )
    op.execute("COMMENT ON COLUMN core.documentos.numero IS 'LGPD: criptografado (AES-256).'")

    op.execute("UPDATE core.pessoas_fisicas SET nome = '' WHERE nome IS NULL")
    op.alter_column(
        "pessoas_fisicas",
        "nome",
        existing_type=sa.Text(),
        server_default=None,
        schema="core",
    )

    # -- core.contatos ---------------------------------------------------------
    op.create_table(
        "contatos",
        uuid_column(),
        sa.Column("pessoa_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("tipo", sa.Text(), nullable=False),
        sa.Column("valor", sa.Text(), nullable=False),
        sa.Column("principal", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        *audit_columns(),
        sa.ForeignKeyConstraint(
            ["pessoa_id"], ["core.pessoas.id"], onupdate="CASCADE", ondelete="RESTRICT"
        ),
        sa.CheckConstraint("tipo IN ('TEL', 'EMAIL', 'REDES', 'WHATSAPP')", name="ck_contatos_tipo"),
        sa.CheckConstraint("deleted_at IS NULL OR deleted_at <= NOW()", name="ck_contatos_deleted"),
        schema="core",
    )

    # -- Triggers de updated_at (padrão da migration fundacional) ------------
    for table in _NOVAS_TABELAS:
        op.execute(
            f"CREATE TRIGGER trg_{table}_updated_at "
            f"BEFORE UPDATE ON core.{table} "
            "FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp()"
        )

    # -- Índices ---------------------------------------------------------------
    op.create_index("idx_enderecos_pessoa_id", "enderecos", ["pessoa_id"], schema="core")
    op.create_index("idx_documentos_pessoa_id", "documentos", ["pessoa_id"], schema="core")
    op.create_index("idx_documentos_tipo_numero", "documentos", ["tipo", "numero"], schema="core")
    op.create_index("idx_contatos_pessoa_id", "contatos", ["pessoa_id"], schema="core")
    op.create_index("idx_pessoas_fisicas_nome", "pessoas_fisicas", ["nome"], schema="core")


def downgrade() -> None:
    for table in _NOVAS_TABELAS:
        op.execute(f"DROP TRIGGER IF EXISTS trg_{table}_updated_at ON core.{table}")
    op.drop_index("idx_pessoas_fisicas_nome", table_name="pessoas_fisicas", schema="core")
    op.drop_index("idx_contatos_pessoa_id", table_name="contatos", schema="core")
    op.drop_index("idx_documentos_tipo_numero", table_name="documentos", schema="core")
    op.drop_index("idx_documentos_pessoa_id", table_name="documentos", schema="core")
    op.drop_index("idx_enderecos_pessoa_id", table_name="enderecos", schema="core")
    op.drop_table("contatos", schema="core")
    op.drop_table("documentos", schema="core")
    op.drop_table("enderecos", schema="core")
    op.drop_column("pessoas_fisicas", "nome", schema="core")

