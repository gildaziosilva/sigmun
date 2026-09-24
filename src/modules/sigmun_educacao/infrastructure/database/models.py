"""Modelos SQLAlchemy do DOM-EDU (schema edu)."""

from __future__ import annotations

import uuid

from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, Text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AlunoModel(Base):
    """Modelo de alunos da rede municipal."""

    __tablename__ = "alunos"
    __table_args__ = {"schema": "edu"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(Text, nullable=False)
    cpf = Column(Text)
    data_nascimento = Column(Text)
    sexo = Column(Text, nullable=False, server_default="ignorado")
    nome_mae = Column(Text)
    telefone = Column(Text)
    endereco = Column(Text)
    status = Column(Text, nullable=False, server_default="ativo")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class MatriculaModel(Base):
    """Modelo de matriculas escolares."""

    __tablename__ = "matriculas"
    __table_args__ = {"schema": "edu"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    aluno_id = Column(Text, nullable=False)
    escola = Column(Text, nullable=False)
    serie = Column(Text, nullable=False)
    turno = Column(Text, nullable=False, server_default="manha")
    ano_letivo = Column(Integer, nullable=False, server_default="0")
    data_matricula = Column(Date)
    status = Column(Text, nullable=False, server_default="ativa")
    escola_destino = Column(Text)
    motivo = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)


class LancamentoDiarioModel(Base):
    """Modelo do diario de classe digital."""

    __tablename__ = "lancamentos_diario"
    __table_args__ = {"schema": "edu"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    matricula_id = Column(Text, nullable=False)
    data = Column(Date)
    presente = Column(Boolean, nullable=False, server_default=func.true())
    nota = Column(Float)
    observacao = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(Text)


class RotaTransporteModel(Base):
    """Modelo de rotas de transporte escolar."""

    __tablename__ = "rotas_transporte"
    __table_args__ = {"schema": "edu"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    identificacao = Column(Text, nullable=False)
    veiculo = Column(Text)
    motorista = Column(Text, nullable=False)
    vagas = Column(Integer, nullable=False, server_default="0")
    turno = Column(Text, nullable=False, server_default="manha")
    status = Column(Text, nullable=False, server_default="ativa")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)


class PassagemTransporteModel(Base):
    """Modelo de passagens de transporte escolar."""

    __tablename__ = "passagens_transporte"
    __table_args__ = {"schema": "edu"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    rota_id = Column(Text, nullable=False)
    matricula_id = Column(Text, nullable=False)
    data = Column(Date)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(Text)


class ItemMerendaModel(Base):
    """Modelo do estoque de merenda."""

    __tablename__ = "itens_merenda"
    __table_args__ = {"schema": "edu"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(Text, nullable=False)
    tipo = Column(Text, nullable=False, server_default="refeicao")
    estoque = Column(Float, nullable=False, server_default="0")
    estoque_minimo = Column(Float, nullable=False, server_default="0")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Text)
    is_deleted = Column(Boolean, nullable=False, server_default=func.false())


class DistribuicaoMerendaModel(Base):
    """Modelo de distribuicoes de merenda."""

    __tablename__ = "distribuicoes_merenda"
    __table_args__ = {"schema": "edu"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    matricula_id = Column(Text, nullable=False)
    item_id = Column(Text, nullable=False)
    quantidade = Column(Float, nullable=False, server_default="0")
    data = Column(Date)
    refeicao = Column(Text, nullable=False, server_default="almoco")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(Text)


__all__ = [
    "Base",
    "AlunoModel",
    "MatriculaModel",
    "LancamentoDiarioModel",
    "RotaTransporteModel",
    "PassagemTransporteModel",
    "ItemMerendaModel",
    "DistribuicaoMerendaModel",
]
