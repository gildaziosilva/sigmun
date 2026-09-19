"""Modelos SQLAlchemy do DOM-CON — execução (schema con)."""

from __future__ import annotations

import uuid

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class EmpenhoModel(Base):
    """Modelo de empenhos."""

    __tablename__ = "empenhos"
    __table_args__ = {"schema": "con"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    exercicio = Column(Integer, nullable=False)
    numero = Column(Text, nullable=False)
    dotacao_id = Column(Text, nullable=False)
    reserva_id = Column(Text)
    favorecido_nome = Column(Text)
    tipo = Column(Text, nullable=False, server_default="ordinario")
    descricao = Column(Text)
    valor_empenhado = Column(Float, nullable=False, server_default="0")
    valor_anulado = Column(Float, nullable=False, server_default="0")
    valor_liquidado = Column(Float, nullable=False, server_default="0")
    valor_pago = Column(Float, nullable=False, server_default="0")
    status = Column(Text, nullable=False, server_default="emitido")
    data_emissao = Column(DateTime(timezone=True), server_default=func.now())
    motivo_anulacao = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    updated_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class LiquidacaoModel(Base):
    """Modelo de liquidações."""

    __tablename__ = "liquidacoes"
    __table_args__ = {"schema": "con"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    empenho_id = Column(UUID(as_uuid=True),
                        ForeignKey("con.empenhos.id", onupdate="CASCADE", ondelete="RESTRICT"),
                        nullable=False)
    numero = Column(Text)
    valor = Column(Float, nullable=False, server_default="0")
    documento_fiscal = Column(Text)
    status = Column(Text, nullable=False, server_default="registrada")
    motivo_cancelamento = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    updated_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class PagamentoModel(Base):
    """Modelo de pagamentos."""

    __tablename__ = "pagamentos"
    __table_args__ = {"schema": "con"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    liquidacao_id = Column(UUID(as_uuid=True),
                           ForeignKey(
                               "con.liquidacoes.id",
                               onupdate="CASCADE",
                               ondelete="RESTRICT",
                           ),
                           nullable=False)
    empenho_id = Column(UUID(as_uuid=True),
                        ForeignKey("con.empenhos.id", onupdate="CASCADE", ondelete="RESTRICT"),
                        nullable=False)
    numero_ob = Column(Text)
    valor = Column(Float, nullable=False, server_default="0")
    conta_bancaria = Column(Text)
    status = Column(Text, nullable=False, server_default="programado")
    motivo_cancelamento = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    updated_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


__all__ = ["Base", "EmpenhoModel", "LiquidacaoModel", "PagamentoModel"]
