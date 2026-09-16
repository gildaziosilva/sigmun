"""Interfaces para repositórios do módulo de Segurança da Informação."""

from abc import ABC, abstractmethod

from src.modules.sigmun_seg.domain.entities import (
    ChaveCriptografica,
    ControleSeguranca,
    Credencial,
    IncidenteSeguranca,
    PoliticaSeguranca,
)


class ControleSegurancaRepositoryInterface(ABC):
    """Interface para repositório de controles de segurança."""

    @abstractmethod
    def get_by_id(self, controle_id: str) -> ControleSeguranca | None:
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str) -> ControleSeguranca | None:
        pass

    @abstractmethod
    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        status: str | None = None,
        tipo: str | None = None,
        categoria: str | None = None,
    ) -> tuple[list[ControleSeguranca], int]:
        pass

    @abstractmethod
    def save(self, controle: ControleSeguranca) -> ControleSeguranca:
        pass

    @abstractmethod
    def delete(self, controle_id: str) -> bool:
        pass

    @abstractmethod
    def exists_by_codigo(self, codigo: str) -> bool:
        pass


class PoliticaSegurancaRepositoryInterface(ABC):
    """Interface para repositório de políticas de segurança."""

    @abstractmethod
    def get_by_id(self, politica_id: str) -> PoliticaSeguranca | None:
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str) -> PoliticaSeguranca | None:
        pass

    @abstractmethod
    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        ativa: bool | None = None,
    ) -> tuple[list[PoliticaSeguranca], int]:
        pass

    @abstractmethod
    def save(self, politica: PoliticaSeguranca) -> PoliticaSeguranca:
        pass

    @abstractmethod
    def delete(self, politica_id: str) -> bool:
        pass

    @abstractmethod
    def exists_by_codigo(self, codigo: str) -> bool:
        pass


class IncidenteSegurancaRepositoryInterface(ABC):
    """Interface para repositório de incidentes de segurança."""

    @abstractmethod
    def get_by_id(self, incidente_id: str) -> IncidenteSeguranca | None:
        pass

    @abstractmethod
    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        severidade: str | None = None,
        status: str | None = None,
    ) -> tuple[list[IncidenteSeguranca], int]:
        pass

    @abstractmethod
    def save(self, incidente: IncidenteSeguranca) -> IncidenteSeguranca:
        pass

    @abstractmethod
    def delete(self, incidente_id: str) -> bool:
        pass


class ChaveCriptograficaRepositoryInterface(ABC):
    """Interface para repositório de chaves criptográficas."""

    @abstractmethod
    def get_by_id(self, chave_id: str) -> ChaveCriptografica | None:
        pass

    @abstractmethod
    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        status: str | None = None,
    ) -> tuple[list[ChaveCriptografica], int]:
        pass

    @abstractmethod
    def get_by_nome(self, nome: str) -> ChaveCriptografica | None:
        pass

    @abstractmethod
    def exists_by_nome(self, nome: str) -> bool:
        pass

    @abstractmethod
    def save(self, chave: ChaveCriptografica) -> ChaveCriptografica:
        pass

    @abstractmethod
    def delete(self, chave_id: str) -> bool:
        pass


class CredencialRepositoryInterface(ABC):
    """Interface para repositório de credenciais."""

    @abstractmethod
    def get_by_id(self, credencial_id: str) -> Credencial | None:
        pass

    @abstractmethod
    def get_by_usuario(self, usuario_id: str) -> list[Credencial]:
        pass

    @abstractmethod
    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        status: str | None = None,
        tipo: str | None = None,
    ) -> tuple[list[Credencial], int]:
        pass

    @abstractmethod
    def save(self, credencial: Credencial) -> Credencial:
        pass

    @abstractmethod
    def delete(self, credencial_id: str) -> bool:
        pass


__all__ = [
    "ControleSegurancaRepositoryInterface",
    "PoliticaSegurancaRepositoryInterface",
    "IncidenteSegurancaRepositoryInterface",
    "ChaveCriptograficaRepositoryInterface",
    "CredencialRepositoryInterface",
]
