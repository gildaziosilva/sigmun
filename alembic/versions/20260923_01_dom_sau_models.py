"""Migracao DOM-SAU: saude municipal (schema sau)."""
from __future__ import annotations
import uuid
from alembic import op
from sqlalchemy import Boolean, Column, Date, DateTime, Float, Text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
revision = "20260923_01_dom_sau_models"
down_revision = "20260920_03_dom_fro_models"
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS sau")
    op.create_table("pacientes", Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4), Column("nome", Text, nullable=False), Column("cns", Text, nullable=False, unique=True), Column("cpf", Text), Column("data_nascimento", Text), Column("sexo", Text, nullable=False, server_default="ignorado"), Column("nome_mae", Text), Column("telefone", Text), Column("endereco", Text), Column("ubs_referencia", Text), Column("status", Text, nullable=False, server_default="ativo"), Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()), Column("updated_at", DateTime(timezone=True)), Column("created_by", Text), Column("is_deleted", Boolean, nullable=False, server_default="false"), schema="sau")
    op.create_table("atendimentos", Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4), Column("paciente_id", Text, nullable=False), Column("data", Date), Column("tipo", Text, nullable=False, server_default="consulta"), Column("profissional", Text, nullable=False), Column("estabelecimento", Text, nullable=False), Column("queixa", Text), Column("conduta", Text), Column("cid10", Text), Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()), Column("created_by", Text), schema="sau")
    op.create_table("agendamentos", Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4), Column("paciente_id", Text, nullable=False), Column("especialidade", Text, nullable=False), Column("data", Date), Column("hora", Text), Column("estabelecimento", Text), Column("status", Text, nullable=False, server_default="agendado"), Column("motivo_cancelamento", Text), Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()), Column("updated_at", DateTime(timezone=True)), Column("created_by", Text), schema="sau")
    op.create_table("regulacoes", Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4), Column("paciente_id", Text, nullable=False), Column("procedimento", Text, nullable=False), Column("prioridade", Text, nullable=False, server_default="rotina"), Column("solicitante", Text), Column("data_solicitacao", Date), Column("status", Text, nullable=False, server_default="solicitada"), Column("justificativa", Text), Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()), Column("updated_at", DateTime(timezone=True)), Column("created_by", Text), schema="sau")
    op.create_table("medicamentos", Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4), Column("nome", Text, nullable=False), Column("apresentacao", Text), Column("estoque", Float, nullable=False, server_default="0"), Column("estoque_minimo", Float, nullable=False, server_default="0"), Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()), Column("updated_at", DateTime(timezone=True)), Column("created_by", Text), Column("is_deleted", Boolean, nullable=False, server_default="false"), schema="sau")
    op.create_table("dispensacoes", Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4), Column("paciente_id", Text, nullable=False), Column("medicamento_id", Text, nullable=False), Column("quantidade", Float, nullable=False, server_default="0"), Column("data", Date), Column("receita", Text), Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()), Column("created_by", Text), schema="sau")

def downgrade() -> None:
    op.drop_table("dispensacoes", schema="sau")
    op.drop_table("medicamentos", schema="sau")
    op.drop_table("regulacoes", schema="sau")
    op.drop_table("agendamentos", schema="sau")
    op.drop_table("atendimentos", schema="sau")
    op.drop_table("pacientes", schema="sau")
