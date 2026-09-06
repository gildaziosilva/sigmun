"""Interfaces de repositório da aplicação de Gestão Documental."""

from abc import ABC, abstractmethod
from typing import List, Optional

from ...domain.entities import (
    Documento,
    VersaoDocumento,
    TramitacaoDocumento,
    ProcessoDocumento,
    ClassificacaoDocumental,
    TabelaTemporalidade,
    ArquivamentoDocumento,
    AssinaturaDocumento,
    TipoDocumental,
)


class RepositorioDocumento(ABC):
    """Interface de repositório para Documento."""

    @abstractmethod
    def save(self, documento: Documento) -> Documento:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[Documento]:
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str, ano: int) -> Optional[Documento]:
        pass

    @abstractmethod
    def find_by_processo(self, processo_id: str) -> List[Documento]:
        pass

    @abstractmethod
    def find_ativos(self) -> List[Documento]:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass


class RepositorioVersaoDocumento(ABC):
    """Interface de repositório para VersaoDocumento."""

    @abstractmethod
    def save(self, versao: VersaoDocumento) -> VersaoDocumento:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[VersaoDocumento]:
        pass

    @abstractmethod
    def find_by_documento(self, documento_id: str) -> List[VersaoDocumento]:
        pass

    @abstractmethod
    def get_ultima_versao(self, documento_id: str) -> Optional[VersaoDocumento]:
        pass


class RepositorioTramitacao(ABC):
    """Interface de repositório para TramitacaoDocumento."""

    @abstractmethod
    def save(self, tramitacao: TramitacaoDocumento) -> TramitacaoDocumento:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[TramitacaoDocumento]:
        pass

    @abstractmethod
    def find_by_documento(self, documento_id: str) -> List[TramitacaoDocumento]:
        pass


class RepositorioProcessoDocumento(ABC):
    """Interface de repositório para ProcessoDocumento."""

    @abstractmethod
    def save(self, processo: ProcessoDocumento) -> ProcessoDocumento:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[ProcessoDocumento]:
        pass

    @abstractmethod
    def find_all_abertos(self) -> List[ProcessoDocumento]:
        pass


class RepositorioClassificacaoDocumental(ABC):
    """Interface de repositório para ClassificacaoDocumental."""

    @abstractmethod
    def save(self, classificacao: ClassificacaoDocumental) -> ClassificacaoDocumental:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[ClassificacaoDocumental]:
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str) -> Optional[ClassificacaoDocumental]:
        pass

    @abstractmethod
    def find_all(self) -> List[ClassificacaoDocumental]:
        pass


class RepositorioTabelaTemporalidade(ABC):
    """Interface de repositório para TabelaTemporalidade."""

    @abstractmethod
    def save(self, tabela: TabelaTemporalidade) -> TabelaTemporalidade:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[TabelaTemporalidade]:
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str) -> Optional[TabelaTemporalidade]:
        pass


class RepositorioArquivamento(ABC):
    """Interface de repositório para ArquivamentoDocumento."""

    @abstractmethod
    def save(self, arquivamento: "ArquivamentoDocumento") -> "ArquivamentoDocumento":
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional["ArquivamentoDocumento"]:
        pass

    @abstractmethod
    def find_by_documento(self, documento_id: str) -> List["ArquivamentoDocumento"]:
        pass


class RepositorioAssinatura(ABC):
    """Interface de repositório para AssinaturaDocumento."""

    @abstractmethod
    def save(self, assinatura: "AssinaturaDocumento") -> "AssinaturaDocumento":
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional["AssinaturaDocumento"]:
        pass

    @abstractmethod
    def find_by_documento(self, documento_id: str) -> List["AssinaturaDocumento"]:
        pass


class RepositorioTipoDocumental(ABC):
    """Interface de repositório para TipoDocumental."""

    @abstractmethod
    def save(self, tipo: "TipoDocumental") -> "TipoDocumental":
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str) -> Optional["TipoDocumental"]:
        pass

    @abstractmethod
    def find_ativos(self) -> List["TipoDocumental"]:
        pass

    @abstractmethod
    def find_all(self) -> List["TipoDocumental"]:
        pass


class PublicadorEventos(ABC):
    """Interface de publicação de eventos de integração (Transactional Outbox).

    Implementações gravam o evento de forma transacional com o negócio
    (014-Modelo-de-Integracao, seção 6 — Eventos de Domínio), garantindo
    atomicidade entre o estado e o evento publicado.
    """

    @abstractmethod
    def publicar(
        self,
        topico: str,
        evento_nome: str,
        agregado_tipo: str,
        agregado_id: str,
        payload: dict,
    ) -> None:
        """Registra um evento para despacho assíncrono ao barramento."""
        pass


__all__ = [
    "RepositorioDocumento",
    "RepositorioVersaoDocumento",
    "RepositorioTramitacao",
    "RepositorioProcessoDocumento",
    "RepositorioClassificacaoDocumental",
    "RepositorioTabelaTemporalidade",
    "RepositorioArquivamento",
    "RepositorioAssinatura",
    "RepositorioTipoDocumental",
    "PublicadorEventos",
]
