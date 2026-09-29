"""Interfaces (ports) dos repositórios do DOM-TEL."""

from __future__ import annotations

from typing import Protocol

from ..domain.entities import Bairro, Georreferencia, Logradouro, PlantaGenericaValores


class RepositorioBairro(Protocol):
    """Port de persistência de divisões territoriais."""

    def save(self, bairro: Bairro) -> Bairro:
        """Persiste um bairro."""
        ...

    def get_by_id(self, bairro_id: str) -> Bairro | None:
        """Busca bairro por id."""
        ...

    def get_by_codigo(self, codigo: str) -> Bairro | None:
        """Busca bairro pelo código cadastral."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list[Bairro]:
        """Lista bairros paginados."""
        ...


class RepositorioLogradouro(Protocol):
    """Port de persistência de logradouros públicos."""

    def save(self, logradouro: Logradouro) -> Logradouro:
        """Persiste um logradouro."""
        ...

    def get_by_id(self, logradouro_id: str) -> Logradouro | None:
        """Busca logradouro por id."""
        ...

    def get_by_codigo(self, codigo: str) -> Logradouro | None:
        """Busca logradouro pelo código cadastral."""
        ...

    def list_by_bairro(self, bairro_id: str) -> list[Logradouro]:
        """Lista logradouros de um bairro."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list[Logradouro]:
        """Lista logradouros paginados."""
        ...


class RepositorioPlantaValores(Protocol):
    """Port de persistência da planta genérica de valores."""

    def save(self, planta: PlantaGenericaValores) -> PlantaGenericaValores:
        """Persiste uma planta genérica de valores."""
        ...

    def get_by_id(self, planta_id: str) -> PlantaGenericaValores | None:
        """Busca planta genérica de valores por id."""
        ...

    def get_vigente(
        self, ano: int, bairro_id: str, ocupacao: str
    ) -> PlantaGenericaValores | None:
        """Busca a planta vigente para ano, bairro e ocupação (RN-TEL-003)."""
        ...

    def get_by_ano_bairro_ocupacao(
        self, ano: int, bairro_id: str, ocupacao: str
    ) -> PlantaGenericaValores | None:
        """Busca a planta da combinação, independente da situação."""
        ...

    def list_all(
        self, page: int = 1, page_size: int = 20, bairro_id: str | None = None
    ) -> list[PlantaGenericaValores]:
        """Lista plantas genéricas de valores, opcionalmente por bairro."""
        ...


class RepositorioGeorreferencia(Protocol):
    """Port de persistência de georreferências territoriais."""

    def save(self, georreferencia: Georreferencia) -> Georreferencia:
        """Persiste uma georreferência."""
        ...

    def get_by_id(self, georreferencia_id: str) -> Georreferencia | None:
        """Busca georreferência por id."""
        ...

    def list_by_referencia(
        self, bairro_id: str | None = None, logradouro_id: str | None = None
    ) -> list[Georreferencia]:
        """Lista georreferências por bairro ou logradouro."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list[Georreferencia]:
        """Lista georreferências paginadas."""
        ...


__all__ = [
    "RepositorioBairro",
    "RepositorioLogradouro",
    "RepositorioPlantaValores",
    "RepositorioGeorreferencia",
]
