"""Entidades do domínio de Metadados Corporativos."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class TipoDadoMetadado(Enum):
    """Tipo de dado aceito por um metadado."""

    TEXTO = "texto"
    NUMERO = "numero"
    DATA = "data"
    BOOLEANO = "booleano"
    LISTA = "lista"
    JSON = "json"


class StatusMetadado(Enum):
    """Status de um metadado."""

    ATIVO = "ativo"
    INATIVO = "inativo"


class TipoClassificacao(Enum):
    """Tipo de esquema de classificação."""

    CONFIDENCIALIDADE = "confidencialidade"
    ASSUNTO = "assunto"
    RETENCAO = "retencao"
    ORIGEM = "origem"


@dataclass
class Metadado:
    """Entidade de Metadado (definição de um campo de metadado corporativo)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    tipo_dado: TipoDadoMetadado = TipoDadoMetadado.TEXTO
    obrigatorio: bool = False
    multi_valor: bool = False
    aplicavel_a: list[str] = field(default_factory=list)
    valor_padrao: str = ""
    status: StatusMetadado = StatusMetadado.ATIVO
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return self.status == StatusMetadado.ATIVO

    def ativar(self) -> None:
        """Ativa o metadado."""
        self.status = StatusMetadado.ATIVO
        self.updated_at = datetime.utcnow()

    def desativar(self) -> None:
        """Desativa o metadado."""
        self.status = StatusMetadado.INATIVO
        self.updated_at = datetime.utcnow()

    def adicionar_aplicavel(self, entidade_tipo: str) -> None:
        """Adiciona tipo de entidade aplicável."""
        if entidade_tipo not in self.aplicavel_a:
            self.aplicavel_a.append(entidade_tipo)
            self.updated_at = datetime.utcnow()

    def remover_aplicavel(self, entidade_tipo: str) -> None:
        """Remove tipo de entidade aplicável."""
        if entidade_tipo in self.aplicavel_a:
            self.aplicavel_a.remove(entidade_tipo)
            self.updated_at = datetime.utcnow()

    # Aliases de compatibilidade (nomes anteriores em inglês).
    @property
    def is_active(self) -> bool:
        return self.esta_ativo

    def activate(self) -> None:
        self.ativar()

    def deactivate(self) -> None:
        self.desativar()

    def add_aplicavel(self, entidade_tipo: str) -> None:
        self.adicionar_aplicavel(entidade_tipo)

    def remove_aplicavel(self, entidade_tipo: str) -> None:
        self.remover_aplicavel(entidade_tipo)


@dataclass
class ValorMetadado:
    """Entidade de Valor de Metadado (valor atribuído a uma entidade)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    metadado_id: str = ""
    entidade_tipo: str = ""
    entidade_id: str = ""
    valor: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return not self.is_deleted

    @property
    def foi_excluido(self) -> bool:
        return self.is_deleted

    # Alias de compatibilidade.
    @property
    def is_active(self) -> bool:
        return self.esta_ativo


@dataclass
class Classificacao:
    """Entidade de Classificação (esquema de classificação corporativa)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    tipo: TipoClassificacao = TipoClassificacao.CONFIDENCIALIDADE
    nivel: int = 0
    cor: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return not self.is_deleted

    @property
    def foi_excluido(self) -> bool:
        return self.is_deleted

    # Alias de compatibilidade.
    @property
    def is_active(self) -> bool:
        return self.esta_ativo


@dataclass
class Taxonomia:
    """Entidade de Taxonomia (conjunto hierárquico de termos)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    termos_ids: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return not self.is_deleted

    @property
    def foi_excluido(self) -> bool:
        return self.is_deleted

    # Alias de compatibilidade.
    @property
    def is_active(self) -> bool:
        return self.esta_ativo

    def adicionar_termo(self, termo_id: str) -> None:
        """Adiciona termo raiz à taxonomia."""
        if termo_id not in self.termos_ids:
            self.termos_ids.append(termo_id)
            self.updated_at = datetime.utcnow()

    def remover_termo(self, termo_id: str) -> None:
        """Remove termo raiz da taxonomia."""
        if termo_id in self.termos_ids:
            self.termos_ids.remove(termo_id)
            self.updated_at = datetime.utcnow()

    # Aliases de compatibilidade (nomes anteriores em inglês).
    def add_termo(self, termo_id: str) -> None:
        self.adicionar_termo(termo_id)

    def remove_termo(self, termo_id: str) -> None:
        self.remover_termo(termo_id)


@dataclass
class TermoTaxonomia:
    """Entidade de Termo de Taxonomia (nó hierárquico)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    taxonomia_id: str = ""
    termo_pai_id: str = ""
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    sinonimos: list[str] = field(default_factory=list)
    ordem: int = 0
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    is_deleted: bool = False

    @property
    def eh_raiz(self) -> bool:
        return not self.termo_pai_id

    @property
    def esta_ativo(self) -> bool:
        return not self.is_deleted

    @property
    def foi_excluido(self) -> bool:
        return self.is_deleted

    # Aliases de compatibilidade.
    @property
    def is_root(self) -> bool:
        return self.eh_raiz

    @property
    def is_active(self) -> bool:
        return self.esta_ativo

    def adicionar_sinonimo(self, sinonimo: str) -> None:
        """Adiciona sinônimo ao termo."""
        if sinonimo not in self.sinonimos:
            self.sinonimos.append(sinonimo)
            self.updated_at = datetime.utcnow()

    def remover_sinonimo(self, sinonimo: str) -> None:
        """Remove sinônimo do termo."""
        if sinonimo in self.sinonimos:
            self.sinonimos.remove(sinonimo)
            self.updated_at = datetime.utcnow()

    # Aliases de compatibilidade (nomes anteriores em inglês).
    def add_sinonimo(self, sinonimo: str) -> None:
        self.adicionar_sinonimo(sinonimo)

    def remove_sinonimo(self, sinonimo: str) -> None:
        self.remover_sinonimo(sinonimo)


__all__ = [
    "Metadado",
    "TipoDadoMetadado",
    "StatusMetadado",
    "ValorMetadado",
    "Classificacao",
    "TipoClassificacao",
    "Taxonomia",
    "TermoTaxonomia",
]
