"""Entidade Ferias — período aquisitivo e gozo de férias (DOM-PES).

RN-PES-040: período de gozo deve estar dentro do período aquisitivo + 12 meses.
RN-PES-041: mínimo de 10 dias por parcela; máximo de 3 parcelas.
RN-PES-042: máquina de estados PLANEJADA → APROVADA → EM_GOZO → CONCLUIDA
    (+ CANCELADA a partir de PLANEJADA/APROVADA).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from uuid import uuid4

TRANSICOES_FERIAS: dict[str, set[str]] = {
    "planejada": {"aprovada", "cancelada"},
    "aprovada": {"em_gozo", "cancelada"},
    "em_gozo": {"concluida"},
    "concluida": set(),
    "cancelada": set(),
}

ESTADOS_TERMINAIS_FERIAS: set[str] = {"concluida", "cancelada"}


class StatusFerias(Enum):
    """Estado do período de férias."""

    PLANEJADA = "planejada"
    APROVADA = "aprovada"
    EM_GOZO = "em_gozo"
    CONCLUIDA = "concluida"
    CANCELADA = "cancelada"


@dataclass
class Ferias:
    """Período de férias de um servidor."""

    id: str = field(default_factory=lambda: str(uuid4()))
    servidor_id: str = ""
    periodo_aquisitivo_inicio: date | None = None
    periodo_aquisitivo_fim: date | None = None
    data_inicio_gozo: date | None = None
    data_fim_gozo: date | None = None
    dias: int = 30
    parcela: int = 1
    status: StatusFerias = field(default=StatusFerias.PLANEJADA)
    data_aprovacao: datetime | None = None
    data_cancelamento: datetime | None = None
    motivo_cancelamento: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        """Indica se o registro não foi excluído."""
        return not self.is_deleted

    @property
    def is_terminal(self) -> bool:
        """Indica se as férias estão em estado terminal."""
        return self.status.value in ESTADOS_TERMINAIS_FERIAS

    def _transicao_valida(self, novo: StatusFerias) -> None:
        from ...domain.exceptions import RegraNegocioError

        atual = self.status.value
        if novo.value not in TRANSICOES_FERIAS.get(atual, set()):
            raise RegraNegocioError(f"Transição inválida: {atual} → {novo.value}")

    def aprovar(self) -> None:
        """Aprova as férias planejadas."""
        self._transicao_valida(StatusFerias.APROVADA)
        self.status = StatusFerias.APROVADA
        self.data_aprovacao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def iniciar_gozo(self) -> None:
        """Inicia o gozo das férias aprovadas."""
        self._transicao_valida(StatusFerias.EM_GOZO)
        self.status = StatusFerias.EM_GOZO
        self.updated_at = datetime.utcnow()

    def concluir(self) -> None:
        """Conclui o gozo das férias."""
        self._transicao_valida(StatusFerias.CONCLUIDA)
        self.status = StatusFerias.CONCLUIDA
        self.updated_at = datetime.utcnow()

    def cancelar(self, motivo: str) -> None:
        """Cancela férias planejadas/aprovadas (requer motivo)."""
        from ...domain.exceptions import RegraNegocioError

        if not motivo:
            raise RegraNegocioError("Cancelamento de férias requer motivo")
        self._transicao_valida(StatusFerias.CANCELADA)
        self.status = StatusFerias.CANCELADA
        self.motivo_cancelamento = motivo
        self.data_cancelamento = datetime.utcnow()
        self.updated_at = datetime.utcnow()


__all__ = [
    "StatusFerias",
    "Ferias",
    "TRANSICOES_FERIAS",
    "ESTADOS_TERMINAIS_FERIAS",
]
