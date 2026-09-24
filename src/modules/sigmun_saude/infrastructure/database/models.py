"""Modelos SQLAlchemy do DOM-SAU (schema sau)."""

from __future__ import annotations

import uuid

from sqlalchemy import Boolean, Column, Date, DateTime, Float, Text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class PacienteModel(Base):
    """Modelo de pacientes."""

    __tablename__ = "pacientes"
    __table_args__ = {"schema": "sau"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(Text, nullable=False)
    cns = Column(Text, nullable=False, unique=True)
    cpf = Column(Text)
    data_nascimento = Column(Text)
    sexo = Column(Text, nullable=False, server_default="ignorado")
    nome_mae = Column(Text)
    telefone = Column(Text)
    endereco = Column(Text)
    ubs_referencia = Column(Text)
    status = Column(Text, nullable=False, server_default="ativo")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class AtendimentoModel(Base):
    """Modelo de atendimentos do prontuario."""

    __tablename__ = "atendimentos"
    __table_args__ = {"schema": "sau"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    paciente_id = Column(Text, nullable=False)
    data = Column(Date)
    tipo = Column(Text, nullable=False, server_default="consulta")
    profissional = Column(Text, nullable=False)
    estabelecimento = Column(Text, nullable=False)
    queixa = Column(Text)
    conduta = Column(Text)
    cid10 = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(Text)


class AgendamentoModel(Base):
    """Modelo de agendamentos SUS."""

    __tablename__ = "agendamentos"
    __table_args__ = {"schema": "sau"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    paciente_id = Column(Text, nullable=False)
    especialidade = Column(Text, nullable=False)
    data = Column(Date)
    hora = Column(Text)
    estabelecimento = Column(Text)
    status = Column(Text, nullable=False, server_default="agendado")
    motivo_cancelamento = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)


class RegulacaoModel(Base):
    """Modelo da central de regulacao."""

    __tablename__ = "regulacoes"
    __table_args__ = {"schema": "sau"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    paciente_id = Column(Text, nullable=False)
    procedimento = Column(Text, nullable=False)
    prioridade = Column(Text, nullable=False, server_default="rotina")
    solicitante = Column(Text)
    data_solicitacao = Column(Date)
    status = Column(Text, nullable=False, server_default="solicitada")
    justificativa = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)


class MedicamentoModel(Base):
    """Modelo da farmacia basica."""

    __tablename__ = "medicamentos"
    __table_args__ = {"schema": "sau"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(Text, nullable=False)
    apresentacao = Column(Text)
    estoque = Column(Float, nullable=False, server_default="0")
    estoque_minimo = Column(Float, nullable=False, server_default="0")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class DispensacaoModel(Base):
    """Modelo de dispensacoes."""

    __tablename__ = "dispensacoes"
    __table_args__ = {"schema": "sau"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    paciente_id = Column(Text, nullable=False)
    medicamento_id = Column(Text, nullable=False)
    quantidade = Column(Float, nullable=False, server_default="0")
    data = Column(Date)
    receita = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(Text)


__all__ = ["Base", "PacienteModel", "AtendimentoModel", "AgendamentoModel", "RegulacaoModel", "MedicamentoModel", "DispensacaoModel"]
