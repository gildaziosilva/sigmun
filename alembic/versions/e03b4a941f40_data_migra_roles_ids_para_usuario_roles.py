"""data: migra roles_ids para usuario_roles

Revision ID: e03b4a941f40
Revises: b2fe9a5c6929
Create Date: 2026-09-22

Migra as associações de roles mantidas no campo legado
idn.usuarios.roles_ids para a tabela normalizada
idn.usuario_roles.

A coluna roles_ids é preservada nesta etapa por compatibilidade
transitória. A migration é idempotente: associações já existentes
não são duplicadas.

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e03b4a941f40"
down_revision = "b2fe9a5c6929"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Materializa as relações legadas na tabela N:N normalizada."""
    connection = op.get_bind()

    connection.execute(
        sa.text(
            """
            INSERT INTO idn.usuario_roles (
                id,
                usuario_id,
                role_id,
                created_at,
                created_by
            )
            SELECT
                gen_random_uuid(),
                u.id,
                r.id,
                NOW(),
                NULL
            FROM idn.usuarios AS u
            CROSS JOIN LATERAL unnest(
                string_to_array(
                    NULLIF(BTRIM(u.roles_ids), ''),
                    ','
                )
            ) AS legado(role_id_text)
            JOIN idn.roles AS r
              ON r.id = BTRIM(legado.role_id_text)::uuid
            WHERE NULLIF(BTRIM(u.roles_ids), '') IS NOT NULL
              AND NOT EXISTS (
                  SELECT 1
                  FROM idn.usuario_roles AS ur
                  WHERE ur.usuario_id = u.id
                    AND ur.role_id = r.id
              )
            """
        )
    )


def downgrade() -> None:
    """Não remove associações normalizadas criadas ou alteradas após a migração.

    A reversão é deliberadamente conservadora. A migration não mantém
    metadado suficiente para distinguir, de forma segura, associações
    originalmente migradas de associações posteriormente criadas pela
    aplicação.
    """
    pass
