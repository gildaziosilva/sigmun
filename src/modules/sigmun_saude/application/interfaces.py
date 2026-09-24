"""Interfaces (ports) dos repositorios do DOM-SAU."""

from __future__ import annotations

from typing import Protocol


class RepositorioPaciente(Protocol):
    """Port de persistencia de pacientes."""

    def save(self, paciente):  # type: ignore[no-untyped-def]
        """Persiste um paciente."""
        ...

    def get_by_id(self, paciente_id: str):  # type: ignore[no-untyped-def]
        """Busca paciente por id."""
        ...

    def get_by_cns(self, cns: str):  # type: ignore[no-untyped-def]
        """Busca paciente pelo CNS."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista pacientes paginados."""
        ...


class RepositorioAtendimento(Protocol):
    """Port de persistencia de atendimentos do prontuario."""

    def save(self, atendimento):  # type: ignore[no-untyped-def]
        """Persiste um atendimento."""
        ...

    def get_by_id(self, atendimento_id: str):  # type: ignore[no-untyped-def]
        """Busca atendimento por id."""
        ...

    def list_by_paciente(self, paciente_id: str) -> list:  # type: ignore[type-arg]
        """Lista atendimentos do paciente em ordem cronologica."""
        ...


class RepositorioAgendamento(Protocol):
    """Port de persistencia de agendamentos SUS."""

    def save(self, agendamento):  # type: ignore[no-untyped-def]
        """Persiste um agendamento."""
        ...

    def get_by_id(self, agendamento_id: str):  # type: ignore[no-untyped-def]
        """Busca agendamento por id."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista agendamentos paginados."""
        ...


class RepositorioRegulacao(Protocol):
    """Port de persistencia da central de regulacao."""

    def save(self, regulacao):  # type: ignore[no-untyped-def]
        """Persiste uma solicitacao."""
        ...

    def get_by_id(self, regulacao_id: str):  # type: ignore[no-untyped-def]
        """Busca solicitacao por id."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista solicitacoes paginadas."""
        ...


class RepositorioMedicamento(Protocol):
    """Port de persistencia da farmacia basica."""

    def save(self, medicamento):  # type: ignore[no-untyped-def]
        """Persiste um medicamento."""
        ...

    def get_by_id(self, medicamento_id: str):  # type: ignore[no-untyped-def]
        """Busca medicamento por id."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista medicamentos paginados."""
        ...


class RepositorioDispensacao(Protocol):
    """Port de persistencia de dispensacoes."""

    def save(self, dispensacao):  # type: ignore[no-untyped-def]
        """Persiste uma dispensacao."""
        ...

    def get_by_id(self, dispensacao_id: str):  # type: ignore[no-untyped-def]
        """Busca dispensacao por id."""
        ...

    def list_by_paciente(self, paciente_id: str) -> list:  # type: ignore[type-arg]
        """Lista dispensacoes do paciente."""
        ...


__all__ = [
    "RepositorioPaciente",
    "RepositorioAtendimento",
    "RepositorioAgendamento",
    "RepositorioRegulacao",
    "RepositorioMedicamento",
    "RepositorioDispensacao",
]
