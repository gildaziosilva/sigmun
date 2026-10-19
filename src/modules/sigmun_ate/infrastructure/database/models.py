"""Modelos ORM (SQLAlchemy) da persistência do domínio Atendimento ao Cidadão (DOM-ATE)."""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import JSON, DateTime, Integer, Text, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class AteBase(DeclarativeBase):
    """Base declarativa dos modelos ORM do domínio Atendimento ao Cidadão."""

    pass


class ServicoAtendimentoModel(AteBase):
    __tablename__ = "servicos_atendimento"
    __table_args__ = (
        UniqueConstraint("codigo", name="uq_servicos_atendimento_codigo"),
        {"schema": "ate"},
    )
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    prioridade: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    ativo: Mapped[bool] = mapped_column(nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[str | None] = mapped_column(Text)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"<ServicoAtendimentoModel id={self.id} codigo={self.codigo}>"


class CanalAtendimentoModel(AteBase):
    __tablename__ = "canais_atendimento"
    __table_args__ = (
        UniqueConstraint("codigo", name="uq_canais_atendimento_codigo"),
        {"schema": "ate"},
    )
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    tipo: Mapped[str] = mapped_column(Text, nullable=False)
    ativo: Mapped[bool] = mapped_column(nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[str | None] = mapped_column(Text)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"<CanalAtendimentoModel id={self.id} codigo={self.codigo}>"


class UnidadeAtendimentoModel(AteBase):
    __tablename__ = "unidades_atendimento"
    __table_args__ = (
        UniqueConstraint("codigo", name="uq_unidades_atendimento_codigo"),
        {"schema": "ate"},
    )
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    ativo: Mapped[bool] = mapped_column(nullable=False, default=True)
    max_rechamadas: Mapped[int] = mapped_column(Integer, nullable=False, default=3)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[str | None] = mapped_column(Text)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"<UnidadeAtendimentoModel id={self.id} codigo={self.codigo}>"


class GuicheModel(AteBase):
    __tablename__ = "guiches"
    __table_args__ = {"schema": "ate"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    unidade_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    numero: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    ativo: Mapped[bool] = mapped_column(nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[str | None] = mapped_column(Text)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"<GuicheModel id={self.id} numero={self.numero}>"


class FilaAtendimentoModel(AteBase):
    __tablename__ = "filas_atendimento"
    __table_args__ = {"schema": "ate"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    unidade_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    servico_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    data: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    status: Mapped[str] = mapped_column(Text, nullable=False, default="aberta")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[str | None] = mapped_column(Text)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:
        return (
            f"<FilaAtendimentoModel id={self.id} unidade_id={self.unidade_id} status={self.status}>"
        )


class TriagemModel(AteBase):
    __tablename__ = "triagens"
    __table_args__ = {"schema": "ate"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    servico_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    data_hora: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    classificacao: Mapped[str] = mapped_column(Text, nullable=False)
    prioridade: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    observacao: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[str | None] = mapped_column(Text)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"<TriagemModel id={self.id} servico_id={self.servico_id}>"


class SenhaModel(AteBase):
    __tablename__ = "senhas"
    __table_args__ = {"schema": "ate"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    fila_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    servico_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    triagem_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    numero: Mapped[str] = mapped_column(Text, nullable=False)
    data_hora_emissao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    prioridade: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    status: Mapped[str] = mapped_column(Text, nullable=False, default="emitida")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[str | None] = mapped_column(Text)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"<SenhaModel id={self.id} numero={self.numero} status={self.status}>"


class ChamadaModel(AteBase):
    __tablename__ = "chamadas"
    __table_args__ = {"schema": "ate"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    senha_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    guiche_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    unidade_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    operador: Mapped[str] = mapped_column(Text, nullable=False)
    data_hora: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    ordem: Mapped[int] = mapped_column(Integer, nullable=False)
    tentativa: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    resultado: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[str | None] = mapped_column(Text)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"<ChamadaModel id={self.id} senha_id={self.senha_id} ordem={self.ordem}>"


class AtendimentoModel(AteBase):
    __tablename__ = "atendimentos"
    __table_args__ = {"schema": "ate"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    chamada_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    canal_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    inicio: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    fim: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    status: Mapped[str] = mapped_column(Text, nullable=False, default="aguardando")
    descricao: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[str | None] = mapped_column(Text)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"<AtendimentoModel id={self.id} status={self.status}>"


class AvaliacaoAtendimentoModel(AteBase):
    __tablename__ = "avaliacoes_atendimento"
    __table_args__ = {"schema": "ate"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    atendimento_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    nota: Mapped[int] = mapped_column(Integer, nullable=False)
    comentario: Mapped[str | None] = mapped_column(Text)
    data_hora: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[str | None] = mapped_column(Text)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"<AvaliacaoAtendimentoModel id={self.id} atendimento_id={self.atendimento_id} nota={self.nota}>"


class EncaminhamentoModel(AteBase):
    __tablename__ = "encaminhamentos"
    __table_args__ = {"schema": "ate"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    atendimento_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    data_hora: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    destino: Mapped[str] = mapped_column(Text, nullable=False)
    motivo: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(Text, nullable=False, default="pendente")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    created_by: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_by: Mapped[str | None] = mapped_column(Text)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"<EncaminhamentoModel id={self.id} atendimento_id={self.atendimento_id} status={self.status}>"


class EventoOutboxModel(AteBase):
    __tablename__ = "eventos_outbox"
    __table_args__ = {"schema": "ate"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    topico: Mapped[str] = mapped_column(Text, nullable=False)
    evento_nome: Mapped[str] = mapped_column(Text, nullable=False)
    agregado_tipo: Mapped[str] = mapped_column(Text, nullable=False)
    agregado_id: Mapped[str] = mapped_column(Text, nullable=False)
    payload: Mapped[dict] = mapped_column(JSON, nullable=False)
    status: Mapped[str] = mapped_column(Text, nullable=False, default="pendente")
    tentativas: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    ultimo_erro: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    def __repr__(self) -> str:
        return f"<EventoOutboxModel id={self.id} topico={self.topico} status={self.status}>"


__all__ = [
    "AteBase",
    "ServicoAtendimentoModel",
    "CanalAtendimentoModel",
    "UnidadeAtendimentoModel",
    "GuicheModel",
    "FilaAtendimentoModel",
    "TriagemModel",
    "SenhaModel",
    "ChamadaModel",
    "AtendimentoModel",
    "AvaliacaoAtendimentoModel",
    "EncaminhamentoModel",
    "EventoOutboxModel",
]
