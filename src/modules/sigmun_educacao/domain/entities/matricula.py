"""Entidade Matrícula — matrícula escolar na rede municipal (DOM-EDU).

RN-EDU-010: o aluno possui no máximo UMA matrícula ``ativa`` por vez;
a matrícula nasce ``ativa`` e só transita para ``transferida``,
``cancelada`` ou ``concluida`` (estados finais).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from uuid import uuid4


class StatusMatricula(Enum):
    """Situação da matrícula escolar."""

    ATIVA = "ativa"
    TRANSFERIDA = "transferida"
    CANCELADA = "cancelada"
    CONCLUIDA = "concluida"


@dataclass
class Matricula:
    """Vínculo do aluno com uma escola/série no ano letivo vigente."""

    id: str = field(default_factory=lambda: str(uuid4()))
    aluno_id: str = ""
    escola: str = ""
    serie: str = ""
    turno: str = "manha"
    ano_letivo: int = 0
    data_matricula: date | None = None
    status: StatusMatricula = field(default=StatusMatricula.ATIVA)
    escola_destino: str = ""
    motivo: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""

    @property
    def esta_ativa(self) -> bool:
        """Indica se a matrícula está vigente."""
        return self.status == StatusMatricula.ATIVA

    def validar(self) -> None:
        """Valida regras estruturais da matrícula."""
        from ..exceptions import RegraNegocioError

        if not self.aluno_id:
            raise RegraNegocioError("Matrícula exige aluno vinculado (RN-EDU-010)")
        if not self.escola or not self.serie:
            raise RegraNegocioError(
                "Escola e série são obrigatórias na matrícula (RN-EDU-010)"
            )
        if self.ano_letivo < 1:
            raise RegraNegocioError("Ano letivo inválido (RN-EDU-010)")

    def transferir(self, escola_destino: str, motivo: str = "") -> None:
        """Transfere a matrícula para outra escola (RN-EDU-010)."""
        from ..exceptions import EstadoMatriculaInvalidoError, RegraNegocioError

        if self.status != StatusMatricula.ATIVA:
            raise EstadoMatriculaInvalidoError(
                f"Só é possível transferir matrícula ativa (atual: {self.status.value})"
            )
        if not escola_destino:
            raise RegraNegocioError("Transferência exige escola destino (RN-EDU-010)")
        self.status = StatusMatricula.TRANSFERIDA
        self.escola_destino = escola_destino
        self.motivo = motivo
        self.updated_at = datetime.utcnow()

    def cancelar(self, motivo: str = "") -> None:
        """Cancela a matrícula vigente (RN-EDU-010)."""
        from ..exceptions import EstadoMatriculaInvalidoError

        if self.status != StatusMatricula.ATIVA:
            raise EstadoMatriculaInvalidoError(
                f"Só é possível cancelar matrícula ativa (atual: {self.status.value})"
            )
        self.status = StatusMatricula.CANCELADA
        self.motivo = motivo
        self.updated_at = datetime.utcnow()

    def concluir(self) -> None:
        """Conclui a matrícula (fim do ano letivo) (RN-EDU-010)."""
        from ..exceptions import EstadoMatriculaInvalidoError

        if self.status != StatusMatricula.ATIVA:
            raise EstadoMatriculaInvalidoError(
                f"Só é possível concluir matrícula ativa (atual: {self.status.value})"
            )
        self.status = StatusMatricula.CONCLUIDA
        self.updated_at = datetime.utcnow()


__all__ = ["StatusMatricula", "Matricula"]
