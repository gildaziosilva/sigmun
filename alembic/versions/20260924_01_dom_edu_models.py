"""Migracao DOM-EDU: educacao publica (schema edu)."""
from __future__ import annotations
import uuid
from alembic import op
from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, Text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
revision = "20260924_01_dom_edu_models"
down_revision = "670428446c32"
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS edu")
    op.create_table("alunos", Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4), Column("nome", Text, nullable=False), Column("cpf", Text), Column("data_nascimento", Text), Column("sexo", Text, nullable=False, server_default="ignorado"), Column("nome_mae", Text), Column("telefone", Text), Column("endereco", Text), Column("status", Text, nullable=False, server_default="ativo"), Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()), Column("updated_at", DateTime(timezone=True)), Column("created_by", Text), Column("is_deleted", Boolean, nullable=False, server_default="false"), schema="edu")
    # RN-EDU-001: CPF unico entre alunos nao excluidos (quando informado).
    op.execute("CREATE UNIQUE INDEX uq_edu_alunos_cpf ON edu.alunos (cpf) WHERE cpf IS NOT NULL AND cpf <> '' AND is_deleted = false")
    op.create_table("matriculas", Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4), Column("aluno_id", Text, nullable=False), Column("escola", Text, nullable=False), Column("serie", Text, nullable=False), Column("turno", Text, nullable=False, server_default="manha"), Column("ano_letivo", Integer, nullable=False, server_default="0"), Column("data_matricula", Date), Column("status", Text, nullable=False, server_default="ativa"), Column("escola_destino", Text), Column("motivo", Text), Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()), Column("updated_at", DateTime(timezone=True)), Column("created_by", Text), schema="edu")
    # RN-EDU-010: uma unica matricula ativa por aluno.
    op.execute("CREATE UNIQUE INDEX uq_edu_matriculas_ativa ON edu.matriculas (aluno_id) WHERE status = 'ativa'")
    op.create_table("lancamentos_diario", Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4), Column("matricula_id", Text, nullable=False), Column("data", Date), Column("presente", Boolean, nullable=False, server_default="true"), Column("nota", Float), Column("observacao", Text), Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()), Column("created_by", Text), schema="edu")
    op.create_table("rotas_transporte", Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4), Column("identificacao", Text, nullable=False), Column("veiculo", Text), Column("motorista", Text, nullable=False), Column("vagas", Integer, nullable=False, server_default="0"), Column("turno", Text, nullable=False, server_default="manha"), Column("status", Text, nullable=False, server_default="ativa"), Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()), Column("updated_at", DateTime(timezone=True)), Column("created_by", Text), schema="edu")
    op.create_table("passagens_transporte", Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4), Column("rota_id", Text, nullable=False), Column("matricula_id", Text, nullable=False), Column("data", Date), Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()), Column("created_by", Text), schema="edu")
    op.create_table("itens_merenda", Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4), Column("nome", Text, nullable=False), Column("tipo", Text, nullable=False, server_default="refeicao"), Column("estoque", Float, nullable=False, server_default="0"), Column("estoque_minimo", Float, nullable=False, server_default="0"), Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()), Column("updated_at", DateTime(timezone=True)), Column("created_by", Text), Column("is_deleted", Boolean, nullable=False, server_default="false"), schema="edu")
    op.create_table("distribuicoes_merenda", Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4), Column("matricula_id", Text, nullable=False), Column("item_id", Text, nullable=False), Column("quantidade", Float, nullable=False, server_default="0"), Column("data", Date), Column("refeicao", Text, nullable=False, server_default="almoco"), Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()), Column("created_by", Text), schema="edu")

def downgrade() -> None:
    op.drop_table("distribuicoes_merenda", schema="edu")
    op.drop_table("itens_merenda", schema="edu")
    op.drop_table("passagens_transporte", schema="edu")
    op.drop_table("rotas_transporte", schema="edu")
    op.drop_table("lancamentos_diario", schema="edu")
    op.drop_table("matriculas", schema="edu")
    op.drop_table("alunos", schema="edu")
    op.execute("DROP SCHEMA IF EXISTS edu")
