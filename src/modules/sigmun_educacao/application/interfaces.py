"""Interfaces (ports) dos repositorios do DOM-EDU."""

from __future__ import annotations

from typing import Protocol


class RepositorioAluno(Protocol):
    """Port de persistencia de alunos."""

    def save(self, aluno):  # type: ignore[no-untyped-def]
        """Persiste um aluno."""
        ...

    def get_by_id(self, aluno_id: str):  # type: ignore[no-untyped-def]
        """Busca aluno por id."""
        ...

    def get_by_cpf(self, cpf: str):  # type: ignore[no-untyped-def]
        """Busca aluno pelo CPF."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista alunos paginados."""
        ...


class RepositorioMatricula(Protocol):
    """Port de persistencia de matriculas escolares."""

    def save(self, matricula):  # type: ignore[no-untyped-def]
        """Persiste uma matricula."""
        ...

    def get_by_id(self, matricula_id: str):  # type: ignore[no-untyped-def]
        """Busca matricula por id."""
        ...

    def get_ativa_by_aluno(self, aluno_id: str):  # type: ignore[no-untyped-def]
        """Busca a matricula ativa do aluno."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista matriculas paginadas."""
        ...


class RepositorioLancamentoDiario(Protocol):
    """Port de persistencia do diario de classe digital."""

    def save(self, lancamento):  # type: ignore[no-untyped-def]
        """Persiste um lancamento."""
        ...

    def get_by_id(self, lancamento_id: str):  # type: ignore[no-untyped-def]
        """Busca lancamento por id."""
        ...

    def list_by_matricula(self, matricula_id: str) -> list:  # type: ignore[type-arg]
        """Lista lancamentos da matricula em ordem cronologica."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista lancamentos paginados."""
        ...


class RepositorioRotaTransporte(Protocol):
    """Port de persistencia de rotas de transporte escolar."""

    def save(self, rota):  # type: ignore[no-untyped-def]
        """Persiste uma rota."""
        ...

    def get_by_id(self, rota_id: str):  # type: ignore[no-untyped-def]
        """Busca rota por id."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista rotas paginadas."""
        ...


class RepositorioPassagemTransporte(Protocol):
    """Port de persistencia de passagens de transporte escolar."""

    def save(self, passagem):  # type: ignore[no-untyped-def]
        """Persiste uma passagem."""
        ...

    def get_by_id(self, passagem_id: str):  # type: ignore[no-untyped-def]
        """Busca passagem por id."""
        ...

    def count_by_rota_data(self, rota_id: str, data) -> int:  # type: ignore[no-untyped-def]
        """Conta passagens da rota em uma data (cheque de vagas)."""
        ...

    def list_by_rota(self, rota_id: str) -> list:  # type: ignore[type-arg]
        """Lista passagens da rota."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista passagens paginadas."""
        ...


class RepositorioItemMerenda(Protocol):
    """Port de persistencia do estoque de merenda."""

    def save(self, item):  # type: ignore[no-untyped-def]
        """Persiste um item."""
        ...

    def get_by_id(self, item_id: str):  # type: ignore[no-untyped-def]
        """Busca item por id."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista itens paginados."""
        ...


class RepositorioDistribuicaoMerenda(Protocol):
    """Port de persistencia de distribuicoes de merenda."""

    def save(self, distribuicao):  # type: ignore[no-untyped-def]
        """Persiste uma distribuicao."""
        ...

    def get_by_id(self, distribuicao_id: str):  # type: ignore[no-untyped-def]
        """Busca distribuicao por id."""
        ...

    def list_by_matricula(self, matricula_id: str) -> list:  # type: ignore[type-arg]
        """Lista distribuicoes da matricula."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list:  # type: ignore[type-arg]
        """Lista distribuicoes paginadas."""
        ...


__all__ = [
    "RepositorioAluno",
    "RepositorioMatricula",
    "RepositorioLancamentoDiario",
    "RepositorioRotaTransporte",
    "RepositorioPassagemTransporte",
    "RepositorioItemMerenda",
    "RepositorioDistribuicaoMerenda",
]
