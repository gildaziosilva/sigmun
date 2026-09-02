"""Modelos ORM (SQLAlchemy) da persistência do domínio Compras.

Mapeiam as tabelas criadas pela migração 20260820_01 (alembic).
A criação de schema é responsabilidade exclusiva das migrações;
estes modelos servem para leitura e escrita.
"""

from __future__ import annotations

import uuid
from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import JSON, Date, DateTime, Numeric, Text, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ComprasBase(DeclarativeBase):
    """Base declarativa dos modelos ORM do domínio Compras."""


class UnidadeAdministrativaModel(ComprasBase):
    """Modelo ORM mínimo da tabela ``core.unidades_administrativas``.

    Mapeamento para validação de vínculos; o CRUD completo pertence ao
    domínio de Administração.
    """

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


class ProcessoDocumentalModel(ComprasBase):
    """Modelo ORM da tabela ``core.processos_documentais``.

    Referências:
      - Modelo Físico / migration 20260820_01
      - RN-COMPRAS-025 – Processo Único
    """

    __tablename__ = "processos_documentais"
    __table_args__ = {"schema": "core"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    unidade_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    numero: Mapped[str] = mapped_column(Text, nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)
    assunto: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)

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
        return f"<ProcessoDocumentalModel id={self.id} numero={self.numero}>"


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


class ItemCompraModel(ComprasBase):
    """Modelo ORM da tabela ``compras.itens_compras``.

    Referências:
      - Modelo Físico / migration 20260820_01
      - ENT-COMPRAS-004 – Item da Contratação
    """

    __tablename__ = "itens_compras"
    __table_args__ = {"schema": "compras"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    compra_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    descricao: Mapped[str] = mapped_column(Text, nullable=False)
    quantidade: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)
    valor_unitario: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)
    valor_total: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)

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
        return f"<ItemCompraModel id={self.id} compra_id={self.compra_id}>"


class CompraModel(ComprasBase):
    """Modelo ORM da tabela ``compras.compras``.

    Referências:
      - Modelo Físico / migration 20260820_01
      - Processo de Contratação (consolidado) – ver 013-Modelo-de-Dados
    """

    __tablename__ = "compras"
    __table_args__ = {"schema": "compras"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    processo_documental_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    fornecedor_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    unidade_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    numero: Mapped[str] = mapped_column(Text, nullable=False)
    data: Mapped[date] = mapped_column(Date, nullable=False)
    valor_total: Mapped[Decimal | None] = mapped_column(Numeric(15, 2))
    situacao: Mapped[str] = mapped_column(Text, nullable=False)
    pendencias_impeditivas: Mapped[bool] = mapped_column(
        nullable=False, server_default=text("false")
    )

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
        return f"<CompraModel id={self.id} numero={self.numero} situacao={self.situacao}>"


class ContratoModel(ComprasBase):
    """Modelo ORM da tabela ``compras.contratos``.

    Referências:
      - Modelo Físico / migration 20260820_01
      - ENT-COMPRAS-009 – Contrato
    """

    __tablename__ = "contratos"
    __table_args__ = {"schema": "compras"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    processo_documental_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    fornecedor_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    unidade_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    licitacao_master_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    compra_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    numero: Mapped[str] = mapped_column(Text, nullable=False)
    data_inicio: Mapped[date] = mapped_column(Date, nullable=False)
    data_fim: Mapped[date | None] = mapped_column(Date)
    valor: Mapped[Decimal | None] = mapped_column(Numeric(15, 2))
    objeto: Mapped[str | None] = mapped_column(Text)
    situacao: Mapped[str] = mapped_column(Text, nullable=False, default="EM_ELABORACAO")

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
        return f"<ContratoModel id={self.id} numero={self.numero} situacao={self.situacao}>"


class TrilhaAuditoriaModel(ComprasBase):
    """Modelo ORM da trilha de auditoria (tabela ``auditoria.eventos``).

    Referências:
      - 017-Modelo-de-Auditoria (seções 26/37/39): registro append-only,
        armazenamento logicamente separado dos dados transacionais.

    A tabela não recebe UPDATE/DELETE pela aplicação: somente INSERT e SELECT.
    """

    __tablename__ = "eventos"
    __table_args__ = {"schema": "auditoria"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    ocorrido_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    categoria: Mapped[str] = mapped_column(Text, nullable=False)
    tipo_evento: Mapped[str] = mapped_column(Text, nullable=False)
    ator_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    ator_perfil: Mapped[str | None] = mapped_column(Text)
    origem: Mapped[str] = mapped_column(Text, nullable=False)
    operacao: Mapped[str] = mapped_column(Text, nullable=False)
    recurso_tipo: Mapped[str] = mapped_column(Text, nullable=False)
    recurso_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    chave_negocio: Mapped[str | None] = mapped_column(Text)
    resultado: Mapped[str] = mapped_column(Text, nullable=False)
    correlation_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    justificativa: Mapped[str | None] = mapped_column(Text)
    detalhes: Mapped[dict | None] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"<TrilhaAuditoriaModel id={self.id} categoria={self.categoria} "
            f"tipo_evento={self.tipo_evento}>"
        )


__all__ = [
    "ComprasBase",
    "UnidadeAdministrativaModel",
    "ProcessoDocumentalModel",
    "FornecedorModel",
    "ItemCompraModel",
    "CompraModel",
    "ContratoModel",
    "TrilhaAuditoriaModel",
]
