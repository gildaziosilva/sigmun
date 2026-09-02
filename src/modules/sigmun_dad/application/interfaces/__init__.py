"""Interfaces para repositórios do módulo de Dados Corporativos."""

from abc import ABC, abstractmethod

from src.modules.sigmun_dad.domain.entities import (
    AtivoDado,
    Catalogo,
    LinhagemDado,
    PoliticaDado,
    QualidadeDado,
)


class AtivoRepositoryInterface(ABC):
    """Interface para repositório de ativos de dados."""

    @abstractmethod
    def get_by_id(self, ativo_id: str) -> AtivoDado | None:
        pass

    @abstractmethod
    def get_by_nome(self, nome: str) -> AtivoDado | None:
        pass

    @abstractmethod
    def list_all(
        self, page: int = 0, page_size: int = 50,
        tipo: str | None = None, status: str | None = None,
    ) -> tuple[list[AtivoDado], int]:
        """Lista ativos com paginação."""
        pass

    @abstractmethod
    def save(self, ativo: AtivoDado) -> AtivoDado:
        pass

    @abstractmethod
    def delete(self, ativo_id: str) -> bool:
        pass

    @abstractmethod
    def exists_by_nome(self, nome: str) -> bool:
        pass


class CatalogoRepositoryInterface(ABC):
    """Interface para repositório de catálogos."""

    @abstractmethod
    def get_by_id(self, catalogo_id: str) -> Catalogo | None:
        pass

    @abstractmethod
    def get_by_nome(self, nome: str) -> Catalogo | None:
        pass

    @abstractmethod
    def list_all(self, page: int = 0, page_size: int = 50) -> tuple[list[Catalogo], int]:
        pass

    @abstractmethod
    def save(self, catalogo: Catalogo) -> Catalogo:
        pass

    @abstractmethod
    def delete(self, catalogo_id: str) -> bool:
        pass


class LinhagemRepositoryInterface(ABC):
    """Interface para repositório de linhagens."""

    @abstractmethod
    def get_by_id(self, linhagem_id: str) -> LinhagemDado | None:
        pass

    @abstractmethod
    def get_by_origem(self, ativo_origem_id: str) -> list[LinhagemDado]:
        pass

    @abstractmethod
    def get_by_destino(self, ativo_destino_id: str) -> list[LinhagemDado]:
        pass

    @abstractmethod
    def list_all(self, page: int = 0, page_size: int = 50) -> tuple[list[LinhagemDado], int]:
        pass

    @abstractmethod
    def save(self, linhagem: LinhagemDado) -> LinhagemDado:
        pass

    @abstractmethod
    def delete(self, linhagem_id: str) -> bool:
        pass


class PoliticaRepositoryInterface(ABC):
    """Interface para repositório de políticas."""

    @abstractmethod
    def get_by_id(self, politica_id: str) -> PoliticaDado | None:
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str) -> PoliticaDado | None:
        pass

    @abstractmethod
    def list_all(self, page: int = 0, page_size: int = 50) -> tuple[list[PoliticaDado], int]:
        pass

    @abstractmethod
    def save(self, politica: PoliticaDado) -> PoliticaDado:
        pass

    @abstractmethod
    def delete(self, politica_id: str) -> bool:
        pass


class QualidadeRepositoryInterface(ABC):
    """Interface para repositório de qualidade de dados."""

    @abstractmethod
    def get_by_id(self, qualidade_id: str) -> QualidadeDado | None:
        pass

    @abstractmethod
    def get_by_ativo(self, ativo_id: str) -> QualidadeDado | None:
        pass

    @abstractmethod
    def list_all(self, page: int = 0, page_size: int = 50) -> tuple[list[QualidadeDado], int]:
        pass

    @abstractmethod
    def save(self, qualidade: QualidadeDado) -> QualidadeDado:
        pass

    @abstractmethod
    def delete(self, qualidade_id: str) -> bool:
        pass


__all__ = [
    "AtivoRepositoryInterface",
    "CatalogoRepositoryInterface",
    "LinhagemRepositoryInterface",
    "PoliticaRepositoryInterface",
    "QualidadeRepositoryInterface",
]
