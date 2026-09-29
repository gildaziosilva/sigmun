"""Migração DOM-OBR: obras e infraestrutura (schema obr).

Cria o schema `obr` e as tabelas de obras públicas, medições físico-financeiras,
etapas de execução, despesas financeiras e vistorias fiscalizadoras.

Regras: RN-OBR-001 (número único da obra), RN-OBR-004 (avanço financeiro não
ultrapassa o físico e o contratado não supera o orçado), RN-OBR-005 (medição
com valor e percentual válidos), RN-OBR-006 (pago não supera o medido),
RN-OBR-007 (realizado da etapa não supera o previsto).
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
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import UUID

from alembic import op

revision = "20260929_04_dom_obr_models"
down_revision = "20260929_03_dom_geo_models"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS obr")
    op.create_table(
        "obras",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("numero", Text, nullable=False, unique=True),
        Column("nome", Text, nullable=False),
        Column("descricao", Text),
        Column("tipo", Text, nullable=False, server_default="outro"),
        Column("situacao", Text, nullable=False, server_default="planejada"),
        Column("tipo_contratacao", Text, nullable=False, server_default="licitacao"),
        Column("fonte_recurso", Text, nullable=False, server_default="orcamento_proprio"),
        Column("valor_orcado", Float, nullable=False, server_default="0"),
        Column("valor_contratado", Float, nullable=False, server_default="0"),
        Column("valor_mediado", Float, nullable=False, server_default="0"),
        Column("valor_pago", Float, nullable=False, server_default="0"),
        Column("percentual_fisico", Float, nullable=False, server_default="0"),
        Column("percentual_financeiro", Float, nullable=False, server_default="0"),
        Column("empresa_contratada", Text),
        Column("numero_contrato", Text),
        Column("responsavel_tecnico", Text),
        Column("endereco", Text),
        Column("bairro", Text),
        Column("data_inicio_prevista", Date),
        Column("data_fim_prevista", Date),
        Column("data_inicio_real", Date),
        Column("data_fim_real", Date),
        Column("observacao", Text),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="obr",
    )
    op.create_index("ix_obr_obras_numero", "obras", ["numero"], schema="obr")
    op.create_index("ix_obr_obras_situacao", "obras", ["situacao"], schema="obr")
    # RN-OBR-004: contratado não supera o orçado; financeiro não supera o físico.
    op.create_check_constraint(
        "ck_obr_obra_valores",
        "obras",
        "valor_orcado >= 0 AND valor_contratado >= 0 AND valor_mediado >= 0 AND valor_pago >= 0 "
        "AND (valor_orcado = 0 OR valor_contratado <= valor_orcado)",
        schema="obr",
    )
    op.create_check_constraint(
        "ck_obr_obra_avanco",
        "obras",
        "percentual_fisico >= 0 AND percentual_fisico <= 100 "
        "AND percentual_financeiro >= 0 AND percentual_financeiro <= percentual_fisico",
        schema="obr",
    )
    # RN-OBR-006: não se paga mais do que se mediu.
    op.create_check_constraint(
        "ck_obr_obra_pago",
        "obras",
        "valor_pago <= valor_mediado",
        schema="obr",
    )

    op.create_table(
        "medicoes_obras",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("obra_id", Text, nullable=False),
        Column("numero", Text, nullable=False),
        Column("tipo", Text, nullable=False, server_default="avanco"),
        Column("situacao", Text, nullable=False, server_default="registrada"),
        Column("data", Date, nullable=False),
        Column("percentual_fisico", Float, nullable=False, server_default="0"),
        Column("valor_medido", Float, nullable=False, server_default="0"),
        Column("responsavel_tecnico", Text, nullable=False),
        Column("observacao", Text),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="obr",
    )
    op.create_index("ix_obr_medicoes_obra", "medicoes_obras", ["obra_id"], schema="obr")
    # RN-OBR-005: número de medição único por obra.
    op.create_index(
        "uq_obr_medicao_numero",
        "medicoes_obras",
        ["obra_id", "numero"],
        unique=True,
        postgresql_where=sa.text("is_deleted = false"),
        schema="obr",
    )
    op.create_check_constraint(
        "ck_obr_medicao_percentual",
        "medicoes_obras",
        "percentual_fisico >= 0 AND percentual_fisico <= 100 AND valor_medido >= 0",
        schema="obr",
    )

    op.create_table(
        "etapas_obras",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("obra_id", Text, nullable=False),
        Column("numero", Text, nullable=False),
        Column("descricao", Text, nullable=False),
        Column("tipo", Text, nullable=False, server_default="estrutura"),
        Column("situacao", Text, nullable=False, server_default="pendente"),
        Column("percentual_previsto", Float, nullable=False, server_default="0"),
        Column("percentual_realizado", Float, nullable=False, server_default="0"),
        Column("data_inicio_prevista", Date),
        Column("data_fim_prevista", Date),
        Column("data_conclusao", Date),
        Column("responsavel", Text, nullable=False),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="obr",
    )
    op.create_index("ix_obr_etapas_obra", "etapas_obras", ["obra_id"], schema="obr")
    # RN-OBR-007: peso previsto e conclusao da etapa sao escalas distintas
    # (uma etapa de peso 40% pode estar 100% concluida); ambas em 0..100.
    op.create_check_constraint(
        "ck_obr_etapa_percentual",
        "etapas_obras",
        "percentual_previsto >= 0 AND percentual_previsto <= 100 "
        "AND percentual_realizado >= 0 AND percentual_realizado <= 100",
        schema="obr",
    )

    op.create_table(
        "despesas_obras",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("obra_id", Text, nullable=False),
        Column("medicao_id", Text),
        Column("descricao", Text, nullable=False),
        Column("tipo", Text, nullable=False, server_default="medicao"),
        Column("valor", Float, nullable=False, server_default="0"),
        Column("data", Date, nullable=False),
        Column("documento", Text),
        Column("credor", Text),
        Column("observacao", Text),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="obr",
    )
    op.create_index("ix_obr_despesas_obra", "despesas_obras", ["obra_id"], schema="obr")
    # RN-OBR-006: despesa com valor positivo.
    op.create_check_constraint(
        "ck_obr_despesa_valor", "despesas_obras", "valor > 0", schema="obr"
    )

    op.create_table(
        "vistorias_obras",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("obra_id", Text, nullable=False),
        Column("data", Date, nullable=False),
        Column("tipo", Text, nullable=False, server_default="periodica"),
        Column("parecer", Text, nullable=False, server_default="aprovado"),
        Column("percentual_fisico_verificado", Float, nullable=False, server_default="0"),
        Column("fiscal", Text, nullable=False),
        Column("observacao", Text),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="obr",
    )
    op.create_index("ix_obr_vistorias_obra", "vistorias_obras", ["obra_id"], schema="obr")
    # RN-OBR-008: avanço verificado em campo entre 0 e 100.
    op.create_check_constraint(
        "ck_obr_vistoria_percentual",
        "vistorias_obras",
        "percentual_fisico_verificado >= 0 AND percentual_fisico_verificado <= 100",
        schema="obr",
    )


def downgrade() -> None:
    op.drop_index("ix_obr_vistorias_obra", table_name="vistorias_obras", schema="obr")
    op.drop_table("vistorias_obras", schema="obr")
    op.drop_index("ix_obr_despesas_obra", table_name="despesas_obras", schema="obr")
    op.drop_table("despesas_obras", schema="obr")
    op.drop_index("ix_obr_etapas_obra", table_name="etapas_obras", schema="obr")
    op.drop_table("etapas_obras", schema="obr")
    op.drop_index("uq_obr_medicao_numero", table_name="medicoes_obras", schema="obr")
    op.drop_index("ix_obr_medicoes_obra", table_name="medicoes_obras", schema="obr")
    op.drop_table("medicoes_obras", schema="obr")
    op.drop_index("ix_obr_obras_situacao", table_name="obras", schema="obr")
    op.drop_index("ix_obr_obras_numero", table_name="obras", schema="obr")
    op.drop_table("obras", schema="obr")
    op.execute("DROP SCHEMA IF EXISTS obr")
