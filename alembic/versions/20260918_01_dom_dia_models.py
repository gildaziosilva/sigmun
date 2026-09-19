"""Criação das tabelas do DOM-DIA (Gestão de Diárias, Viagens e Deslocamentos).

Referência: DOM-DIA-013, DOM-DIA-026, espelhado no DOM-GDO e DOM-SEG.
"""

from __future__ import annotations

import uuid

from alembic import op
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    String,
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "20260918_01_dom_dia_models"
down_revision = "20260916_01"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS dia")

    # Tabela viagens
    op.create_table(
        "viagens",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("servidor_id", String(36), nullable=False),
        Column("dota_id", String(36), nullable=False),
        Column("motivo", Text, nullable=False),
        Column("cargo_ocupado", Text),
        Column("unidade_origem_id", String(36), nullable=False),
        Column("unidade_destino_id", String(36), nullable=False),
        Column("data_inicio", DateTime(timezone=True)),
        Column("data_fim", DateTime(timezone=True)),
        Column("destino", Text, nullable=False),
        Column("is_antecipacao", Boolean, nullable=False, server_default=func.false()),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("created_by", Text),
        Column("updated_at", DateTime(timezone=True)),
        Column("is_deleted", Boolean, nullable=False, server_default=func.false()),
        schema="dia",
    )
    op.create_index("ix_viagens_servidor", "viagens", ["servidor_id"], schema="dia")
    op.create_index("ix_viagens_dota", "viagens", ["dota_id"], schema="dia")

    # Tabela diarias
    op.create_table(
        "diarias",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("viagem_id", Text, nullable=False),
        Column("servidor_id", String(36), nullable=False),
        Column("dota_id", String(36), nullable=False),
        Column("categoria", Text, nullable=False),
        Column("descricao", Text),
        Column("data_inicio", DateTime(timezone=True)),
        Column("data_fim", DateTime(timezone=True)),
        Column("valor_diaria", Float, nullable=False, server_default="0"),
        Column("valor_total", Float, nullable=False, server_default="0"),
        Column("status", Text, nullable=False, server_default="solicitada"),
        Column("data_solicitacao", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("data_autorizacao", DateTime(timezone=True)),
        Column("data_calculo", DateTime(timezone=True)),
        Column("data_concessao", DateTime(timezone=True)),
        Column("data_inicio_prestacao", DateTime(timezone=True)),
        Column("data_fim_prestacao", DateTime(timezone=True)),
        Column("data_pagamento", DateTime(timezone=True)),
        Column("data_aprovacao", DateTime(timezone=True)),
        Column("data_glosa", DateTime(timezone=True)),
        Column("data_restituicao", DateTime(timezone=True)),
        Column("data_cancelamento", DateTime(timezone=True)),
        Column("motivo_cancelamento", Text),
        Column("motivo_glosa", Text),
        Column("valor_glosado", Float, nullable=False, server_default="0"),
        Column("documento_prestacao_id", Text),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("created_by", Text),
        Column("updated_at", DateTime(timezone=True)),
        Column("updated_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default=func.false()),
        schema="dia",
    )
    op.create_index("ix_diarias_servidor", "diarias", ["servidor_id"], schema="dia")
    op.create_index("ix_diarias_dota", "diarias", ["dota_id"], schema="dia")
# Tabela prestacoes_contas
    op.create_table(
        "prestacoes_contas",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("diaria_id", Text, nullable=False),
        Column("servidor_id", String(36), nullable=False),
        Column("dota_id", String(36), nullable=False),
        Column("data_emissao", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("data_vencimento", DateTime(timezone=True)),
        Column("documento_id", Text),
        Column("valor_previsto", Float, nullable=False, server_default="0"),
        Column("valor_apresentado", Float, nullable=False, server_default="0"),
        Column("valor_glosado", Float, nullable=False, server_default="0"),
        Column("valor_liquido", Float, nullable=False, server_default="0"),
        Column("status", Text, nullable=False, server_default="aberta"),
        Column("motivo_glosa", Text),
        Column("data_aprovacao", DateTime(timezone=True)),
        Column("data_glosa", DateTime(timezone=True)),
        Column("data_restituicao", DateTime(timezone=True)),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("created_by", Text),
        Column("updated_at", DateTime(timezone=True)),
        Column("updated_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default=func.false()),
        schema="dia",
    )
    op.create_index("ix_prestacoes_diaria", "prestacoes_contas", ["diaria_id"], schema="dia")

    # Tabela eventos_diarias (audit log de transições de estado)
    op.create_table(
        "eventos_diarias",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("diaria_id", Text, nullable=False),
        Column("status_anterior", String(40), nullable=False),
        Column("status_posterior", String(40), nullable=False),
        Column("usuario_id", String(36), nullable=False),
        Column("motivo", Text),
        Column("data_evento", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("detalhes", Text),
        schema="dia",
    )
    op.create_index("ix_eventos_diarias_diaria", "eventos_diarias", ["diaria_id"], schema="dia")


def downgrade() -> None:
    op.drop_table("eventos_diarias", schema="dia")
    op.drop_table("prestacoes_contas", schema="dia")
    op.drop_table("diarias", schema="dia")
    op.drop_table("viagens", schema="dia")
    op.create_index("ix_diarias_status", "diarias", ["status"], schema="dia")