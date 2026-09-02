"""Modelos ORM (SQLAlchemy) da persistência do domínio Cadastro (DOM-CUM).

Mapeiam as tabelas criadas pelas migrações 20260820_01 (fundacional) e
20260831_02 (enderecos/documentos/contatos + nome em pessoas_fisicas).
A criação de schema é responsabilidade exclusiva das migrações; estes
modelos servem para leitura e escrita.
"""

from __future__ import annotations

import uuid
from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Boolean, Date, DateTime, Numeric, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class CadastroBase(DeclarativeBase):
    """Base declarativa dos modelos ORM do domínio Cadastro."""


class AuditMixin:
    """Colunas de auditoria (padrão corporativo das migrações)."""

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


class PessoaModel(CadastroBase, AuditMixin):
    """Modelo ORM da tabela ``core.pessoas`` (entidade-mestra)."""

    __tablename__ = "pessoas"
    __table_args__ = {"schema": "core"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    tipo: Mapped[str] = mapped_column(Text, nullable=False)
    categoria: Mapped[str] = mapped_column(Text, nullable=False)
    unidade_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))

    def __repr__(self) -> str:  # pragma: no cover
        return f"<PessoaModel id={self.id} tipo={self.tipo}>"


class PessoaFisicaModel(CadastroBase, AuditMixin):
    """Modelo ORM da tabela ``core.pessoas_fisicas`` (extensão 1:1)."""

    __tablename__ = "pessoas_fisicas"
    __table_args__ = {"schema": "core"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    pessoa_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    data_nascimento: Mapped[date | None] = mapped_column(Date)
    sexo: Mapped[str | None] = mapped_column(Text)
    estado_civil: Mapped[str | None] = mapped_column(Text)
    mae: Mapped[str | None] = mapped_column(Text)
    pai: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<PessoaFisicaModel id={self.id} nome={self.nome}>"


class PessoaJuridicaModel(CadastroBase, AuditMixin):
    """Modelo ORM da tabela ``core.pessoas_juridicas`` (extensão 1:1)."""

    __tablename__ = "pessoas_juridicas"
    __table_args__ = {"schema": "core"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    pessoa_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, unique=True)
    razao_social: Mapped[str] = mapped_column(Text, nullable=False)
    nome_fantasia: Mapped[str | None] = mapped_column(Text)
    cnae_principal: Mapped[str | None] = mapped_column(Text)
    capital: Mapped[Decimal | None] = mapped_column(Numeric(15, 2))

    def __repr__(self) -> str:  # pragma: no cover
        return f"<PessoaJuridicaModel id={self.id} razao_social={self.razao_social}>"


class EnderecoModel(CadastroBase, AuditMixin):
    """Modelo ORM da tabela ``core.enderecos`` (histórico de vigência)."""

    __tablename__ = "enderecos"
    __table_args__ = {"schema": "core"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    pessoa_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    tipo: Mapped[str] = mapped_column(Text, nullable=False)
    logradouro: Mapped[str] = mapped_column(Text, nullable=False)
    numero: Mapped[str] = mapped_column(Text, nullable=False)
    complemento: Mapped[str | None] = mapped_column(Text)
    bairro: Mapped[str | None] = mapped_column(Text)
    cep: Mapped[str | None] = mapped_column(Text)
    cidade: Mapped[str | None] = mapped_column(Text)
    estado: Mapped[str | None] = mapped_column(Text)
    pais: Mapped[str | None] = mapped_column(Text)
    principal: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    vigencia_inicio: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    vigencia_fim: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    motivo_alteracao: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<EnderecoModel id={self.id} pessoa_id={self.pessoa_id}>"


class DocumentoModel(CadastroBase, AuditMixin):
    """Modelo ORM da tabela ``core.documentos`` (número: dado LGPD)."""

    __tablename__ = "documentos"
    __table_args__ = {"schema": "core"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    pessoa_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    tipo: Mapped[str] = mapped_column(Text, nullable=False)
    numero: Mapped[str] = mapped_column(Text, nullable=False)
    orgao_emissor: Mapped[str | None] = mapped_column(Text)
    data_emissao: Mapped[date | None] = mapped_column(Date)
    data_validade: Mapped[date | None] = mapped_column(Date)
    principal: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<DocumentoModel id={self.id} tipo={self.tipo}>"


class ContatoModel(CadastroBase, AuditMixin):
    """Modelo ORM da tabela ``core.contatos``."""

    __tablename__ = "contatos"
    __table_args__ = {"schema": "core"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    pessoa_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    tipo: Mapped[str] = mapped_column(Text, nullable=False)
    valor: Mapped[str] = mapped_column(Text, nullable=False)
    principal: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<ContatoModel id={self.id} tipo={self.tipo}>"


class UnidadeAdministrativaModel(CadastroBase, AuditMixin):
    """Modelo ORM da tabela ``core.unidades_administrativas`` (hierárquica)."""

    __tablename__ = "unidades_administrativas"
    __table_args__ = {"schema": "core"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    unidade_pai_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    codigo_ibge: Mapped[str | None] = mapped_column(Text)
    codigo_siafi: Mapped[str | None] = mapped_column(Text)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    sigla: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<UnidadeAdministrativaModel id={self.id} nome={self.nome}>"


__all__ = [
    "CadastroBase",
    "PessoaModel",
    "PessoaFisicaModel",
    "PessoaJuridicaModel",
    "EnderecoModel",
    "DocumentoModel",
    "ContatoModel",
    "UnidadeAdministrativaModel",
]
