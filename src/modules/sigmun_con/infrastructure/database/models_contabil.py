"""Modelos SQLAlchemy do DOM-CON — PCASP e conciliação (schema con)."""

from __future__ import annotations

import uuid

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, Text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID

from .models import Base


class ContaContabilModel(Base):
    """Modelo do PCASP."""

    __tablename__ = "contas_contabeis"
    __table_args__ = {"schema": "con"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo = Column(Text, nullable=False, unique=True)
    nome = Column(Text, nullable=False)
    classe = Column(Text)
    natureza_saldo = Column(Text, nullable=False, server_default="devedora")
    tipo = Column(Text, nullable=False, server_default="analitica")
    aceita_lancamento = Column(Boolean, nullable=False, server_default=func.true())
    ativa = Column(Boolean, nullable=False, server_default=func.true())
    conta_pai_id = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class LancamentoModel(Base):
    """Modelo de lançamentos (cabeçalho + partidas JSON)."""

    __tablename__ = "lancamentos"
    __table_args__ = {"schema": "con"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    exercicio = Column(Integer, nullable=False)
    numero = Column(Text)
    historico = Column(Text)
    origem = Column(Text)
    origem_id = Column(Text)
    partidas = Column(Text, nullable=False, server_default="[]")
    total_debito = Column(Float, nullable=False, server_default="0")
    total_credito = Column(Float, nullable=False, server_default="0")
    status = Column(Text, nullable=False, server_default="rascunho")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class ConciliacaoModel(Base):
    """Modelo de conciliações contábeis."""

    __tablename__ = "conciliacoes"
    __table_args__ = {"schema": "con"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conta_id = Column(Text, nullable=False)
    codigo_conta = Column(Text)
    competencia_ano = Column(Integer, nullable=False)
    competencia_mes = Column(Integer, nullable=False)
    saldo_contabil = Column(Float, nullable=False, server_default="0")
    saldo_extrato = Column(Float, nullable=False, server_default="0")
    diferenca = Column(Float, nullable=False, server_default="0")
    status = Column(Text, nullable=False, server_default="aberta")
    justificativa = Column(Text)
    data_conciliacao = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


__all__ = ["ContaContabilModel", "LancamentoModel", "ConciliacaoModel"]
