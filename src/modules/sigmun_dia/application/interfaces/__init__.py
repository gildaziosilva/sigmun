"""Interfaces de repositório da aplicação de DOM-DIA."""

from abc import ABC, abstractmethod
from typing import Optional

from src.modules.sigmun_dia.domain.entities import Diaria, PrestacaoContas, Viagem


class RepositorioViagem(ABC):
    """Interface de repositório para Viagem."""

    @abstractmethod
    def save(self, viagem: Viagem) -> Viagem:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[Viagem]:
        pass

    @abstractmethod
    def find_by_servidor(self, servidor_id: str) -> list[Viagem]:
        pass

    @abstractmethod
    def find_by_dota(self, dota_id: str) -> list[Viagem]:
        pass

    @abstractmethod
    def find_ativos(self) -> list[Viagem]:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass


class RepositorioDiaria(ABC):
    """Interface de repositório para Diaria."""

    @abstractmethod
    def save(self, diaria: Diaria) -> Diaria:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[Diaria]:
        pass

    @abstractmethod
    def get_by_viagem(self, viagem_id: str) -> Optional[Diaria]:
        pass

    @abstractmethod
    def find_by_servidor(self, servidor_id: str) -> list[Diaria]:
        pass

    @abstractmethod
    def find_by_dota(self, dota_id: str) -> list[Diaria]:
        pass

    @abstractmethod
    def find_by_status(self, status: str) -> list[Diaria]:
        pass

    @abstractmethod
    def find_ativas(self) -> list[Diaria]:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass


class RepositorioPrestacaoContas(ABC):
    """Interface de repositório para PrestacaoContas."""

    @abstractmethod
    def save(self, prestacao: PrestacaoContas) -> PrestacaoContas:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[PrestacaoContas]:
        pass

    @abstractmethod
    def get_by_diaria(self, diaria_id: str) -> Optional[PrestacaoContas]:
        pass

    @abstractmethod
    def find_authors(self) -> list[PrestacaoContas]:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass


__all__ = [
    'RepositorioViagem',
    'RepositorioDiaria',
    'RepositorioPrestacaoContas',
]
