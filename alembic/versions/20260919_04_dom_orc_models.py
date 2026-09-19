"""Migração DOM-ORC: PPA/LDO/LOA/dotações/reservas (schemas orc)."""

from __future__ import annotations

import uuid

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, Text, func
from sqlalchemy.dialects.postgresql import UUID

from alembic import op

revision = "20260919_04_dom_orc_models"
down_revision = "20260919_03"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Cria schema orc e tabelas do orçamento."""
    op.execute("CREATE SCHEMA IF NOT EXISTS orc")
    op.create_table(
        "ppas",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("ano_inicial", Integer, nullable=False),
        Column("ano_final", Integer, nullable=False),
        Column("descricao", Text),
        Column("status", Text, nullable=False, server_default="elaboracao"),
        Column("data_publicacao", DateTime(timezone=True)),
        Column("data_encerramento", DateTime(timezone=True)),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("updated_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="orc",
    )
    op.create_table(
        "ldos",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("exercicio", Integer, nullable=False, unique=True),
        Column("ppa_id", UUID(as_uuid=True),
               ForeignKey("orc.ppas.id", onupdate="CASCADE", ondelete="RESTRICT"),
               nullable=False),
        Column("descricao", Text),
        Column("status", Text, nullable=False, server_default="elaboracao"),
        Column("meta_fiscal_receita", Float, nullable=False, server_default="0"),
        Column("meta_fiscal_despesa", Float, nullable=False, server_default="0"),
        Column("data_aprovacao", DateTime(timezone=True)),
        Column("data_sancao", DateTime(timezone=True)),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("updated_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="orc",
    )
    op.create_table(
        "loas",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("exercicio", Integer, nullable=False, unique=True),
        Column("ldo_id", UUID(as_uuid=True),
               ForeignKey("orc.ldos.id", onupdate="CASCADE", ondelete="RESTRICT"),
               nullable=False),
        Column("descricao", Text),
        Column("status", Text, nullable=False, server_default="elaboracao"),
        Column("valor_receita_prevista", Float, nullable=False, server_default="0"),
        Column("valor_despesa_fixada", Float, nullable=False, server_default="0"),
        Column("data_aprovacao", DateTime(timezone=True)),
        Column("data_publicacao", DateTime(timezone=True)),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("updated_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="orc",
    )
    op.create_table(
        "dotacoes",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("loa_id", UUID(as_uuid=True),
               ForeignKey("orc.loas.id", onupdate="CASCADE", ondelete="RESTRICT"),
               nullable=False),
        Column("exercicio", Integer, nullable=False),
        Column("codigo", Text, nullable=False),
        Column("unidade_orcamentaria", Text),
        Column("natureza_despesa", Text),
        Column("fonte_recursos", Text),
        Column("valor_inicial", Float, nullable=False, server_default="0"),
        Column("valor_suplementado", Float, nullable=False, server_default="0"),
        Column("valor_anulado", Float, nullable=False, server_default="0"),
        Column("valor_reservado", Float, nullable=False, server_default="0"),
        Column("valor_empenhado", Float, nullable=False, server_default="0"),
        Column("status", Text, nullable=False, server_default="ativa"),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("updated_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="orc",
    )
    op.create_table(
        "reservas",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("dotacao_id", UUID(as_uuid=True),
               ForeignKey("orc.dotacoes.id", onupdate="CASCADE", ondelete="RESTRICT"),
               nullable=False),
        Column("numero", Text),
        Column("valor", Float, nullable=False, server_default="0"),
        Column("finalidade", Text),
        Column("status", Text, nullable=False, server_default="ativa"),
        Column("data_reserva", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("data_conversao", DateTime(timezone=True)),
        Column("data_cancelamento", DateTime(timezone=True)),
        Column("motivo_cancelamento", Text),
        Column("empenho_id", Text),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("updated_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="orc",
    )


def downgrade() -> None:
    """Remove tabelas do orçamento."""
    op.drop_table("reservas", schema="orc")
    op.drop_table("dotacoes", schema="orc")
    op.drop_table("loas", schema="orc")
    op.drop_table("ldos", schema="orc")
    op.drop_table("ppas", schema="orc")
