"""Migracao DOM-PES parte 1: cargos/servidores/lotacoes."""

from __future__ import annotations

import uuid

from alembic import op
from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, String, Text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID

revision = "20260919_01_dom_pes_models"
down_revision = "20260918_01_dom_dia_models"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Cria schema rh e tabelas base."""
    op.execute("CREATE SCHEMA IF NOT EXISTS rh")
    op.create_table(
        "cargos",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("codigo", Text, nullable=False, unique=True),
        Column("nome", Text, nullable=False),
        Column("descricao", Text),
        Column("nivel", Text, nullable=False, server_default="basico"),
        Column("salario_base", Float, nullable=False, server_default="0"),
        Column("carga_horaria_semanal", Integer, nullable=False,
               server_default="40"),
        Column("ativo", Boolean, nullable=False, server_default="true"),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False,
               server_default="false"),
        schema="rh",
    )
    op.create_table(
        "servidores",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("matricula", Text, nullable=False, unique=True),
        Column("cpf", String(11), nullable=False, unique=True),
        Column("nome", Text, nullable=False),
        Column("cargo_id", Text, nullable=False),
        Column("tipo_vinculo", Text, nullable=False, server_default="efetivo"),
        Column("status", Text, nullable=False, server_default="ativo"),
        Column("data_admissao", Date),
        Column("data_desligamento", Date),
        Column("salario", Float, nullable=False, server_default="0"),
        Column("email", Text),
        Column("telefone", Text),
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
        "lotacoes",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("servidor_id", Text, nullable=False),
        Column("unidade_id", Text, nullable=False),
        Column("cargo_id", Text),
        Column("data_inicio", Date),
        Column("data_fim", Date),
        Column("vigente", Boolean, nullable=False, server_default="true"),
        Column("motivo", Text),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False,
               server_default="false"),
        schema="rh",
    )


def downgrade() -> None:
    """Remove tabelas base."""
    op.drop_table("lotacoes", schema="rh")
    op.drop_table("servidores", schema="rh")
    op.drop_table("cargos", schema="rh")
