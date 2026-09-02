"""Entidades do domínio de Dados Corporativos."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class TipoAtivoDado(Enum):
    """Tipo do ativo de dado."""
    TABELA = "tabela"
    CAMPO = "campo"
    RELATORIO = "relatorio"
    API = "api"
    ARQUIVO = "arquivo"


class QualidadeNivel(Enum):
    """Nível de qualidade do dado."""
    ALTO = "alto"
    MEDIO = "medio"
    BAIXO = "baixo"
    CRITICO = "critico"


class StatusAtivo(Enum):
    """Status do ativo de dado."""
    ATIVO = "ativo"
    INATIVO = "inativo"
    PENDENTE = "pendente"
    ARQUIVADO = "arquivado"


@dataclass
class AtivoDado:
    """Entidade de Ativo de Dado (item do catálogo de dados)."""
    id: str = field(default_factory=lambda: str(uuid4()))
    nome: str = ""
    descricao: str = ""
    tipo: TipoAtivoDado = TipoAtivoDado.TABELA
    status: StatusAtivo = StatusAtivo.PENDENTE
    qualidade: QualidadeNivel = QualidadeNivel.MEDIO
    dono_id: str = ""
    steward_id: str = ""
    schema_origem: str = ""
    tabela_origem: str = ""
    classificacao: str = ""
    tags: list[str] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return self.status == StatusAtivo.ATIVO

    def activate(self):
        """Ativa o ativo de dado."""
        self.status = StatusAtivo.ATIVO
        self.updated_at = datetime.utcnow()

    def deactivate(self):
        """Desativa o ativo de dado."""
        self.status = StatusAtivo.INATIVO
        self.updated_at = datetime.utcnow()

    def archive(self):
        """Arquiva o ativo de dado."""
        self.status = StatusAtivo.ARQUIVADO
        self.updated_at = datetime.utcnow()

    def update_quality(self, nivel: QualidadeNivel):
        """Atualiza nível de qualidade."""
        self.qualidade = nivel
        self.updated_at = datetime.utcnow()

    def add_tag(self, tag: str):
        """Adiciona tag ao ativo."""
        if tag not in self.tags:
            self.tags.append(tag)
            self.updated_at = datetime.utcnow()

    def remove_tag(self, tag: str):
        """Remove tag do ativo."""
        if tag in self.tags:
            self.tags.remove(tag)
            self.updated_at = datetime.utcnow()


@dataclass
class Catalogo:
    """Entidade de Catálogo de Dados."""
    id: str = field(default_factory=lambda: str(uuid4()))
    nome: str = ""
    descricao: str = ""
    dominio: str = ""
    ativos_ids: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return not self.is_deleted

    def add_ativo(self, ativo_id: str):
        """Adiciona ativo ao catálogo."""
        if ativo_id not in self.ativos_ids:
            self.ativos_ids.append(ativo_id)
            self.updated_at = datetime.utcnow()

    def remove_ativo(self, ativo_id: str):
        """Remove ativo do catálogo."""
        if ativo_id in self.ativos_ids:
            self.ativos_ids.remove(ativo_id)
            self.updated_at = datetime.utcnow()


@dataclass
class LinhagemDado:
    """Entidade de Linhagem de Dado (rastreamento de origem/destino)."""
    id: str = field(default_factory=lambda: str(uuid4()))
    ativo_origem_id: str = ""
    ativo_destino_id: str = ""
    tipo_transformacao: str = ""
    descricao: str = ""
    regras: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return not self.is_deleted


@dataclass
class PoliticaDado:
    """Entidade de Política de Dado."""
    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    tipo: str = ""
    regras: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return not self.is_deleted

    def add_rule(self, regra: str):
        """Adiciona regra à política."""
        if regra not in self.regras:
            self.regras.append(regra)
            self.updated_at = datetime.utcnow()

    def remove_rule(self, regra: str):
        """Remove regra da política."""
        if regra in self.regras:
            self.regras.remove(regra)
            self.updated_at = datetime.utcnow()


@dataclass
class QualidadeDado:
    """Entidade de Qualidade de Dado."""
    id: str = field(default_factory=lambda: str(uuid4()))
    ativo_id: str = ""
    nivel: QualidadeNivel = QualidadeNivel.MEDIO
    score: float = 0.0
    criterios: list[str] = field(default_factory=list)
    observacao: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return not self.is_deleted

    def update_score(self, score: float):
        """Atualiza score de qualidade."""
        self.score = max(0.0, min(100.0, score))
        self.updated_at = datetime.utcnow()
        # Atualiza nível baseado no score
        if self.score >= 80:
            self.nivel = QualidadeNivel.ALTO
        elif self.score >= 50:
            self.nivel = QualidadeNivel.MEDIO
        elif self.score >= 20:
            self.nivel = QualidadeNivel.BAIXO
        else:
            self.nivel = QualidadeNivel.CRITICO


__all__ = [
    "AtivoDado",
    "TipoAtivoDado",
    "StatusAtivo",
    "QualidadeNivel",
    "Catalogo",
    "LinhagemDado",
    "PoliticaDado",
    "QualidadeDado",
]
