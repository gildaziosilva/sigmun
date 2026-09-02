"""Trilha de auditoria do domínio Compras (schema separado).

Cria o schema ``auditoria`` e a tabela ``auditoria.eventos``
(017-Modelo-de-Auditoria: seção 26 – estrutura do registro; seção 37 –
imutabilidade; seção 39 – separação entre dados operacionais e auditoria).

Imutabilidade garantida no banco por trigger que bloqueia UPDATE/DELETE.

Revision ID: 20260822_01
Revises: 20260821_01
Create Date: 2026-08-22
"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision = "20260822_01"
down_revision = "20260821_01"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS auditoria")

    op.create_table(
        "eventos",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("gen_random_uuid()"),
        ),
        sa.Column(
            "ocorrido_em",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column("categoria", sa.Text(), nullable=False),
        sa.Column("tipo_evento", sa.Text(), nullable=False),
        sa.Column("ator_id", postgresql.UUID(as_uuid=True)),
        sa.Column("ator_perfil", sa.Text()),
        sa.Column(
            "origem", sa.Text(), nullable=False, server_default="gestao-compras"
        ),
        sa.Column("operacao", sa.Text(), nullable=False),
        sa.Column("recurso_tipo", sa.Text(), nullable=False),
        sa.Column("recurso_id", postgresql.UUID(as_uuid=True)),
        sa.Column("chave_negocio", sa.Text()),
        sa.Column("resultado", sa.Text(), nullable=False),
        sa.Column("correlation_id", postgresql.UUID(as_uuid=True)),
        sa.Column("justificativa", sa.Text()),
        sa.Column("detalhes", postgresql.JSONB()),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.CheckConstraint(
            "categoria IN ('AUTENTICACAO','AUTORIZACAO','ACESSO','CRIACAO',"
            "'ALTERACAO','EXCLUSAO','APROVACAO','REJEICAO','CANCELAMENTO',"
            "'ASSINATURA','PUBLICACAO','EXECUCAO','INTEGRACAO','EXPORTACAO',"
            "'IMPORTACAO','SEGURANCA','ADMINISTRACAO')",
            name="ck_eventos_categoria",
        ),
        sa.CheckConstraint(
            "resultado IN ('SUCESSO','ERRO')", name="ck_eventos_resultado"
        ),
        schema="auditoria",
    )

    # Seção 37 – Imutabilidade: bloqueia alteração e exclusão na trilha.
    op.execute(
        """
        CREATE OR REPLACE FUNCTION auditoria.fn_bloqueia_mutacao()
        RETURNS TRIGGER AS $$
        BEGIN
            RAISE EXCEPTION 'Trilha de auditoria é imutável (%.%)',
                TG_TABLE_SCHEMA, TG_TABLE_NAME;
        END;
        $$ LANGUAGE plpgsql
        """
    )
    op.execute(
        """
        CREATE TRIGGER trg_eventos_imutavel
        BEFORE UPDATE OR DELETE ON auditoria.eventos
        FOR EACH ROW EXECUTE FUNCTION auditoria.fn_bloqueia_mutacao()
        """
    )

    op.create_index(
        "idx_eventos_ocorrido_em", "eventos", ["ocorrido_em"], schema="auditoria"
    )
    op.create_index(
        "idx_eventos_recurso",
        "eventos",
        ["recurso_tipo", "recurso_id"],
        schema="auditoria",
    )
    op.create_index("idx_eventos_ator_id", "eventos", ["ator_id"], schema="auditoria")
    op.create_index(
        "idx_eventos_correlation_id", "eventos", ["correlation_id"], schema="auditoria"
    )


def downgrade() -> None:
    for index_name in (
        "idx_eventos_correlation_id",
        "idx_eventos_ator_id",
        "idx_eventos_recurso",
        "idx_eventos_ocorrido_em",
    ):
        op.drop_index(index_name, table_name="eventos", schema="auditoria")

    op.execute("DROP TRIGGER IF EXISTS trg_eventos_imutavel ON auditoria.eventos")
    op.execute("DROP FUNCTION IF EXISTS auditoria.fn_bloqueia_mutacao()")
    op.drop_table("eventos", schema="auditoria")
    op.execute("DROP SCHEMA IF EXISTS auditoria")
