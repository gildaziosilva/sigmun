"""Create document management (GDO) tables.

Revision ID: 20260901_02
Revises: 20260901_01
Create Date: 2026-09-01

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision = "20260901_02"
down_revision = "20260901_01"
branch_labels = None
depends_on = None


def uuid_column() -> sa.Column:
    return sa.Column(
        "id",
        postgresql.UUID(as_uuid=True),
        primary_key=True,
        server_default=sa.text("gen_random_uuid()"),
    )


def ts_column(name: str, nullable: bool = True) -> sa.Column:
    """Coluna de timestamp; não-nuláveis recebem default NOW() no banco."""
    if nullable:
        return sa.Column(name, sa.TIMESTAMP(timezone=True), nullable=True)
    return sa.Column(
        name,
        sa.TIMESTAMP(timezone=True),
        nullable=False,
        server_default=sa.func.now(),
    )


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS gdo")

    # Tabela de processos documentais
    op.create_table(
        "processos_documentos",
        uuid_column(),
        sa.Column("numero", sa.Text(), nullable=False),
        sa.Column("ano", sa.Integer(), nullable=False),
        sa.Column("tipo_processo_id", sa.Text(), nullable=False),
        sa.Column("titulo", sa.Text(), nullable=False),
        sa.Column("descricao", sa.Text()),
        sa.Column("unidade_autor_id", sa.Text(), nullable=False),
        ts_column("data_abertura", nullable=False),
        ts_column("data_encerramento"),
        sa.Column("status", sa.Text(), nullable=False, server_default="aberto"),
        sa.Column("created_by", sa.Text()),
        ts_column("created_at", nullable=False),
        ts_column("updated_at", nullable=False),
        ts_column("deleted_at"),
        sa.Column("deleted_by", sa.Text()),
        sa.CheckConstraint("status IN ('aberto', 'encerrado')", name="ck_processos_status"),
        schema="gdo",
    )
    op.create_index(
        "idx_processos_numero_ano", "processos_documentos", ["numero", "ano"], schema="gdo"
    )
    op.create_index("idx_processos_status", "processos_documentos", ["status"], schema="gdo")
    op.create_index(
        "idx_processos_unidade_autor", "processos_documentos", ["unidade_autor_id"], schema="gdo"
    )

    # Tabela de classificações documentais (plano de classificação)
    op.create_table(
        "classificacoes_documentais",
        uuid_column(),
        sa.Column("codigo", sa.Text(), nullable=False, unique=True),
        sa.Column("nome", sa.Text(), nullable=False),
        sa.Column("descricao", sa.Text()),
        sa.Column("nivel", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("classificacao_pai_id", sa.Text()),
        sa.Column("prazo_retencao", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("unidade_destino_id", sa.Text()),
        ts_column("created_at", nullable=False),
        sa.Column("created_by", sa.Text()),
        ts_column("updated_at", nullable=False),
        sa.Column("updated_by", sa.Text()),
        ts_column("deleted_at"),
        sa.Column("deleted_by", sa.Text()),
        schema="gdo",
    )
    op.create_index(
        "idx_classificacoes_pai",
        "classificacoes_documentais",
        ["classificacao_pai_id"],
        schema="gdo",
    )

    # Tabela de tabelas de temporalidade
    op.create_table(
        "tabelas_temporalidades",
        uuid_column(),
        sa.Column("codigo", sa.Text(), nullable=False, unique=True),
        sa.Column("nome", sa.Text(), nullable=False),
        sa.Column("prazo_tempo", sa.Integer(), nullable=False),
        sa.Column("unidade_tempo", sa.Text(), nullable=False, server_default="meses"),
        sa.Column("evento_fim", sa.Text(), nullable=False),
        sa.Column("tipo_destinacao", sa.Text(), nullable=False, server_default="eliminacao"),
        sa.Column("is_ativo", sa.Boolean(), nullable=False, server_default=sa.true()),
        ts_column("created_at", nullable=False),
        sa.Column("created_by", sa.Text()),
        ts_column("updated_at", nullable=False),
        sa.Column("updated_by", sa.Text()),
        ts_column("deleted_at"),
        sa.Column("deleted_by", sa.Text()),
        sa.CheckConstraint(
            "tipo_destinacao IN ('eliminacao', 'guarda_permanente', 'prorrogacao')",
            name="ck_temporalidades_tipo_destinacao",
        ),
        sa.CheckConstraint(
            "unidade_tempo IN ('dias', 'meses', 'anos')",
            name="ck_temporalidades_unidade_tempo",
        ),
        schema="gdo",
    )

    # Tabela principal de documentos
    op.create_table(
        "documentos",
        uuid_column(),
        sa.Column("codigo", sa.Text(), nullable=False, unique=True),
        sa.Column("numero", sa.Text(), nullable=False),
        sa.Column("ano", sa.Integer(), nullable=False),
        sa.Column("tipo_documental_id", sa.Text(), nullable=False),
        sa.Column("titulo", sa.Text(), nullable=False),
        sa.Column("descricao", sa.Text()),
        ts_column("data_criacao"),
        ts_column("data_recebimento"),
        ts_column("data_arquivamento"),
        ts_column("data_encerramento"),
        ts_column("data_eliminacao"),
        sa.Column("unidade_autor_id", sa.Text(), nullable=False),
        sa.Column("unidade_arquivo_id", sa.Text()),
        sa.Column("processo_id", sa.Text()),
        sa.Column("status", sa.Text(), nullable=False, server_default="rascunho"),
        sa.Column("is_sigiloso", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("conteudo_ref", sa.Text()),
        sa.Column("hash_integridade", sa.Text()),
        ts_column("created_at", nullable=False),
        sa.Column("created_by", sa.Text()),
        ts_column("updated_at", nullable=False),
        sa.Column("updated_by", sa.Text()),
        ts_column("deleted_at"),
        sa.Column("deleted_by", sa.Text()),
        sa.CheckConstraint(
            "status IN ('rascunho', 'ativo', 'arquivado', 'encerrado', 'rejeitado')",
            name="ck_documentos_status",
        ),
        schema="gdo",
    )
    op.create_index("idx_documentos_status", "documentos", ["status"], schema="gdo")
    op.create_index("idx_documentos_ano", "documentos", ["ano"], schema="gdo")
    op.create_index("idx_documentos_processo", "documentos", ["processo_id"], schema="gdo")
    op.create_index(
        "idx_documentos_unidade_autor", "documentos", ["unidade_autor_id"], schema="gdo"
    )
    op.create_index(
        "idx_documentos_tipo_documental", "documentos", ["tipo_documental_id"], schema="gdo"
    )

    # Tabela de versões imutáveis de documentos (RN-GDO-005)
    op.create_table(
        "versoes_documentos",
        uuid_column(),
        sa.Column("documento_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("numero_versao", sa.Integer(), nullable=False),
        sa.Column("conteudo_ref", sa.Text()),
        sa.Column("hash_integridade", sa.Text()),
        ts_column("data_versao", nullable=False),
        sa.Column("created_by", sa.Text()),
        ts_column("deleted_at"),
        sa.Column("deleted_by", sa.Text()),
        sa.ForeignKeyConstraint(
            ["documento_id"], ["gdo.documentos.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        sa.UniqueConstraint("documento_id", "numero_versao", name="uq_versoes_doc_numero"),
        schema="gdo",
    )
    op.create_index(
        "idx_versoes_documento", "versoes_documentos", ["documento_id"], schema="gdo"
    )

    # Tabela de tramitações de documentos
    op.create_table(
        "tramitacoes_documentos",
        uuid_column(),
        sa.Column("documento_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("unidade_origem_id", sa.Text(), nullable=False),
        sa.Column("unidade_destino_id", sa.Text(), nullable=False),
        sa.Column("tipo", sa.Text(), nullable=False, server_default="envio"),
        ts_column("data_envio"),
        ts_column("data_recebimento"),
        ts_column("data_devolucao"),
        sa.Column("motivo", sa.Text()),
        sa.Column("observacao", sa.Text()),
        sa.Column("created_by", sa.Text()),
        ts_column("created_at", nullable=False),
        ts_column("updated_at", nullable=False),
        sa.ForeignKeyConstraint(
            ["documento_id"], ["gdo.documentos.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        sa.CheckConstraint(
            "tipo IN ('envio', 'recepcao', 'devolvido', 'arquivamento', 'restauracao')",
            name="ck_tramitacoes_tipo",
        ),
        schema="gdo",
    )
    op.create_index(
        "idx_tramitacoes_documento", "tramitacoes_documentos", ["documento_id"], schema="gdo"
    )
    op.create_index(
        "idx_tramitacoes_destino", "tramitacoes_documentos", ["unidade_destino_id"], schema="gdo"
    )

    # Tabela de arquivamentos de documentos
    op.create_table(
        "arquivamentos_documentos",
        uuid_column(),
        sa.Column("documento_id", postgresql.UUID(as_uuid=True), nullable=False),
        ts_column("data_arquivamento", nullable=False),
        ts_column("data_restauracao"),
        sa.Column("created_by", sa.Text()),
        sa.Column("observacao", sa.Text()),
        sa.ForeignKeyConstraint(
            ["documento_id"], ["gdo.documentos.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        schema="gdo",
    )
    op.create_index(
        "idx_arquivamentos_documento", "arquivamentos_documentos", ["documento_id"], schema="gdo"
    )

    # Tabela de assinaturas digitais de documentos
    op.create_table(
        "assinaturas_documentos",
        uuid_column(),
        sa.Column("documento_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("signatario_id", sa.Text(), nullable=False),
        ts_column("data_assinatura", nullable=False),
        sa.Column("hash_assinatura", sa.Text(), nullable=False),
        sa.Column("certificado_id", sa.Text()),
        sa.Column("is_valida", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("is_revogada", sa.Boolean(), nullable=False, server_default=sa.false()),
        ts_column("created_at", nullable=False),
        sa.ForeignKeyConstraint(
            ["documento_id"], ["gdo.documentos.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        schema="gdo",
    )
    op.create_index(
        "idx_assinaturas_documento", "assinaturas_documentos", ["documento_id"], schema="gdo"
    )
    op.create_index(
        "idx_assinaturas_signatario", "assinaturas_documentos", ["signatario_id"], schema="gdo"
    )

    # Tabela de metadados de documentos
    op.create_table(
        "metadados_documentos",
        uuid_column(),
        sa.Column("documento_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("metadado_id", sa.Text(), nullable=False),
        sa.Column("valor", sa.Text(), nullable=False),
        ts_column("created_at", nullable=False),
        sa.ForeignKeyConstraint(
            ["documento_id"], ["gdo.documentos.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        schema="gdo",
    )
    op.create_index(
        "idx_metadados_doc_documento", "metadados_documentos", ["documento_id"], schema="gdo"
    )
    op.create_index(
        "idx_metadados_doc_metadado", "metadados_documentos", ["metadado_id"], schema="gdo"
    )

    # Triggers de atualização de timestamp
    tabelas = (
        "processos_documentos",
        "classificacoes_documentais",
        "tabelas_temporalidades",
        "documentos",
        "versoes_documentos",
        "tramitacoes_documentos",
        "arquivamentos_documentos",
        "assinaturas_documentos",
        "metadados_documentos",
    )
    for table in tabelas:
        op.execute(
            f"CREATE TRIGGER trg_{table}_updated_at "
            f"BEFORE UPDATE ON gdo.{table} "
            "FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp()"
        )


def downgrade() -> None:
    tabelas = (
        "metadados_documentos",
        "assinaturas_documentos",
        "arquivamentos_documentos",
        "tramitacoes_documentos",
        "versoes_documentos",
        "documentos",
        "tabelas_temporalidades",
        "classificacoes_documentais",
        "processos_documentos",
    )
    for table in tabelas:
        op.execute(f"DROP TRIGGER IF EXISTS trg_{table}_updated_at ON gdo.{table}")
    op.drop_table("metadados_documentos", schema="gdo")
    op.drop_table("assinaturas_documentos", schema="gdo")
    op.drop_table("arquivamentos_documentos", schema="gdo")
    op.drop_table("tramitacoes_documentos", schema="gdo")
    op.drop_table("versoes_documentos", schema="gdo")
    op.drop_table("documentos", schema="gdo")
    op.drop_table("tabelas_temporalidades", schema="gdo")
    op.drop_table("classificacoes_documentais", schema="gdo")
    op.drop_table("processos_documentos", schema="gdo")
    op.execute("DROP SCHEMA IF EXISTS gdo")


