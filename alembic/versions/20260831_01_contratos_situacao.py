"""Adiciona a situação do contrato a ``compras.contratos``.

Corrige omissão da migration 20260820_01: a tabela ``compras.contratos``
não recebeu a coluna ``situacao`` (Text NOT NULL), embora a entidade
``Contrato`` (SituacaoContrato), o repositório SQLAlchemy e as APIs REST
já a utilizassem (RN-COMPRAS-046 – controle de vigência; RN-COMPRAS-106 –
estados terminais).

A coluna recebe ``server_default='EM_ELABORACAO'`` para preencher linhas
existentes e permitir a constraint NOT NULL, seguindo o mesmo padrão das
demais tabelas do domínio (ex.: ``compras.compras.situacao``).

Revision ID: 20260831_01
Revises: 20260823_01
Create Date: 2026-08-31
"""

import sqlalchemy as sa

from alembic import op

revision = "20260831_01"
down_revision = "20260823_01"
branch_labels = None
depends_on = None

_ESTADOS = (
    "EM_ELABORACAO",
    "ASSINADO",
    "VIGENTE",
    "SUSPENSO",
    "ENCERRADO",
    "RESCINDIDO",
    "EXTINTO",
)


def upgrade() -> None:
    op.add_column(
        "contratos",
        sa.Column(
            "situacao",
            sa.Text(),
            nullable=False,
            server_default="EM_ELABORACAO",
        ),
        schema="compras",
    )
    op.create_check_constraint(
        "ck_contratos_situacao",
        "contratos",
        f"situacao IN {tuple(_ESTADOS)}",
        schema="compras",
    )


def downgrade() -> None:
    op.drop_constraint(
        "ck_contratos_situacao",
        "contratos",
        schema="compras",
        type_="check",
    )
    op.drop_column("contratos", "situacao", schema="compras")
