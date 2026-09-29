"""Interfaces (ports) dos repositórios do DOM-ASS."""

from __future__ import annotations

from typing import Protocol

from ..domain.entities import (
    AtendimentoSocial,
    BeneficioEventual,
    FamiliaCadUnico,
    PessoaCadUnico,
    UnidadeAssistencia,
)


class RepositorioFamilia(Protocol):
    """Port de persistência de famílias do CadÚnico."""

    def save(self, familia: FamiliaCadUnico) -> FamiliaCadUnico:
        """Persiste uma família."""
        ...

    def get_by_id(self, familia_id: str) -> FamiliaCadUnico | None:
        """Busca família por id."""
        ...

    def get_by_nis(self, nis: str) -> FamiliaCadUnico | None:
        """Busca família pelo NIS."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list[FamiliaCadUnico]:
        """Lista famílias paginadas."""
        ...


class RepositorioPessoa(Protocol):
    """Port de persistência de pessoas do CadÚnico."""

    def save(self, pessoa: PessoaCadUnico) -> PessoaCadUnico:
        """Persiste uma pessoa."""
        ...

    def get_by_id(self, pessoa_id: str) -> PessoaCadUnico | None:
        """Busca pessoa por id."""
        ...

    def get_by_cpf(self, cpf: str) -> PessoaCadUnico | None:
        """Busca pessoa pelo CPF."""
        ...

    def list_by_familia(self, familia_id: str) -> list[PessoaCadUnico]:
        """Lista pessoas da família."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list[PessoaCadUnico]:
        """Lista pessoas paginadas."""
        ...


class RepositorioUnidade(Protocol):
    """Port de persistência de unidades CRAS/CREAS."""

    def save(self, unidade: UnidadeAssistencia) -> UnidadeAssistencia:
        """Persiste uma unidade."""
        ...

    def get_by_id(self, unidade_id: str) -> UnidadeAssistencia | None:
        """Busca unidade por id."""
        ...

    def get_by_codigo(self, codigo: str) -> UnidadeAssistencia | None:
        """Busca unidade pelo código."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list[UnidadeAssistencia]:
        """Lista unidades paginadas."""
        ...


class RepositorioBeneficio(Protocol):
    """Port de persistência de benefícios eventuais."""

    def save(self, beneficio: BeneficioEventual) -> BeneficioEventual:
        """Persiste um benefício."""
        ...

    def get_by_id(self, beneficio_id: str) -> BeneficioEventual | None:
        """Busca benefício por id."""
        ...

    def list_by_familia(self, familia_id: str) -> list[BeneficioEventual]:
        """Lista benefícios da família."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list[BeneficioEventual]:
        """Lista benefícios paginados."""
        ...


class RepositorioAtendimento(Protocol):
    """Port de persistência de atendimentos sociais."""

    def save(self, atendimento: AtendimentoSocial) -> AtendimentoSocial:
        """Persiste um atendimento."""
        ...

    def get_by_id(self, atendimento_id: str) -> AtendimentoSocial | None:
        """Busca atendimento por id."""
        ...

    def list_by_pessoa(self, pessoa_id: str) -> list[AtendimentoSocial]:
        """Lista atendimentos da pessoa."""
        ...

    def list_by_unidade(self, unidade_id: str) -> list[AtendimentoSocial]:
        """Lista atendimentos da unidade."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list[AtendimentoSocial]:
        """Lista atendimentos paginados."""
        ...


__all__ = [
    "RepositorioFamilia",
    "RepositorioPessoa",
    "RepositorioUnidade",
    "RepositorioBeneficio",
    "RepositorioAtendimento",
]
