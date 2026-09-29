"""Modelos SQLAlchemy do DOM-OBR (schema obr)."""

from __future__ import annotations

import uuid
from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, Float, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base declarativa dos modelos ORM do domínio Obras e Infraestrutura."""

    pass


class ObraModel(Base):
    """Modelo de obras públicas com acompanhamento físico-financeiro."""

    __tablename__ = "obras"
    __table_args__ = {"schema": "obr"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    numero: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, server_default="outro")
    situacao: Mapped[str] = mapped_column(Text, nullable=False, server_default="planejada")
    tipo_contratacao: Mapped[str] = mapped_column(
        Text, nullable=False, server_default="licitacao"
    )
    fonte_recurso: Mapped[str] = mapped_column(
        Text, nullable=False, server_default="orcamento_proprio"
    )
    valor_orcado: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    valor_contratado: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    valor_mediado: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    valor_pago: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    percentual_fisico: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    percentual_financeiro: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    empresa_contratada: Mapped[str | None] = mapped_column(Text)
    numero_contrato: Mapped[str | None] = mapped_column(Text)
    responsavel_tecnico: Mapped[str | None] = mapped_column(Text)
    endereco: Mapped[str | None] = mapped_column(Text)
    bairro: Mapped[str | None] = mapped_column(Text)
    data_inicio_prevista: Mapped[date | None] = mapped_column(Date)
    data_fim_prevista: Mapped[date | None] = mapped_column(Date)
    data_inicio_real: Mapped[date | None] = mapped_column(Date)
    data_fim_real: Mapped[date | None] = mapped_column(Date)
    observacao: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class MedicaoObraModel(Base):
    """Modelo de medições físico-financeiras (RN-OBR-005)."""

    __tablename__ = "medicoes_obras"
    __table_args__ = {"schema": "obr"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    obra_id: Mapped[str] = mapped_column(Text, nullable=False)
    numero: Mapped[str] = mapped_column(Text, nullable=False)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, server_default="avanco")
    situacao: Mapped[str] = mapped_column(Text, nullable=False, server_default="registrada")
    data: Mapped[date] = mapped_column(Date, nullable=False)
    percentual_fisico: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    valor_medido: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    responsavel_tecnico: Mapped[str] = mapped_column(Text, nullable=False)
    observacao: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class EtapaObraModel(Base):
    """Modelo de etapas de execução da obra (RN-OBR-007)."""

    __tablename__ = "etapas_obras"
    __table_args__ = {"schema": "obr"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    obra_id: Mapped[str] = mapped_column(Text, nullable=False)
    numero: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str] = mapped_column(Text, nullable=False)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, server_default="estrutura")
    situacao: Mapped[str] = mapped_column(Text, nullable=False, server_default="pendente")
    percentual_previsto: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    percentual_realizado: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    data_inicio_prevista: Mapped[date | None] = mapped_column(Date)
    data_fim_prevista: Mapped[date | None] = mapped_column(Date)
    data_conclusao: Mapped[date | None] = mapped_column(Date)
    responsavel: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class DespesaObraModel(Base):
    """Modelo de despesas financeiras da obra (RN-OBR-006)."""

    __tablename__ = "despesas_obras"
    __table_args__ = {"schema": "obr"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    obra_id: Mapped[str] = mapped_column(Text, nullable=False)
    medicao_id: Mapped[str | None] = mapped_column(Text)
    descricao: Mapped[str] = mapped_column(Text, nullable=False)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, server_default="medicao")
    valor: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    data: Mapped[date] = mapped_column(Date, nullable=False)
    documento: Mapped[str | None] = mapped_column(Text)
    credor: Mapped[str | None] = mapped_column(Text)
    observacao: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class VistoriaObraModel(Base):
    """Modelo de vistorias fiscalizadoras da obra (RN-OBR-008)."""

    __tablename__ = "vistorias_obras"
    __table_args__ = {"schema": "obr"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    obra_id: Mapped[str] = mapped_column(Text, nullable=False)
    data: Mapped[date] = mapped_column(Date, nullable=False)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, server_default="periodica")
    parecer: Mapped[str] = mapped_column(Text, nullable=False, server_default="aprovado")
    percentual_fisico_verificado: Mapped[float] = mapped_column(
        Float, nullable=False, server_default="0"
    )
    fiscal: Mapped[str] = mapped_column(Text, nullable=False)
    observacao: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


__all__ = [
    "Base",
    "ObraModel",
    "MedicaoObraModel",
    "EtapaObraModel",
    "DespesaObraModel",
    "VistoriaObraModel",
]
