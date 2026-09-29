"""Migração DOM-IMO: cadastro imobiliário (schema imo).

Cria o schema `imo` e as tabelas de imóveis, vínculos de propriedade,
avaliações de valor venal, características construtivas e geometrias dos lotes.

Regras materializadas: RN-IMO-001 (inscrição imobiliária única),
RN-IMO-006 (um único titular principal por imóvel, via índice parcial),
RN-IMO-005 (uma avaliação por imóvel e exercício).
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

revision = "20260929_02_dom_imo_models"
down_revision = "20260929_01_dom_tel_models"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS imo")
    op.create_table(
        "imoveis",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("inscricao_imobiliaria", Text, nullable=False, unique=True),
        Column("logradouro_id", Text, nullable=False),
        Column("bairro_id", Text, nullable=False),
        Column("numero", Text),
        Column("complemento", Text),
        Column("tipo", Text, nullable=False, server_default="lote"),
        Column("situacao", Text, nullable=False, server_default="ativo"),
        Column("tipo_propriedade", Text, nullable=False, server_default="proprio"),
        Column("area_terreno_m2", Float, nullable=False, server_default="0"),
        Column("area_construida_m2", Float, nullable=False, server_default="0"),
        Column("ano_construcao", Integer),
        Column(
            "created_at", DateTime(timezone=True), nullable=False, server_default=func.now()
        ),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="imo",
    )
    op.create_index("ix_imo_imoveis_inscricao", "imoveis", ["inscricao_imobiliaria"], schema="imo")
    op.create_index("ix_imo_imoveis_logradouro", "imoveis", ["logradouro_id"], schema="imo")
    op.create_index("ix_imo_imoveis_bairro", "imoveis", ["bairro_id"], schema="imo")

    op.create_table(
        "proprietarios_imoveis",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("imovel_id", Text, nullable=False),
        Column("pessoa_id", Text),
        Column("nome", Text, nullable=False),
        Column("cpf", Text, nullable=False),
        Column("vinculo", Text, nullable=False, server_default="titular"),
        Column("principal", Boolean, nullable=False, server_default="false"),
        Column(
            "created_at", DateTime(timezone=True), nullable=False, server_default=func.now()
        ),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="imo",
    )
    op.create_index(
        "ix_imo_prop_imovel", "proprietarios_imoveis", ["imovel_id"], schema="imo"
    )
    # RN-IMO-006: no máximo um proprietário titular principal por imóvel.
    op.create_index(
        "uq_imo_titular_principal",
        "proprietarios_imoveis",
        ["imovel_id"],
        unique=True,
        postgresql_where=sa.text(
            "principal = true AND vinculo = 'titular' AND is_deleted = false"
        ),
        schema="imo",
    )


    op.create_table(
        "avaliacoes_imoveis",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("imovel_id", Text, nullable=False),
        Column("ano", Integer, nullable=False),
        Column("valor_terreno_m2_unitario", Float, nullable=False, server_default="0"),
        Column("valor_construcao_m2_unitario", Float, nullable=False, server_default="0"),
        Column("aliquota_percent", Float, nullable=False, server_default="0"),
        Column("area_terreno_m2", Float, nullable=False, server_default="0"),
        Column("area_construida_m2", Float, nullable=False, server_default="0"),
        Column("situacao", Text, nullable=False, server_default="rascunho"),
        Column("data_avaliacao", Date, nullable=False),
        Column(
            "created_at", DateTime(timezone=True), nullable=False, server_default=func.now()
        ),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="imo",
    )
    # RN-IMO-005: uma avaliação por imóvel e exercício.
    op.create_index(
        "uq_imo_avaliacao_exercicio",
        "avaliacoes_imoveis",
        ["imovel_id", "ano"],
        unique=True,
        postgresql_where=sa.text("is_deleted = false"),
        schema="imo",
    )

    op.create_table(
        "caracteristicas_imoveis",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("imovel_id", Text, nullable=False),
        Column("obra", Text, nullable=False, server_default="residencial"),
        Column("numero_pavimentos", Integer, nullable=False, server_default="1"),
        Column("ano_renovacao", Integer),
        Column("observacao", Text),
        Column(
            "created_at", DateTime(timezone=True), nullable=False, server_default=func.now()
        ),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        schema="imo",
    )
    op.create_index(
        "uq_imo_caracteristica", "caracteristicas_imoveis", ["imovel_id"], unique=True, schema="imo"
    )

    op.create_table(
        "geometrias_imoveis",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("imovel_id", Text, nullable=False),
        Column("geometria", Text, nullable=False, server_default="ponto"),
        Column("latitude", Float, nullable=False, server_default="0"),
        Column("longitude", Float, nullable=False, server_default="0"),
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
        schema="imo",
    )
    # RN-IMO-007: uma geometria vigente por lote.
    op.create_index(
        "uq_imo_geometria_lote",
        "geometrias_imoveis",
        ["imovel_id"],
        unique=True,
        postgresql_where=sa.text("is_deleted = false"),
        schema="imo",
    )


def downgrade() -> None:
    op.drop_index("uq_imo_geometria_lote", table_name="geometrias_imoveis", schema="imo")
    op.drop_table("geometrias_imoveis", schema="imo")
    op.drop_index("uq_imo_caracteristica", table_name="caracteristicas_imoveis", schema="imo")
    op.drop_table("caracteristicas_imoveis", schema="imo")
    op.drop_index("uq_imo_avaliacao_exercicio", table_name="avaliacoes_imoveis", schema="imo")
    op.drop_table("avaliacoes_imoveis", schema="imo")
    op.drop_index("uq_imo_titular_principal", table_name="proprietarios_imoveis", schema="imo")
    op.drop_index("ix_imo_prop_imovel", table_name="proprietarios_imoveis", schema="imo")
    op.drop_table("proprietarios_imoveis", schema="imo")
    op.drop_index("ix_imo_imoveis_bairro", table_name="imoveis", schema="imo")
    op.drop_index("ix_imo_imoveis_logradouro", table_name="imoveis", schema="imo")
    op.drop_index("ix_imo_imoveis_inscricao", table_name="imoveis", schema="imo")
    op.drop_table("imoveis", schema="imo")
    op.execute("DROP SCHEMA IF EXISTS imo")

