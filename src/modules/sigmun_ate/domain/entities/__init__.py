"""Entidades do domínio de Atendimento ao Cidadão (DOM-ATE)."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class StatusAtendimento(Enum):
    """Status de um atendimento."""
    AGUARDANDO = "aguardando"
    EM_ANDAMENTO = "em_andamento"
    CONCLUIDO = "concluido"
    ENCERRADO = "encerrado"
    CANCELADO = "cancelado"


class StatusSenha(Enum):
    """Status de uma senha de atendimento."""
    EMITIDA = "emitida"
    CHAMADA = "chamada"
    ATENDIDA = "atendida"
    RECHAMADA = "rechamada"
    NAO_COMPARECEU = "nao_compareceu"
    CANCELADA = "cancelada"


class TipoCanal(Enum):
    """Tipo de canal de atendimento."""
    PRESENCIAL = "presencial"
    TELEFONE = "telefone"
    EMAIL = "email"
    CHAT = "chat"
    PORTAL = "portal"
    MOBILE = "mobile"


class PrioridadeAtendimento(Enum):
    """Prioridade do atendimento."""
    BAIXA = 1
    NORMAL = 2
    ALTA = 3
    URGENTE = 4


@dataclass
class ServicoAtendimento:
    """Entidade de Serviço de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    prioridade: int = 0
    ativo: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return self.ativo and not self.is_deleted
    @property
    def is_active(self) -> bool:
        return self.esta_ativo


@dataclass
class CanalAtendimento:
    """Entidade de Canal de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    tipo: TipoCanal = TipoCanal.PRESENCIAL
    ativo: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return self.ativo and not self.is_deleted
    @property
    def is_active(self) -> bool:
        return self.esta_ativo


@dataclass
class UnidadeAtendimento:
    """Entidade de Unidade de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    ativo: bool = True
    max_rechamadas: int = 3
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return self.ativo and not self.is_deleted
    @property
    def is_active(self) -> bool:
        return self.esta_ativo


@dataclass
class Guiche:
    """Entidade de Guichê de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    unidade_id: str = ""
    numero: str = ""
    descricao: str = ""
    ativo: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return self.ativo and not self.is_deleted
    @property
    def is_active(self) -> bool:
        return self.esta_ativo


@dataclass
class FilaAtendimento:
    """Entidade de Fila de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    unidade_id: str = ""
    servico_id: str = ""
    data: datetime = field(default_factory=lambda: datetime.utcnow().date())
    status: str = "aberta"
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_aberta(self) -> bool:
        return self.status == "aberta" and not self.is_deleted


@dataclass
class Triagem:
    """Entidade de Triagem de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    servico_id: str = ""
    data_hora: datetime = field(default_factory=datetime.utcnow)
    classificacao: str = ""
    prioridade: int = 0
    observacao: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return not self.is_deleted
    @property
    def is_active(self) -> bool:
        return self.esta_ativo


@dataclass
class Senha:
    """Entidade de Senha de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    fila_id: str = ""
    servico_id: str = ""
    triagem_id: str = ""
    numero: str = ""
    data_hora_emissao: datetime = field(default_factory=datetime.utcnow)
    prioridade: int = 0
    status: StatusSenha = StatusSenha.EMITIDA
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativa(self) -> bool:
        return self.status in (StatusSenha.EMITIDA, StatusSenha.CHAMADA, StatusSenha.RECHAMADA) and not self.is_deleted
    @property
    def is_active(self) -> bool:
        return self.esta_ativa


@dataclass
class Chamada:
    """Entidade de Chamada de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    senha_id: str = ""
    guiche_id: str = ""
    unidade_id: str = ""
    operador: str = ""
    data_hora: datetime = field(default_factory=datetime.utcnow)
    ordem: int = 0
    tentativa: int = 1
    resultado: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativa(self) -> bool:
        return not self.is_deleted
    @property
    def is_active(self) -> bool:
        return self.esta_ativa


@dataclass
class Atendimento:
    """Entidade de Atendimento (núcleo do DOM-ATE)."""
    id: str = field(default_factory=lambda: str(uuid4()))
    chamada_id: str = ""
    canal_id: str = ""
    inicio: datetime | None = None
    fim: datetime | None = None
    status: StatusAtendimento = StatusAtendimento.AGUARDANDO
    descricao: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return self.status in (
            StatusAtendimento.AGUARDANDO,
            StatusAtendimento.EM_ANDAMENTO,
        ) and not self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo

    @property
    def duracao_segundos(self) -> int | None:
        if self.inicio and self.fim:
            return int((self.fim - self.inicio).total_seconds())
        return None


@dataclass
class AvaliacaoAtendimento:
    """Entidade de Avaliação de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    atendimento_id: str = ""
    nota: int = 0
    comentario: str = ""
    data_hora: datetime = field(default_factory=datetime.utcnow)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_valida(self) -> bool:
        return 1 <= self.nota <= 5 and not self.is_deleted


