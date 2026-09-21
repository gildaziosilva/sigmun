"""Modelos SQLAlchemy do DOM-PAT (schema pat)."""

from __future__ import annotations

import uuid

from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, Text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BemModel(Base):
    """Modelo de bens patrimoniais."""

    __tablename__ = "bens"
    __table_args__ = {"schema": "pat"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo = Column(Text, nullable=False, unique=True)
    tipo = Column(Text, nullable=False, server_default="movel")
    descricao = Column(Text, nullable=False)
    categoria = Column(Text)
    valor_aquisicao = Column(Float, nullable=False, server_default="0")
    data_aquisicao = Column(Date)
    valor_residual = Column(Float, nullable=False, server_default="0")
    vida_util_anos = Column(Integer, nullable=False, server_default="0")
    valor_contabil = Column(Float, nullable=False, server_default="0")
    status = Column(Text, nullable=False, server_default="em_uso")
    localizacao = Column(Text)
    responsavel_id = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class DepreciacaoModel(Base):
    """Modelo de depreciações de bens."""

    __tablename__ = "depreciacoes"
    __table_args__ = {"schema": "pat"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    bem_id = Column(Text, nullable=False)
    data = Column(Date)
    valor_depreciado = Column(Float, nullable=False, server_default="0")
    valor_acumulado = Column(Float, nullable=False, server_default="0")
    valor_liquido = Column(Float, nullable=False, server_default="0")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(Text)


class TransferenciaModel(Base):
    """Modelo de transferências de bens."""

    __tablename__ = "transferencias"
    __table_args__ = {"schema": "pat"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    bem_id = Column(Text, nullable=False)
    de_localizacao = Column(Text)
    para_localizacao = Column(Text, nullable=False)
    de_responsavel_id = Column(Text)
    para_responsavel_id = Column(Text)
    data_transferencia = Column(Date)
    motivo = Column(Text)
    status = Column(Text, nullable=False, server_default="pendente")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(Text)


__all__ = ["Base", "BemModel", "DepreciacaoModel", "TransferenciaModel"]