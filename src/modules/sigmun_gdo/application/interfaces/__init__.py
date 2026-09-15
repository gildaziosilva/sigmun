"""Interfaces de repositório da aplicação de Gestão Documental."""

from abc import ABC, abstractmethod
from typing import Optional

from ...domain.entities import (
    ArquivamentoDocumento,
    AssinaturaDocumento,
    ClassificacaoDocumental,
    Documento,
    ProcessoDocumento,
    TabelaTemporalidade,
    TipoDocumental,
    TramitacaoDocumento,
    VersaoDocumento,
)


class RepositorioDocumento(ABC):
    """Interface de repositório para Documento."""

    @abstractmethod
    def save(self, documento: Documento) -> Documento:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Documento | None:
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str, ano: int) -> Documento | None:
        pass

    @abstractmethod
    def find_by_processo(self, processo_id: str) -> list[Documento]:
        pass

    @abstractmethod
    def find_ativos(self) -> list[Documento]:
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
    def get_by_id(self, id: str) -> VersaoDocumento | None:
        pass

    @abstractmethod
    def find_by_documento(self, documento_id: str) -> list[VersaoDocumento]:
        pass

    @abstractmethod
    def get_ultima_versao(self, documento_id: str) -> VersaoDocumento | None:
        pass


class RepositorioTramitacao(ABC):
    """Interface de repositório para TramitacaoDocumento."""

    @abstractmethod
    def save(self, tramitacao: TramitacaoDocumento) -> TramitacaoDocumento:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> TramitacaoDocumento | None:
        pass

    @abstractmethod
    def find_by_documento(self, documento_id: str) -> list[TramitacaoDocumento]:
        pass


class RepositorioProcessoDocumento(ABC):
    """Interface de repositório para ProcessoDocumento."""

    @abstractmethod
    def save(self, processo: ProcessoDocumento) -> ProcessoDocumento:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> ProcessoDocumento | None:
        pass

    @abstractmethod
    def find_all_abertos(self) -> list[ProcessoDocumento]:
        pass


class RepositorioClassificacaoDocumental(ABC):
    """Interface de repositório para ClassificacaoDocumental."""

    @abstractmethod
    def save(self, classificacao: ClassificacaoDocumental) -> ClassificacaoDocumental:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> ClassificacaoDocumental | None:
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str) -> ClassificacaoDocumental | None:
        pass

    @abstractmethod
    def find_all(self) -> list[ClassificacaoDocumental]:
        pass


class RepositorioTabelaTemporalidade(ABC):
    """Interface de repositório para TabelaTemporalidade."""

    @abstractmethod
    def save(self, tabela: TabelaTemporalidade) -> TabelaTemporalidade:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> TabelaTemporalidade | None:
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str) -> TabelaTemporalidade | None:
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
    def find_by_documento(self, documento_id: str) -> list["ArquivamentoDocumento"]:
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
    def find_by_documento(self, documento_id: str) -> list["AssinaturaDocumento"]:
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
    def find_ativos(self) -> list["TipoDocumental"]:
        pass

    @abstractmethod
    def find_all(self) -> list["TipoDocumental"]:
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
