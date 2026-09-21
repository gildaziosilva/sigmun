"""Interfaces (ports) dos repositórios do DOM-TRI."""

from __future__ import annotations

from typing import Protocol


class RepositorioContribuinte(Protocol):
    """Port de persistência de contribuintes."""

    def save(self, contribuinte):  # type: ignore[no-untyped-def]
        """Persiste um contribuinte."""
        ...

    def get_by_id(self, contribuinte_id: str):  # type: ignore[no-untyped-def]
        """Busca contribuinte por id."""
        ...

    def get_by_cpf_cnpj(self, documento: str):  # type: ignore[no-untyped-def]
        """Busca contribuinte por CPF/CNPJ."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista contribuintes paginados."""
        ...


class RepositorioImovel(Protocol):
    """Port de persistência de imóveis."""

    def save(self, imovel):  # type: ignore[no-untyped-def]
        """Persiste um imóvel."""
        ...

    def get_by_id(self, imovel_id: str):  # type: ignore[no-untyped-def]
        """Busca imóvel por id."""
        ...

    def get_by_inscricao(self, inscricao: str):  # type: ignore[no-untyped-def]
        """Busca imóvel por inscrição imobiliária."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista imóveis paginados."""
        ...


class RepositorioLancamento(Protocol):
    """Port de persistência de lançamentos (créditos tributários)."""

    def save(self, lancamento):  # type: ignore[no-untyped-def]
        """Persiste um lançamento."""
        ...

    def get_by_id(self, lancamento_id: str):  # type: ignore[no-untyped-def]
        """Busca lançamento por id."""
        ...

    def get_by_numero(self, numero: str):  # type: ignore[no-untyped-def]
        """Busca lançamento pelo número."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista lançamentos paginados."""
        ...

    def list_abertos_por_contribuinte(self, contribuinte_id: str) -> list:  # type: ignore[type-arg]
        """Lista débitos abertos (lançados ou inscritos) do contribuinte."""
        ...


class RepositorioDividaAtiva(Protocol):
    """Port de persistência de inscrições em dívida ativa."""

    def save(self, inscricao):  # type: ignore[no-untyped-def]
        """Persiste uma inscrição."""
        ...

    def get_by_id(self, inscricao_id: str):  # type: ignore[no-untyped-def]
        """Busca inscrição por id."""
        ...

    def get_by_numero(self, numero: str):  # type: ignore[no-untyped-def]
        """Busca inscrição pelo número."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista inscrições paginadas."""
        ...


class RepositorioCertidao(Protocol):
    """Port de persistência de certidões."""

    def save(self, certidao):  # type: ignore[no-untyped-def]
        """Persiste uma certidão."""
        ...

    def get_by_id(self, certidao_id: str):  # type: ignore[no-untyped-def]
        """Busca certidão por id."""
        ...

    def list_by_contribuinte(self, contribuinte_id: str) -> list:  # type: ignore[type-arg]
        """Lista certidões de um contribuinte."""
        ...


__all__ = [
    "RepositorioContribuinte",
    "RepositorioImovel",
    "RepositorioLancamento",
    "RepositorioDividaAtiva",
    "RepositorioCertidao",
]