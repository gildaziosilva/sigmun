"""Entidades de lançamentos e conciliação (DOM-CON)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class TipoPartida(Enum):
    """Natureza da partida dobrada."""

    DEBITO = "debito"
    CREDITO = "credito"


class StatusLancamento(Enum):
    """Estado do lançamento contábil."""

    RASCUNHO = "rascunho"
    LANCADO = "lancado"
    ESTORNADO = "estornado"


class StatusConciliacao(Enum):
    """Estado da conciliação contábil."""

    ABERTA = "aberta"
    CONCILIADA = "conciliada"
    DIVERGENTE = "divergente"


@dataclass
class Partida:
    """Partida dobrada de um lançamento."""

    conta_id: str = ""
    codigo_conta: str = ""
    tipo: TipoPartida = field(default=TipoPartida.DEBITO)
    valor: float = 0.0
    historico: str = ""


@dataclass
class LancamentoContabil:
    """Lançamento contábil por partidas dobradas."""

    id: str = field(default_factory=lambda: str(uuid4()))
    exercicio: int = 0
    numero: str = ""
    data_lancamento: datetime = field(default_factory=datetime.utcnow)
    historico: str = ""
    origem: str = ""
    origem_id: str = ""
    partidas: list = field(default_factory=list)
    status: StatusLancamento = field(default=StatusLancamento.RASCUNHO)
    created_at: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""
    is_deleted: bool = False

    @property
    def total_debito(self) -> float:
        """Total a débito."""
        return sum(p.valor for p in self.partidas if p.tipo == TipoPartida.DEBITO)

    @property
    def total_credito(self) -> float:
        """Total a crédito."""
        return sum(p.valor for p in self.partidas if p.tipo == TipoPartida.CREDITO)

    @property
    def balanceado(self) -> bool:
        """Indica se débito == crédito (RN-CON-040)."""
        return abs(self.total_debito - self.total_credito) < 0.005 and self.total_debito > 0

    def lancar(self) -> None:
        """Lança o rascunho (exige balanceamento)."""
        from ...domain.exceptions import LancamentoDesequilibradoError, RegraNegocioError

        if self.status != StatusLancamento.RASCUNHO:
            raise RegraNegocioError("Apenas rascunho pode ser lançado")
        if not self.partidas:
            raise RegraNegocioError("Lançamento sem partidas")
        if not self.balanceado:
            raise LancamentoDesequilibradoError("Débito diferente de crédito")
        self.status = StatusLancamento.LANCADO

    def estornar(self) -> None:
        """Estorna o lançamento lançado."""
        from ...domain.exceptions import RegraNegocioError

        if self.status != StatusLancamento.LANCADO:
            raise RegraNegocioError("Apenas lançado pode ser estornado")
        self.status = StatusLancamento.ESTORNADO


@dataclass
class ConciliacaoContabil:
    """Conciliação entre saldo contábil e extrato."""

    id: str = field(default_factory=lambda: str(uuid4()))
    conta_id: str = ""
    codigo_conta: str = ""
    competencia_ano: int = 0
    competencia_mes: int = 0
    saldo_contabil: float = 0.0
    saldo_extrato: float = 0.0
    diferenca: float = 0.0
    status: StatusConciliacao = field(default=StatusConciliacao.ABERTA)
    justificativa: str = ""
    data_conciliacao: datetime | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""
    is_deleted: bool = False

    def conciliar(self) -> None:
        """Marca como conciliada (diferença zerada)."""
        from ...domain.exceptions import RegraNegocioError

        self.diferenca = round(self.saldo_contabil - self.saldo_extrato, 2)
        if abs(self.diferenca) > 0.005:
            raise RegraNegocioError("Há divergência; use divergente")
        self.status = StatusConciliacao.CONCILIADA
        self.data_conciliacao = datetime.utcnow()

    def marcar_divergente(self, justificativa: str) -> None:
        """Marca como divergente com justificativa."""
        self.diferenca = round(self.saldo_contabil - self.saldo_extrato, 2)
        self.status = StatusConciliacao.DIVERGENTE
        self.justificativa = justificativa
        self.data_conciliacao = datetime.utcnow()


__all__ = ["TipoPartida", "StatusLancamento", "Partida", "LancamentoContabil",
           "StatusConciliacao", "ConciliacaoContabil"]
