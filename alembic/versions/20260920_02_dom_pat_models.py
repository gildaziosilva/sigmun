"""Migracao DOM-PAT: gestao patrimonial (schema pat)."""

from __future__ import annotations

import uuid

from alembic import op
from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, Text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID

revision = "20260920_02_dom_pat_models"
down_revision = "20260920_01_dom_tri_models"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Cria schema pat e tabelas patrimoniais."""
    op.execute("CREATE SCHEMA IF NOT EXISTS pat")
    op.create_table(
        "bens",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("codigo", Text, nullable=False, unique=True),
        Column("tipo", Text, nullable=False, server_default="movel"),
        Column("descricao", Text, nullable=False),
        Column("categoria", Text),
        Column("valor_aquisicao", Float, nullable=False, server_default="0"),
        Column("data_aquisicao", Date),
        Column("valor_residual", Float, nullable=False, server_default="0"),
        Column("vida_util_anos", Integer, nullable=False, server_default="0"),
        Column("valor_contabil", Float, nullable=False, server_default="0"),
        Column("status", Text, nullable=False, server_default="em_uso"),
        Column("localizacao", Text),
        Column("responsavel_id", Text),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="pat",
    )
    op.create_table(
        "depreciacoes",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("bem_id", Text, nullable=False),
        Column("data", Date),
        Column("valor_depreciado", Float, nullable=False, server_default="0"),
        Column("valor_acumulado", Float, nullable=False, server_default="0"),
        Column("valor_liquido", Float, nullable=False, server_default="0"),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("created_by", Text),
        schema="pat",
    )
    op.create_table(
        "transferencias",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("bem_id", Text, nullable=False),
        Column("de_localizacao", Text),
        Column("para_localizacao", Text, nullable=False),
        Column("de_responsavel_id", Text),
        Column("para_responsavel_id", Text),
        Column("data_transferencia", Date),
        Column("motivo", Text),
        Column("status", Text, nullable=False, server_default="pendente"),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("created_by", Text),
        schema="pat",
    )


def downgrade() -> None:
    """Remove as tabelas patrimoniais."""
    op.drop_table("transferencias", schema="pat")
    op.drop_table("depreciacoes", schema="pat")
    op.drop_table("bens", schema="pat")