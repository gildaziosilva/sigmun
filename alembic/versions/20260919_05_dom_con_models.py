"""Migração DOM-CON parte 1: empenhos/liquidações/pagamentos."""

from __future__ import annotations

import uuid

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, Text, func
from sqlalchemy.dialects.postgresql import UUID

from alembic import op

revision = "20260919_05_dom_con_models"
down_revision = "20260919_04_dom_orc_models"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Cria schema con e tabelas de execução."""
    op.execute("CREATE SCHEMA IF NOT EXISTS con")
    op.create_table(
        "empenhos",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("exercicio", Integer, nullable=False),
        Column("numero", Text, nullable=False),
        Column("dotacao_id", Text, nullable=False),
        Column("reserva_id", Text),
        Column("favorecido_nome", Text),
        Column("tipo", Text, nullable=False, server_default="ordinario"),
        Column("descricao", Text),
        Column("valor_empenhado", Float, nullable=False, server_default="0"),
        Column("valor_anulado", Float, nullable=False, server_default="0"),
        Column("valor_liquidado", Float, nullable=False, server_default="0"),
        Column("valor_pago", Float, nullable=False, server_default="0"),
        Column("status", Text, nullable=False, server_default="emitido"),
        Column("data_emissao", DateTime(timezone=True), server_default=func.now()),
        Column("motivo_anulacao", Text),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("updated_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="con",
    )
    op.create_table(
        "liquidacoes",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("empenho_id", UUID(as_uuid=True),
               ForeignKey("con.empenhos.id", onupdate="CASCADE", ondelete="RESTRICT"),
               nullable=False),
        Column("numero", Text),
        Column("valor", Float, nullable=False, server_default="0"),
        Column("documento_fiscal", Text),
        Column("status", Text, nullable=False, server_default="registrada"),
        Column("motivo_cancelamento", Text),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("updated_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="con",
    )
    op.create_table(
        "pagamentos",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("liquidacao_id", UUID(as_uuid=True),
               ForeignKey("con.liquidacoes.id", onupdate="CASCADE", ondelete="RESTRICT"),
               nullable=False),
        Column("empenho_id", UUID(as_uuid=True),
               ForeignKey("con.empenhos.id", onupdate="CASCADE", ondelete="RESTRICT"),
               nullable=False),
        Column("numero_ob", Text),
        Column("valor", Float, nullable=False, server_default="0"),
        Column("conta_bancaria", Text),
        Column("status", Text, nullable=False, server_default="programado"),
        Column("motivo_cancelamento", Text),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("updated_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="con",
    )


def downgrade() -> None:
    """Remove tabelas de execução."""
    op.drop_table("pagamentos", schema="con")
    op.drop_table("liquidacoes", schema="con")
    op.drop_table("empenhos", schema="con")
