"""Entidade FolhaPagamento — competência mensal da folha (DOM-PES).

RN-PES-030: competência (ano/mês) é única no município.
RN-PES-031: folha ABERTA pode receber lançamentos; FECHADA não.
RN-PES-032: fechamento exige ao menos um lançamento.
RN-PES-033: folha HOMOLOGADA ou PAGA é terminal (imutável).

Máquina de estados:
    ABERTA → FECHADA → HOMOLOGADA → PAGA (+ CANCELADA a partir de ABERTA)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4

TRANSICOES_FOLHA: dict[str, set[str]] = {
    "aberta": {"fechada", "cancelada"},
    "fechada": {"homologada", "aberta"},
    "homologada": {"paga"},
    "paga": set(),
    "cancelada": set(),
}

ESTADOS_TERMINAIS_FOLHA: set[str] = {"paga", "cancelada"}


class StatusFolha(Enum):
    """Estado da folha de pagamento na competência."""

    ABERTA = "aberta"
    FECHADA = "fechada"
    HOMOLOGADA = "homologada"
    PAGA = "paga"
    CANCELADA = "cancelada"


@dataclass
class FolhaPagamento:
    """Folha mensal consolidada (cabeçalho da competência)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    competencia_ano: int = 0
    competencia_mes: int = 0
    descricao: str = ""
    status: StatusFolha = field(default=StatusFolha.ABERTA)
    total_proventos: float = 0.0
    total_descontos: float = 0.0
    total_liquido: float = 0.0
    quantidade_servidores: int = 0
    data_fechamento: datetime | None = None
    data_homologacao: datetime | None = None
    data_pagamento: datetime | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    updated_by: str = ""
    is_deleted: bool = False

    @property
    def competencia(self) -> str:
        """Competência formatada como ``AAAA-MM``."""
        return f"{self.competencia_ano:04d}-{self.competencia_mes:02d}"

    @property
    def is_terminal(self) -> bool:
        """Indica se a folha está em estado terminal."""
        return self.status.value in ESTADOS_TERMINAIS_FOLHA

    @property
    def is_active(self) -> bool:
        """Indica se a folha não foi excluída."""
        return not self.is_deleted

    def _transicao_valida(self, novo: StatusFolha) -> None:
        from ...domain.exceptions import RegraNegocioError

        atual = self.status.value
        if novo.value not in TRANSICOES_FOLHA.get(atual, set()):
            raise RegraNegocioError(f"Transição inválida: {atual} → {novo.value}")

    def fechar(self) -> None:
        """Fecha a folha (ABERTA → FECHADA)."""
        from ...domain.exceptions import RegraNegocioError

        if self.quantidade_servidores <= 0:
            raise RegraNegocioError(
                "Fechamento exige ao menos um lançamento (RN-PES-032)"
            )
        self._transicao_valida(StatusFolha.FECHADA)
        self.status = StatusFolha.FECHADA
        self.data_fechamento = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def reabrir(self) -> None:
        """Reabre a folha (FECHADA → ABERTA)."""
        self._transicao_valida(StatusFolha.ABERTA)
        self.status = StatusFolha.ABERTA
        self.data_fechamento = None
        self.updated_at = datetime.utcnow()

    def homologar(self) -> None:
        """Homologa a folha (FECHADA → HOMOLOGADA)."""
        self._transicao_valida(StatusFolha.HOMOLOGADA)
        self.status = StatusFolha.HOMOLOGADA
        self.data_homologacao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def pagar(self) -> None:
        """Registra pagamento da folha (HOMOLOGADA → PAGA)."""
        self._transicao_valida(StatusFolha.PAGA)
        self.status = StatusFolha.PAGA
        self.data_pagamento = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def cancelar(self) -> None:
        """Cancela a folha ainda aberta."""
        self._transicao_valida(StatusFolha.CANCELADA)
        self.status = StatusFolha.CANCELADA
        self.updated_at = datetime.utcnow()

    def consolidar(self, proventos: float, descontos: float, qtd: int) -> None:
        """Consolida totais (permitido apenas com folha ABERTA)."""
        from ...domain.exceptions import RegraNegocioError

        if self.status != StatusFolha.ABERTA:
            raise RegraNegocioError(
                f"Apenas folhas abertas recebem lançamentos (atual: {self.status.value})"
            )
        self.total_proventos = proventos
        self.total_descontos = descontos
        self.total_liquido = proventos - descontos
        self.quantidade_servidores = qtd
        self.updated_at = datetime.utcnow()


__all__ = [
    "StatusFolha",
    "FolhaPagamento",
    "TRANSICOES_FOLHA",
    "ESTADOS_TERMINAIS_FOLHA",
]
