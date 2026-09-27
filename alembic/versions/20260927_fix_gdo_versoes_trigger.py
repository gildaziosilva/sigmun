"""Remove trigger updated_at incompatível de versões de documentos.

Revision ID: 20260927_fix_gdo_versoes_trigger
Revises: 20260926_fix_gdo_doc_unique
Create Date: 2026-09-27

A tabela gdo.versoes_documentos representa versões imutáveis de documentos
(RN-GDO-005) e não possui a coluna updated_at.

A migration fundacional 20260901_02_gdo_documentos_tramitacoes_processos.py
aplicou indevidamente o trigger genérico de updated_at à tabela. A função
core.fn_update_timestamp() tenta atribuir NEW.updated_at, o que é
incompatível com a estrutura física da tabela.

Esta migration corrige somente o trigger, preservando a estrutura da tabela.
"""

from alembic import op


revision = "20260927_fix_gdo_versoes_trigger"
down_revision = "20260926_fix_gdo_doc_unique"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Remove o trigger updated_at incompatível."""
    op.execute(
        """
        DROP TRIGGER IF EXISTS trg_versoes_documentos_updated_at
        ON gdo.versoes_documentos
        """
    )


def downgrade() -> None:
    """Restaura o estado anterior à migration corretiva."""
    op.execute(
        """
        CREATE TRIGGER trg_versoes_documentos_updated_at
        BEFORE UPDATE ON gdo.versoes_documentos
        FOR EACH ROW
        EXECUTE FUNCTION core.fn_update_timestamp()
        """
    )
