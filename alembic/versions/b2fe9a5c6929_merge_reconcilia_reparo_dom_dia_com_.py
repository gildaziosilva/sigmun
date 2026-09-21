"""merge: reconcilia reparo DOM-DIA com cadeia TRI PAT FRO

Revision ID: b2fe9a5c6929
Revises: 20260920_03_dom_fro_models, 3b584e46028d
Create Date: 2026-09-21 11:19:24.410474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2fe9a5c6929'
down_revision = ('20260920_03_dom_fro_models', '3b584e46028d')
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
