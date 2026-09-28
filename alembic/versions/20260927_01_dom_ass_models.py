"""Migracao DOM-ASS: assistencia social (schema ass)."""
from __future__ import annotations
import uuid
from alembic import op
from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, Text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
revision = "20260927_01_dom_ass_models"
down_revision = "20260927_fix_gdo_versoes_trigger"
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS ass")
    op.create_table(
        "familias_cadunico",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("nis", Text, nullable=False, unique=True),
        Column("responsavel_nome", Text, nullable=False),
        Column("responsavel_cpf", Text),
        Column("endereco", Text),
        Column("telefone", Text),
        Column("renda_per_capita", Float, nullable=False, server_default="0"),
        Column("quantidade_pessoas", Integer, nullable=False, server_default="0"),
        Column("status", Text, nullable=False, server_default="ativa"),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="ass",
    )
    op.create_table(
        "pessoas_cadunico",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("familia_id", Text, nullable=False),
        Column("nome", Text, nullable=False),
        Column("cpf", Text, nullable=False, unique=True),
        Column("data_nascimento", Text),
        Column("sexo", Text, nullable=False, server_default="ignorado"),
        Column("nome_mae", Text),
        Column("parentesco", Text),
        Column("escolaridade", Text),
        Column("ocupacao", Text),
        Column("renda", Float, nullable=False, server_default="0"),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="ass",
    )
    op.create_table(
        "unidades_assistencia",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("codigo", Text, nullable=False, unique=True),
        Column("nome", Text, nullable=False),
        Column("tipo", Text, nullable=False, server_default="cras"),
        Column("endereco", Text),
        Column("telefone", Text),
        Column("email", Text),
        Column("responsavel", Text),
        Column("status", Text, nullable=False, server_default="ativa"),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="ass",
    )
    op.create_table(
        "beneficios_eventuais",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("familia_id", Text, nullable=False),
        Column("tipo", Text, nullable=False, server_default="alimentacao"),
        Column("descricao", Text),
        Column("valor", Float, nullable=False, server_default="0"),
        Column("quantidade", Integer, nullable=False, server_default="1"),
        Column("data_solicitacao", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("data_aprovacao", DateTime(timezone=True)),
        Column("data_entrega", DateTime(timezone=True)),
        Column("status", Text, nullable=False, server_default="solicitado"),
        Column("unidade_id", Text),
        Column("observacao", Text),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        schema="ass",
    )
    op.create_table(
        "atendimentos_sociais",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("pessoa_id", Text, nullable=False),
        Column("unidade_id", Text, nullable=False),
        Column("tipo", Text, nullable=False, server_default="acolhimento"),
        Column("data", Date),
        Column("descricao", Text),
        Column("encaminhamento", Text),
        Column("profissional", Text, nullable=False),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("created_by", Text),
        schema="ass",
    )

def downgrade() -> None:
    op.drop_table("atendimentos_sociais", schema="ass")
    op.drop_table("beneficios_eventuais", schema="ass")
    op.drop_table("unidades_assistencia", schema="ass")
    op.drop_table("pessoas_cadunico", schema="ass")
    op.drop_table("familias_cadunico", schema="ass")
    op.execute("DROP SCHEMA IF EXISTS ass")
