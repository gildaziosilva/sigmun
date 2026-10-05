"""merge: reconcilia DOM-OBR com a cadeia DOM-OUV

Une as duas cabeças remanescentes da cadeia de migrations:

- ``20260929_04_dom_obr_models`` — modelos de Obras e Infraestrutura;
- ``20261002_01`` — modelos de Ouvidoria (DOM-OUV).

Sem esta revision, ``alembic upgrade head`` falha com
``Multiple head revisions are present``, impedindo a implantacao de
ambientes novos (achado C6 da auditoria DOM-OUV de 2026-10-03).

A migration e apenas estrutural: nao altera o schema, pois as duas
ramificacoes ja foram aplicadas.

Revision ID: c6ouv001merge01
Revises: 20260929_04_dom_obr_models, 20261002_01
Create Date: 2026-10-03
"""

# revision identifiers, used by Alembic.
revision = "c6ouv001merge01"
down_revision = ("20260929_04_dom_obr_models", "20261002_01")
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Une as ramificacoes. Nenhuma alteracao de schema e necessaria."""
    pass


def downgrade() -> None:
    """Desfaz o merge. As duas ramificacoes permanecem aplicadas."""
    pass