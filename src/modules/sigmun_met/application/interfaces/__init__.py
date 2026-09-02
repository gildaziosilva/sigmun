"""Interfaces para repositórios do módulo de Metadados Corporativos."""

from abc import ABC, abstractmethod

from src.modules.sigmun_met.domain.entities import (
    Classificacao,
    Metadado,
    Taxonomia,
    TermoTaxonomia,
    ValorMetadado,
)


class MetadadoRepositoryInterface(ABC):
    """Interface para repositório de metadados."""

    @abstractmethod
    def get_by_id(self, metadado_id: str) -> Metadado | None:
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str) -> Metadado | None:
        pass

    @abstractmethod
    def list_all(
        self, page: int = 0, page_size: int = 50,
        status: str | None = None, tipo_dado: str | None = None,
    ) -> tuple[list[Metadado], int]:
        """Lista metadados com paginação."""
        pass

    @abstractmethod
    def save(self, metadado: Metadado) -> Metadado:
        pass

    @abstractmethod
    def delete(self, metadado_id: str) -> bool:
        pass

    @abstractmethod
    def exists_by_codigo(self, codigo: str) -> bool:
        pass


class ValorMetadadoRepositoryInterface(ABC):
    """Interface para repositório de valores de metadados."""

    @abstractmethod
    def get_by_id(self, valor_id: str) -> ValorMetadado | None:
        pass

    @abstractmethod
    def get_by_entidade(self, entidade_tipo: str, entidade_id: str) -> list[ValorMetadado]:
        pass

    @abstractmethod
    def get_by_metadado_e_entidade(
        self, metadado_id: str, entidade_tipo: str, entidade_id: str
    ) -> ValorMetadado | None:
        pass

    @abstractmethod
    def list_all(
        self, page: int = 0, page_size: int = 50,
        metadado_id: str | None = None, entidade_tipo: str | None = None,
    ) -> tuple[list[ValorMetadado], int]:
        pass

    @abstractmethod
    def save(self, valor: ValorMetadado) -> ValorMetadado:
        pass

    @abstractmethod
    def delete(self, valor_id: str) -> bool:
        pass


class ClassificacaoRepositoryInterface(ABC):
    """Interface para repositório de classificações."""

    @abstractmethod
    def get_by_id(self, classificacao_id: str) -> Classificacao | None:
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str) -> Classificacao | None:
        pass

    @abstractmethod
    def list_all(
        self, page: int = 0, page_size: int = 50, tipo: str | None = None,
    ) -> tuple[list[Classificacao], int]:
        pass

    @abstractmethod
    def save(self, classificacao: Classificacao) -> Classificacao:
        pass

    @abstractmethod
    def delete(self, classificacao_id: str) -> bool:
        pass

    @abstractmethod
    def exists_by_codigo(self, codigo: str) -> bool:
        pass


class TaxonomiaRepositoryInterface(ABC):
    """Interface para repositório de taxonomias."""

    @abstractmethod
    def get_by_id(self, taxonomia_id: str) -> Taxonomia | None:
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str) -> Taxonomia | None:
        pass

    @abstractmethod
    def list_all(self, page: int = 0, page_size: int = 50) -> tuple[list[Taxonomia], int]:
        pass

    @abstractmethod
    def save(self, taxonomia: Taxonomia) -> Taxonomia:
        pass

    @abstractmethod
    def delete(self, taxonomia_id: str) -> bool:
        pass

    @abstractmethod
    def exists_by_codigo(self, codigo: str) -> bool:
        pass


class TermoTaxonomiaRepositoryInterface(ABC):
    """Interface para repositório de termos de taxonomia."""

    @abstractmethod
    def get_by_id(self, termo_id: str) -> TermoTaxonomia | None:
        pass

    @abstractmethod
    def get_by_taxonomia(self, taxonomia_id: str) -> list[TermoTaxonomia]:
        pass

    @abstractmethod
    def get_by_pai(self, termo_pai_id: str) -> list[TermoTaxonomia]:
        pass

    @abstractmethod
    def list_all(
        self, page: int = 0, page_size: int = 50, taxonomia_id: str | None = None,
    ) -> tuple[list[TermoTaxonomia], int]:
        pass

    @abstractmethod
    def save(self, termo: TermoTaxonomia) -> TermoTaxonomia:
        pass

    @abstractmethod
    def delete(self, termo_id: str) -> bool:
        pass


__all__ = [
    "MetadadoRepositoryInterface",
    "ValorMetadadoRepositoryInterface",
    "ClassificacaoRepositoryInterface",
    "TaxonomiaRepositoryInterface",
    "TermoTaxonomiaRepositoryInterface",
]
