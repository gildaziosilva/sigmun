"""Modelos ORM (SQLAlchemy) da persistência do domínio Compras.

Mapeiam as tabelas criadas pela migração 20260820_01 (alembic).
A criação de schema é responsabilidade exclusiva das migrações;
estes modelos servem para leitura e escrita.
"""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import DateTime, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ComprasBase(DeclarativeBase):
    """Base declarativa dos modelos ORM do domínio Compras."""


class FornecedorModel(ComprasBase):
    """Modelo ORM da tabela ``core.fornecedores``.

    Referências:
      - Modelo Físico: Tabela core.fornecedores
      - ENT-COMPRAS-007 – Fornecedor
    """

    __tablename__ = "fornecedores"
    __table_args__ = {"schema": "core"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    pessoa_juridica_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), nullable=False, unique=True
    )
    situacao_cadastro: Mapped[str] = mapped_column(Text, nullable=False, default="ATIVO")
    macro_categoria: Mapped[str | None] = mapped_column(Text)

    # Colunas de auditoria (padrão corporativo)
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

    def __repr__(self) -> str:  # pragma: no cover
        return f"<FornecedorModel id={self.id} situacao={self.situacao_cadastro}>"


__all__ = ["ComprasBase", "FornecedorModel"]
