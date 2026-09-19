"""Migração DOM-CON parte 2: PCASP/lançamentos/conciliação."""

from __future__ import annotations

import uuid

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, Text, func
from sqlalchemy.dialects.postgresql import UUID

from alembic import op

revision = "20260919_06_dom_con_contabil"
down_revision = "20260919_05_dom_con_models"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Cria tabelas contábeis no schema con."""
    op.create_table(
        "contas_contabeis",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("codigo", Text, nullable=False, unique=True),
        Column("nome", Text, nullable=False),
        Column("classe", Text),
        Column("natureza_saldo", Text, nullable=False, server_default="devedora"),
        Column("tipo", Text, nullable=False, server_default="analitica"),
        Column("aceita_lancamento", Boolean, nullable=False, server_default="true"),
        Column("ativa", Boolean, nullable=False, server_default="true"),
        Column("conta_pai_id", Text),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="con",
    )
    op.create_table(
        "lancamentos",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("exercicio", Integer, nullable=False),
        Column("numero", Text),
        Column("historico", Text),
        Column("origem", Text),
        Column("origem_id", Text),
        Column("partidas", Text, nullable=False, server_default="[]"),
        Column("total_debito", Float, nullable=False, server_default="0"),
        Column("total_credito", Float, nullable=False, server_default="0"),
        Column("status", Text, nullable=False, server_default="rascunho"),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="con",
    )
    op.create_table(
        "conciliacoes",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("conta_id", Text, nullable=False),
        Column("codigo_conta", Text),
        Column("competencia_ano", Integer, nullable=False),
        Column("competencia_mes", Integer, nullable=False),
        Column("saldo_contabil", Float, nullable=False, server_default="0"),
        Column("saldo_extrato", Float, nullable=False, server_default="0"),
        Column("diferenca", Float, nullable=False, server_default="0"),
        Column("status", Text, nullable=False, server_default="aberta"),
        Column("justificativa", Text),
        Column("data_conciliacao", DateTime(timezone=True)),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="con",
    )


def downgrade() -> None:
    """Remove tabelas contábeis."""
    op.drop_table("conciliacoes", schema="con")
    op.drop_table("lancamentos", schema="con")
    op.drop_table("contas_contabeis", schema="con")
