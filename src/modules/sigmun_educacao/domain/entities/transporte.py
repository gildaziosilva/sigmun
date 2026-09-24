"""Entidades RotaTransporte e PassagemTransporte — transporte escolar (DOM-EDU).

RN-EDU-030: passagem exige rota ``ativa``, matrícula ativa e vaga
disponível (passagens do dia < vagas da rota); rota transita
``ativa`` ⇄ ``inativa``.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from uuid import uuid4


class StatusRota(Enum):
    """Situação da rota de transporte escolar."""

    ATIVA = "ativa"
    INATIVA = "inativa"


@dataclass
class RotaTransporte:
    """Rota com veículo, motorista e vagas para o transporte escolar."""

    id: str = field(default_factory=lambda: str(uuid4()))
    identificacao: str = ""
    veiculo: str = ""
    motorista: str = ""
    vagas: int = 0
    turno: str = "manha"
    status: StatusRota = field(default=StatusRota.ATIVA)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""

    @property
    def esta_ativa(self) -> bool:
        """Indica se a rota aceita passagens."""
        return self.status == StatusRota.ATIVA

    def validar(self) -> None:
        """Valida regras estruturais da rota."""
        from ..exceptions import RegraNegocioError

        if not self.identificacao or not self.motorista:
            raise RegraNegocioError(
                "Identificação e motorista são obrigatórios na rota (RN-EDU-030)"
            )
        if self.vagas < 1:
            raise RegraNegocioError("Rota deve oferecer ao menos 1 vaga (RN-EDU-030)")

    def inativar(self) -> None:
        """Inativa a rota (para novas passagens)."""
        from ..exceptions import EstadoRotaInvalidoError

        if self.status != StatusRota.ATIVA:
            raise EstadoRotaInvalidoError("Rota já está inativa")
        self.status = StatusRota.INATIVA
        self.updated_at = datetime.utcnow()

    def ativar(self) -> None:
        """Reativa a rota."""
        from ..exceptions import EstadoRotaInvalidoError

        if self.status != StatusRota.ATIVA:
            self.status = StatusRota.ATIVA
            self.updated_at = datetime.utcnow()
            return
        raise EstadoRotaInvalidoError("Rota já está ativa")


@dataclass
class PassagemTransporte:
    """Registro diário de embarque do aluno em uma rota (ida ou volta)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    rota_id: str = ""
    matricula_id: str = ""
    data: date | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""

    def validar(self) -> None:
        """Valida regras estruturais da passagem."""
        from ..exceptions import RegraNegocioError

        if not self.rota_id or not self.matricula_id:
            raise RegraNegocioError(
                "Passagem exige rota e matrícula vinculadas (RN-EDU-030)"
            )


__all__ = ["StatusRota", "RotaTransporte", "PassagemTransporte"]
