"""Add ATE (Atendimento ao Cidadão) models.

Revision ID: 20261002_01_ate_models
Revises: 20260929_01_dom_tel_models
Create Date: 2026-10-02
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '20261002_01_ate_models'
down_revision = '20260929_01_dom_tel_models'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create schema
    op.execute('CREATE SCHEMA IF NOT EXISTS ate')

    # servicos_atendimento
    op.create_table(
        'servicos_atendimento',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('codigo', sa.Text(), nullable=False, unique=True),
        sa.Column('nome', sa.Text(), nullable=False),
        sa.Column('prioridade', sa.Integer(), nullable=False, default=0),
        sa.Column('ativo', sa.Boolean(), nullable=False, default=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('created_by', sa.Text(), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_by', sa.Text(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deleted_by', sa.Text(), nullable=True),
        schema='ate',
    )

    # canais_atendimento
    op.create_table(
        'canais_atendimento',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('codigo', sa.Text(), nullable=False, unique=True),
        sa.Column('nome', sa.Text(), nullable=False),
        sa.Column('tipo', sa.Text(), nullable=False),
        sa.Column('ativo', sa.Boolean(), nullable=False, default=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('created_by', sa.Text(), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_by', sa.Text(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deleted_by', sa.Text(), nullable=True),
        schema='ate',
    )

    # unidades_atendimento
    op.create_table(
        'unidades_atendimento',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('codigo', sa.Text(), nullable=False, unique=True),
        sa.Column('nome', sa.Text(), nullable=False),
        sa.Column('ativo', sa.Boolean(), nullable=False, default=True),
        sa.Column('max_rechamadas', sa.Integer(), nullable=False, default=3),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('created_by', sa.Text(), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_by', sa.Text(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deleted_by', sa.Text(), nullable=True),
        schema='ate',
    )

    # guiches
    op.create_table(
        'guiches',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('unidade_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('numero', sa.Text(), nullable=False),
        sa.Column('descricao', sa.Text(), nullable=True),
        sa.Column('ativo', sa.Boolean(), nullable=False, default=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('created_by', sa.Text(), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_by', sa.Text(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deleted_by', sa.Text(), nullable=True),
        schema='ate',
    )

    # filas_atendimento
    op.create_table(
        'filas_atendimento',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('unidade_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('servico_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('data', sa.DateTime(timezone=True), nullable=False),
        sa.Column('status', sa.Text(), nullable=False, default='aberta'),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('created_by', sa.Text(), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_by', sa.Text(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deleted_by', sa.Text(), nullable=True),
        schema='ate',
    )

    # triagens
    op.create_table(
        'triagens',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('servico_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('data_hora', sa.DateTime(timezone=True), nullable=False),
        sa.Column('classificacao', sa.Text(), nullable=False),
        sa.Column('prioridade', sa.Integer(), nullable=False, default=0),
        sa.Column('observacao', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('created_by', sa.Text(), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_by', sa.Text(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deleted_by', sa.Text(), nullable=True),
        schema='ate',
    )

    # senhas
    op.create_table(
        'senhas',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('fila_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('servico_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('triagem_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('numero', sa.Text(), nullable=False),
        sa.Column('data_hora_emissao', sa.DateTime(timezone=True), nullable=False),
        sa.Column('prioridade', sa.Integer(), nullable=False, default=0),
        sa.Column('status', sa.Text(), nullable=False, default='emitida'),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('created_by', sa.Text(), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_by', sa.Text(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deleted_by', sa.Text(), nullable=True),
        schema='ate',
    )

    # chamadas
    op.create_table(
        'chamadas',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('senha_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('guiche_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('unidade_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('operador', sa.Text(), nullable=False),
        sa.Column('data_hora', sa.DateTime(timezone=True), nullable=False),
        sa.Column('ordem', sa.Integer(), nullable=False),
        sa.Column('tentativa', sa.Integer(), nullable=False, default=1),
        sa.Column('resultado', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('created_by', sa.Text(), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_by', sa.Text(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deleted_by', sa.Text(), nullable=True),
        schema='ate',
    )

    # atendimentos
    op.create_table(
        'atendimentos',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('chamada_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('canal_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('inicio', sa.DateTime(timezone=True), nullable=True),
        sa.Column('fim', sa.DateTime(timezone=True), nullable=True),
        sa.Column('status', sa.Text(), nullable=False, default='aguardando'),
        sa.Column('descricao', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('created_by', sa.Text(), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_by', sa.Text(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deleted_by', sa.Text(), nullable=True),
        schema='ate',
    )

    # avaliacoes_atendimento
    op.create_table(
        'avaliacoes_atendimento',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('atendimento_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('nota', sa.Integer(), nullable=False),
        sa.Column('comentario', sa.Text(), nullable=True),
        sa.Column('data_hora', sa.DateTime(timezone=True), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('created_by', sa.Text(), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_by', sa.Text(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deleted_by', sa.Text(), nullable=True),
        schema='ate',
    )

    # encaminhamentos
    op.create_table(
        'encaminhamentos',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('atendimento_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('data_hora', sa.DateTime(timezone=True), nullable=False),
        sa.Column('destino', sa.Text(), nullable=False),
        sa.Column('motivo', sa.Text(), nullable=False),
        sa.Column('status', sa.Text(), nullable=False, default='pendente'),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('created_by', sa.Text(), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_by', sa.Text(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deleted_by', sa.Text(), nullable=True),
        schema='ate',
    )

    # eventos_outbox
    op.create_table(
        'eventos_outbox',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('topico', sa.Text(), nullable=False),
        sa.Column('evento_nome', sa.Text(), nullable=False),
        sa.Column('agregado_tipo', sa.Text(), nullable=False),
        sa.Column('agregado_id', sa.Text(), nullable=False),
        sa.Column('payload', postgresql.JSON(astext_type=sa.Text()), nullable=False),
        sa.Column('status', sa.Text(), nullable=False, default='pendente'),
        sa.Column('tentativas', sa.Integer(), nullable=False, default=0),
        sa.Column('ultimo_erro', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('published_at', sa.DateTime(timezone=True), nullable=True),
        schema='ate',
    )

    # Create indexes
    op.create_index('ix_ate_servicos_codigo', 'servicos_atendimento', ['codigo'], schema='ate')
    op.create_index('ix_ate_canais_codigo', 'canais_atendimento', ['codigo'], schema='ate')
    op.create_index('ix_ate_unidades_codigo', 'unidades_atendimento', ['codigo'], schema='ate')
    op.create_index('ix_ate_filas_unidade_servico_status', 'filas_atendimento', ['unidade_id', 'servico_id', 'status'], schema='ate')
    op.create_index('ix_ate_senhas_fila_status', 'senhas', ['fila_id', 'status'], schema='ate')
    op.create_index('ix_ate_senhas_numero', 'senhas', ['numero'], schema='ate')
    op.create_index('ix_ate_chamadas_senha', 'chamadas', ['senha_id'], schema='ate')
    op.create_index('ix_ate_chamadas_guiche_data', 'chamadas', ['guiche_id', 'data_hora'], schema='ate')
    op.create_index('ix_ate_atendimentos_chamada', 'atendimentos', ['chamada_id'], schema='ate')
    op.create_index('ix_ate_atendimentos_status', 'atendimentos', ['status'], schema='ate')
    op.create_index('ix_ate_avaliacoes_atendimento', 'avaliacoes_atendimento', ['atendimento_id'], schema='ate')
    op.create_index('ix_ate_encaminhamentos_atendimento', 'encaminhamentos', ['atendimento_id'], schema='ate')
    op.create_index('ix_ate_encaminhamentos_status', 'encaminhamentos', ['status'], schema='ate')
    op.create_index('ix_ate_eventos_outbox_status', 'eventos_outbox', ['status'], schema='ate')


def downgrade() -> None:
    op.drop_table('eventos_outbox', schema='ate')
    op.drop_table('encaminhamentos', schema='ate')
    op.drop_table('avaliacoes_atendimento', schema='ate')
    op.drop_table('atendimentos', schema='ate')
    op.drop_table('chamadas', schema='ate')
    op.drop_table('senhas', schema='ate')
    op.drop_table('triagens', schema='ate')
    op.drop_table('filas_atendimento', schema='ate')
    op.drop_table('guiches', schema='ate')
    op.drop_table('unidades_atendimento', schema='ate')
    op.drop_table('canais_atendimento', schema='ate')
    op.drop_table('servicos_atendimento', schema='ate')
    op.execute('DROP SCHEMA IF EXISTS ate')
