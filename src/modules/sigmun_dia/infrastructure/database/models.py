"""Modelos ORM (SQLAlchemy) da persistência do domínio Gestão de Diárias, Viagens e Deslocamentos."""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, Text, func
from sqlalchemy.dialects.postgresql import UUID as PgUUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class DiaBase(DeclarativeBase):
    """Base declarativa dos modelos ORM do domínio DOM-DIA."""

    pass


# =============================================================================
# Modelos de Viagem
# =============================================================================


class ViagemModel(DiaBase):
    """Modelo ORM da tabela `dia.viagens`."""

    __tablename__ = "viagens"
    __table_args__ = {"schema": "dia"}

    id: Mapped[uuid.UUID] = mapped_column(PgUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    servidor_id: Mapped[str] = mapped_column(Text, nullable=False)
    dota_id: Mapped[str] = mapped_column(Text, nullable=False)
    motivo: Mapped[str] = mapped_column(Text, nullable=False)
    cargo_ocupado: Mapped[str] = mapped_column(Text)
    unidade_origem_id: Mapped[str] = mapped_column(Text, nullable=False)
    unidade_destino_id: Mapped[str] = mapped_column(Text, nullable=False)
    data_inicio: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_fim: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    destino: Mapped[str] = mapped_column(Text)
    is_antecipacao: Mapped[bool] = mapped_column(nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<ViagemModel id={self.id} destino={self.destino}>"


# =============================================================================
# Modelos de Diária
# =============================================================================


class DiariaModel(DiaBase):
    """Modelo ORM da tabela `dia.diarias`."""

    __tablename__ = "diarias"
    __table_args__ = {"schema": "dia"}

    id: Mapped[uuid.UUID] = mapped_column(PgUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    viagem_id: Mapped[str] = mapped_column(Text, nullable=False)
    servidor_id: Mapped[str] = mapped_column(Text, nullable=False)
    dota_id: Mapped[str] = mapped_column(Text, nullable=False)
    categoria: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str] = mapped_column(Text)
    data_inicio: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_fim: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    valor_diaria: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    valor_total: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    status: Mapped[str] = mapped_column(Text, nullable=False, default="solicitada")
    data_solicitacao: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    data_autorizacao: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_calculo: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_concessao: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_inicio_prestacao: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_fim_prestacao: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_pagamento: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_aprovacao: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_glosa: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_restituicao: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_cancelamento: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    motivo_cancelamento: Mapped[str] = mapped_column(Text)
    motivo_glosa: Mapped[str] = mapped_column(Text)
    valor_glosado: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    documento_prestacao_id: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str] = mapped_column(Text)
    updated_by: Mapped[str] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<DiariaModel id={self.id} status={self.status}>"


# =============================================================================
# Modelos de PrestacaoContas
# =============================================================================


class PrestacaoContasModel(DiaBase):
    """Modelo ORM da tabela `dia.prestacoes_contas`."""

    __tablename__ = "prestacoes_contas"
    __table_args__ = {"schema": "dia"}

    id: Mapped[uuid.UUID] = mapped_column(PgUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    diaria_id: Mapped[str] = mapped_column(Text, nullable=False)
    servidor_id: Mapped[str] = mapped_column(Text, nullable=False)
    dota_id: Mapped[str] = mapped_column(Text, nullable=False)
    data_emissao: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    data_vencimento: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    documento_id: Mapped[str] = mapped_column(Text)
    valor_previsto: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    valor_apresentado: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    valor_glosado: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    valor_liquido: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    status: Mapped[str] = mapped_column(Text, nullable=False, default="aberta")
    motivo_glosa: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<PrestacaoContasModel id={self.id} status={self.status}>"


# =============================================================================
# Modelos de EventoDiaria
# =============================================================================


class EventoDiariaModel(DiaBase):
    """Modelo ORM da tabela `dia.eventos_diarias`."""

    __tablename__ = "eventos_diarias"
    __table_args__ = {"schema": "dia"}

    id: Mapped[uuid.UUID] = mapped_column(PgUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    diaria_id: Mapped[str] = mapped_column(Text, nullable=False)
    status_anterior: Mapped[str] = mapped_column(Text, nullable=False)
    status_posterior: Mapped[str] = mapped_column(Text, nullable=False)
    usuario_id: Mapped[str] = mapped_column(Text, nullable=False)
    motivo: Mapped[str] = mapped_column(Text)
    data_evento: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    detalhes: Mapped[str] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"<EventoDiariaModel id={self.id} diaria_id={self.diaria_id}>"


__all__ = [
    "DiaBase",
    "ViagemModel",
    "DiariaModel",
    "PrestacaoContasModel",
    "EventoDiariaModel",
]
