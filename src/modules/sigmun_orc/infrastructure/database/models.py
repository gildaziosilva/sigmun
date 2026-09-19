"""Modelos SQLAlchemy do DOM-ORC (schema orc)."""

from __future__ import annotations

import uuid

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class PPAModel(Base):
    """Modelo de PPAs."""

    __tablename__ = "ppas"
    __table_args__ = {"schema": "orc"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ano_inicial = Column(Integer, nullable=False)
    ano_final = Column(Integer, nullable=False)
    descricao = Column(Text)
    status = Column(Text, nullable=False, server_default="elaboracao")
    data_publicacao = Column(DateTime(timezone=True))
    data_encerramento = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    updated_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class LDOModel(Base):
    """Modelo de LDOs."""

    __tablename__ = "ldos"
    __table_args__ = {"schema": "orc"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    exercicio = Column(Integer, nullable=False, unique=True)
    ppa_id = Column(UUID(as_uuid=True),
                    ForeignKey("orc.ppas.id", onupdate="CASCADE", ondelete="RESTRICT"),
                    nullable=False)
    descricao = Column(Text)
    status = Column(Text, nullable=False, server_default="elaboracao")
    meta_fiscal_receita = Column(Float, nullable=False, server_default="0")
    meta_fiscal_despesa = Column(Float, nullable=False, server_default="0")
    data_aprovacao = Column(DateTime(timezone=True))
    data_sancao = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    updated_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class LOAModel(Base):
    """Modelo de LOAs."""

    __tablename__ = "loas"
    __table_args__ = {"schema": "orc"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    exercicio = Column(Integer, nullable=False, unique=True)
    ldo_id = Column(UUID(as_uuid=True),
                    ForeignKey("orc.ldos.id", onupdate="CASCADE", ondelete="RESTRICT"),
                    nullable=False)
    descricao = Column(Text)
    status = Column(Text, nullable=False, server_default="elaboracao")
    valor_receita_prevista = Column(Float, nullable=False, server_default="0")
    valor_despesa_fixada = Column(Float, nullable=False, server_default="0")
    data_aprovacao = Column(DateTime(timezone=True))
    data_publicacao = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    updated_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class DotacaoModel(Base):
    """Modelo de dotações orçamentárias."""

    __tablename__ = "dotacoes"
    __table_args__ = {"schema": "orc"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    loa_id = Column(UUID(as_uuid=True),
                    ForeignKey("orc.loas.id", onupdate="CASCADE", ondelete="RESTRICT"),
                    nullable=False)
    exercicio = Column(Integer, nullable=False)
    codigo = Column(Text, nullable=False)
    unidade_orcamentaria = Column(Text)
    natureza_despesa = Column(Text)
    fonte_recursos = Column(Text)
    valor_inicial = Column(Float, nullable=False, server_default="0")
    valor_suplementado = Column(Float, nullable=False, server_default="0")
    valor_anulado = Column(Float, nullable=False, server_default="0")
    valor_reservado = Column(Float, nullable=False, server_default="0")
    valor_empenhado = Column(Float, nullable=False, server_default="0")
    status = Column(Text, nullable=False, server_default="ativa")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    updated_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class ReservaModel(Base):
    """Modelo de reservas de saldo."""

    __tablename__ = "reservas"
    __table_args__ = {"schema": "orc"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    dotacao_id = Column(UUID(as_uuid=True),
                        ForeignKey("orc.dotacoes.id", onupdate="CASCADE", ondelete="RESTRICT"),
                        nullable=False)
    numero = Column(Text)
    valor = Column(Float, nullable=False, server_default="0")
    finalidade = Column(Text)
    status = Column(Text, nullable=False, server_default="ativa")
    data_reserva = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    data_conversao = Column(DateTime(timezone=True))
    data_cancelamento = Column(DateTime(timezone=True))
    motivo_cancelamento = Column(Text)
    empenho_id = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    updated_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


__all__ = ["Base", "PPAModel", "LDOModel", "LOAModel", "DotacaoModel", "ReservaModel"]
