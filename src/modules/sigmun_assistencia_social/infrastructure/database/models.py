"""Modelos SQLAlchemy do DOM-ASS (schema ass)."""

from __future__ import annotations

import uuid

from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, Text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class FamiliaCadUnicoModel(Base):
    """Modelo de famílias do CadÚnico."""

    __tablename__ = "familias_cadunico"
    __table_args__ = {"schema": "ass"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nis = Column(Text, nullable=False, unique=True)
    responsavel_nome = Column(Text, nullable=False)
    responsavel_cpf = Column(Text)
    endereco = Column(Text)
    telefone = Column(Text)
    renda_per_capita = Column(Float, nullable=False, server_default="0")
    quantidade_pessoas = Column(Integer, nullable=False, server_default="0")
    status = Column(Text, nullable=False, server_default="ativa")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class PessoaCadUnicoModel(Base):
    """Modelo de pessoas do CadÚnico."""

    __tablename__ = "pessoas_cadunico"
    __table_args__ = {"schema": "ass"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    familia_id = Column(Text, nullable=False)
    nome = Column(Text, nullable=False)
    cpf = Column(Text, nullable=False, unique=True)
    data_nascimento = Column(Text)
    sexo = Column(Text, nullable=False, server_default="ignorado")
    nome_mae = Column(Text)
    parentesco = Column(Text)
    escolaridade = Column(Text)
    ocupacao = Column(Text)
    renda = Column(Float, nullable=False, server_default="0")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class UnidadeAssistenciaModel(Base):
    """Modelo de unidades CRAS/CREAS."""

    __tablename__ = "unidades_assistencia"
    __table_args__ = {"schema": "ass"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo = Column(Text, nullable=False, unique=True)
    nome = Column(Text, nullable=False)
    tipo = Column(Text, nullable=False, server_default="cras")
    endereco = Column(Text)
    telefone = Column(Text)
    email = Column(Text)
    responsavel = Column(Text)
    status = Column(Text, nullable=False, server_default="ativa")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class BeneficioEventualModel(Base):
    """Modelo de benefícios eventuais."""

    __tablename__ = "beneficios_eventuais"
    __table_args__ = {"schema": "ass"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    familia_id = Column(Text, nullable=False)
    tipo = Column(Text, nullable=False, server_default="alimentacao")
    descricao = Column(Text)
    valor = Column(Float, nullable=False, server_default="0")
    quantidade = Column(Text, nullable=False, server_default="1")
    data_solicitacao = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    data_aprovacao = Column(DateTime(timezone=True))
    data_entrega = Column(DateTime(timezone=True))
    status = Column(Text, nullable=False, server_default="solicitado")
    unidade_id = Column(Text)
    observacao = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)


class AtendimentoSocialModel(Base):
    """Modelo de atendimentos sociais."""

    __tablename__ = "atendimentos_sociais"
    __table_args__ = {"schema": "ass"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pessoa_id = Column(Text, nullable=False)
    unidade_id = Column(Text, nullable=False)
    tipo = Column(Text, nullable=False, server_default="acolhimento")
    data = Column(Date)
    descricao = Column(Text)
    encaminhamento = Column(Text)
    profissional = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(Text)


__all__ = [
    "Base",
    "FamiliaCadUnicoModel",
    "PessoaCadUnicoModel",
    "UnidadeAssistenciaModel",
    "BeneficioEventualModel",
    "AtendimentoSocialModel",
]