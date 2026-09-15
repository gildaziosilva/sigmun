"""Entidades do domínio de Gestão Documental."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class StatusDocumento(Enum):
    """Status de um documento."""

    RASCUNHO = "rascunho"
    ATIVO = "ativo"
    ARQUIVADO = "arquivado"
    ENCERRADO = "encerrado"
    REJEITADO = "rejeitado"


class TipoDestinacao(Enum):
    """Tipo de destinação de documento."""

    ELIMINACAO = "eliminacao"
    GUARDA_PERMANENTE = "guarda_permanente"
    PRORROGACAO = "prorrogacao"


class TipoTramitacao(Enum):
    """Tipo de movimentação de tramitação."""

    ENVIO = "envio"
    RECEPCAO = "recepcao"
    DEVOLVIDO = "devolvido"
    ARQUIVAMENTO = "arquivamento"
    RESTAURACAO = "restauracao"


@dataclass
class ClassificacaoDocumental:
    """Entidade de Classificação Documental."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    nivel: int = 0
    classificacao_pai_id: str = ""
    prazo_retencao: int = 0
    unidade_destino_id: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return not self.is_deleted

    @property
    def foi_excluido(self) -> bool:
        return self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo

    @property
    def eh_raiz(self) -> bool:
        return not self.classificacao_pai_id

    @property
    def is_root(self) -> bool:
        return self.eh_raiz


@dataclass
class Documento:
    """Entidade de Documento (núcleo do DOM-GDO)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    numero: str = ""
    ano: int = 0
    tipo_documental_id: str = ""
    titulo: str = ""
    descricao: str = ""
    data_criacao: datetime | None = None
    data_recebimento: datetime | None = None
    data_arquivamento: datetime | None = None
    data_encerramento: datetime | None = None
    data_eliminacao: datetime | None = None
    unidade_autor_id: str = ""
    unidade_arquivo_id: str = ""
    processo_id: str = ""
    status: StatusDocumento = StatusDocumento.RASCUNHO
    is_sigiloso: bool = False
    conteudo_ref: str = ""
    hash_integridade: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    updated_by: str = ""
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return not self.is_deleted

    @property
    def foi_excluido(self) -> bool:
        return self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo

    @property
    def is_assinado(self) -> bool:
        return bool(self.hash_integridade)


@dataclass
class VersaoDocumento:
    """Entidade de Versão de Documento (imutável após criação)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    documento_id: str = ""
    numero_versao: int = 1
    conteudo_ref: str = ""
    hash_integridade: str = ""
    data_versao: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return not self.is_deleted

    @property
    def foi_excluido(self) -> bool:
        return self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo


@dataclass
class TramitacaoDocumento:
    """Entidade de Tramitação de Documento."""

    id: str = field(default_factory=lambda: str(uuid4()))
    documento_id: str = ""
    unidade_origem_id: str = ""
    unidade_destino_id: str = ""
    tipo: TipoTramitacao = TipoTramitacao.ENVIO
    data_envio: datetime | None = None
    data_recebimento: datetime | None = None
    data_devolucao: datetime | None = None
    motivo: str = ""
    observacao: str = ""
    created_by: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None

    @property
    def is_concluida(self) -> bool:
        return self.data_recebimento is not None or self.data_devolucao is not None


@dataclass
class ProcessoDocumento:
    """Entidade de Processo Documental."""

    id: str = field(default_factory=lambda: str(uuid4()))
    numero: str = ""
    ano: int = 0
    tipo_processo_id: str = ""
    titulo: str = ""
    descricao: str = ""
    unidade_autor_id: str = ""
    data_abertura: datetime = field(default_factory=datetime.utcnow)
    data_encerramento: datetime | None = None
    status: str = "aberto"
    is_encerrado: bool = False
    created_by: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return not self.is_deleted

    @property
    def foi_excluido(self) -> bool:
        return self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo


@dataclass
class TabelaTemporalidade:
    """Entidade de Tabela de Temporalidade."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    prazo_tempo: int = 0
    unidade_tempo: str = "meses"
    evento_fim: str = ""
    tipo_destinacao: TipoDestinacao = TipoDestinacao.ELIMINACAO
    is_ativo: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return not self.is_deleted

    @property
    def foi_excluido(self) -> bool:
        return self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo


@dataclass
class TipoDocumental:
    """Entidade de Tipo Documental (referência para documentos)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    is_ativo: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None

    @property
    def is_active(self) -> bool:
        return self.is_ativo


@dataclass
class ArquivamentoDocumento:
    """Entidade de Arquivamento de Documento."""

    id: str = field(default_factory=lambda: str(uuid4()))
    documento_id: str = ""
    data_arquivamento: datetime = field(default_factory=datetime.utcnow)
    data_restauracao: datetime | None = None
    created_by: str = ""
    observacao: str = ""
    is_restaurado: bool = False

    @property
    def is_ativo(self) -> bool:
        return not self.is_restaurado


@dataclass
class AssinaturaDocumento:
    """Entidade de Assinatura Digital de Documento."""

    id: str = field(default_factory=lambda: str(uuid4()))
    documento_id: str = ""
    signatario_id: str = ""
    data_assinatura: datetime = field(default_factory=datetime.utcnow)
    hash_assinatura: str = ""
    certificado_id: str = ""
    is_valida: bool = True
    is_revogada: bool = False

    @property
    def is_ativa(self) -> bool:
        return self.is_valida and not self.is_revogada


__all__ = [
    "StatusDocumento",
    "TipoDestinacao",
    "TipoTramitacao",
    "ClassificacaoDocumental",
    "Documento",
    "VersaoDocumento",
    "TramitacaoDocumento",
    "ProcessoDocumento",
    "TabelaTemporalidade",
    "ArquivamentoDocumento",
    "AssinaturaDocumento",
    "TipoDocumental",
]
