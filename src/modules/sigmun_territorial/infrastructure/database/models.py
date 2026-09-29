"""Modelos SQLAlchemy do DOM-TEL (schema tel)."""

from __future__ import annotations

import uuid
from datetime import date, datetime

from sqlalchemy import (
    JSON,
    Boolean,
    Date,
    DateTime,
    Float,
    Integer,
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base declarativa dos modelos ORM do domínio Gestão Territorial."""

    pass


class BairroModel(Base):
    """Modelo de divisões territoriais (bairro, distrito, setor, zona rural)."""

    __tablename__ = "bairros"
    __table_args__ = {"schema": "tel"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, server_default="bairro")
    populacao_estimada: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    area_km2: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    situacao: Mapped[str] = mapped_column(Text, nullable=False, server_default="ativo")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class LogradouroModel(Base):
    """Modelo de logradouros públicos."""

    __tablename__ = "logradouros"
    __table_args__ = {"schema": "tel"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, server_default="rua")
    bairro_id: Mapped[str] = mapped_column(Text, nullable=False)
    cep: Mapped[str | None] = mapped_column(Text)
    numero_inicial: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    numero_final: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    situacao: Mapped[str] = mapped_column(Text, nullable=False, server_default="ativo")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class PlantaGenericaValoresModel(Base):
    """Modelo da planta genérica de valores por ano, bairro e ocupação."""

    __tablename__ = "planta_generica_valores"
    __table_args__ = {"schema": "tel"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ano: Mapped[int] = mapped_column(Integer, nullable=False)
    bairro_id: Mapped[str] = mapped_column(Text, nullable=False)
    ocupacao: Mapped[str] = mapped_column(Text, nullable=False, server_default="residencial")
    valor_terreno_m2: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    valor_construcao_m2: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    aliquota_percent: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    situacao: Mapped[str] = mapped_column(Text, nullable=False, server_default="rascunho")
    legislacao: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class GeorreferenciaModel(Base):
    """Modelo de georreferências territoriais."""

    __tablename__ = "georreferencias"
    __table_args__ = {"schema": "tel"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    bairro_id: Mapped[str | None] = mapped_column(Text)
    logradouro_id: Mapped[str | None] = mapped_column(Text)
    geometria: Mapped[str] = mapped_column(Text, nullable=False, server_default="ponto")
    latitude: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    longitude: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    altitude_m: Mapped[float | None] = mapped_column(Float)
    vertices: Mapped[list | None] = mapped_column(JSON)
    datum: Mapped[str] = mapped_column(Text, nullable=False, server_default="sirgas2000")
    precisao_m: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    data_levantamento: Mapped[date] = mapped_column(Date, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


__all__ = [
    "Base",
    "BairroModel",
    "LogradouroModel",
    "PlantaGenericaValoresModel",
    "GeorreferenciaModel",
]
