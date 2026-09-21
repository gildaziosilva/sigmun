"""Migracao DOM-FRO: gestao de frota (schema fro)."""

from __future__ import annotations

import uuid

from alembic import op
from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, Text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID

revision = "20260920_03_dom_fro_models"
down_revision = "20260920_02_dom_pat_models"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Cria schema fro e tabelas de gestao de frota."""
    op.execute("CREATE SCHEMA IF NOT EXISTS fro")
    op.create_table(
        "veiculos",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("placa", Text, nullable=False, unique=True),
        Column("chassi", Text),
        Column("renavam", Text),
        Column("marca", Text, nullable=False),
        Column("modelo", Text, nullable=False),
        Column("ano_fabricacao", Integer, nullable=False, server_default="0"),
        Column("ano_modelo", Integer, nullable=False, server_default="0"),
        Column("tipo", Text, nullable=False, server_default="leve"),
        Column("combustivel", Text, nullable=False, server_default="flex"),
        Column("capacidade", Float, nullable=False, server_default="0"),
        Column("odometro_atual", Float, nullable=False, server_default="0"),
        Column("status", Text, nullable=False, server_default="ativo"),
        Column("unidade_id", Text),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="fro",
    )
    op.create_table(
        "abastecimentos",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("veiculo_id", Text, nullable=False),
        Column("data", Date),
        Column("quantidade_litros", Float, nullable=False, server_default="0"),
        Column("valor_unitario", Float, nullable=False, server_default="0"),
        Column("valor_total", Float, nullable=False, server_default="0"),
        Column("odometro", Float, nullable=False, server_default="0"),
        Column("posto", Text),
        Column("tipo_combustivel", Text, nullable=False, server_default="flex"),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("created_by", Text),
        schema="fro",
    )
    op.create_table(
        "manutencoes",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("veiculo_id", Text, nullable=False),
        Column("data_entrada", Date),
        Column("data_saida", Date),
        Column("tipo", Text, nullable=False, server_default="preventiva"),
        Column("descricao", Text, nullable=False),
        Column("oficina", Text),
        Column("valor", Float, nullable=False, server_default="0"),
        Column("status", Text, nullable=False, server_default="aberta"),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("created_by", Text),
        schema="fro",
    )
    op.create_table(
        "rotas",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("veiculo_id", Text, nullable=False),
        Column("data", Date),
        Column("origem", Text, nullable=False),
        Column("destino", Text, nullable=False),
        Column("km_inicio", Float, nullable=False, server_default="0"),
        Column("km_fim", Float, nullable=False, server_default="0"),
        Column("distancia_km", Float, nullable=False, server_default="0"),
        Column("descricao", Text),
        Column("status", Text, nullable=False, server_default="planejada"),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("created_by", Text),
        schema="fro",
    )


def downgrade() -> None:
    """Remove as tabelas de gestao de frota."""
    op.drop_table("rotas", schema="fro")
    op.drop_table("manutencoes", schema="fro")
    op.drop_table("abastecimentos", schema="fro")
    op.drop_table("veiculos", schema="fro")