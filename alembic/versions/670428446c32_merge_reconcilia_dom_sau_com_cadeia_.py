"""merge: reconcilia DOM-SAU com cadeia principal

Revision ID: 670428446c32
Revises: 20260923_01_dom_sau_models, 28cda5671e8b
Create Date: 2026-09-24 07:01:40.361924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '670428446c32'
down_revision = ('20260923_01_dom_sau_models', '28cda5671e8b')
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
