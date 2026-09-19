"""Entidade Empenho — estágio da despesa (DOM-CON).

RN-CON-001: número do empenho é único por exercício.
RN-CON-002: empenho exige saldo na dotação (validado no use case).
RN-CON-003: liquidado acumulado nunca excede empenhado líquido.
RN-CON-004: empenho PAGO/ANULADO/CANCELADO é terminal.

Máquina: EMITIDO → LIQUIDADO → PAGO (+ ANULADO/CANCELADO)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4

TRANSICOES_EMPENHO: dict[str, set[str]] = {
    "emitido": {"liquidado", "anulado", "cancelado"},
    "liquidado": {"pago", "emitido", "cancelado"},
    "pago": set(),
    "anulado": set(),
    "cancelado": set(),
}

ESTADOS_TERMINAIS_EMPENHO: set[str] = {"pago", "anulado", "cancelado"}


class StatusEmpenho(Enum):
    """Estado do empenho."""

    EMITIDO = "emitido"
    LIQUIDADO = "liquidado"
    PAGO = "pago"
    ANULADO = "anulado"
    CANCELADO = "cancelado"


class TipoEmpenho(Enum):
    """Tipo de empenho (Lei 4.320/64)."""

    ORDINARIO = "ordinario"
    GLOBAL = "global"
    ESTIMATIVO = "estimativo"


@dataclass
class Empenho:
    """Empenho de despesa vinculado a dotação."""

    id: str = field(default_factory=lambda: str(uuid4()))
    exercicio: int = 0
    numero: str = ""
    dotacao_id: str = ""
    reserva_id: str = ""
    favorecido_id: str = ""
    favorecido_nome: str = ""
    tipo: TipoEmpenho = field(default=TipoEmpenho.ORDINARIO)
    descricao: str = ""
    valor_empenhado: float = 0.0
    valor_anulado: float = 0.0
    valor_liquidado: float = 0.0
    valor_pago: float = 0.0
    status: StatusEmpenho = field(default=StatusEmpenho.EMITIDO)
    data_emissao: datetime = field(default_factory=datetime.utcnow)
    data_anulacao: datetime | None = None
    motivo_anulacao: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    updated_by: str = ""
    is_deleted: bool = False

    @property
    def valor_liquido(self) -> float:
        """Valor líquido = empenhado - anulado."""
        return self.valor_empenhado - self.valor_anulado

    @property
    def saldo_a_liquidar(self) -> float:
        """Saldo ainda não liquidado."""
        return self.valor_liquido - self.valor_liquidado

    @property
    def saldo_a_pagar(self) -> float:
        """Saldo liquidado ainda não pago."""
        return self.valor_liquidado - self.valor_pago

    @property
    def is_terminal(self) -> bool:
        """Indica se o empenho está em estado terminal."""
        return self.status.value in ESTADOS_TERMINAIS_EMPENHO

    @property
    def is_active(self) -> bool:
        """Indica se o empenho não foi excluído."""
        return not self.is_deleted

    def _transicao(self, novo: StatusEmpenho) -> None:
        from ...domain.exceptions import RegraNegocioError

        atual = self.status.value
        if novo.value not in TRANSICOES_EMPENHO.get(atual, set()):
            raise RegraNegocioError(f"Transição inválida: {atual} → {novo.value}")

    def liquidar(self, valor: float) -> None:
        """Registra liquidação parcial/total (RN-CON-003)."""
        from ...domain.exceptions import RegraNegocioError

        if valor <= 0:
            raise RegraNegocioError("Liquidação deve ser maior que zero")
        if self.status not in (StatusEmpenho.EMITIDO, StatusEmpenho.LIQUIDADO):
            raise RegraNegocioError(f"Não pode liquidar ({self.status.value})")
        if self.saldo_a_liquidar < valor:
            raise RegraNegocioError("Excede saldo a liquidar (RN-CON-003)")
        self.valor_liquidado += valor
        if self.status == StatusEmpenho.EMITIDO:
            self._transicao(StatusEmpenho.LIQUIDADO)
            self.status = StatusEmpenho.LIQUIDADO
        self.updated_at = datetime.utcnow()

    def estornar_liquidacao(self, valor: float) -> None:
        """Estorna liquidação (volta a EMITIDO quando zera)."""
        from ...domain.exceptions import RegraNegocioError

        if self.status != StatusEmpenho.LIQUIDADO:
            raise RegraNegocioError("Apenas liquidado sofre estorno")
        if valor <= 0 or self.valor_liquidado < valor:
            raise RegraNegocioError("Estorno inválido")
        if self.valor_pago > self.valor_liquidado - valor:
            raise RegraNegocioError("Estorno comprometeria valor pago")
        self.valor_liquidado -= valor
        if self.valor_liquidado == 0:
            self._transicao(StatusEmpenho.EMITIDO)
            self.status = StatusEmpenho.EMITIDO
        self.updated_at = datetime.utcnow()

    def pagar(self, valor: float) -> None:
        """Registra pagamento parcial/total."""
        from ...domain.exceptions import RegraNegocioError

        if self.status != StatusEmpenho.LIQUIDADO:
            raise RegraNegocioError("Pagamento exige liquidado")
        if valor <= 0 or self.saldo_a_pagar < valor:
            raise RegraNegocioError("Pagamento excede saldo a pagar")
        self.valor_pago += valor
        if self.valor_pago == self.valor_liquidado and self.saldo_a_liquidar == 0:
            self._transicao(StatusEmpenho.PAGO)
            self.status = StatusEmpenho.PAGO
        self.updated_at = datetime.utcnow()

    def anular(self, valor: float, motivo: str = "") -> None:
        """Anula parcial/total do empenho."""
        from ...domain.exceptions import RegraNegocioError

        if self.status not in (StatusEmpenho.EMITIDO, StatusEmpenho.LIQUIDADO):
            raise RegraNegocioError("Não pode anular neste estado")
        if valor <= 0 or self.saldo_a_liquidar < valor:
            raise RegraNegocioError("Anulação excede saldo a liquidar")
        self.valor_anulado += valor
        self.motivo_anulacao = motivo
        if self.valor_liquido == 0 and self.valor_liquidado == 0:
            self._transicao(StatusEmpenho.ANULADO)
            self.status = StatusEmpenho.ANULADO
        self.data_anulacao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def cancelar(self, motivo: str = "") -> None:
        """Cancela o empenho ainda não pago."""
        from ...domain.exceptions import RegraNegocioError

        if self.status == StatusEmpenho.PAGO:
            raise RegraNegocioError("Empenho pago não pode ser cancelado")
        self._transicao(StatusEmpenho.CANCELADO)
        self.status = StatusEmpenho.CANCELADO
        self.motivo_anulacao = motivo
        self.updated_at = datetime.utcnow()


__all__ = ["StatusEmpenho", "TipoEmpenho", "Empenho", "TRANSICOES_EMPENHO",
           "ESTADOS_TERMINAIS_EMPENHO"]

