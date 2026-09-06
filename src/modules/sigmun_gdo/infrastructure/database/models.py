"""Modelos ORM (SQLAlchemy) da persistência do domínio Gestão Documental."""
from __future__ import annotations
import uuid
from datetime import datetime
from sqlalchemy import JSON, DateTime, Integer, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class GdoBase(DeclarativeBase):
    """Base declarativa dos modelos ORM do domínio Gestão Documental."""
    pass

class DocumentoModel(GdoBase):
    """Modelo ORM da tabela `gdo.documentos`."""
    __tablename__ = "documentos"
    __table_args__ = {"schema": "gdo"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    numero: Mapped[str] = mapped_column(Text, nullable=False)
    ano: Mapped[int] = mapped_column(Integer, nullable=False)
    tipo_documental_id: Mapped[str] = mapped_column(Text, nullable=False)
    titulo: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    data_criacao: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_recebimento: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_arquivamento: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_encerramento: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_eliminacao: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    unidade_autor_id: Mapped[str] = mapped_column(Text, nullable=False)
    unidade_arquivo_id: Mapped[str | None] = mapped_column(Text)
    processo_id: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(Text, nullable=False, default="rascunho")
    is_sigiloso: Mapped[bool] = mapped_column(nullable=False, default=False)
    conteudo_ref: Mapped[str | None] = mapped_column(Text)
    hash_integridade: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_by: Mapped[str | None] = mapped_column(Text)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)
    def __repr__(self) -> str:
        return f"<DocumentoModel id={self.id} codigo={self.codigo}>"

class VersaoDocumentoModel(GdoBase):
    """Modelo ORM da tabela `gdo.versoes_documentos`."""
    __tablename__ = "versoes_documentos"
    __table_args__ = {"schema": "gdo"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    documento_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    numero_versao: Mapped[int] = mapped_column(Integer, nullable=False)
    conteudo_ref: Mapped[str | None] = mapped_column(Text)
    hash_integridade: Mapped[str | None] = mapped_column(Text)
    data_versao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by: Mapped[str | None] = mapped_column(Text)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)
    def __repr__(self) -> str:
        return f"<VersaoDocumentoModel id={self.id} documento_id={self.documento_id}>"

