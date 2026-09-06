"""Create GDO reference types (document types) and event outbox tables.

Revision ID: 20260901_03
Revises: 20260901_02
Create Date: 2026-09-01

Tarefa 2: `gdo.tipos_documentais` — tabela de referência para o
`tipo_documental_id` dos documentos (antes texto livre).

Tarefa 3: `gdo.eventos_outbox` — Transactional Outbox (014-Modelo-de-
Integracao): eventos de domínio gravados na mesma transação do negócio e
despachados depois para o barramento (Redis Streams).
"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision = "20260901_03"
down_revision = "20260901_02"
branch_labels = None
depends_on = None


def uuid_column() -> sa.Column:
    return sa.Column(
        "id",
        postgresql.UUID(as_uuid=True),
        primary_key=True,
        server_default=sa.text("gen_random_uuid()"),
    )


def upgrade() -> None:
    # Tabela de referência de tipos documentais
    op.create_table(
        "tipos_documentais",
        uuid_column(),
        sa.Column("codigo", sa.Text(), nullable=False, unique=True),
        sa.Column("nome", sa.Text(), nullable=False),
        sa.Column("descricao", sa.Text()),
        sa.Column("is_ativo", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column("created_by", sa.Text()),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column("updated_by", sa.Text()),
        sa.Column("deleted_at", sa.TIMESTAMP(timezone=True)),
        sa.Column("deleted_by", sa.Text()),
        schema="gdo",
    )
    op.create_index(
        "idx_tipos_documentais_ativo", "tipos_documentais", ["is_ativo"], schema="gdo"
    )

    # Transactional Outbox de eventos de integração (014-Modelo-de-Integracao)
    op.create_table(
        "eventos_outbox",
        uuid_column(),
        sa.Column("topico", sa.Text(), nullable=False),
        sa.Column("evento_nome", sa.Text(), nullable=False),
        sa.Column("agregado_tipo", sa.Text(), nullable=False),
        sa.Column("agregado_id", sa.Text(), nullable=False),
        sa.Column("payload", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("status", sa.Text(), nullable=False, server_default="pendente"),
        sa.Column("tentativas", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("ultimo_erro", sa.Text()),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column("published_at", sa.TIMESTAMP(timezone=True)),
        sa.CheckConstraint(
            "status IN ('pendente', 'publicado', 'erro')",
            name="ck_eventos_outbox_status",
        ),
        schema="gdo",
    )
    op.create_index(
        "idx_outbox_status", "eventos_outbox", ["status"], schema="gdo"
    )
    op.create_index(
        "idx_outbox_topico", "eventos_outbox", ["topico"], schema="gdo"
    )
    op.create_index(
        "idx_outbox_agregado",
        "eventos_outbox",
        ["agregado_tipo", "agregado_id"],
        schema="gdo",
    )
    op.create_index(
        "idx_outbox_created", "eventos_outbox", ["created_at"], schema="gdo"
    )


def downgrade() -> None:
    op.drop_table("eventos_outbox", schema="gdo")
    op.drop_table("tipos_documentais", schema="gdo")
