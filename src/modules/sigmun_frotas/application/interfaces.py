"""Interfaces (ports) dos repositórios do DOM-FRO."""

from __future__ import annotations

from typing import Protocol


class RepositorioVeiculo(Protocol):
    """Port de persistência de veículos."""

    def save(self, veiculo):  # type: ignore[no-untyped-def]
        """Persiste um veículo."""
        ...

    def get_by_id(self, veiculo_id: str):  # type: ignore[no-untyped-def]
        """Busca veículo por id."""
        ...

    def get_by_placa(self, placa: str):  # type: ignore[no-untyped-def]
        """Busca veículo pela placa."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista veículos paginados."""
        ...


class RepositorioAbastecimento(Protocol):
    """Port de persistência de abastecimentos."""

    def save(self, abastecimento):  # type: ignore[no-untyped-def]
        """Persiste um abastecimento."""
        ...

    def get_by_id(self, abastecimento_id: str):  # type: ignore[no-untyped-def]
        """Busca abastecimento por id."""
        ...

    def list_by_veiculo(self, veiculo_id: str) -> list:  # type: ignore[type-arg]
        """Lista abastecimentos de um veículo."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista abastecimentos paginados."""
        ...


class RepositorioManutencao(Protocol):
    """Port de persistência de manutenções."""

    def save(self, manutencao):  # type: ignore[no-untyped-def]
        """Persiste uma manutenção."""
        ...

    def get_by_id(self, manutencao_id: str):  # type: ignore[no-untyped-def]
        """Busca manutenção por id."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista manutenções paginadas."""
        ...


class RepositorioRota(Protocol):
    """Port de persistência de rotas."""

    def save(self, rota):  # type: ignore[no-untyped-def]
        """Persiste uma rota."""
        ...

    def get_by_id(self, rota_id: str):  # type: ignore[no-untyped-def]
        """Busca rota por id."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista rotas paginadas."""
        ...


__all__ = [
    "RepositorioVeiculo",
    "RepositorioAbastecimento",
    "RepositorioManutencao",
    "RepositorioRota",
]