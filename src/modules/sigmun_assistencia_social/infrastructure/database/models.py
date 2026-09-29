"""Modelos SQLAlchemy do DOM-ASS (schema ass)."""

from __future__ import annotations

import uuid
from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, Float, Integer, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base declarativa dos modelos ORM do domínio Assistência Social."""

    pass


class FamiliaCadUnicoModel(Base):
    """Modelo de famílias do CadÚnico."""

    __tablename__ = "familias_cadunico"
    __table_args__ = {"schema": "ass"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nis: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    responsavel_nome: Mapped[str] = mapped_column(Text, nullable=False)
    responsavel_cpf: Mapped[str | None] = mapped_column(Text)
    endereco: Mapped[str | None] = mapped_column(Text)
    telefone: Mapped[str | None] = mapped_column(Text)
    renda_per_capita: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    quantidade_pessoas: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    status: Mapped[str] = mapped_column(Text, nullable=False, server_default="ativa")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class PessoaCadUnicoModel(Base):
    """Modelo de pessoas do CadÚnico."""

    __tablename__ = "pessoas_cadunico"
    __table_args__ = {"schema": "ass"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    familia_id: Mapped[str] = mapped_column(Text, nullable=False)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    cpf: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    data_nascimento: Mapped[str | None] = mapped_column(Text)
    sexo: Mapped[str] = mapped_column(Text, nullable=False, server_default="ignorado")
    nome_mae: Mapped[str | None] = mapped_column(Text)
    parentesco: Mapped[str | None] = mapped_column(Text)
    escolaridade: Mapped[str | None] = mapped_column(Text)
    ocupacao: Mapped[str | None] = mapped_column(Text)
    renda: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class UnidadeAssistenciaModel(Base):
    """Modelo de unidades CRAS/CREAS."""

    __tablename__ = "unidades_assistencia"
    __table_args__ = {"schema": "ass"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, server_default="cras")
    endereco: Mapped[str | None] = mapped_column(Text)
    telefone: Mapped[str | None] = mapped_column(Text)
    email: Mapped[str | None] = mapped_column(Text)
    responsavel: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(Text, nullable=False, server_default="ativa")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class BeneficioEventualModel(Base):
    """Modelo de benefícios eventuais."""

    __tablename__ = "beneficios_eventuais"
    __table_args__ = {"schema": "ass"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    familia_id: Mapped[str] = mapped_column(Text, nullable=False)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, server_default="alimentacao")
    descricao: Mapped[str | None] = mapped_column(Text)
    valor: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    quantidade: Mapped[int] = mapped_column(Integer, nullable=False, server_default="1")
    data_solicitacao: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    data_aprovacao: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_entrega: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    status: Mapped[str] = mapped_column(Text, nullable=False, server_default="solicitado")
    unidade_id: Mapped[str | None] = mapped_column(Text)
    observacao: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)


class AtendimentoSocialModel(Base):
    """Modelo de atendimentos sociais."""

    __tablename__ = "atendimentos_sociais"
    __table_args__ = {"schema": "ass"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pessoa_id: Mapped[str] = mapped_column(Text, nullable=False)
    unidade_id: Mapped[str] = mapped_column(Text, nullable=False)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, server_default="acolhimento")
    data: Mapped[date | None] = mapped_column(Date)
    descricao: Mapped[str | None] = mapped_column(Text)
    encaminhamento: Mapped[str | None] = mapped_column(Text)
    profissional: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[str | None] = mapped_column(Text)


__all__ = [
    "Base",
    "FamiliaCadUnicoModel",
    "PessoaCadUnicoModel",
    "UnidadeAssistenciaModel",
    "BeneficioEventualModel",
    "AtendimentoSocialModel",
]
