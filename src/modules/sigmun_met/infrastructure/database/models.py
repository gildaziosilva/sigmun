"""Modelos ORM (SQLAlchemy) da persistência do domínio Metadados Corporativos.

Mapeiam as tabelas criadas pela migração 20260901_01 (alembic).
A criação de schema é responsabilidade exclusiva das migrações; estes
modelos servem para leitura e escrita.
"""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import JSON, DateTime, Integer, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class MetBase(DeclarativeBase):
    """Base declarativa dos modelos ORM do domínio Metadados Corporativos."""


class MetadadoModel(MetBase):
    """Modelo ORM da tabela `met.metadados`."""

    __tablename__ = "metadados"
    __table_args__ = {"schema": "met"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    tipo_dado: Mapped[str] = mapped_column(Text, nullable=False, default="texto")
    obrigatorio: Mapped[bool] = mapped_column(nullable=False, default=False)
    multi_valor: Mapped[bool] = mapped_column(nullable=False, default=False)
    aplicavel_a: Mapped[str] = mapped_column(Text, nullable=False, default="")
    valor_padrao: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(Text, nullable=False, default="ativo")
    config_json: Mapped[dict | None] = mapped_column("config", JSON)

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
        return f"<MetadadoModel id={self.id} codigo={self.codigo}>"


class ValorMetadadoModel(MetBase):
    """Modelo ORM da tabela `met.valores_metadados`."""

    __tablename__ = "valores_metadados"
    __table_args__ = {"schema": "met"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    metadado_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    entidade_tipo: Mapped[str] = mapped_column(Text, nullable=False)
    entidade_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    valor: Mapped[str] = mapped_column(Text, nullable=False)

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
        return f"<ValorMetadadoModel id={self.id} metadado={self.metadado_id}>"


class ClassificacaoModel(MetBase):
    """Modelo ORM da tabela `met.classificacoes`."""

    __tablename__ = "classificacoes"
    __table_args__ = {"schema": "met"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, default="confidencialidade")
    nivel: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    cor: Mapped[str | None] = mapped_column(Text)

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
        return f"<ClassificacaoModel id={self.id} codigo={self.codigo}>"


class TaxonomiaModel(MetBase):
    """Modelo ORM da tabela `met.taxonomias`."""

    __tablename__ = "taxonomias"
    __table_args__ = {"schema": "met"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    termos_ids: Mapped[str] = mapped_column(Text, nullable=False, default="")

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
        return f"<TaxonomiaModel id={self.id} codigo={self.codigo}>"


class TermoTaxonomiaModel(MetBase):
    """Modelo ORM da tabela `met.termos_taxonomias`."""

    __tablename__ = "termos_taxonomias"
    __table_args__ = {"schema": "met"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    taxonomia_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    termo_pai_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    codigo: Mapped[str] = mapped_column(Text, nullable=False)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    sinonimos: Mapped[str] = mapped_column(Text, nullable=False, default="")
    ordem: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

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
        return f"<TermoTaxonomiaModel id={self.id} codigo={self.codigo}>"


__all__ = [
    "MetBase",
    "MetadadoModel",
    "ValorMetadadoModel",
    "ClassificacaoModel",
    "TaxonomiaModel",
    "TermoTaxonomiaModel",
]
