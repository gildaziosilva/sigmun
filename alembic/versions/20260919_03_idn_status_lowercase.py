"""Align DOM-IDN user status constraint with domain enum values.

Revision ID: 20260919_03
Revises: 20260919_02_dom_pes_folha
Create Date: 2026-09-19

Contexto:
A migration original do DOM-IDN criou a constraint
ck_usuarios_status com valores em caixa alta:

    ATIVO
    INATIVO
    BLOQUEADO
    PENDENTE

O domínio UsuarioStatus utiliza valores em caixa baixa:

    ativo
    inativo
    bloqueado
    pendente

O repositório persiste diretamente UsuarioStatus.value.
Esta migration corrige exclusivamente o contrato persistente,
sem alterar o histórico da migration original.

A tabela idn.usuarios encontra-se sem registros no momento
da correção, portanto não há necessidade de conversão de dados.
"""

import sqlalchemy as sa

from alembic import op


revision = "20260919_03"
down_revision = "20260919_02_dom_pes_folha"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_constraint(
        "ck_usuarios_status",
        "usuarios",
        schema="idn",
        type_="check",
    )

    op.create_check_constraint(
        "ck_usuarios_status",
        "usuarios",
        "status IN ('ativo', 'inativo', 'bloqueado', 'pendente')",
        schema="idn",
    )


def downgrade() -> None:
    op.drop_constraint(
        "ck_usuarios_status",
        "usuarios",
        schema="idn",
        type_="check",
    )

    op.create_check_constraint(
        "ck_usuarios_status",
        "usuarios",
        "status IN ('ATIVO', 'INATIVO', 'BLOQUEADO', 'PENDENTE')",
        schema="idn",
    )
