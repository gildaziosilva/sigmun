"""Ports de repositórios do DOM-CON."""

from __future__ import annotations

from typing import Protocol


class RepositorioEmpenho(Protocol):
    """Port de persistência de empenhos."""

    def save(self, empenho):  # type: ignore[no-untyped-def]
        """Persiste um empenho."""
        ...

    def get_by_id(self, empenho_id: str):  # type: ignore[no-untyped-def]
        """Busca empenho por id."""
        ...

    def get_by_numero_exercicio(self, numero: str, exercicio: int):  # type: ignore[no-untyped-def]
        """Busca empenho por número/exercício."""
        ...


class RepositorioLiquidacao(Protocol):
    """Port de persistência de liquidações."""

    def save(self, liquidacao):  # type: ignore[no-untyped-def]
        """Persiste uma liquidação."""
        ...

    def get_by_id(self, liquidacao_id: str):  # type: ignore[no-untyped-def]
        """Busca liquidação por id."""
        ...


class RepositorioPagamento(Protocol):
    """Port de persistência de pagamentos."""

    def save(self, pagamento):  # type: ignore[no-untyped-def]
        """Persiste um pagamento."""
        ...

    def get_by_id(self, pagamento_id: str):  # type: ignore[no-untyped-def]
        """Busca pagamento por id."""
        ...


class RepositorioContaContabil(Protocol):
    """Port de persistência do PCASP."""

    def save(self, conta):  # type: ignore[no-untyped-def]
        """Persiste uma conta contábil."""
        ...

    def get_by_id(self, conta_id: str):  # type: ignore[no-untyped-def]
        """Busca conta por id."""
        ...

    def get_by_codigo(self, codigo: str):  # type: ignore[no-untyped-def]
        """Busca conta por código."""
        ...


class RepositorioLancamento(Protocol):
    """Port de persistência de lançamentos."""

    def save(self, lancamento):  # type: ignore[no-untyped-def]
        """Persiste um lançamento."""
        ...

    def get_by_id(self, lancamento_id: str):  # type: ignore[no-untyped-def]
        """Busca lançamento por id."""
        ...


class RepositorioConciliacao(Protocol):
    """Port de persistência de conciliações."""

    def save(self, conciliacao):  # type: ignore[no-untyped-def]
        """Persiste uma conciliação."""
        ...

    def get_by_id(self, conciliacao_id: str):  # type: ignore[no-untyped-def]
        """Busca conciliação por id."""
        ...


__all__ = [
    "RepositorioEmpenho",
    "RepositorioLiquidacao",
    "RepositorioPagamento",
    "RepositorioContaContabil",
    "RepositorioLancamento",
    "RepositorioConciliacao",
]
