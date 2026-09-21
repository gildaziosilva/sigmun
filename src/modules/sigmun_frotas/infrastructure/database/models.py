"""Modelos SQLAlchemy do DOM-FRO (schema fro)."""

from __future__ import annotations

import uuid

from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, Text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class VeiculoModel(Base):
    """Modelo de veículos da frota."""

    __tablename__ = "veiculos"
    __table_args__ = {"schema": "fro"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    placa = Column(Text, nullable=False, unique=True)
    chassi = Column(Text)
    renavam = Column(Text)
    marca = Column(Text, nullable=False)
    modelo = Column(Text, nullable=False)
    ano_fabricacao = Column(Integer, nullable=False, server_default="0")
    ano_modelo = Column(Integer, nullable=False, server_default="0")
    tipo = Column(Text, nullable=False, server_default="leve")
    combustivel = Column(Text, nullable=False, server_default="flex")
    capacidade = Column(Float, nullable=False, server_default="0")
    odometro_atual = Column(Float, nullable=False, server_default="0")
    status = Column(Text, nullable=False, server_default="ativo")
    unidade_id = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class AbastecimentoModel(Base):
    """Modelo de abastecimentos."""

    __tablename__ = "abastecimentos"
    __table_args__ = {"schema": "fro"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    veiculo_id = Column(Text, nullable=False)
    data = Column(Date)
    quantidade_litros = Column(Float, nullable=False, server_default="0")
    valor_unitario = Column(Float, nullable=False, server_default="0")
    valor_total = Column(Float, nullable=False, server_default="0")
    odometro = Column(Float, nullable=False, server_default="0")
    posto = Column(Text)
    tipo_combustivel = Column(Text, nullable=False, server_default="flex")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(Text)


class ManutencaoModel(Base):
    """Modelo de manutenções."""

    __tablename__ = "manutencoes"
    __table_args__ = {"schema": "fro"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    veiculo_id = Column(Text, nullable=False)
    data_entrada = Column(Date)
    data_saida = Column(Date)
    tipo = Column(Text, nullable=False, server_default="preventiva")
    descricao = Column(Text, nullable=False)
    oficina = Column(Text)
    valor = Column(Float, nullable=False, server_default="0")
    status = Column(Text, nullable=False, server_default="aberta")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(Text)


class RotaModel(Base):
    """Modelo de rotas/deslocamentos."""

    __tablename__ = "rotas"
    __table_args__ = {"schema": "fro"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    veiculo_id = Column(Text, nullable=False)
    data = Column(Date)
    origem = Column(Text, nullable=False)
    destino = Column(Text, nullable=False)
    km_inicio = Column(Float, nullable=False, server_default="0")
    km_fim = Column(Float, nullable=False, server_default="0")
    distancia_km = Column(Float, nullable=False, server_default="0")
    descricao = Column(Text)
    status = Column(Text, nullable=False, server_default="planejada")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(Text)


__all__ = [
    "Base",
    "VeiculoModel",
    "AbastecimentoModel",
    "ManutencaoModel",
    "RotaModel",
]