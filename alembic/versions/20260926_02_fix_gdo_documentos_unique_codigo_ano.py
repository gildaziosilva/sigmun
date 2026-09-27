"""Fix GDO documentos unique constraint on codigo + ano

Revision ID: 20260926_fix_gdo_doc_unique
Revises: 20260926_fix_gdo_doc_uuid
Create Date: 2026-09-26

Add unique constraint on (codigo, ano) for gdo.documentos
"""

from alembic import op

revision = '20260926_fix_gdo_doc_unique'
down_revision = '20260926_fix_gdo_doc_uuid'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Drop the existing unique constraint on codigo
    op.drop_constraint('documentos_codigo_key', 'documentos', schema='gdo', type_='unique')

    # Add unique constraint on (codigo, ano)
    op.create_unique_constraint(
        'uq_documentos_codigo_ano',
        'documentos',
        ['codigo', 'ano'],
        schema='gdo'
    )


def downgrade() -> None:
    # Drop the unique constraint on (codigo, ano)
    op.drop_constraint('uq_documentos_codigo_ano', 'documentos', schema='gdo', type_='unique')

    # Recreate unique constraint on codigo
    op.create_unique_constraint(
        'documentos_codigo_key',
        'documentos',
        ['codigo'],
        schema='gdo'
    )
