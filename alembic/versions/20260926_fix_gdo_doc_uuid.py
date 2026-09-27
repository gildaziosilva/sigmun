"""Fix GDO documentos UUID columns

Revision ID: 20260926_fix_gdo_doc_uuid
Revises: 20260924_01_dom_edu_models
Create Date: 2026-09-26

Fix unidade_arquivo_id and processo_id columns in gdo.documentos
to be UUID instead of Text.
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = '20260926_fix_gdo_doc_uuid'
down_revision = '20260924_01_dom_edu_models'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Change unidade_arquivo_id from text to UUID
    op.alter_column('documentos', 'unidade_arquivo_id',
                    existing_type=sa.Text(),
                    type_=postgresql.UUID(as_uuid=True),
                    existing_nullable=True,
                    postgresql_using='unidade_arquivo_id::uuid',
                    schema='gdo')

    # Change processo_id from text to UUID
    op.alter_column('documentos', 'processo_id',
                    existing_type=sa.Text(),
                    type_=postgresql.UUID(as_uuid=True),
                    existing_nullable=True,
                    postgresql_using='processo_id::uuid',
                    schema='gdo')


def downgrade() -> None:
    # Revert unidade_arquivo_id from UUID to text
    op.alter_column('documentos', 'unidade_arquivo_id',
                    existing_type=postgresql.UUID(as_uuid=True),
                    type_=sa.Text(),
                    existing_nullable=True,
                    schema='gdo')

    # Revert processo_id from UUID to text
    op.alter_column('documentos', 'processo_id',
                    existing_type=postgresql.UUID(as_uuid=True),
                    type_=sa.Text(),
                    existing_nullable=True,
                    schema='gdo')
