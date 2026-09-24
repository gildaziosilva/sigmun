"""Entidade Aluno — estudante da rede municipal de ensino (DOM-EDU).

RN-EDU-001: o CPF do aluno, quando informado, tem 11 dígitos e é único
no cadastro municipal (checagem no caso de uso + índice parcial no banco).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class Sexo(Enum):
    """Sexo biológico registrado."""

    MASCULINO = "masculino"
    FEMININO = "feminino"
    IGNORADO = "ignorado"


class StatusAluno(Enum):
    """Situação cadastral do aluno."""

    ATIVO = "ativo"
    INATIVO = "inativo"


def _valida_cpf(cpf: str) -> None:
    """Valida a forma do CPF (11 dígitos), apenas quando informado."""
    from ..exceptions import RegraNegocioError

    if cpf and (not cpf.isdigit() or len(cpf) != 11):
        raise RegraNegocioError(
            "CPF inválido: informe 11 dígitos numéricos ou deixe em branco (RN-EDU-001)"
        )


@dataclass
class Aluno:
    """Estudante matriculado (ou a matricular) na rede municipal."""

    id: str = field(default_factory=lambda: str(uuid4()))
    nome: str = ""
    cpf: str = ""
    data_nascimento: str = ""
    sexo: Sexo = field(default=Sexo.IGNORADO)
    nome_mae: str = ""
    telefone: str = ""
    endereco: str = ""
    status: StatusAluno = field(default=StatusAluno.ATIVO)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        """Indica se o aluno está ativo e não excluído."""
        return self.status == StatusAluno.ATIVO and not self.is_deleted

    def inativar(self) -> None:
        """Inativa o cadastro do aluno."""
        self.status = StatusAluno.INATIVO
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca o aluno como excluído (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida regras estruturais da entidade."""
        from ..exceptions import RegraNegocioError

        if not self.nome:
            raise RegraNegocioError("Nome do aluno é obrigatório (RN-EDU-001)")
        _valida_cpf(self.cpf)


__all__ = ["Sexo", "StatusAluno", "Aluno"]
