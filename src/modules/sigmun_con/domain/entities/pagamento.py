"""Entidade Pagamento — estágio do pagamento (DOM-CON).

RN-CON-030: pagamento exige liquidação CONFIRMADA com saldo a pagar.
RN-CON-031: valor pago nunca excede saldo a pagar.
RN-CON-032: pagamento EFETIVADO/CANCELADO é terminal.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class StatusPagamento(Enum):
    """Estado do pagamento."""

    PROGRAMADO = "programado"
    EFETIVADO = "efetivado"
    CANCELADO = "cancelado"


@dataclass
class Pagamento:
    """Pagamento de liquidação (ordem bancária)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    liquidacao_id: str = ""
    empenho_id: str = ""
    numero_ob: str = ""
    valor: float = 0.0
    conta_bancaria: str = ""
    descricao: str = ""
    status: StatusPagamento = field(default=StatusPagamento.PROGRAMADO)
    data_programacao: datetime = field(default_factory=datetime.utcnow)
    data_efetivacao: datetime | None = None
    motivo_cancelamento: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    updated_by: str = ""
    is_deleted: bool = False

    def efetivar(self) -> None:
        """Efetiva o pagamento programado."""
        from ...domain.exceptions import RegraNegocioError

        if self.status != StatusPagamento.PROGRAMADO:
            raise RegraNegocioError("Apenas programado pode ser efetivado")
        self.status = StatusPagamento.EFETIVADO
        self.data_efetivacao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def cancelar(self, motivo: str = "") -> None:
        """Cancela o pagamento programado."""
        from ...domain.exceptions import RegraNegocioError

        if self.status != StatusPagamento.PROGRAMADO:
            raise RegraNegocioError("Apenas programado pode ser cancelado")
        self.status = StatusPagamento.CANCELADO
        self.motivo_cancelamento = motivo
        self.updated_at = datetime.utcnow()


__all__ = ["StatusPagamento", "Pagamento"]
