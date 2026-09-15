"""Correct DOM-SEG schema placement and temporal defaults.

Revision ID: 20260901_05
Revises: 20260901_04
Create Date: 2026-09-09

Tarefa:
- Criar o schema seg;
- mover as tabelas DOM-SEG de public para seg;
- alinhar created_at e updated_at com o ORM utilizando
  server_default=now();
- preservar dados, constraints, índices e ownership.

Contexto:
A migration 20260901_04 foi aplicada e criou as tabelas
DOM-SEG no schema public por ausência do parâmetro schema
no upgrade(). Esta migration corrige o estado sem reescrever
o histórico da migration 04.
"""

import sqlalchemy as sa

from alembic import op


revision = "20260901_05"
down_revision = "20260901_04"
branch_labels = None
depends_on = None


TABLES = (
    "controles_seguranca",
    "politicas_seguranca",
    "incidentes_seguranca",
    "chaves_criptograficas",
    "credenciais",
)


def upgrade() -> None:
    # O schema é criado explicitamente conforme o padrão
    # adotado nas demais migrations de domínio do SIGMUN.
    op.execute("CREATE SCHEMA IF NOT EXISTS seg AUTHORIZATION sigmun")

    # A operação SET SCHEMA preserva a tabela e seus objetos
    # internos (PKs, UNIQUEs e índices).
    for table in TABLES:
        op.execute(
            f"ALTER TABLE public.{table} SET SCHEMA seg"
        )

    # Alinha os defaults temporais do banco com o ORM.
    for table in TABLES:
        op.alter_column(
            table,
            "created_at",
            schema="seg",
            existing_type=sa.DateTime(timezone=True),
            existing_nullable=False,
            server_default=sa.func.now(),
        )
        op.alter_column(
            table,
            "updated_at",
            schema="seg",
            existing_type=sa.DateTime(timezone=True),
            existing_nullable=False,
            server_default=sa.func.now(),
        )


def downgrade() -> None:
    # Remove os defaults introduzidos por esta migration.
    for table in reversed(TABLES):
        op.alter_column(
            table,
            "updated_at",
            schema="seg",
            existing_type=sa.DateTime(timezone=True),
            existing_nullable=False,
            server_default=None,
        )
        op.alter_column(
            table,
            "created_at",
            schema="seg",
            existing_type=sa.DateTime(timezone=True),
            existing_nullable=False,
            server_default=None,
        )

    # Retorna as tabelas ao estado físico produzido pela migration 04.
    for table in reversed(TABLES):
        op.execute(
            f"ALTER TABLE seg.{table} SET SCHEMA public"
        )

    op.execute("DROP SCHEMA IF EXISTS seg")
