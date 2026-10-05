"""Modelos SQLAlchemy do DOM-OUV (schema ouv)."""

from __future__ import annotations

import uuid

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Numeric,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class ProtocoloModel(Base):
    """Controle de protocolos por ano (RN-OUV-001)."""

    __tablename__ = "protocolos"
    __table_args__ = ({"schema": "ouv"},)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ano = Column(Integer, nullable=False)
    sequencial = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))

    __table_args__ = (
        UniqueConstraint("ano", "sequencial", name="uq_protocolo_ano_sequencial"),
        {"schema": "ouv"},
    )


class ManifestacaoModel(Base):
    """Modelo base de manifestações."""

    __tablename__ = "manifestacoes"
    __table_args__ = ({"schema": "ouv"},)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    protocolo = Column(Text, nullable=False, unique=True)
    ano_protocolo = Column(Integer, nullable=False)
    numero_protocolo = Column(Integer, nullable=False)

    tipo = Column(
        Enum(
            "sugestao",
            "elogio",
            "reclamacao",
            "solicitacao",
            "denuncia",
            "pedido_acesso_informacao",
            name="tipo_manifestacao_ouv",
        ),
        nullable=False,
        server_default="solicitacao",
    )
    status = Column(
        Enum(
            "registrada",
            "em_analise",
            "encaminhada",
            "em_tratamento",
            "aguardando_complementacao",
            "respondida",
            "concluida",
            "arquivada",
            "cancelada",
            name="status_manifestacao_ouv",
        ),
        nullable=False,
        server_default="registrada",
    )
    prioridade = Column(
        Enum("baixa", "normal", "alta", "urgente", name="prioridade_ouv"),
        nullable=False,
        server_default="normal",
    )

    assunto = Column(Text, nullable=False)
    descricao = Column(Text, nullable=False)

    # Dados do cidadão (LGPD)
    cidadao_nome = Column(Text)
    cidadao_cpf = Column(Text)
    cidadao_email = Column(Text)
    cidadao_telefone = Column(Text)
    cidadao_endereco = Column(Text)
    cidadao_anonimo = Column(Boolean, nullable=False, server_default=func.false())

    canal = Column(
        Enum(
            "portal_cidadao",
            "presencial",
            "telefone",
            "email",
            "correios",
            "aplicativo",
            "outro",
            name="canal_recebimento_ouv",
        ),
        nullable=False,
        server_default="portal_cidadao",
    )

    orgao_destino = Column(Text, nullable=False)
    setor_responsavel = Column(Text)

    # Prazo
    prazo_data_limite = Column(Date)
    prazo_dias_uteis = Column(Integer)
    prazo_prorrogado = Column(Boolean, nullable=False, server_default=func.false())
    prazo_data_prorrogacao = Column(Date)
    prazo_justificativa_prorrogacao = Column(Text)

    # Resposta
    resposta = Column(Text)
    forma_resposta = Column(
        Enum("portal", "email", "correios", "presencial", "telefone", name="forma_resposta_ouv"),
    )
    data_resposta = Column(Date)
    respondido_por = Column(Text)

    # Avaliação
    avaliacao_cidadao = Column(Integer)
    comentario_avaliacao = Column(Text)

    # Campos de auditoria
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    updated_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())

    # Relacionamentos
    anexos = relationship(
        "AnexoModel",
        back_populates="manifestacao",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )
    tramitacoes = relationship(
        "TramitacaoModel",
        back_populates="manifestacao",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )


