"""Ports de repositórios do DOM-ORC."""

from __future__ import annotations

from typing import Protocol


class RepositorioPPA(Protocol):
    """Port de persistência de PPAs."""

    def save(self, ppa):  # type: ignore[no-untyped-def]
        """Persiste um PPA."""
        ...

    def get_by_id(self, ppa_id: str):  # type: ignore[no-untyped-def]
        """Busca PPA por id."""
        ...

    def get_by_quadrienio(self, ano_inicial: int, ano_final: int):  # type: ignore[no-untyped-def]
        """Busca PPA pelo quadriênio."""
        ...


class RepositorioLDO(Protocol):
    """Port de persistência de LDOs."""

    def save(self, ldo):  # type: ignore[no-untyped-def]
        """Persiste uma LDO."""
        ...

    def get_by_id(self, ldo_id: str):  # type: ignore[no-untyped-def]
        """Busca LDO por id."""
        ...

    def get_by_exercicio(self, exercicio: int):  # type: ignore[no-untyped-def]
        """Busca LDO pelo exercício."""
        ...


class RepositorioLOA(Protocol):
    """Port de persistência de LOAs."""

    def save(self, loa):  # type: ignore[no-untyped-def]
        """Persiste uma LOA."""
        ...

    def get_by_id(self, loa_id: str):  # type: ignore[no-untyped-def]
        """Busca LOA por id."""
        ...

    def get_by_exercicio(self, exercicio: int):  # type: ignore[no-untyped-def]
        """Busca LOA pelo exercício."""
        ...


class RepositorioDotacao(Protocol):
    """Port de persistência de dotações."""

    def save(self, dotacao):  # type: ignore[no-untyped-def]
        """Persiste uma dotação."""
        ...

    def get_by_id(self, dotacao_id: str):  # type: ignore[no-untyped-def]
        """Busca dotação por id."""
        ...

    def get_by_codigo_exercicio(self, codigo: str, exercicio: int):  # type: ignore[no-untyped-def]
        """Busca dotação por código/exercício."""
        ...


class RepositorioReserva(Protocol):
    """Port de persistência de reservas de saldo."""

    def save(self, reserva):  # type: ignore[no-untyped-def]
        """Persiste uma reserva."""
        ...

    def get_by_id(self, reserva_id: str):  # type: ignore[no-untyped-def]
        """Busca reserva por id."""
        ...


__all__ = [
    "RepositorioPPA",
    "RepositorioLDO",
    "RepositorioLOA",
    "RepositorioDotacao",
    "RepositorioReserva",
]
