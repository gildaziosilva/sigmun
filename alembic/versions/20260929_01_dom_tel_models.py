"""Migração DOM-TEL: gestão territorial (schema tel).

Cria o schema `tel` e as tabelas de divisões territoriais, logradouros,
planta genérica de valores e georreferências.

Regras: RN-TEL-001 (código único de bairro), RN-TEL-002 (código único de
logradouro), RN-TEL-003 (unicidade da planta vigente por ano/bairro/ocupação),
RN-TEL-005 (georreferência vinculada a bairro OU logradouro).
"""

from __future__ import annotations

import uuid

import sqlalchemy as sa
from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    Integer,
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import JSON, UUID

from alembic import op

revision = "20260929_01_dom_tel_models"
down_revision = "20260927_01_dom_ass_models"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS tel")
    op.create_table(
        "bairros",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("codigo", Text, nullable=False, unique=True),
        Column("nome", Text, nullable=False),
        Column("tipo", Text, nullable=False, server_default="bairro"),
        Column("populacao_estimada", Integer, nullable=False, server_default="0"),
        Column("area_km2", Float, nullable=False, server_default="0"),
        Column("situacao", Text, nullable=False, server_default="ativo"),
        Column(
            "created_at", DateTime(timezone=True), nullable=False, server_default=func.now()
        ),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="tel",
    )
    op.create_index("ix_tel_bairros_codigo", "bairros", ["codigo"], schema="tel")

    op.create_table(
        "logradouros",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("codigo", Text, nullable=False, unique=True),
        Column("nome", Text, nullable=False),
        Column("tipo", Text, nullable=False, server_default="rua"),
        Column("bairro_id", Text, nullable=False),
        Column("cep", Text),
        Column("numero_inicial", Integer, nullable=False, server_default="0"),
        Column("numero_final", Integer, nullable=False, server_default="0"),
        Column("situacao", Text, nullable=False, server_default="ativo"),
        Column(
            "created_at", DateTime(timezone=True), nullable=False, server_default=func.now()
        ),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="tel",
    )
    op.create_index("ix_tel_logradouros_codigo", "logradouros", ["codigo"], schema="tel")
    op.create_index("ix_tel_logradouros_bairro", "logradouros", ["bairro_id"], schema="tel")

    op.create_table(
        "planta_generica_valores",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("ano", Integer, nullable=False),
        Column("bairro_id", Text, nullable=False),
        Column("ocupacao", Text, nullable=False, server_default="residencial"),
        Column("valor_terreno_m2", Float, nullable=False, server_default="0"),
        Column("valor_construcao_m2", Float, nullable=False, server_default="0"),
        Column("aliquota_percent", Float, nullable=False, server_default="0"),
        Column("situacao", Text, nullable=False, server_default="rascunho"),
        Column("legislacao", Text),
        Column(
            "created_at", DateTime(timezone=True), nullable=False, server_default=func.now()
        ),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="tel",
    )
    # RN-TEL-003: no máximo uma planta vigente por ano, bairro e ocupação.
    op.create_index(
        "uq_tel_planta_vigente",
        "planta_generica_valores",
        ["ano", "bairro_id", "ocupacao"],
        unique=True,
        postgresql_where=sa.text("situacao = 'vigente' AND is_deleted = false"),
        schema="tel",
    )

    op.create_table(
        "georreferencias",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("bairro_id", Text),
        Column("logradouro_id", Text),
        Column("geometria", Text, nullable=False, server_default="ponto"),
        Column("latitude", Float, nullable=False, server_default="0"),
        Column("longitude", Float, nullable=False, server_default="0"),
        Column("altitude_m", Float),
        Column("vertices", JSON),
        Column("datum", Text, nullable=False, server_default="sirgas2000"),
        Column("precisao_m", Float, nullable=False, server_default="0"),
        Column("data_levantamento", Date, nullable=False),
        Column(
            "created_at", DateTime(timezone=True), nullable=False, server_default=func.now()
        ),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="tel",
    )
    # RN-TEL-005: georreferência vinculada a um bairro OU a um logradouro.
    op.create_check_constraint(
        "ck_tel_geo_referencia",
        "georreferencias",
        "(bairro_id IS NOT NULL AND logradouro_id IS NULL) "
        "OR (bairro_id IS NULL AND logradouro_id IS NOT NULL)",
        schema="tel",
    )
    op.create_index("ix_tel_geo_bairro", "georreferencias", ["bairro_id"], schema="tel")
    op.create_index("ix_tel_geo_logradouro", "georreferencias", ["logradouro_id"], schema="tel")



def downgrade() -> None:
    op.drop_index("ix_tel_geo_logradouro", table_name="georreferencias", schema="tel")
    op.drop_index("ix_tel_geo_bairro", table_name="georreferencias", schema="tel")
    op.drop_constraint(
        "ck_tel_geo_referencia", "georreferencias", schema="tel", type_="check"
    )
    op.drop_table("georreferencias", schema="tel")
    op.drop_index(
        "uq_tel_planta_vigente", table_name="planta_generica_valores", schema="tel"
    )
    op.drop_table("planta_generica_valores", schema="tel")
    op.drop_index("ix_tel_logradouros_bairro", table_name="logradouros", schema="tel")
    op.drop_index("ix_tel_logradouros_codigo", table_name="logradouros", schema="tel")
    op.drop_table("logradouros", schema="tel")
    op.drop_index("ix_tel_bairros_codigo", table_name="bairros", schema="tel")
    op.drop_table("bairros", schema="tel")
    op.execute("DROP SCHEMA IF EXISTS tel")

