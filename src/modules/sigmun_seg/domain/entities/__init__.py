"""Entidades do domínio de Segurança da Informação."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class TipoControle(Enum):
    """Tipo de controle de segurança."""

    FISICO = "fisico"
    TECNICO = "tecnico"
    ADMINISTRATIVO = "administrativo"


class CategoriaControle(Enum):
    """Categoria do controle (família ISO 27001)."""

    ACESSO = "acesso"
    CRIPTOGRAFIA = "criptografia"
    INCIDENTE = "incidente"
    CONTINUIDADE = "continuidade"
    CONFORMIDADE = "conformidade"


class StatusControle(Enum):
    """Status do controle de segurança."""

    IMPLEMENTADO = "implementado"
    PARCIAL = "parcial"
    PLANEJADO = "planejado"


class SeveridadeIncidente(Enum):
    """Severidade do incidente de segurança."""

    BAIXA = "baixa"
    MEDIA = "media"
    ALTA = "alta"
    CRITICA = "critica"


class StatusIncidente(Enum):
    """Status do incidente de segurança."""

    ABERTO = "aberto"
    EM_ANALISE = "em_analise"
    EM_MITIGACAO = "em_mitigacao"
    RESOLVIDO = "resolvido"
    ENCERRADO = "encerrado"


class StatusCredencial(Enum):
    """Status da credencial de acesso."""

    ATIVA = "ativa"
    SUSPENSA = "suspensa"
    REVOGADA = "revogada"
    EXPIRADA = "expirada"


@dataclass
class ControleSeguranca:
    """Controle de segurança da informação (ISO 27001)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    tipo: TipoControle = TipoControle.TECNICO
    categoria: CategoriaControle = CategoriaControle.ACESSO
    status: StatusControle = StatusControle.PLANEJADO
    responsavel_id: str = ""
    nivel_risco: str = "medio"  # baixo, medio, alto, critico
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return self.status == StatusControle.IMPLEMENTADO

    def implementar(self) -> None:
        """Marca o controle como implementado."""
        self.status = StatusControle.IMPLEMENTADO
        self.updated_at = datetime.utcnow()

    def parcial(self) -> None:
        """Marca o controle como parcialmente implementado."""
        self.status = StatusControle.PARCIAL
        self.updated_at = datetime.utcnow()


@dataclass
class PoliticaSeguranca:
    """Política de segurança da informação do município."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    titulo: str = ""
    conteudo: str = ""
    versao: str = "1.0"
    aprovador_id: str = ""
    data_aprovacao: datetime | None = None
    data_revisao: datetime | None = None
    ativa: bool = False
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return self.ativa

    def aprovar(self, aprovador_id: str) -> None:
        """Aprova a política de segurança."""
        self.aprovador_id = aprovador_id
        self.data_aprovacao = datetime.utcnow()
        self.ativa = True
        self.updated_at = datetime.utcnow()


@dataclass
class IncidenteSeguranca:
    """Incidente de segurança da informação registrado."""

    id: str = field(default_factory=lambda: str(uuid4()))
    titulo: str = ""
    descricao: str = ""
    severidade: SeveridadeIncidente = SeveridadeIncidente.BAIXA
    status: StatusIncidente = StatusIncidente.ABERTO
    data_ocorrencia: datetime = field(default_factory=datetime.utcnow)
    data_deteccao: datetime | None = None
    data_resolucao: datetime | None = None
    relator_id: str = ""
    atribuido_a: str = ""
    impacto: str = ""
    categoria: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return self.status not in (StatusIncidente.RESOLVIDO, StatusIncidente.ENCERRADO)

    def detectar(self, data: datetime) -> None:
        """Registra a data de detecção do incidente."""
        self.data_deteccao = data
        self.updated_at = datetime.utcnow()

    def escalar(self, atribuido_a: str) -> None:
        """Atribui o incidente a um responsável."""
        self.atribuido_a = atribuido_a
        self.status = StatusIncidente.EM_ANALISE
        self.updated_at = datetime.utcnow()

    def mitigar(self) -> None:
        """Inicia mitigação do incidente."""
        self.status = StatusIncidente.EM_MITIGACAO
        self.updated_at = datetime.utcnow()

    def resolver(self) -> None:
        """Resolve o incidente."""
        self.status = StatusIncidente.RESOLVIDO
        self.data_resolucao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def encerrar(self) -> None:
        """Encerra o incidente."""
        self.status = StatusIncidente.ENCERRADO
        self.updated_at = datetime.utcnow()


@dataclass
class ChaveCriptografica:
    """Chave criptográfica gerenciada pelo município."""

    id: str = field(default_factory=lambda: str(uuid4()))
    nome: str = ""
    algoritmo: str = "AES256"  # AES256, RSA4096, ECDSA
    tamanho_bits: int = 256
    tipo: str = "simetrica"  # simetrica, assimetrica
    status: str = "ativa"  # ativa, revogada, expirada
    data_expiracao: datetime | None = None
    responsavel_id: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return self.status == "ativa" and not self.is_deleted

    def revogar(self) -> None:
        """Revoga a chave."""
        self.status = "revogada"
        self.updated_at = datetime.utcnow()

    def expirar(self) -> None:
        """Marca a chave como expirada."""
        self.status = "expirada"
        self.updated_at = datetime.utcnow()


@dataclass
class Credencial:
    """Credencial de acesso a sistemas externos ou internos."""

    id: str = field(default_factory=lambda: str(uuid4()))
    usuario_id: str = ""
    tipo: str = "senha"  # senha, certificado, chave_api, token
    identificador: str = ""  # hash ou referência, nunca o valor real
    status: StatusCredencial = StatusCredencial.ATIVA
    validade: datetime | None = None
    ultimo_uso: datetime | None = None
    tentativas_falhas: int = 0
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return self.status == StatusCredencial.ATIVA and not self.is_deleted

    def suspender(self) -> None:
        """Suspende a credencial."""
        self.status = StatusCredencial.SUSPENSA
        self.updated_at = datetime.utcnow()

    def revogar(self) -> None:
        """Revoga a credencial."""
        self.status = StatusCredencial.REVOGADA
        self.updated_at = datetime.utcnow()

    def registrar_falha(self) -> None:
        """Registra uma tentativa de uso falha."""
        self.tentativas_falhas += 1
        self.updated_at = datetime.utcnow()

    def registrar_uso(self) -> None:
        """Registra uso bem-sucedido."""
        self.ultimo_uso = datetime.utcnow()
        self.tentativas_falhas = 0
        self.updated_at = datetime.utcnow()


__all__ = [
    "ControleSeguranca",
    "TipoControle",
    "CategoriaControle",
    "StatusControle",
    "PoliticaSeguranca",
    "IncidenteSeguranca",
    "SeveridadeIncidente",
    "StatusIncidente",
    "ChaveCriptografica",
    "Credencial",
    "StatusCredencial",
]
