"""Interfaces (ports) dos repositórios do DOM-PES."""

from __future__ import annotations

from datetime import date
from typing import Protocol


class RepositorioCargo(Protocol):
    """Port de persistência de cargos."""

    def save(self, cargo):  # type: ignore[no-untyped-def]
        """Persiste um cargo."""
        ...

    def get_by_id(self, cargo_id: str):  # type: ignore[no-untyped-def]
        """Busca cargo por id."""
        ...

    def get_by_codigo(self, codigo: str):  # type: ignore[no-untyped-def]
        """Busca cargo por código."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista cargos paginados."""
        ...


class RepositorioServidor(Protocol):
    """Port de persistência de servidores."""

    def save(self, servidor):  # type: ignore[no-untyped-def]
        """Persiste um servidor."""
        ...

    def get_by_id(self, servidor_id: str):  # type: ignore[no-untyped-def]
        """Busca servidor por id."""
        ...

    def get_by_matricula(self, matricula: str):  # type: ignore[no-untyped-def]
        """Busca servidor por matrícula."""
        ...

    def get_by_cpf(self, cpf: str):  # type: ignore[no-untyped-def]
        """Busca servidor por CPF."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista servidores paginados."""
        ...


class RepositorioLotacao(Protocol):
    """Port de persistência de lotações."""

    def save(self, lotacao):  # type: ignore[no-untyped-def]
        """Persiste uma lotação."""
        ...

    def get_by_id(self, lotacao_id: str):  # type: ignore[no-untyped-def]
        """Busca lotação por id."""
        ...

    def list_vigentes_por_servidor(self, servidor_id: str) -> list:  # type: ignore[type-arg]
        """Lista lotações vigentes de um servidor."""
        ...

    def list_by_servidor(self, servidor_id: str) -> list:  # type: ignore[type-arg]
        """Lista todas as lotações de um servidor."""
        ...


class RepositorioFolha(Protocol):
    """Port de persistência da folha de pagamento."""

    def save(self, folha):  # type: ignore[no-untyped-def]
        """Persiste uma folha."""
        ...

    def get_by_id(self, folha_id: str):  # type: ignore[no-untyped-def]
        """Busca folha por id."""
        ...

    def get_by_competencia(self, ano: int, mes: int):  # type: ignore[no-untyped-def]
        """Busca folha pela competência."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista folhas paginadas."""
        ...


class RepositorioFerias(Protocol):
    """Port de persistência de férias."""

    def save(self, ferias):  # type: ignore[no-untyped-def]
        """Persiste um período de férias."""
        ...

    def get_by_id(self, ferias_id: str):  # type: ignore[no-untyped-def]
        """Busca férias por id."""
        ...

    def list_by_servidor(self, servidor_id: str) -> list:  # type: ignore[type-arg]
        """Lista férias de um servidor."""
        ...


class RepositorioFrequencia(Protocol):
    """Port de persistência de frequência."""

    def save(self, frequencia):  # type: ignore[no-untyped-def]
        """Persiste um registro de frequência."""
        ...

    def get_by_id(self, frequencia_id: str):  # type: ignore[no-untyped-def]
        """Busca frequência por id."""
        ...

    def get_por_servidor_data(self, servidor_id: str, data: date):  # type: ignore[no-untyped-def]
        """Busca registro de um servidor em uma data."""
        ...

    def list_by_servidor(self, servidor_id: str) -> list:  # type: ignore[type-arg]
        """Lista registros de um servidor."""
        ...


__all__ = [
    "RepositorioCargo",
    "RepositorioServidor",
    "RepositorioLotacao",
    "RepositorioFolha",
    "RepositorioFerias",
    "RepositorioFrequencia",
]
