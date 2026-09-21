"""Migracao DOM-TRI: administracao tributaria (schema trib)."""

from __future__ import annotations

import uuid

from alembic import op
from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, String, Text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID

revision = "20260920_01_dom_tri_models"
down_revision = "20260919_06_dom_con_contabil"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Cria schema trib e tabelas de administracao tributaria."""
    op.execute("CREATE SCHEMA IF NOT EXISTS trib")
    op.create_table(
        "contribuintes",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("tipo", Text, nullable=False, server_default="pf"),
        Column("nome", Text, nullable=False),
        Column("cpf_cnpj", String(14), nullable=False, unique=True),
        Column("inscricao_municipal", Text),
        Column("email", Text),
        Column("telefone", Text),
        Column("endereco", Text),
        Column("status", Text, nullable=False, server_default="ativo"),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="trib",
    )
    op.create_table(
        "imoveis",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("contribuinte_id", Text, nullable=False),
        Column("inscricao_imobiliaria", Text, nullable=False, unique=True),
        Column("logradouro", Text),
        Column("numero", Text),
        Column("bairro", Text),
        Column("cidade", Text),
        Column("uf", String(2)),
        Column("cep", String(8)),
        Column("area_terreno", Float, nullable=False, server_default="0"),
        Column("area_construida", Float, nullable=False, server_default="0"),
        Column("valor_venal", Float, nullable=False, server_default="0"),
        Column("aliquota", Float, nullable=False, server_default="0"),
        Column("status", Text, nullable=False, server_default="ativo"),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="trib",
    )
    op.create_table(
        "lancamentos",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("contribuinte_id", Text, nullable=False),
        Column("imovel_id", Text),
        Column("tipo_tributo", Text, nullable=False, server_default="taxa"),
        Column("exercicio", Integer, nullable=False),
        Column("numero_lancamento", Text, nullable=False, unique=True),
        Column("descricao", Text),
        Column("base_calculo", Float, nullable=False, server_default="0"),
        Column("aliquota", Float, nullable=False, server_default="0"),
        Column("valor_tributo", Float, nullable=False, server_default="0"),
        Column("juros", Float, nullable=False, server_default="0"),
        Column("multa", Float, nullable=False, server_default="0"),
        Column("valor_total", Float, nullable=False, server_default="0"),
        Column("data_vencimento", Date),
        Column("status", Text, nullable=False, server_default="lancado"),
        Column("data_pagamento", Date),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="trib",
    )
    op.create_table(
        "divida_ativa",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("lancamento_id", Text, nullable=False, unique=True),
        Column("numero_inscricao", Text, nullable=False, unique=True),
        Column("data_inscricao", Date),
        Column("valor_original", Float, nullable=False, server_default="0"),
        Column("valor_atualizado", Float, nullable=False, server_default="0"),
        Column("status", Text, nullable=False, server_default="ativa"),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="trib",
    )
    op.create_table(
        "certidoes",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("contribuinte_id", Text, nullable=False),
        Column("tipo", Text, nullable=False, server_default="negativa"),
        Column("numero", Text, nullable=False, unique=True),
        Column("data_emissao", Date),
        Column("valido_ate", Date),
        Column("observacao", Text),
        Column("status", Text, nullable=False, server_default="emitida"),
        Column("created_at", DateTime(timezone=True), nullable=False,
               server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="trib",
    )


def downgrade() -> None:
    """Remove as tabelas de administracao tributaria."""
    op.drop_table("certidoes", schema="trib")
    op.drop_table("divida_ativa", schema="trib")
    op.drop_table("lancamentos", schema="trib")
    op.drop_table("imoveis", schema="trib")
    op.drop_table("contribuintes", schema="trib")