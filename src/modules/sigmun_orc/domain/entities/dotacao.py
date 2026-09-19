"""Entidade Dotacao — dotação orçamentária da LOA (DOM-ORC).

RN-ORC-030: código da dotação é único por exercício.
RN-ORC-031: suplementação/anulação nunca deixa valor atualizado negativo.
RN-ORC-032: reserva/empenho exige saldo disponível.
RN-ORC-033: dotação encerrada é terminal (imutável).

Máquina de estados: ATIVA → ENCERRADA
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4

TRANSICOES_DOTACAO: dict[str, set[str]] = {
    "ativa": {"encerrada"},
    "encerrada": set(),
}

ESTADOS_TERMINAIS_DOTACAO: set[str] = {"encerrada"}


class StatusDotacao(Enum):
    """Estado da dotação orçamentária."""

    ATIVA = "ativa"
    ENCERRADA = "encerrada"


@dataclass
class Dotacao:
    """Dotação orçamentária vinculada a uma LOA."""

    id: str = field(default_factory=lambda: str(uuid4()))
    loa_id: str = ""
    exercicio: int = 0
    codigo: str = ""
    unidade_orcamentaria: str = ""
    funcao: str = ""
    subfuncao: str = ""
    programa: str = ""
    acao: str = ""
    natureza_despesa: str = ""
    fonte_recursos: str = ""
    valor_inicial: float = 0.0
    valor_suplementado: float = 0.0
    valor_anulado: float = 0.0
    valor_reservado: float = 0.0
    valor_empenhado: float = 0.0
    status: StatusDotacao = field(default=StatusDotacao.ATIVA)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    updated_by: str = ""
    is_deleted: bool = False

    @property
    def valor_atualizado(self) -> float:
        """Valor atualizado = inicial + suplementado - anulado."""
        return self.valor_inicial + self.valor_suplementado - self.valor_anulado

    @property
    def saldo_disponivel(self) -> float:
        """Saldo livre para reserva/empenho."""
        return self.valor_atualizado - self.valor_reservado - self.valor_empenhado

    @property
    def is_active(self) -> bool:
        """Indica se a dotação está ativa e não excluída."""
        return self.status == StatusDotacao.ATIVA and not self.is_deleted

    def _exige_ativa(self) -> None:
        from ...domain.exceptions import RegraNegocioError

        if self.status != StatusDotacao.ATIVA:
            raise RegraNegocioError(f"Dotação não ativa (atual: {self.status.value})")

    def suplementar(self, valor: float) -> None:
        """Suplementa a dotação (RN-ORC-031)."""
        from ...domain.exceptions import RegraNegocioError

        self._exige_ativa()
        if valor <= 0:
            raise RegraNegocioError("Suplementação deve ser maior que zero")
        self.valor_suplementado += valor
        self.updated_at = datetime.utcnow()

    def anular(self, valor: float) -> None:
        """Anula parcialmente a dotação."""
        from ...domain.exceptions import RegraNegocioError

        self._exige_ativa()
        if valor <= 0:
            raise RegraNegocioError("Anulação deve ser maior que zero")
        if self.valor_atualizado - valor < 0:
            raise RegraNegocioError("Anulação deixaria dotação negativa")
        if self.saldo_disponivel - valor < 0:
            raise RegraNegocioError("Anulação compromete saldo usado")
        self.valor_anulado += valor
        self.updated_at = datetime.utcnow()

    def reservar(self, valor: float) -> None:
        """Bloqueia saldo para futura despesa (RN-ORC-032)."""
        from ...domain.exceptions import DotacaoSemSaldoError, RegraNegocioError

        self._exige_ativa()
        if valor <= 0:
            raise RegraNegocioError("Reserva deve ser maior que zero")
        if self.saldo_disponivel < valor:
            raise DotacaoSemSaldoError(
                f"Saldo insuficiente: {self.saldo_disponivel:.2f} (RN-ORC-032)"
            )
        self.valor_reservado += valor
        self.updated_at = datetime.utcnow()

    def liberar_reserva(self, valor: float) -> None:
        """Libera saldo previamente reservado."""
        from ...domain.exceptions import RegraNegocioError

        self._exige_ativa()
        if valor <= 0:
            raise RegraNegocioError("Liberação deve ser maior que zero")
        if self.valor_reservado < valor:
            raise RegraNegocioError("Reserva insuficiente para liberação")
        self.valor_reservado -= valor
        self.updated_at = datetime.utcnow()

    def consumir_reserva_empenhar(self, valor: float) -> None:
        """Converte reserva em empenho (reserva → empenhado)."""
        from ...domain.exceptions import DotacaoSemSaldoError, RegraNegocioError

        self._exige_ativa()
        if valor <= 0:
            raise RegraNegocioError("Empenho deve ser maior que zero")
        if self.valor_reservado < valor:
            raise DotacaoSemSaldoError("Reserva insuficiente para empenho")
        self.valor_reservado -= valor
        self.valor_empenhado += valor
        self.updated_at = datetime.utcnow()

    def empenhar_direto(self, valor: float) -> None:
        """Empenha direto do saldo livre (sem reserva prévia)."""
        from ...domain.exceptions import DotacaoSemSaldoError, RegraNegocioError

        self._exige_ativa()
        if valor <= 0:
            raise RegraNegocioError("Empenho deve ser maior que zero")
        if self.saldo_disponivel < valor:
            raise DotacaoSemSaldoError("Saldo insuficiente (RN-ORC-032)")
        self.valor_empenhado += valor
        self.updated_at = datetime.utcnow()

    def anular_empenho(self, valor: float) -> None:
        """Anula empenho (devolve saldo)."""
        from ...domain.exceptions import RegraNegocioError

        self._exige_ativa()
        if valor <= 0:
            raise RegraNegocioError("Anulação de empenho deve ser > zero")
        if self.valor_empenhado < valor:
            raise RegraNegocioError("Empenho insuficiente para anulação")
        self.valor_empenhado -= valor
        self.updated_at = datetime.utcnow()

    def encerrar(self) -> None:
        """Encerra a dotação (terminal)."""
        from ...domain.exceptions import RegraNegocioError

        if "encerrada" not in TRANSICOES_DOTACAO.get(self.status.value, set()):
            raise RegraNegocioError(f"Transição inválida: {self.status.value}")
        self.status = StatusDotacao.ENCERRADA
        self.updated_at = datetime.utcnow()


__all__ = ["StatusDotacao", "Dotacao", "TRANSICOES_DOTACAO", "ESTADOS_TERMINAIS_DOTACAO"]
