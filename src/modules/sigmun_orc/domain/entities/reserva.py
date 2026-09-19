"""Entidade ReservaSaldo — pré-empenho / bloqueio de saldo (DOM-ORC).

RN-ORC-040: reserva consome saldo disponível da dotação no ato da criação.
RN-ORC-041: reserva ATIVA pode ser cancelada (devolve saldo) ou convertida
    em empenho (transfere para valor_empenhado).
RN-ORC-042: reserva CANCELADA/CONVERTIDA/EXPIRADA é terminal.

Máquina de estados:
    ATIVA → CONVERTIDA | CANCELADA | EXPIRADA
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4

TRANSICOES_RESERVA: dict[str, set[str]] = {
    "ativa": {"convertida", "cancelada", "expirada"},
    "convertida": set(),
    "cancelada": set(),
    "expirada": set(),
}

ESTADOS_TERMINAIS_RESERVA: set[str] = {"convertida", "cancelada", "expirada"}


class StatusReserva(Enum):
    """Estado da reserva de saldo."""

    ATIVA = "ativa"
    CONVERTIDA = "convertida"
    CANCELADA = "cancelada"
    EXPIRADA = "expirada"


@dataclass
class ReservaSaldo:
    """Bloqueio de saldo de uma dotação para futura despesa."""

    id: str = field(default_factory=lambda: str(uuid4()))
    dotacao_id: str = ""
    numero: str = ""
    valor: float = 0.0
    finalidade: str = ""
    status: StatusReserva = field(default=StatusReserva.ATIVA)
    data_reserva: datetime = field(default_factory=datetime.utcnow)
    data_conversao: datetime | None = None
    data_cancelamento: datetime | None = None
    motivo_cancelamento: str = ""
    empenho_id: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    updated_by: str = ""
    is_deleted: bool = False

    @property
    def is_terminal(self) -> bool:
        """Indica se a reserva está em estado terminal."""
        return self.status.value in ESTADOS_TERMINAIS_RESERVA

    @property
    def is_active(self) -> bool:
        """Indica se a reserva está ativa e não excluída."""
        return self.status == StatusReserva.ATIVA and not self.is_deleted

    def _transicao_valida(self, novo: StatusReserva) -> None:
        from ...domain.exceptions import RegraNegocioError

        atual = self.status.value
        if novo.value not in TRANSICOES_RESERVA.get(atual, set()):
            raise RegraNegocioError(f"Transição inválida de reserva: {atual} → {novo.value}")

    def converter(self, empenho_id: str = "") -> None:
        """Converte a reserva em empenho (ATIVA → CONVERTIDA)."""
        self._transicao_valida(StatusReserva.CONVERTIDA)
        self.status = StatusReserva.CONVERTIDA
        self.empenho_id = empenho_id
        self.data_conversao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def cancelar(self, motivo: str = "") -> None:
        """Cancela a reserva ativa (devolve saldo à dotação)."""
        self._transicao_valida(StatusReserva.CANCELADA)
        self.status = StatusReserva.CANCELADA
        self.motivo_cancelamento = motivo
        self.data_cancelamento = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def expirar(self) -> None:
        """Expira a reserva ativa por decurso de prazo."""
        self._transicao_valida(StatusReserva.EXPIRADA)
        self.status = StatusReserva.EXPIRADA
        self.updated_at = datetime.utcnow()


__all__ = ["StatusReserva", "ReservaSaldo", "TRANSICOES_RESERVA", "ESTADOS_TERMINAIS_RESERVA"]
