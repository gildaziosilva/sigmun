"""Modelos SQLAlchemy de folha/ferias/frequencia (DOM-PES)."""

from __future__ import annotations

import uuid

from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, String, Text
from sqlalchemy import Time, func
from sqlalchemy.dialects.postgresql import UUID

from .models import Base


class FolhaPagamentoModel(Base):
    """Modelo de folhas de pagamento."""

    __tablename__ = "folhas_pagamento"
    __table_args__ = {"schema": "rh"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    competencia_ano = Column(Integer, nullable=False)
    competencia_mes = Column(Integer, nullable=False)
    descricao = Column(Text)
    status = Column(Text, nullable=False, server_default="aberta")
    total_proventos = Column(Float, nullable=False, server_default="0")
    total_descontos = Column(Float, nullable=False, server_default="0")
    total_liquido = Column(Float, nullable=False, server_default="0")
    quantidade_servidores = Column(Integer, nullable=False, server_default="0")
    data_fechamento = Column(DateTime(timezone=True))
    data_homologacao = Column(DateTime(timezone=True))
    data_pagamento = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    updated_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class FeriasModel(Base):
    """Modelo de ferias."""

    __tablename__ = "ferias"
    __table_args__ = {"schema": "rh"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    servidor_id = Column(Text, nullable=False)
    periodo_aquisitivo_inicio = Column(Date)
    periodo_aquisitivo_fim = Column(Date)
    data_inicio_gozo = Column(Date)
    data_fim_gozo = Column(Date)
    dias = Column(Integer, nullable=False, server_default="30")
    parcela = Column(Integer, nullable=False, server_default="1")
    status = Column(Text, nullable=False, server_default="planejada")
    data_aprovacao = Column(DateTime(timezone=True))
    data_cancelamento = Column(DateTime(timezone=True))
    motivo_cancelamento = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class FrequenciaModel(Base):
    """Modelo de frequencia diaria."""

    __tablename__ = "frequencias"
    __table_args__ = {"schema": "rh"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    servidor_id = Column(String(36), nullable=False)
    data = Column(Date, nullable=False)
    tipo = Column(Text, nullable=False, server_default="presenca")
    hora_entrada = Column(Time)
    hora_saida = Column(Time)
    minutos_atraso = Column(Integer, nullable=False, server_default="0")
    justificativa = Column(Text)
    desconto_folha = Column(Boolean, nullable=False, server_default=func.false())
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


__all__ = ["FolhaPagamentoModel", "FeriasModel", "FrequenciaModel"]
