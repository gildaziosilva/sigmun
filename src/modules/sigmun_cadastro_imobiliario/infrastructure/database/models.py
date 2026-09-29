"""Modelos SQLAlchemy do DOM-IMO (schema imo)."""

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
    """Base declarativa dos modelos ORM do domínio Cadastro Imobiliário."""

    pass


class ImovelModel(Base):
    """Modelo das unidades imobiliárias (lotes)."""

    __tablename__ = "imoveis"
    __table_args__ = {"schema": "imo"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    inscricao_imobiliaria: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    logradouro_id: Mapped[str] = mapped_column(Text, nullable=False)
    bairro_id: Mapped[str] = mapped_column(Text, nullable=False)
    numero: Mapped[str | None] = mapped_column(Text)
    complemento: Mapped[str | None] = mapped_column(Text)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, server_default="lote")
    situacao: Mapped[str] = mapped_column(Text, nullable=False, server_default="ativo")
    tipo_propriedade: Mapped[str] = mapped_column(Text, nullable=False, server_default="proprio")
    area_terreno_m2: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    area_construida_m2: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    ano_construcao: Mapped[int | None] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class ProprietarioImovelModel(Base):
    """Modelo dos vínculos de propriedade pessoa-imóvel."""

    __tablename__ = "proprietarios_imoveis"
    __table_args__ = {"schema": "imo"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    imovel_id: Mapped[str] = mapped_column(Text, nullable=False)
    pessoa_id: Mapped[str | None] = mapped_column(Text)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    cpf: Mapped[str] = mapped_column(Text, nullable=False)
    vinculo: Mapped[str] = mapped_column(Text, nullable=False, server_default="titular")
    principal: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class AvaliacaoImovelModel(Base):
    """Modelo das avaliações de valor venal dos imóveis."""

    __tablename__ = "avaliacoes_imoveis"
    __table_args__ = {"schema": "imo"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    imovel_id: Mapped[str] = mapped_column(Text, nullable=False)
    ano: Mapped[int] = mapped_column(Integer, nullable=False)
    valor_terreno_m2_unitario: Mapped[float] = mapped_column(
        Float, nullable=False, server_default="0"
    )
    valor_construcao_m2_unitario: Mapped[float] = mapped_column(
        Float, nullable=False, server_default="0"
    )
    aliquota_percent: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    area_terreno_m2: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    area_construida_m2: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    situacao: Mapped[str] = mapped_column(Text, nullable=False, server_default="rascunho")
    data_avaliacao: Mapped[date] = mapped_column(Date, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class CaracteristicaImovelModel(Base):
    """Modelo das características construtivas dos imóveis."""

    __tablename__ = "caracteristicas_imoveis"
    __table_args__ = {"schema": "imo"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    imovel_id: Mapped[str] = mapped_column(Text, nullable=False)
    obra: Mapped[str] = mapped_column(Text, nullable=False, server_default="residencial")
    numero_pavimentos: Mapped[int] = mapped_column(Integer, nullable=False, server_default="1")
    ano_renovacao: Mapped[int | None] = mapped_column(Integer)
    observacao: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)


class GeometriaImovelModel(Base):
    """Modelo das geometrias georreferenciadas dos lotes."""

    __tablename__ = "geometrias_imoveis"
    __table_args__ = {"schema": "imo"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    imovel_id: Mapped[str] = mapped_column(Text, nullable=False)
    geometria: Mapped[str] = mapped_column(Text, nullable=False, server_default="ponto")
    latitude: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    longitude: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
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
    "ImovelModel",
    "ProprietarioImovelModel",
    "AvaliacaoImovelModel",
    "CaracteristicaImovelModel",
    "GeometriaImovelModel",
]

