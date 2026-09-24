"""Entidade Paciente — cidadão com prontuário eletrônico (DOM-SAU).

RN-SAU-001: o CNS do paciente é único no cadastro municipal.
RN-SAU-002: prontuário reúne atendimentos em ordem cronológica.
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


class StatusPaciente(Enum):
    """Situação cadastral do paciente."""

    ATIVO = "ativo"
    INATIVO = "inativo"
    OBITO = "obito"


def _valida_cns(cns: str) -> None:
    """Valida a forma do CNS (15 dígitos numéricos)."""
    from ..exceptions import RegraNegocioError

    if not cns or not cns.isdigit() or len(cns) != 15:
        raise RegraNegocioError(
            "CNS inválido: informe 15 dígitos numéricos (RN-SAU-001)"
        )


@dataclass
class Paciente:
    """Cidadão atendido pela rede municipal de saúde."""

    id: str = field(default_factory=lambda: str(uuid4()))
    nome: str = ""
    cns: str = ""
    cpf: str = ""
    data_nascimento: str = ""
    sexo: Sexo = field(default=Sexo.IGNORADO)
    nome_mae: str = ""
    telefone: str = ""
    endereco: str = ""
    ubs_referencia: str = ""
    status: StatusPaciente = field(default=StatusPaciente.ATIVO)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        """Indica se o paciente está ativo e não excluído."""
        return self.status == StatusPaciente.ATIVO and not self.is_deleted

    def inativar(self) -> None:
        """Inativa o cadastro do paciente."""
        self.status = StatusPaciente.INATIVO
        self.updated_at = datetime.utcnow()

    def registrar_obito(self) -> None:
        """Registra óbito do paciente."""
        self.status = StatusPaciente.OBITO
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca o paciente como excluído (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida regras estruturais da entidade."""
        from ..exceptions import RegraNegocioError

        if not self.nome:
            raise RegraNegocioError("Nome do paciente é obrigatório")
        _valida_cns(self.cns)


__all__ = ["Sexo", "StatusPaciente", "Paciente"]
