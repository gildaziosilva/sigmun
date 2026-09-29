"""Modelos SQLAlchemy do DOM-GEO (schema geo)."""

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
    """Base declarativa dos modelos ORM do domínio Geoinformação Municipal."""

    pass


class CamadaMapaModel(Base):
    """Modelo de camadas cartográficas do geoportal municipal."""

    __tablename__ = "camadas_mapa"
    __table_args__ = {"schema": "geo"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, server_default="outro")
    formato: Mapped[str] = mapped_column(Text, nullable=False, server_default="geojson")
    fonte: Mapped[str | None] = mapped_column(Text)
    data_atualizacao: Mapped[date] = mapped_column(Date, nullable=False)
    datum: Mapped[str] = mapped_column(Text, nullable=False, server_default="sirgas2000")
    srid: Mapped[int] = mapped_column(Integer, nullable=False, server_default="4326")
    url_servico: Mapped[str | None] = mapped_column(Text)
    zoom_minimo: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    zoom_maximo: Mapped[int] = mapped_column(Integer, nullable=False, server_default="24")
    visivel: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.true())
    situacao: Mapped[str] = mapped_column(Text, nullable=False, server_default="rascunho")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class MapaSigModel(Base):
    """Modelo de mapas SIG publicados no geoportal municipal."""

    __tablename__ = "mapas_sig"
    __table_args__ = {"schema": "geo"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, server_default="tematico")
    situacao: Mapped[str] = mapped_column(Text, nullable=False, server_default="rascunho")
    datum: Mapped[str] = mapped_column(Text, nullable=False, server_default="sirgas2000")
    srid: Mapped[int] = mapped_column(Integer, nullable=False, server_default="4326")
    escala_denominador: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    zoom_inicial: Mapped[int] = mapped_column(Integer, nullable=False, server_default="13")
    zoom_minimo: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    zoom_maximo: Mapped[int] = mapped_column(Integer, nullable=False, server_default="24")
    lat_min: Mapped[float | None] = mapped_column(Float)
    lon_min: Mapped[float | None] = mapped_column(Float)
    lat_max: Mapped[float | None] = mapped_column(Float)
    lon_max: Mapped[float | None] = mapped_column(Float)
    publicado_em: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    criado_por: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class MapaCamadaModel(Base):
    """Modelo da composição mapa ↔ camada (RN-GEO-004)."""

    __tablename__ = "mapas_camadas"
    __table_args__ = {"schema": "geo"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    mapa_id: Mapped[str] = mapped_column(Text, nullable=False)
    camada_id: Mapped[str] = mapped_column(Text, nullable=False)
    ordem: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    opacidade: Mapped[float] = mapped_column(Float, nullable=False, server_default="100")
    visivel: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.true())
    rotulo: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class FeatureGeoModel(Base):
    """Modelo de elementos geoespaciais (pontos de interesse) (RN-GEO-003)."""

    __tablename__ = "features_geo"
    __table_args__ = {"schema": "geo"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    camada_id: Mapped[str] = mapped_column(Text, nullable=False)
    geometria: Mapped[str] = mapped_column(Text, nullable=False, server_default="ponto")
    latitude: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    longitude: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    vertices: Mapped[list | None] = mapped_column(JSON)
    datum: Mapped[str] = mapped_column(Text, nullable=False, server_default="sirgas2000")
    atributos: Mapped[dict | None] = mapped_column(JSON)
    criado_por: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


class ServicoGeoModel(Base):
    """Modelo de serviços geoespaciais publicados (RN-GEO-007)."""

    __tablename__ = "servicos_geo"
    __table_args__ = {"schema": "geo"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, server_default="wms")
    situacao: Mapped[str] = mapped_column(Text, nullable=False, server_default="ativo")
    url: Mapped[str | None] = mapped_column(Text)
    camada: Mapped[str | None] = mapped_column(Text)
    datum: Mapped[str] = mapped_column(Text, nullable=False, server_default="sirgas2000")
    srid: Mapped[int] = mapped_column(Integer, nullable=False, server_default="4326")
    zoom_minimo: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    zoom_maximo: Mapped[int] = mapped_column(Integer, nullable=False, server_default="24")
    publico: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=func.false())


__all__ = [
    "Base",
    "CamadaMapaModel",
    "MapaSigModel",
    "MapaCamadaModel",
    "FeatureGeoModel",
    "ServicoGeoModel",
]
