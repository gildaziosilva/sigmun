"""Interfaces de repositório da aplicação de Gestão de Diárias, Viagens e Deslocamentos."""

from abc import ABC, abstractmethod
from typing import Optional

from ...domain.entities import Diaria, PrestacaoContas, Viagem


class RepositorioViagem(ABC):
    """Interface de repositório para Viagem."""

    @abstractmethod
    def save(self, viagem: Viagem) -> Viagem:
        """Insere ou atualiza uma viagem."""
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[Viagem]:
        """Busca viagem por ID."""
        pass

    @abstractmethod
    def find_by_servidor(self, servidor_id: str) -> list[Viagem]:
        """Busca viagens por servidor."""
        pass

    @abstractmethod
    def find_by_dota(self, dota_id: str) -> list[Viagem]:
        """Busca viagens por dotação orçamentária."""
        pass

    @abstractmethod
    def find_ativos(self) -> list[Viagem]:
        """Lista viagens ativas."""
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        """Remove logicamente uma viagem."""
        pass


class RepositorioDiaria(ABC):
    """Interface de repositório para Diaria."""

    @abstractmethod
    def save(self, diaria: Diaria) -> Diaria:
        """Insere ou atualiza uma diária."""
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[Diaria]:
        """Busca diária por ID."""
        pass

    @abstractmethod
    def get_by_viagem(self, viagem_id: str) -> Optional[Diaria]:
        """Busca diária por ID de viagem."""
        pass

    @abstractmethod
    def find_by_servidor(self, servidor_id: str) -> list[Diaria]:
        """Busca diárias por servidor."""
        pass

    @abstractmethod
    def find_by_dota(self, dota_id: str) -> list[Diaria]:
        """Busca diárias por dotação."""
        pass

    @abstractmethod
    def find_by_status(self, status: str) -> list[Diaria]:
        """Busca diárias por status."""
        pass

    @abstractmethod
    def find_ativas(self) -> list[Diaria]:
        """Lista diárias ativas."""
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        """Remove logicamente uma diária."""
        pass


class RepositorioPrestacaoContas(ABC):
    """Interface de repositório para PrestacaoContas."""

    @abstractmethod
    def save(self, prestacao: PrestacaoContas) -> PrestacaoContas:
        """Insere ou atualiza uma prestação de contas."""
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[PrestacaoContas]:
        """Busca prestação de contas por ID."""
        pass

    @abstractmethod
    def get_by_diaria(self, diaria_id: str) -> Optional[PrestacaoContas]:
        """Busca prestação de contas por ID de diária."""
        pass

    @abstractmethod
    def find_authors(self) -> list[PrestacaoContas]:
        """Lista prestações de contas abertas."""
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        """Remove logicamente uma prestação de contas."""
        pass


class PublicadorEventosDiaria(ABC):
    """Interface de publicação de eventos de diárias."""

    @abstractmethod
    def publicar(
        self,
        topico: str,
        evento_nome: str,
        agregado_tipo: str,
        agregado_id: str,
        payload: dict,
    ) -> None:
        """Registra um evento para despacho assíncrono."""
        pass


__all__ = [
    "RepositorioViagem",
    "RepositorioDiaria",
    "RepositorioPrestacaoContas",
    "PublicadorEventosDiaria",
]
