"""Pendências impeditivas do processo de compras (RN-COMPRAS-027).

Adiciona a coluna ``pendencias_impeditivas`` (booleano, default false) a
``compras.compras`` para sustentar o bloqueio de avanço processual enquanto
existirem pendências impeditivas.

Revision ID: 20260823_01
Revises: 20260822_01
Create Date: 2026-08-23
"""

import sqlalchemy as sa

from alembic import op

revision = "20260823_01"
down_revision = "20260822_01"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "compras",
        sa.Column(
            "pendencias_impeditivas",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("false"),
        ),
        schema="compras",
    )


def downgrade() -> None:
    op.drop_column("compras", "pendencias_impeditivas", schema="compras")
