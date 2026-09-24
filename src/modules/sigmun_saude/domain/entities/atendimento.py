"""Entidades Atendimento e Agendamento — prontuário e agenda SUS (DOM-SAU).

RN-SAU-010: atendimento exige paciente e profissional/estabelecimento.
RN-SAU-020: agendamento nasce ``agendado`` e só transita para
    ``confirmado/cancelado/realizado/falta``; realizado/falta são finais.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from uuid import uuid4


class TipoAtendimento(Enum):
    """Tipo de contato assistencial."""

    CONSULTA = "consulta"
    RETORNO = "retorno"
    URGENCIA = "urgencia"
    VISITA_DOMICILIAR = "visita_domiciliar"
    TELEATENDIMENTO = "teleatendimento"


class StatusAgendamento(Enum):
    """Situação do agendamento na fila SUS."""

    AGENDADO = "agendado"
    CONFIRMADO = "confirmado"
    CANCELADO = "cancelado"
    REALIZADO = "realizado"
    FALTA = "falta"


@dataclass
class Atendimento:
    """Registro clínico do prontuário eletrônico do cidadão."""

    id: str = field(default_factory=lambda: str(uuid4()))
    paciente_id: str = ""
    data: date | None = None
    tipo: TipoAtendimento = field(default=TipoAtendimento.CONSULTA)
    profissional: str = ""
    estabelecimento: str = ""
    queixa: str = ""
    conduta: str = ""
    cid10: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""

    def validar(self) -> None:
        """Valida regras estruturais do atendimento."""
        from ..exceptions import RegraNegocioError

        if not self.paciente_id:
            raise RegraNegocioError(
                "Atendimento exige paciente vinculado (RN-SAU-010)"
            )
        if not self.profissional or not self.estabelecimento:
            raise RegraNegocioError(
                "Profissional e estabelecimento são obrigatórios (RN-SAU-010)"
            )


@dataclass
class Agendamento:
    """Vaga SUS agendada para o cidadão."""

    id: str = field(default_factory=lambda: str(uuid4()))
    paciente_id: str = ""
    especialidade: str = ""
    data: date | None = None
    hora: str = ""
    estabelecimento: str = ""
    status: StatusAgendamento = field(default=StatusAgendamento.AGENDADO)
    motivo_cancelamento: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""

    def validar(self) -> None:
        """Valida regras estruturais do agendamento."""
        from ..exceptions import RegraNegocioError

        if not self.paciente_id:
            raise RegraNegocioError("Agendamento exige paciente vinculado")
        if not self.especialidade or self.data is None:
            raise RegraNegocioError(
                "Especialidade e data são obrigatórias no agendamento"
            )

    def confirmar(self) -> None:
        """Confirma presença prevista."""
        from ..exceptions import EstadoAgendamentoInvalidoError

        if self.status != StatusAgendamento.AGENDADO:
            raise EstadoAgendamentoInvalidoError(
                f"Só é possível confirmar agendamento agendado (atual: {self.status.value})"
            )
        self.status = StatusAgendamento.CONFIRMADO
        self.updated_at = datetime.utcnow()

    def cancelar(self, motivo: str = "") -> None:
        """Cancela o agendamento."""
        from ..exceptions import EstadoAgendamentoInvalidoError

        if self.status in (StatusAgendamento.REALIZADO, StatusAgendamento.FALTA):
            raise EstadoAgendamentoInvalidoError(
                "Agendamento realizado ou com falta não pode ser cancelado"
            )
        if self.status == StatusAgendamento.CANCELADO:
            raise EstadoAgendamentoInvalidoError("Agendamento já cancelado")
        self.status = StatusAgendamento.CANCELADO
        self.motivo_cancelamento = motivo
        self.updated_at = datetime.utcnow()

    def registrar_realizado(self) -> None:
        """Marca comparecimento."""
        from ..exceptions import EstadoAgendamentoInvalidoError

        if self.status not in (
            StatusAgendamento.AGENDADO,
            StatusAgendamento.CONFIRMADO,
        ):
            raise EstadoAgendamentoInvalidoError(
                "Somente agendamento agendado/confirmado pode ser realizado"
            )
        self.status = StatusAgendamento.REALIZADO
        self.updated_at = datetime.utcnow()

    def registrar_falta(self) -> None:
        """Marca falta do cidadão."""
        from ..exceptions import EstadoAgendamentoInvalidoError

        if self.status not in (
            StatusAgendamento.AGENDADO,
            StatusAgendamento.CONFIRMADO,
        ):
            raise EstadoAgendamentoInvalidoError(
                "Somente agendamento agendado/confirmado pode virar falta"
            )
        self.status = StatusAgendamento.FALTA
        self.updated_at = datetime.utcnow()


__all__ = [
    "TipoAtendimento",
    "StatusAgendamento",
    "Atendimento",
    "Agendamento",
]
