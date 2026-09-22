"""IDN: remove coluna legada roles_ids.

Revision ID: 28cda5671e8b
Revises: e03b4a941f40
Create Date: 2026-09-22

A associação entre usuários e roles passou a ter como fonte oficial
a tabela normalizada ``idn.usuario_roles`` na migration
``e03b4a941f40``.

Após a validação da equivalência entre o conteúdo legado e as
associações normalizadas, a coluna ``idn.usuarios.roles_ids`` deixa
de fazer parte do contrato físico de persistência.

A representação ``roles_ids`` permanece no domínio/API do SIGMUN
durante a fase de compatibilidade do contrato de software, sendo
reconstruída pelo repositório a partir de ``idn.usuario_roles``.

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = "28cda5671e8b"
down_revision = "e03b4a941f40"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Remove a coluna física legada após a normalização das relações."""
    op.drop_column(
        "usuarios",
        "roles_ids",
        schema="idn",
    )


def downgrade() -> None:
    """Recria a coluna legada sem restaurar dados históricos.

    A coluna ``roles_ids`` não é mais fonte oficial de persistência.
    O estado autoritativo das associações permanece em
    ``idn.usuario_roles``.

    A recriação da coluna durante downgrade é estrutural apenas; não
    projeta automaticamente as associações normalizadas para o campo
    legado, pois isso poderia confundir uma reversão de schema com
    uma migração de dados e não distinguir associações posteriores
    à migration original.
    """
    op.add_column(
        "usuarios",
        op.Column(
            "roles_ids",
            op.Text(),
            nullable=False,
            server_default="",
        ),
        schema="idn",
    )
    op.alter_column(
        "usuarios",
        "roles_ids",
        server_default=None,
        schema="idn",
    )