class TramitacaoDocumentoModel(GdoBase):
    """Modelo ORM da tabela `gdo.tramitacoes_documentos`."""
    __tablename__ = "tramitacoes_documentos"
    __table_args__ = {"schema": "gdo"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    documento_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    unidade_origem_id: Mapped[str] = mapped_column(Text, nullable=False)
    unidade_destino_id: Mapped[str] = mapped_column(Text, nullable=False)
    tipo: Mapped[str] = mapped_column(Text, nullable=False, default="envio")
    data_envio: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_recebimento: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    data_devolucao: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    motivo: Mapped[str | None] = mapped_column(Text)
    observacao: Mapped[str | None] = mapped_column(Text)
    created_by: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    def __repr__(self) -> str:
        return f"<TramitacaoDocumentoModel id={self.id} documento_id={self.documento_id}>"

class ProcessoDocumentoModel(GdoBase):
    """Modelo ORM da tabela `gdo.processos_documentos`."""
    __tablename__ = "processos_documentos"
    __table_args__ = {"schema": "gdo"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    numero: Mapped[str] = mapped_column(Text, nullable=False)
    ano: Mapped[int] = mapped_column(Integer, nullable=False)
    tipo_processo_id: Mapped[str] = mapped_column(Text, nullable=False)
    titulo: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    unidade_autor_id: Mapped[str] = mapped_column(Text, nullable=False)
    data_abertura: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    data_encerramento: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    status: Mapped[str] = mapped_column(Text, nullable=False, default="aberto")
    created_by: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)
    def __repr__(self) -> str:
        return f"<ProcessoDocumentoModel id={self.id} numero={self.numero}>"


class ClassificacaoDocumentalModel(GdoBase):
    """Modelo ORM da tabela `gdo.classificacoes_documentais`."""
    __tablename__ = "classificacoes_documentais"
    __table_args__ = {"schema": "gdo"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    nivel: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    classificacao_pai_id: Mapped[str | None] = mapped_column(Text)
    prazo_retencao: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    unidade_destino_id: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_by: Mapped[str | None] = mapped_column(Text)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)
    def __repr__(self) -> str:
        return f"<ClassificacaoDocumentalModel id={self.id} codigo={self.codigo}>"


class TabelaTemporalidadeModel(GdoBase):
    """Modelo ORM da tabela `gdo.tabelas_temporalidades`."""
    __tablename__ = "tabelas_temporalidades"
    __table_args__ = {"schema": "gdo"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    prazo_tempo: Mapped[int] = mapped_column(Integer, nullable=False)
    unidade_tempo: Mapped[str] = mapped_column(Text, nullable=False, default="meses")
    evento_fim: Mapped[str] = mapped_column(Text, nullable=False)
    tipo_destinacao: Mapped[str] = mapped_column(Text, nullable=False, default="eliminacao")
    is_ativo: Mapped[bool] = mapped_column(nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_by: Mapped[str | None] = mapped_column(Text)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)
    def __repr__(self) -> str:
        return f"<TabelaTemporalidadeModel id={self.id} codigo={self.codigo}>"


class ArquivamentoDocumentoModel(GdoBase):
    """Modelo ORM da tabela `gdo.arquivamentos_documentos`."""
    __tablename__ = "arquivamentos_documentos"
    __table_args__ = {"schema": "gdo"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    documento_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    data_arquivamento: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    data_restauracao: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(Text)
    observacao: Mapped[str | None] = mapped_column(Text)
    def __repr__(self) -> str:
        return f"<ArquivamentoDocumentoModel id={self.id} documento_id={self.documento_id}>"


class AssinaturaDocumentoModel(GdoBase):
    """Modelo ORM da tabela `gdo.assinaturas_documentos`."""
    __tablename__ = "assinaturas_documentos"
    __table_args__ = {"schema": "gdo"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    documento_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    signatario_id: Mapped[str] = mapped_column(Text, nullable=False)
    data_assinatura: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    hash_assinatura: Mapped[str] = mapped_column(Text, nullable=False)
    certificado_id: Mapped[str | None] = mapped_column(Text)
    is_valida: Mapped[bool] = mapped_column(nullable=False, default=True)
    is_revogada: Mapped[bool] = mapped_column(nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    def __repr__(self) -> str:
        return f"<AssinaturaDocumentoModel id={self.id} documento_id={self.documento_id}>"


class MetadadoDocumentoModel(GdoBase):
    """Modelo ORM da tabela `gdo.metadados_documentos`."""
    __tablename__ = "metadados_documentos"
    __table_args__ = {"schema": "gdo"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    documento_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    metadado_id: Mapped[str] = mapped_column(Text, nullable=False)
    valor: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    def __repr__(self) -> str:
        return f"<MetadadoDocumentoModel id={self.id} documento_id={self.documento_id}>"


class TipoDocumentalModel(GdoBase):
    """Modelo ORM da tabela `gdo.tipos_documentais` (referência)."""
    __tablename__ = "tipos_documentais"
    __table_args__ = {"schema": "gdo"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text)
    is_ativo: Mapped[bool] = mapped_column(nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_by: Mapped[str | None] = mapped_column(Text)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by: Mapped[str | None] = mapped_column(Text)
    def __repr__(self) -> str:
        return f"<TipoDocumentalModel id={self.id} codigo={self.codigo}>"


class EventoOutboxModel(GdoBase):
    """Modelo ORM da tabela `gdo.eventos_outbox` (Transactional Outbox).

    Eventos de integração são gravados na MESMA transação do negócio
    (014-Modelo-de-Integracao) e despachados depois para o barramento.
    """
    __tablename__ = "eventos_outbox"
    __table_args__ = {"schema": "gdo"}
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    topico: Mapped[str] = mapped_column(Text, nullable=False)
    evento_nome: Mapped[str] = mapped_column(Text, nullable=False)
    agregado_tipo: Mapped[str] = mapped_column(Text, nullable=False)
    agregado_id: Mapped[str] = mapped_column(Text, nullable=False)
    payload: Mapped[dict] = mapped_column(JSON, nullable=False)
    status: Mapped[str] = mapped_column(Text, nullable=False, default="pendente")
    tentativas: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    ultimo_erro: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    def __repr__(self) -> str:
        return f"<EventoOutboxModel id={self.id} topico={self.topico} status={self.status}>"


__all__ = [
    "GdoBase",
    "DocumentoModel",
    "VersaoDocumentoModel",
    "TramitacaoDocumentoModel",
    "ProcessoDocumentoModel",
    "ClassificacaoDocumentalModel",
    "TabelaTemporalidadeModel",
    "ArquivamentoDocumentoModel",
    "AssinaturaDocumentoModel",
    "MetadadoDocumentoModel",
    "TipoDocumentalModel",
    "EventoOutboxModel",
]