@dataclass
class Encaminhamento:
    """Entidade de Encaminhamento de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    atendimento_id: str = ""
    data_hora: datetime = field(default_factory=datetime.utcnow)
    destino: str = ""
    motivo: str = ""
    status: str = "pendente"
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return self.status == "pendente" and not self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo


__all__ = [
    "StatusAtendimento",
    "StatusSenha",
    "TipoCanal",
    "PrioridadeAtendimento",
    "ServicoAtendimento",
    "CanalAtendimento",
    "UnidadeAtendimento",
    "Guiche",
    "FilaAtendimento",
    "Triagem",
    "Senha",
    "Chamada",
    "Atendimento",
    "AvaliacaoAtendimento",
    "Encaminhamento",
]



@dataclass
class Atendimento:
    """Entidade de Atendimento (núcleo do DOM-ATE)."""
    id: str = field(default_factory=lambda: str(uuid4()))
    chamada_id: str = ""
    canal_id: str = ""
    inicio: datetime | None = None
    fim: datetime | None = None
    status: StatusAtendimento = StatusAtendimento.AGUARDANDO
    descricao: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return self.status in (
            StatusAtendimento.AGUARDANDO,
            StatusAtendimento.EM_ANDAMENTO,
        ) and not self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo

    @property
    def duracao_segundos(self) -> int | None:
        if self.inicio and self.fim:
            return int((self.fim - self.inicio).total_seconds())
        return None


@dataclass
class AvaliacaoAtendimento:
    """Entidade de Avaliação de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    atendimento_id: str = ""
    nota: int = 0
    comentario: str = ""
    data_hora: datetime = field(default_factory=datetime.utcnow)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_valida(self) -> bool:
        return 1 <= self.nota <= 5 and not self.is_deleted


@dataclass
class Encaminhamento:
    """Entidade de Encaminhamento de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    atendimento_id: str = ""
    data_hora: datetime = field(default_factory=datetime.utcnow)
    destino: str = ""
    motivo: str = ""
    status: str = "pendente"
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return self.status == "pendente" and not self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo


__all__ = [
    "StatusAtendimento",
    "StatusSenha",
    "TipoCanal",
    "PrioridadeAtendimento",
    "ServicoAtendimento",
    "CanalAtendimento",
    "UnidadeAtendimento",
    "Guiche",
    "FilaAtendimento",
    "Triagem",
    "Senha",
    "Chamada",
    "Atendimento",
    "AvaliacaoAtendimento",
    "Encaminhamento",
]



@dataclass
class Atendimento:
    """Entidade de Atendimento (núcleo do DOM-ATE)."""
    id: str = field(default_factory=lambda: str(uuid4()))
    chamada_id: str = ""
    canal_id: str = ""
    inicio: datetime | None = None
    fim: datetime | None = None
    status: StatusAtendimento = StatusAtendimento.AGUARDANDO
    descricao: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return self.status in (
            StatusAtendimento.AGUARDANDO,
            StatusAtendimento.EM_ANDAMENTO,
        ) and not self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo

    @property
    def duracao_segundos(self) -> int | None:
        if self.inicio and self.fim:
            return int((self.fim - self.inicio).total_seconds())
        return None


@dataclass
class AvaliacaoAtendimento:
    """Entidade de Avaliação de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    atendimento_id: str = ""
    nota: int = 0
    comentario: str = ""
    data_hora: datetime = field(default_factory=datetime.utcnow)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_valida(self) -> bool:
        return 1 <= self.nota <= 5 and not self.is_deleted


