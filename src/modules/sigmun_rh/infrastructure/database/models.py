"""Modelos SQLAlchemy do DOM-PES (schema rh)."""

from __future__ import annotations

import uuid

from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, String, Text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CargoModel(Base):
    """Modelo de cargos."""

    __tablename__ = "cargos"
    __table_args__ = {"schema": "rh"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo = Column(Text, nullable=False, unique=True)
    nome = Column(Text, nullable=False)
    descricao = Column(Text)
    nivel = Column(Text, nullable=False, server_default="basico")
    salario_base = Column(Float, nullable=False, server_default="0")
    carga_horaria_semanal = Column(Integer, nullable=False, server_default="40")
    ativo = Column(Boolean, nullable=False, server_default=func.true())
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class ServidorModel(Base):
    """Modelo de servidores."""

    __tablename__ = "servidores"
    __table_args__ = {"schema": "rh"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    matricula = Column(Text, nullable=False, unique=True)
    cpf = Column(String(11), nullable=False, unique=True)
    nome = Column(Text, nullable=False)
    cargo_id = Column(Text, nullable=False)
    tipo_vinculo = Column(Text, nullable=False, server_default="efetivo")
    status = Column(Text, nullable=False, server_default="ativo")
    data_admissao = Column(Date)
    data_desligamento = Column(Date)
    salario = Column(Float, nullable=False, server_default="0")
    email = Column(Text)
    telefone = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    updated_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class LotacaoModel(Base):
    """Modelo de lotacoes."""

    __tablename__ = "lotacoes"
    __table_args__ = {"schema": "rh"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    servidor_id = Column(Text, nullable=False)
    unidade_id = Column(Text, nullable=False)
    cargo_id = Column(Text)
    data_inicio = Column(Date)
    data_fim = Column(Date)
    vigente = Column(Boolean, nullable=False, server_default=func.true())
    motivo = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())
