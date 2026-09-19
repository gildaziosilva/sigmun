"""Entidade Liquidacao — estágio da liquidação (DOM-CON).

RN-CON-020: liquidação referencia empenho LIQUIDADO/EMITIDO com saldo.
RN-CON-021: valor da liquidação nunca excede saldo a liquidar.
RN-CON-022: liquidação CONFIRMADA/CANCELADA é terminal.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4

TRANSICOES_LIQUIDACAO: dict[str, set[str]] = {
    "registrada": {"confirmada", "cancelada"},
    "confirmada": set(),
    "cancelada": set(),
}

ESTADOS_TERMINAIS_LIQUIDACAO: set[str] = {"confirmada", "cancelada"}


class StatusLiquidacao(Enum):
    """Estado da liquidação."""

    REGISTRADA = "registrada"
    CONFIRMADA = "confirmada"
    CANCELADA = "cancelada"


@dataclass
class Liquidacao:
    """Liquidação de empenho (verificação do direito adquirido)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    empenho_id: str = ""
    numero: str = ""
    valor: float = 0.0
    documento_fiscal: str = ""
    descricao: str = ""
    status: StatusLiquidacao = field(default=StatusLiquidacao.REGISTRADA)
    data_liquidacao: datetime = field(default_factory=datetime.utcnow)
    data_cancelamento: datetime | None = None
    motivo_cancelamento: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    updated_by: str = ""
    is_deleted: bool = False

    def confirmar(self) -> None:
        """Confirma a liquidação registrada."""
        from ...domain.exceptions import RegraNegocioError

        if self.status != StatusLiquidacao.REGISTRADA:
            raise RegraNegocioError("Apenas registrada pode ser confirmada")
        self.status = StatusLiquidacao.CONFIRMADA
        self.updated_at = datetime.utcnow()

    def cancelar(self, motivo: str = "") -> None:
        """Cancela a liquidação registrada."""
        from ...domain.exceptions import RegraNegocioError

        if self.status != StatusLiquidacao.REGISTRADA:
            raise RegraNegocioError("Apenas registrada pode ser cancelada")
        self.status = StatusLiquidacao.CANCELADA
        self.motivo_cancelamento = motivo
        self.data_cancelamento = datetime.utcnow()
        self.updated_at = datetime.utcnow()


__all__ = ["StatusLiquidacao", "Liquidacao", "TRANSICOES_LIQUIDACAO",
           "ESTADOS_TERMINAIS_LIQUIDACAO"]