@dataclass
class Encaminhamento:
    """Entidade de Encaminhamento de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    atendimento_id: str = ""
    data_hora: datetime = field(default_factory=datetime.utcnow)
    destino: str = ""
    motivo: str = ""
    status: str = "pendente"
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return self.status == "pendente" and not self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo


__all__ = [
    "StatusAtendimento",
    "StatusSenha",
    "TipoCanal",
    "PrioridadeAtendimento",
    "ServicoAtendimento",
    "CanalAtendimento",
    "UnidadeAtendimento",
    "Guiche",
    "FilaAtendimento",
    "Triagem",
    "Senha",
    "Chamada",
    "Atendimento",
    "AvaliacaoAtendimento",
    "Encaminhamento",
]


@dataclass
class Atendimento:
    """Entidade de Atendimento (núcleo do DOM-ATE)."""
    id: str = field(default_factory=lambda: str(uuid4()))
    chamada_id: str = ""
    canal_id: str = ""
    inicio: datetime | None = None
    fim: datetime | None = None
    status: StatusAtendimento = StatusAtendimento.AGUARDANDO
    descricao: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return self.status in (
            StatusAtendimento.AGUARDANDO,
            StatusAtendimento.EM_ANDAMENTO,
        ) and not self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo

    @property
    def duracao_segundos(self) -> int | None:
        if self.inicio and self.fim:
            return int((self.fim - self.inicio).total_seconds())
        return None


@dataclass
class AvaliacaoAtendimento:
    """Entidade de Avaliação de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    atendimento_id: str = ""
    nota: int = 0
    comentario: str = ""
    data_hora: datetime = field(default_factory=datetime.utcnow)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_valida(self) -> bool:
        return 1 <= self.nota <= 5 and not self.is_deleted


@dataclass
class Encaminhamento:
    """Entidade de Encaminhamento de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    atendimento_id: str = ""
    data_hora: datetime = field(default_factory=datetime.utcnow)
    destino: str = ""
    motivo: str = ""
    status: str = "pendente"
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return self.status == "pendente" and not self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo


__all__ = [
    "StatusAtendimento",
    "StatusSenha",
    "TipoCanal",
    "PrioridadeAtendimento",
    "ServicoAtendimento",
    "CanalAtendimento",
    "UnidadeAtendimento",
    "Guiche",
    "FilaAtendimento",
    "Triagem",
    "Senha",
    "Chamada",
    "Atendimento",
    "AvaliacaoAtendimento",
    "Encaminhamento",
]



@dataclass
class Atendimento:
    """Entidade de Atendimento (núcleo do DOM-ATE)."""
    id: str = field(default_factory=lambda: str(uuid4()))
    chamada_id: str = ""
    canal_id: str = ""
    inicio: datetime | None = None
    fim: datetime | None = None
    status: StatusAtendimento = StatusAtendimento.AGUARDANDO
    descricao: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return self.status in (
            StatusAtendimento.AGUARDANDO,
            StatusAtendimento.EM_ANDAMENTO,
        ) and not self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo

    @property
    def duracao_segundos(self) -> int | None:
        if self.inicio and self.fim:
            return int((self.fim - self.inicio).total_seconds())
        return None


@dataclass
class AvaliacaoAtendimento:
    """Entidade de Avaliação de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    atendimento_id: str = ""
    nota: int = 0
    comentario: str = ""
    data_hora: datetime = field(default_factory=datetime.utcnow)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_valida(self) -> bool:
        return 1 <= self.nota <= 5 and not self.is_deleted


@dataclass
class Encaminhamento:
    """Entidade de Encaminhamento de Atendimento."""
    id: str = field(default_factory=lambda: str(uuid4()))
    atendimento_id: str = ""
    data_hora: datetime = field(default_factory=datetime.utcnow)
    destino: str = ""
    motivo: str = ""
    status: str = "pendente"
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return self.status == "pendente" and not self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo


__all__ = [
    "StatusAtendimento",
    "StatusSenha",
    "TipoCanal",
    "PrioridadeAtendimento",
    "ServicoAtendimento",
    "CanalAtendimento",
    "UnidadeAtendimento",
    "Guiche",
    "FilaAtendimento",
    "Triagem",
    "Senha",
    "Chamada",
    "Atendimento",
    "AvaliacaoAtendimento",
    "Encaminhamento",
]