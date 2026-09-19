"""Migracao DOM-PES parte 2: folha/ferias/frequencia."""

from __future__ import annotations

import uuid

from alembic import op
from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, String, Text
from sqlalchemy import Time, func
from sqlalchemy.dialects.postgresql import UUID

revision = "20260919_02_dom_pes_folha"
down_revision = "20260919_01_dom_pes_models"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Cria tabelas de folha/ferias/frequencia."""
    op.create_table(
        "folhas_pagamento",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("competencia_ano", Integer, nullable=False),
        Column("competencia_mes", Integer, nullable=False),
        Column("descricao", Text),
        Column("status", Text, nullable=False, server_default="aberta"),
        Column("total_proventos", Float, nullable=False, server_default="0"),
        Column("total_descontos", Float, nullable=False, server_default="0"),
        Column("total_liquido", Float, nullable=False, server_default="0"),
        Column("quantidade_servidores", Integer, nullable=False,
               server_default="0"),
        Column("data_fechamento", DateTime(timezone=True)),
        Column("data_homologacao", DateTime(timezone=True)),
        Column("data_pagamento", DateTime(timezone=True)),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("updated_by", Text),
        Column("is_deleted", Boolean, nullable=False,
               server_default="false"),
        schema="rh",
    )
    op.create_table(
        "ferias",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("servidor_id", Text, nullable=False),
        Column("periodo_aquisitivo_inicio", Date),
        Column("periodo_aquisitivo_fim", Date),
        Column("data_inicio_gozo", Date),
        Column("data_fim_gozo", Date),
        Column("dias", Integer, nullable=False, server_default="30"),
        Column("parcela", Integer, nullable=False, server_default="1"),
        Column("status", Text, nullable=False, server_default="planejada"),
        Column("data_aprovacao", DateTime(timezone=True)),
        Column("data_cancelamento", DateTime(timezone=True)),
        Column("motivo_cancelamento", Text),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False,
               server_default="false"),
        schema="rh",
    )
    op.create_table(
        "frequencias",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("servidor_id", String(36), nullable=False),
        Column("data", Date, nullable=False),
        Column("tipo", Text, nullable=False, server_default="presenca"),
        Column("hora_entrada", Time),
        Column("hora_saida", Time),
        Column("minutos_atraso", Integer, nullable=False, server_default="0"),
        Column("justificativa", Text),
        Column("desconto_folha", Boolean, nullable=False,
               server_default="false"),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False,
               server_default="false"),
        schema="rh",
    )


def downgrade() -> None:
    """Remove tabelas operacionais."""
    op.drop_table("frequencias", schema="rh")
    op.drop_table("ferias", schema="rh")
    op.drop_table("folhas_pagamento", schema="rh")
