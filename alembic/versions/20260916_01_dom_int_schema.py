"""Create DOM-INT integration schema and tables.

Revision ID: 20260916_01
Revises: 20260901_05
Create Date: 2026-09-16

Tarefa:
- criar o schema integracao;
- criar as tabelas do DOM-INT;
- materializar as relações entre contratos e APIs externas;
- materializar a relação entre entregas e webhooks;
- preservar a idempotência do processamento de eventos;
- criar os índices necessários às consultas dos repositórios.
"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op


revision = "20260916_01"
down_revision = "20260901_05"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS integracao")

    op.create_table(
        "apis_externas",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("codigo", sa.Text(), nullable=False),
        sa.Column("nome", sa.Text(), nullable=False),
        sa.Column("descricao", sa.Text(), nullable=True),
        sa.Column("provedor", sa.Text(), nullable=True),
        sa.Column("url_base", sa.Text(), nullable=True),
        sa.Column("tipo", sa.Text(), nullable=False, default="rest"),
        sa.Column("autenticacao", sa.Text(), nullable=False, default="oauth2"),
        sa.Column("estado", sa.Text(), nullable=False, default="rascunho"),
        sa.Column("versao", sa.Text(), nullable=False, default="1.0"),
        sa.Column("limite_por_minuto", sa.Integer(), nullable=False, default=300),
        sa.Column("timeout_seg", sa.Integer(), nullable=False, default=30),
        sa.Column(
            "criado_em",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column(
            "atualizado_em",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column("is_deleted", sa.Boolean(), nullable=False, default=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("codigo", name="uq_apis_externas_codigo"),
        schema="integracao",
    )

    op.create_table(
        "contratos_integracao",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("codigo", sa.Text(), nullable=False),
        sa.Column("nome", sa.Text(), nullable=False),
        sa.Column("descricao", sa.Text(), nullable=True),
        sa.Column("versao_formato", sa.Text(), nullable=False, default="1.0"),
        sa.Column("esquema_ref", sa.Text(), nullable=True),
        sa.Column(
            "api_externa_id",
            postgresql.UUID(as_uuid=True),
            nullable=True,
        ),
        sa.Column("estado", sa.Text(), nullable=False, default="rascunho"),
        sa.Column(
            "criado_em",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column(
            "atualizado_em",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column("is_deleted", sa.Boolean(), nullable=False, default=False),
        sa.ForeignKeyConstraint(
            ["api_externa_id"],
            ["integracao.apis_externas.id"],
            name="contratos_integracao_api_externa_id_fkey",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("codigo", name="uq_contratos_integracao_codigo"),
        schema="integracao",
    )

    op.create_index(
        "idx_contratos_integracao_api_externa_id",
        "contratos_integracao",
        ["api_externa_id"],
        schema="integracao",
    )

    op.create_table(
        "conectores",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("codigo", sa.Text(), nullable=False),
        sa.Column("nome", sa.Text(), nullable=False),
        sa.Column("descricao", sa.Text(), nullable=True),
        sa.Column("provedor", sa.Text(), nullable=True),
        sa.Column("url_base", sa.Text(), nullable=True),
        sa.Column(
            "autenticacao_tipo",
            sa.Text(),
            nullable=False,
            default="oauth2",
        ),
        sa.Column(
            "estado",
            sa.Text(),
            nullable=False,
            default="sem_configuracao",
        ),
        sa.Column("config", sa.JSON(), nullable=False, default=dict),
        sa.Column(
            "criado_em",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column(
            "atualizado_em",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column("is_deleted", sa.Boolean(), nullable=False, default=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("codigo", name="uq_conectores_codigo"),
        schema="integracao",
    )

    op.create_table(
        "webhooks",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("nome", sa.Text(), nullable=False),
        sa.Column("url_destino", sa.Text(), nullable=False),
        sa.Column("segredo_ref", sa.Text(), nullable=True),
        sa.Column("topicos", sa.JSON(), nullable=False, default=list),
        sa.Column("cabecalhos", sa.JSON(), nullable=False, default=dict),
        sa.Column("estado", sa.Text(), nullable=False, default="ativa"),
        sa.Column("max_tentativas", sa.Integer(), nullable=False, default=5),
        sa.Column("backoff_base_seg", sa.Integer(), nullable=False, default=60),
        sa.Column(
            "criado_em",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column(
            "atualizado_em",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column("is_deleted", sa.Boolean(), nullable=False, default=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("nome", name="uq_webhooks_nome"),
        schema="integracao",
    )

    op.create_table(
        "entregas_webhook",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("webhook_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("url_destino", sa.Text(), nullable=False),
        sa.Column("cabecalhos", sa.JSON(), nullable=False, default=dict),
        sa.Column("topico", sa.Text(), nullable=False),
        sa.Column("evento_nome", sa.Text(), nullable=False),
        sa.Column("agregado_tipo", sa.Text(), nullable=False),
        sa.Column("agregado_id", sa.Text(), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=False, default=dict),
        sa.Column("estado", sa.Text(), nullable=False, default="pendente"),
        sa.Column("tentativas", sa.Integer(), nullable=False, default=0),
        sa.Column("max_tentativas", sa.Integer(), nullable=False, default=5),
        sa.Column("backoff_base_seg", sa.Integer(), nullable=False, default=60),
        sa.Column("ultimo_http_status", sa.Integer(), nullable=True),
        sa.Column("ultimo_erro", sa.Text(), nullable=True),
        sa.Column(
            "proximo_retry",
            sa.DateTime(timezone=True),
            nullable=True,
        ),
        sa.Column(
            "criado_em",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column(
            "entregue_em",
            sa.DateTime(timezone=True),
            nullable=True,
        ),
        sa.Column(
            "atualizado_em",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column("is_deleted", sa.Boolean(), nullable=False, default=False),
        sa.ForeignKeyConstraint(
            ["webhook_id"],
            ["integracao.webhooks.id"],
            name="entregas_webhook_webhook_id_fkey",
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="integracao",
    )

    op.create_index(
        "idx_entregas_webhook_webhook_id",
        "entregas_webhook",
        ["webhook_id"],
        schema="integracao",
    )

    op.create_table(
        "eventos_processados",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("fonte", sa.Text(), nullable=False),
        sa.Column("evento_outbox_id", sa.Text(), nullable=False),
        sa.Column("topico", sa.Text(), nullable=False),
        sa.Column("evento_nome", sa.Text(), nullable=False),
        sa.Column("agregado_tipo", sa.Text(), nullable=False),
        sa.Column("agregado_id", sa.Text(), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=False, default=dict),
        sa.Column(
            "recebido_em",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column("is_deleted", sa.Boolean(), nullable=False, default=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "fonte",
            "evento_outbox_id",
            name="uq_eventos_processados_fonte_evento",
        ),
        schema="integracao",
    )


def downgrade() -> None:
    op.drop_table("eventos_processados", schema="integracao")

    op.drop_index(
        "idx_entregas_webhook_webhook_id",
        table_name="entregas_webhook",
        schema="integracao",
    )
    op.drop_table("entregas_webhook", schema="integracao")

    op.drop_table("webhooks", schema="integracao")

    op.drop_table("conectores", schema="integracao")

    op.drop_index(
        "idx_contratos_integracao_api_externa_id",
        table_name="contratos_integracao",
        schema="integracao",
    )
    op.drop_table("contratos_integracao", schema="integracao")

    op.drop_table("apis_externas", schema="integracao")

    op.execute("DROP SCHEMA IF EXISTS integracao")
