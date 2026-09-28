"""Interfaces (ports) dos repositórios do DOM-ASS."""

from __future__ import annotations

from typing import Protocol


class RepositorioFamilia(Protocol):
    """Port de persistência de famílias do CadÚnico."""

    def save(self, familia):  # type: ignore[no-untyped-def]
        """Persiste uma família."""
        ...

    def get_by_id(self, familia_id: str):  # type: ignore[no-untyped-def]
        """Busca família por id."""
        ...

    def get_by_nis(self, nis: str):  # type: ignore[no-untyped-def]
        """Busca família pelo NIS."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista famílias paginadas."""
        ...


class RepositorioPessoa(Protocol):
    """Port de persistência de pessoas do CadÚnico."""

    def save(self, pessoa):  # type: ignore[no-untyped-def]
        """Persiste uma pessoa."""
        ...

    def get_by_id(self, pessoa_id: str):  # type: ignore[no-untyped-def]
        """Busca pessoa por id."""
        ...

    def get_by_cpf(self, cpf: str):  # type: ignore[no-untyped-def]
        """Busca pessoa pelo CPF."""
        ...

    def list_by_familia(self, familia_id: str) -> list:  # type: ignore[type-arg]
        """Lista pessoas da família."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista pessoas paginadas."""
        ...


class RepositorioUnidade(Protocol):
    """Port de persistência de unidades CRAS/CREAS."""

    def save(self, unidade):  # type: ignore[no-untyped-def]
        """Persiste uma unidade."""
        ...

    def get_by_id(self, unidade_id: str):  # type: ignore[no-untyped-def]
        """Busca unidade por id."""
        ...

    def get_by_codigo(self, codigo: str):  # type: ignore[no-untyped-def]
        """Busca unidade pelo código."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista unidades paginadas."""
        ...


class RepositorioBeneficio(Protocol):
    """Port de persistência de benefícios eventuais."""

    def save(self, beneficio):  # type: ignore[no-untyped-def]
        """Persiste um benefício."""
        ...

    def get_by_id(self, beneficio_id: str):  # type: ignore[no-untyped-def]
        """Busca benefício por id."""
        ...

    def list_by_familia(self, familia_id: str) -> list:  # type: ignore[type-arg]
        """Lista benefícios da família."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista benefícios paginados."""
        ...


class RepositorioAtendimento(Protocol):
    """Port de persistência de atendimentos sociais."""

    def save(self, atendimento):  # type: ignore[no-untyped-def]
        """Persiste um atendimento."""
        ...

    def get_by_id(self, atendimento_id: str):  # type: ignore[no-untyped-def]
        """Busca atendimento por id."""
        ...

    def list_by_pessoa(self, pessoa_id: str) -> list:  # type: ignore[type-arg]
        """Lista atendimentos da pessoa."""
        ...

    def list_by_unidade(self, unidade_id: str) -> list:  # type: ignore[type-arg]
        """Lista atendimentos da unidade."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista atendimentos paginados."""
        ...


__all__ = [
    "RepositorioFamilia",
    "RepositorioPessoa",
    "RepositorioUnidade",
    "RepositorioBeneficio",
    "RepositorioAtendimento",
]