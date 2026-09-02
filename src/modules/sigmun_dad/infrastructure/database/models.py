"""Modelos ORM (SQLAlchemy) da persistência do domínio Dados Corporativos.

Mapeiam as tabelas criadas pela migração 20260831_04 (alembic).
A criação de schema é responsabilidade exclusiva das migrações; estes
modelos servem para leitura e escrita.
"""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import JSON, DateTime, Float, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class DadBase(DeclarativeBase):
    """Base declarativa dos modelos ORM do domínio Dados Corporativos."""


class AtivoDadoModel(DadBase):
    """Modelo ORM da tabela `dad.ativos_dados`."""

    __tablename__ = "ativos_dados"
    __table_args__ = {"schema": "dad"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    descricao: Mapped[str | None] = mapped_column(Text)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, default="tabela")
    status: Mapped[str] = mapped_column(Text, nullable=False, default="PENDENTE")
    qualidade: Mapped[str] = mapped_column(Text, nullable=False, default="MEDIO")
    dono_id: Mapped[str | None] = mapped_column(Text)
    steward_id: Mapped[str | None] = mapped_column(Text)
    schema_origem: Mapped[str | None] = mapped_column(Text)
    tabela_origem: Mapped[str | None] = mapped_column(Text)
    classificacao: Mapped[str | None] = mapped_column(Text)
    tags: Mapped[str] = mapped_column(Text, nullable=False, default="")
    metadata_json: Mapped[dict | None] = mapped_column("metadata", JSON)

    # Colunas de auditoria
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))

    def __repr__(self) -> str:
        return f"<AtivoDadoModel id={self.id} nome={self.nome}>"


class CatalogoModel(DadBase):
    """Modelo ORM da tabela `dad.catalogos`."""

    __tablename__ = "catalogos"
    __table_args__ = {"schema": "dad"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    descricao: Mapped[str | None] = mapped_column(Text)
    dominio: Mapped[str | None] = mapped_column(Text)
    ativos_ids: Mapped[str] = mapped_column(Text, nullable=False, default="")

    # Colunas de auditoria
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))

    def __repr__(self) -> str:
        return f"<CatalogoModel id={self.id} nome={self.nome}>"


class LinhagemDadoModel(DadBase):
    """Modelo ORM da tabela `dad.linhagens`."""

    __tablename__ = "linhagens"
    __table_args__ = {"schema": "dad"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ativo_origem_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    ativo_destino_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    tipo_transformacao: Mapped[str | None] = mapped_column(Text)
    descricao: Mapped[str | None] = mapped_column(Text)
    regras: Mapped[str | None] = mapped_column(Text)

    # Colunas de auditoria
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))

    def __repr__(self) -> str:
        return f"<LinhagemDadoModel id={self.id} origem={self.ativo_origem_id}>"


class PoliticaDadoModel(DadBase):
    """Modelo ORM da tabela `dad.politicas`."""

    __tablename__ = "politicas"
    __table_args__ = {"schema": "dad"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    tipo: Mapped[str | None] = mapped_column(Text)
    regras: Mapped[str] = mapped_column(Text, nullable=False, default="")

    # Colunas de auditoria
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))

    def __repr__(self) -> str:
        return f"<PoliticaDadoModel id={self.id} codigo={self.codigo}>"


class QualidadeDadoModel(DadBase):
    """Modelo ORM da tabela `dad.qualidade_dados`."""

    __tablename__ = "qualidade_dados"
    __table_args__ = {"schema": "dad"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ativo_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    nivel: Mapped[str] = mapped_column(Text, nullable=False, default="MEDIO")
    score: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    criterios: Mapped[str] = mapped_column(Text, nullable=False, default="")
    observacao: Mapped[str | None] = mapped_column(Text)

    # Colunas de auditoria
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))

    def __repr__(self) -> str:
        return f"<QualidadeDadoModel id={self.id} ativo={self.ativo_id}>"


__all__ = [
    "DadBase",
    "AtivoDadoModel",
    "CatalogoModel",
    "LinhagemDadoModel",
    "PoliticaDadoModel",
    "QualidadeDadoModel",
]
