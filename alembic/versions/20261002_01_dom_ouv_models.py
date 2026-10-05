"""DOM-OUV - Ouvidoria FalaBR / e-OUV municipal.

Cria tabelas:
- ouv.protocolos (controle de sequencial por ano)
- ouv.manifestacoes (base: sugestao, elogio, reclamacao, solicitacao)
- ouv.denuncias (herda de manifestacoes, adiciona campos específicos)
- ouv.pedidos_lai (herda de manifestacoes, adiciona campos LAI)
- ouv.anexos (anexos das manifestações)
- ouv.tramitacoes (histórico de tramitação)

Revision ID: 20261002_01
Revises: 2061002_01_ate_models
Create Date: 2026-10-02
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

revision = "20261002_01"
down_revision = "20261002_01_ate_models"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Criar schema ouv
    op.execute("CREATE SCHEMA IF NOT EXISTS ouv")

    # Dropar enums existentes se houver
    for enum_name in [
        "tipo_manifestacao_ouv",
        "status_manifestacao_ouv",
        "prioridade_ouv",
        "canal_recebimento_ouv",
        "forma_resposta_ouv",
        "tipo_denuncia_ouv",
        "nivel_sigilo_ouv",
    ]:
        op.execute(f"DROP TYPE IF EXISTS ouv.{enum_name} CASCADE")

    # Criar enums via SQL direto
    op.execute("""
        CREATE TYPE ouv.tipo_manifestacao_ouv AS ENUM (
            'sugestao', 'elogio', 'reclamacao', 'solicitacao',
            'denuncia', 'pedido_acesso_informacao'
        );
    """)
    op.execute("""
        CREATE TYPE ouv.status_manifestacao_ouv AS ENUM (
            'registrada', 'em_analise', 'encaminhada', 'em_tratamento',
            'aguardando_complementacao', 'respondida', 'concluida',
            'arquivada', 'cancelada'
        );
    """)
    op.execute("""
        CREATE TYPE ouv.prioridade_ouv AS ENUM (
            'baixa', 'normal', 'alta', 'urgente'
        );
    """)
    op.execute("""
        CREATE TYPE ouv.canal_recebimento_ouv AS ENUM (
            'portal_cidadao', 'presencial', 'telefone', 'email',
            'correios', 'aplicativo', 'outro'
        );
    """)
    op.execute("""
        CREATE TYPE ouv.forma_resposta_ouv AS ENUM (
            'portal', 'email', 'correios', 'presencial', 'telefone'
        );
    """)
    op.execute("""
        CREATE TYPE ouv.tipo_denuncia_ouv AS ENUM (
            'corrupcao', 'improbidade', 'assedio', 'desvio_verba',
            'nepotismo', 'fraude_licitacao', 'outro'
        );
    """)
    op.execute("""
        CREATE TYPE ouv.nivel_sigilo_ouv AS ENUM (
            'publico', 'restrito', 'sigiloso', 'ultra_sigiloso'
        );
    """)

    # Criar tabelas usando SQL direto para evitar problemas com SQLAlchemy Enum
    op.execute("""
        CREATE TABLE ouv.protocolos (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            ano INTEGER NOT NULL,
            sequencial INTEGER NOT NULL DEFAULT 0,
            created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at TIMESTAMPTZ,
            UNIQUE (ano, sequencial)
        );
    """)

    op.execute("""
        CREATE TABLE ouv.manifestacoes (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            protocolo TEXT NOT NULL UNIQUE,
            ano_protocolo INTEGER NOT NULL,
            numero_protocolo INTEGER NOT NULL,
            tipo ouv.tipo_manifestacao_ouv NOT NULL DEFAULT 'solicitacao',
            status ouv.status_manifestacao_ouv NOT NULL DEFAULT 'registrada',
            prioridade ouv.prioridade_ouv NOT NULL DEFAULT 'normal',
            assunto TEXT NOT NULL,
            descricao TEXT NOT NULL,
            cidadao_nome TEXT,
            cidadao_cpf TEXT,
            cidadao_email TEXT,
            cidadao_telefone TEXT,
            cidadao_endereco TEXT,
            cidadao_anonimo BOOLEAN NOT NULL DEFAULT false,
            canal ouv.canal_recebimento_ouv NOT NULL DEFAULT 'portal_cidadao',
            orgao_destino TEXT NOT NULL,
            setor_responsavel TEXT,
            prazo_data_limite DATE,
            prazo_dias_uteis INTEGER,
            prazo_prorrogado BOOLEAN NOT NULL DEFAULT false,
            prazo_data_prorrogacao DATE,
            prazo_justificativa_prorrogacao TEXT,
            resposta TEXT,
            forma_resposta ouv.forma_resposta_ouv,
            data_resposta DATE,
            respondido_por TEXT,
            avaliacao_cidadao INTEGER,
            comentario_avaliacao TEXT,
            created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at TIMESTAMPTZ,
            created_by TEXT,
            updated_by TEXT,
            is_deleted BOOLEAN NOT NULL DEFAULT false
        );
    """)

    # Índices para manifestacoes
    op.execute("CREATE UNIQUE INDEX ix_ouv_manifestacoes_protocolo ON ouv.manifestacoes (protocolo);")
    op.execute("CREATE INDEX ix_ouv_manifestacoes_status ON ouv.manifestacoes (status);")
    op.execute("CREATE INDEX ix_ouv_manifestacoes_tipo ON ouv.manifestacoes (tipo);")
    op.execute("CREATE INDEX ix_ouv_manifestacoes_orgao_destino ON ouv.manifestacoes (orgao_destino);")
    op.execute("CREATE INDEX ix_ouv_manifestacoes_created_at ON ouv.manifestacoes (created_at);")
    op.execute("CREATE INDEX ix_ouv_manifestacoes_prazo_data_limite ON ouv.manifestacoes (prazo_data_limite);")

    # Tabela: denuncias (herda de manifestacoes via PK/FK)
    op.execute("""
        CREATE TABLE ouv.denuncias (
            id UUID PRIMARY KEY REFERENCES ouv.manifestacoes(id),
            tipo_denuncia ouv.tipo_denuncia_ouv NOT NULL DEFAULT 'outro',
            envolve_servidor_publico BOOLEAN NOT NULL DEFAULT false,
            servidor_envolvido TEXT,
            valor_envolvido NUMERIC(15, 2),
            local_fato TEXT NOT NULL,
            data_fato DATE NOT NULL,
            sigilo_denunciante BOOLEAN NOT NULL DEFAULT true,
            encaminhada_mp BOOLEAN NOT NULL DEFAULT false,
            encaminhada_pf BOOLEAN NOT NULL DEFAULT false,
            encaminhada_tce BOOLEAN NOT NULL DEFAULT false,
            numero_inquerito TEXT,
            resultado_investigacao TEXT
        );
    """)

    # Tabela: pedidos_lai (herda de manifestacoes via PK/FK)
    op.execute("""
        CREATE TABLE ouv.pedidos_lai (
            id UUID PRIMARY KEY REFERENCES ouv.manifestacoes(id),
            informacao_solicitada TEXT NOT NULL,
            fundamentacao TEXT NOT NULL,
            nivel_sigilo ouv.nivel_sigilo_ouv NOT NULL DEFAULT 'publico',
            fundamentacao_sigilo TEXT,
            dados_pessoais_terceiros BOOLEAN NOT NULL DEFAULT false,
            formato_resposta TEXT NOT NULL DEFAULT 'digital',
            is_recurso BOOLEAN NOT NULL DEFAULT false,
            pedido_original_id UUID REFERENCES ouv.pedidos_lai(id),
            decisao_recurso TEXT,
            data_decisao_recurso DATE
        );
    """)

    op.execute("CREATE INDEX ix_ouv_pedidos_lai_pedido_original_id ON ouv.pedidos_lai (pedido_original_id);")

    # Tabela: anexos
    op.execute("""
        CREATE TABLE ouv.anexos (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            manifestacao_id UUID NOT NULL REFERENCES ouv.manifestacoes(id),
            nome_arquivo TEXT NOT NULL,
            tipo_mime TEXT NOT NULL,
            tamanho_bytes INTEGER NOT NULL,
            url TEXT NOT NULL,
            descricao TEXT,
            criado_em TIMESTAMPTZ NOT NULL DEFAULT now()
        );
    """)

    op.execute("CREATE INDEX ix_ouv_anexos_manifestacao_id ON ouv.anexos (manifestacao_id);")

    # Tabela: tramitacoes
    op.execute("""
        CREATE TABLE ouv.tramitacoes (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            manifestacao_id UUID NOT NULL REFERENCES ouv.manifestacoes(id),
            status_anterior ouv.status_manifestacao_ouv,
            status_novo ouv.status_manifestacao_ouv NOT NULL,
            observacao TEXT,
            usuario_id TEXT NOT NULL,
            created_at TIMESTAMPTZ NOT NULL DEFAULT now()
        );
    """)

    op.execute("CREATE INDEX ix_ouv_tramitacoes_manifestacao_id ON ouv.tramitacoes (manifestacao_id);")


def downgrade() -> None:
    op.execute("DROP INDEX IF EXISTS ouv.ix_ouv_tramitacoes_manifestacao_id;")
    op.execute("DROP TABLE IF EXISTS ouv.tramitacoes;")
    op.execute("DROP INDEX IF EXISTS ouv.ix_ouv_anexos_manifestacao_id;")
    op.execute("DROP TABLE IF EXISTS ouv.anexos;")
    op.execute("DROP INDEX IF EXISTS ouv.ix_ouv_pedidos_lai_pedido_original_id;")
    op.execute("DROP TABLE IF EXISTS ouv.pedidos_lai;")
    op.execute("DROP TABLE IF EXISTS ouv.denuncias;")
    op.execute("DROP INDEX IF EXISTS ouv.ix_ouv_manifestacoes_prazo_data_limite;")
    op.execute("DROP INDEX IF EXISTS ouv.ix_ouv_manifestacoes_created_at;")
    op.execute("DROP INDEX IF EXISTS ouv.ix_ouv_manifestacoes_orgao_destino;")
    op.execute("DROP INDEX IF EXISTS ouv.ix_ouv_manifestacoes_tipo;")
    op.execute("DROP INDEX IF EXISTS ouv.ix_ouv_manifestacoes_status;")
    op.execute("DROP INDEX IF EXISTS ouv.ix_ouv_manifestacoes_protocolo;")
    op.execute("DROP TABLE IF EXISTS ouv.manifestacoes;")
    op.execute("DROP INDEX IF EXISTS ouv.uq_protocolo_ano_sequencial;")
    op.execute("DROP TABLE IF EXISTS ouv.protocolos;")
    
    for enum_name in [
        "tipo_manifestacao_ouv",
        "status_manifestacao_ouv",
        "prioridade_ouv",
        "canal_recebimento_ouv",
        "forma_resposta_ouv",
        "tipo_denuncia_ouv",
        "nivel_sigilo_ouv",
    ]:
        op.execute(f"DROP TYPE IF EXISTS ouv.{enum_name} CASCADE")
    
    op.execute("DROP SCHEMA IF EXISTS ouv")
