"""Modelos ORM (SQLAlchemy) da persistência do domínio Segurança da Informação.

Mapeiam as tabelas responsáveis por controles, políticas, incidentes,
chaves criptográficas e credenciais do domínio DOM-SEG.

Base declarativa usada nas migrações Alembic do SIGMUN.
"""

from __future__ import annotations

import logging
import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class SegurancaBase(DeclarativeBase):
    """Base declarativa dos modelos ORM do domínio Segurança da Informação."""

    pass


logger = logging.getLogger(__name__)


class ControleSegurancaModel(SegurancaBase):
    """Modelo ORM da tabela ``seg.controles_seguranca``.

    Mapeia a entidade `ControleSeguranca` do domínio, representando um
    controle de segurança da informação (baseado em famílias ISO 27001).
    """

    __tablename__ = "controles_seguranca"
    __table_args__ = {"schema": "seg"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str] = mapped_column(Text, nullable=True)
    tipo: Mapped[str] = mapped_column(Text, nullable=False)  # fisico, tecnico, administrativo
    categoria: Mapped[str] = mapped_column(
        Text, nullable=False
    )  # acesso, criptografia, incidente, conformidade, continuidade
    status: Mapped[str] = mapped_column(
        Text, nullable=False, default="planejado"
    )  # implementado, parcial, planejado
    nivel_risco: Mapped[str] = mapped_column(
        Text, nullable=False, default="medio"
    )  # baixo, medio, alto, critico
    responsavel_id: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<ControleSegurancaModel id={self.id} codigo={self.codigo}>"


class PoliticaSegurancaModel(SegurancaBase):
    """Modelo ORM da tabela ``seg.politicas_seguranca``.

    Mapeia a entidade `PoliticaSeguranca` do domínio, representando a
    política de segurança da informação do município.
    """

    __tablename__ = "politicas_seguranca"
    __table_args__ = {"schema": "seg"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    titulo: Mapped[str] = mapped_column(Text, nullable=False)
    conteudo: Mapped[str] = mapped_column(Text, nullable=False)
    versao: Mapped[str] = mapped_column(Text, nullable=False, default="1.0")
    aprovador_id: Mapped[str] = mapped_column(Text, nullable=True)
    data_aprovacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    data_revisao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    ativa: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<PoliticaSegurancaModel id={self.id} codigo={self.codigo}>"


class IncidenteSegurancaModel(SegurancaBase):
    """Modelo ORM da tabela ``seg.incidentes_seguranca``.

    Mapeia a entidade `IncidenteSeguranca` do domínio, representando um
    incidente de segurança da informação registrado no município.
    """

    __tablename__ = "incidentes_seguranca"
    __table_args__ = {"schema": "seg"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titulo: Mapped[str] = mapped_column(Text, nullable=False)
    descricao: Mapped[str] = mapped_column(Text, nullable=False)
    severidade: Mapped[str] = mapped_column(Text, nullable=False)  # baixa, media, alta, critica
    impacto: Mapped[str] = mapped_column(Text, nullable=True)
    categoria: Mapped[str] = mapped_column(Text, nullable=True)
    relator_id: Mapped[str] = mapped_column(Text, nullable=True)
    atribuido_a: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(
        Text, nullable=False, default="aberto"
    )  # aberto, em_analise, em_mitigacao, resolvido, encerrado
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    data_resolucao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<IncidenteSegurancaModel id={self.id} titulo={self.titulo}>"


class ChaveCriptograficaModel(SegurancaBase):
    """Modelo ORM da tabela ``seg.chaves_criptograficas``.

    Mapeia a entidade `ChaveCriptografica` do domínio, representando uma
    chave criptográfica gerenciada pelo município (AES256, RSA4096, ECDSA).
    """

    __tablename__ = "chaves_criptograficas"
    __table_args__ = {"schema": "seg"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    algoritmo: Mapped[str] = mapped_column(Text, nullable=False)  # AES256, RSA4096, ECDSA
    tipo: Mapped[str] = mapped_column(Text, nullable=False)  # simetrica, assimetrica
    tamanho_bits: Mapped[int] = mapped_column(nullable=False)  # 256, 4096, etc.
    status: Mapped[str] = mapped_column(
        Text, nullable=False, default="ativa"
    )  # ativa, revogada, expirada
    data_expiracao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    responsavel_id: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<ChaveCriptograficaModel id={self.id} nome={self.nome}>"


class CredencialModel(SegurancaBase):
    """Modelo ORM da tabela ``seg.credenciais``.

    Mapeia a entidade `Credencial` do domínio, representando uma credencial
    de acesso a sistemas externos ou internos (senha, certificado, chave API, token).
    """

    __tablename__ = "credenciais"
    __table_args__ = {"schema": "seg"}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    usuario_id: Mapped[str] = mapped_column(Text, nullable=False)
    tipo: Mapped[str] = mapped_column(Text, nullable=False)  # senha, certificado, chave_api, token
    identificador: Mapped[str] = mapped_column(
        Text, nullable=False
    )  # hash ou referência, nunca o valor real
    status: Mapped[str] = mapped_column(
        Text, nullable=False, default="ativa"
    )  # ativa, suspensa, expirada, revogada
    validade: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    ultimo_uso: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    tentativas_falhas: Mapped[int] = mapped_column(nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<CredencialModel id={self.id} tipo={self.tipo}>"


__all__ = [
    "ControleSegurancaModel",
    "PoliticaSegurancaModel",
    "IncidenteSegurancaModel",
    "ChaveCriptograficaModel",
    "CredencialModel",
    "SegurancaBase",
]
