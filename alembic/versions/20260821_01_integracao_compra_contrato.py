"""Formalização da contratação: vincula Contrato à Compra.

Adiciona a coluna ``compra_id`` (opcional) a ``compras.contratos`` para
permitir a integração Compra -> Contrato (Formalização da Contratação,
UC-COMPRAS-022 / RN-COMPRAS-038).

Revision ID: 20260821_01
Revises: 20260820_01
Create Date: 2026-08-21
"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision = "20260821_01"
down_revision = "20260820_01"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "contratos",
        sa.Column("compra_id", postgresql.UUID(as_uuid=True), nullable=True),
        schema="compras",
    )
    op.create_foreign_key(
        "contratos_compra_id_fkey",
        "contratos",
        "compras",
        ["compra_id"],
        ["id"],
        source_schema="compras",
        referent_schema="compras",
        onupdate="CASCADE",
        ondelete="RESTRICT",
    )
    op.create_index(
        "idx_contratos_compra_id",
        "contratos",
        ["compra_id"],
        schema="compras",
    )


def downgrade() -> None:
    op.drop_index("idx_contratos_compra_id", table_name="contratos", schema="compras")
    op.drop_constraint(
        "contratos_compra_id_fkey",
        "contratos",
        schema="compras",
        type_="foreignkey",
    )
    op.drop_column("contratos", "compra_id", schema="compras")
