"""Entidade InscricaoDividaAtiva — dívida tributária ativa (DOM-TRI).

RN-TRI-030: a inscrição em dívida ativa formaliza créditos vencidos e não
    pagos, com número de inscrição único no exercício.
RN-TRI-031: valores atualizados (juros e multa) podem ser recompostos até a
    baixa da inscrição.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from uuid import uuid4


class StatusDividaAtiva(Enum):
    """Situação da inscrição."""

    ATIVA = "ativa"
    BAIXADA = "baixada"
    CANCELADA = "cancelada"


@dataclass
class InscricaoDividaAtiva:
    """Inscrição formal do crédito tributário em dívida ativa."""

    id: str = field(default_factory=lambda: str(uuid4()))
    lancamento_id: str = ""
    numero_inscricao: str = ""
    data_inscricao: date | None = None
    valor_original: float = 0.0
    valor_atualizado: float = 0.0
    status: StatusDividaAtiva = field(default=StatusDividaAtiva.ATIVA)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    def validar(self) -> None:
        """Valida regras estruturais da inscrição."""
        from ..exceptions import RegraNegocioError

        if not self.lancamento_id:
            raise RegraNegocioError("Inscrição exige lançamento de origem (RN-TRI-030)")
        if not self.numero_inscricao:
            raise RegraNegocioError("Número de inscrição é obrigatório (RN-TRI-030)")

    def atualizar_valor(self, valor_atualizado: float) -> None:
        """Atualiza o valor monetário da inscrição (RN-TRI-031)."""
        from ..exceptions import EstadoLancamentoInvalidoError

        if self.status != StatusDividaAtiva.ATIVA:
            raise EstadoLancamentoInvalidoError(
                "Apenas inscrições ativas podem ter valor atualizado"
            )
        self.valor_atualizado = round(valor_atualizado, 2)
        self.updated_at = datetime.utcnow()

    def baixar(self) -> None:
        """Baixa a inscrição (quitação total)."""
        from ..exceptions import EstadoLancamentoInvalidoError

        if self.status != StatusDividaAtiva.ATIVA:
            raise EstadoLancamentoInvalidoError(
                f"Inscrição '{self.numero_inscricao}' não está ativa para baixa"
            )
        self.status = StatusDividaAtiva.BAIXADA
        self.updated_at = datetime.utcnow()

    def cancelar(self) -> None:
        """Cancela a inscrição."""
        from ..exceptions import EstadoLancamentoInvalidoError

        if self.status == StatusDividaAtiva.BAIXADA:
            raise EstadoLancamentoInvalidoError(
                "Inscrição baixada não pode ser cancelada"
            )
        self.status = StatusDividaAtiva.CANCELADA
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca a inscrição como excluída (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()


__all__ = ["StatusDividaAtiva", "InscricaoDividaAtiva"]