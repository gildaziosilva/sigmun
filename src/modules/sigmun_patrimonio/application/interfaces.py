"""Interfaces (ports) dos repositórios do DOM-PAT."""

from __future__ import annotations

from typing import Protocol


class RepositorioBem(Protocol):
    """Port de persistência de bens."""

    def save(self, bem):  # type: ignore[no-untyped-def]
        """Persiste um bem."""
        ...

    def get_by_id(self, bem_id: str):  # type: ignore[no-untyped-def]
        """Busca bem por id."""
        ...

    def get_by_codigo(self, codigo: str):  # type: ignore[no-untyped-def]
        """Busca bem pelo tombo/código."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista bens paginados."""
        ...


class RepositorioDepreciacao(Protocol):
    """Port de persistência de depreciações."""

    def save(self, depreciacao):  # type: ignore[no-untyped-def]
        """Persiste uma depreciação."""
        ...

    def list_by_bem(self, bem_id: str) -> list:  # type: ignore[type-arg]
        """Lista depreciações de um bem."""
        ...


class RepositorioTransferencia(Protocol):
    """Port de persistência de transferências."""

    def save(self, transferencia):  # type: ignore[no-untyped-def]
        """Persiste uma transferência."""
        ...

    def get_by_id(self, transferencia_id: str):  # type: ignore[no-untyped-def]
        """Busca transferência por id."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista transferências paginadas."""
        ...


__all__ = ["RepositorioBem", "RepositorioDepreciacao", "RepositorioTransferencia"]