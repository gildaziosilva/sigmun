"""Modelos SQLAlchemy do DOM-TRI (schema trib)."""

from __future__ import annotations

import uuid

from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, String, Text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ContribuinteModel(Base):
    """Modelo de contribuintes."""

    __tablename__ = "contribuintes"
    __table_args__ = {"schema": "trib"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tipo = Column(Text, nullable=False, server_default="pf")
    nome = Column(Text, nullable=False)
    cpf_cnpj = Column(String(14), nullable=False, unique=True)
    inscricao_municipal = Column(Text)
    email = Column(Text)
    telefone = Column(Text)
    endereco = Column(Text)
    status = Column(Text, nullable=False, server_default="ativo")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class ImovelModel(Base):
    """Modelo de imóveis (IPTU)."""

    __tablename__ = "imoveis"
    __table_args__ = {"schema": "trib"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    contribuinte_id = Column(Text, nullable=False)
    inscricao_imobiliaria = Column(Text, nullable=False, unique=True)
    logradouro = Column(Text)
    numero = Column(Text)
    bairro = Column(Text)
    cidade = Column(Text)
    uf = Column(String(2))
    cep = Column(String(8))
    area_terreno = Column(Float, nullable=False, server_default="0")
    area_construida = Column(Float, nullable=False, server_default="0")
    valor_venal = Column(Float, nullable=False, server_default="0")
    aliquota = Column(Float, nullable=False, server_default="0")
    status = Column(Text, nullable=False, server_default="ativo")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class LancamentoModel(Base):
    """Modelo de lançamentos (créditos tributários)."""

    __tablename__ = "lancamentos"
    __table_args__ = {"schema": "trib"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    contribuinte_id = Column(Text, nullable=False)
    imovel_id = Column(Text)
    tipo_tributo = Column(Text, nullable=False, server_default="taxa")
    exercicio = Column(Integer, nullable=False)
    numero_lancamento = Column(Text, nullable=False, unique=True)
    descricao = Column(Text)
    base_calculo = Column(Float, nullable=False, server_default="0")
    aliquota = Column(Float, nullable=False, server_default="0")
    valor_tributo = Column(Float, nullable=False, server_default="0")
    juros = Column(Float, nullable=False, server_default="0")
    multa = Column(Float, nullable=False, server_default="0")
    valor_total = Column(Float, nullable=False, server_default="0")
    data_vencimento = Column(Date)
    status = Column(Text, nullable=False, server_default="lancado")
    data_pagamento = Column(Date)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class DividaAtivaModel(Base):
    """Modelo de inscrições em dívida ativa."""

    __tablename__ = "divida_ativa"
    __table_args__ = {"schema": "trib"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lancamento_id = Column(Text, nullable=False, unique=True)
    numero_inscricao = Column(Text, nullable=False, unique=True)
    data_inscricao = Column(Date)
    valor_original = Column(Float, nullable=False, server_default="0")
    valor_atualizado = Column(Float, nullable=False, server_default="0")
    status = Column(Text, nullable=False, server_default="ativa")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class CertidaoModel(Base):
    """Modelo de certidões fiscais."""

    __tablename__ = "certidoes"
    __table_args__ = {"schema": "trib"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    contribuinte_id = Column(Text, nullable=False)
    tipo = Column(Text, nullable=False, server_default="negativa")
    numero = Column(Text, nullable=False, unique=True)
    data_emissao = Column(Date)
    valido_ate = Column(Date)
    observacao = Column(Text)
    status = Column(Text, nullable=False, server_default="emitida")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


__all__ = [
    "Base",
    "ContribuinteModel",
    "ImovelModel",
    "LancamentoModel",
    "DividaAtivaModel",
    "CertidaoModel",
]