class DenunciaModel(ManifestacaoModel):
    """Modelo de denúncia (herda de manifestação)."""

    __tablename__ = "denuncias"
    __table_args__ = ({"schema": "ouv"},)

    id = Column(UUID(as_uuid=True), ForeignKey("ouv.manifestacoes.id"), primary_key=True)

    tipo_denuncia = Column(
        Enum(
            "corrupcao",
            "improbidade",
            "assedio",
            "desvio_verba",
            "nepotismo",
            "fraude_licitacao",
            "outro",
            name="tipo_denuncia_ouv",
        ),
        nullable=False,
        server_default="outro",
    )
    envolve_servidor_publico = Column(Boolean, nullable=False, server_default=func.false())
    servidor_envolvido = Column(Text)
    valor_envolvido = Column(Numeric(15, 2))
    local_fato = Column(Text, nullable=False)
    data_fato = Column(Date, nullable=False)
    sigilo_denunciante = Column(Boolean, nullable=False, server_default=func.true())

    encaminhada_mp = Column(Boolean, nullable=False, server_default=func.false())
    encaminhada_pf = Column(Boolean, nullable=False, server_default=func.false())
    encaminhada_tce = Column(Boolean, nullable=False, server_default=func.false())
    numero_inquerito = Column(Text)
    resultado_investigacao = Column(Text)


class PedidoLaiModel(ManifestacaoModel):
    """Modelo de pedido LAI (herda de manifestação)."""

    __tablename__ = "pedidos_lai"
    __table_args__ = ({"schema": "ouv"},)

    id = Column(UUID(as_uuid=True), ForeignKey("ouv.manifestacoes.id"), primary_key=True)

    informacao_solicitada = Column(Text, nullable=False)
    fundamentacao = Column(Text, nullable=False)

    nivel_sigilo = Column(
        Enum(
            "publico",
            "restrito",
            "sigiloso",
            "ultra_sigiloso",
            name="nivel_sigilo_ouv",
        ),
        nullable=False,
        server_default="publico",
    )
    fundamentacao_sigilo = Column(Text)
    dados_pessoais_terceiros = Column(Boolean, nullable=False, server_default=func.false())
    formato_resposta = Column(Text, nullable=False, server_default="digital")

    is_recurso = Column(Boolean, nullable=False, server_default=func.false())
    pedido_original_id = Column(UUID(as_uuid=True), ForeignKey("ouv.pedidos_lai.id"))
    decisao_recurso = Column(Text)
    data_decisao_recurso = Column(Date)

    pedido_original = relationship(
        "PedidoLaiModel", remote_side=[id], backref="recursos", foreign_keys=[pedido_original_id]
    )


class AnexoModel(Base):
    """Anexos das manifestações."""

    __tablename__ = "anexos"
    __table_args__ = ({"schema": "ouv"},)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    manifestacao_id = Column(UUID(as_uuid=True), ForeignKey("ouv.manifestacoes.id"), nullable=False)

    nome_arquivo = Column(Text, nullable=False)
    tipo_mime = Column(Text, nullable=False)
    tamanho_bytes = Column(Integer, nullable=False)
    url = Column(Text, nullable=False)
    descricao = Column(Text)
    criado_em = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    manifestacao = relationship("ManifestacaoModel", back_populates="anexos")


class TramitacaoModel(Base):
    """Histórico de tramitação da manifestação."""

    __tablename__ = "tramitacoes"
    __table_args__ = ({"schema": "ouv"},)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    manifestacao_id = Column(UUID(as_uuid=True), ForeignKey("ouv.manifestacoes.id"), nullable=False)

    status_anterior = Column(
        Enum(
            "registrada",
            "em_analise",
            "encaminhada",
            "em_tratamento",
            "aguardando_complementacao",
            "respondida",
            "concluida",
            "arquivada",
            "cancelada",
            name="status_manifestacao_ouv",
        ),
    )
    status_novo = Column(
        Enum(
            "registrada",
            "em_analise",
            "encaminhada",
            "em_tratamento",
            "aguardando_complementacao",
            "respondida",
            "concluida",
            "arquivada",
            "cancelada",
            name="status_manifestacao_ouv",
        ),
        nullable=False,
    )
    observacao = Column(Text)
    usuario_id = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    manifestacao = relationship("ManifestacaoModel", back_populates="tramitacoes")


__all__ = [
    "Base",
    "ProtocoloModel",
    "ManifestacaoModel",
    "DenunciaModel",
    "PedidoLaiModel",
    "AnexoModel",
    "TramitacaoModel",
]
