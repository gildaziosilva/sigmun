"""Entidade Lançamento — crédito tributário municipal (DOM-TRI).

Cobre IPTU, ISSQN, ITBI e taxas municipais.

RN-TRI-020: o lançamento constitui o crédito tributário com base de cálculo
    declarada/apurável e alíquota aplicável.
RN-TRI-021: o valor total do lançamento é tributo + juros + multa.
RN-TRI-022: um lançamento pago ou já inscrito em dívida ativa não pode ser
    pago duplamente sem comando específico.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from uuid import uuid4


class TipoTributo(Enum):
    """Natureza do tributo municipal."""

    IPTU = "iptu"
    ISSQN = "issqn"
    ITBI = "itbi"
    TAXA = "taxa"


class StatusLancamento(Enum):
    """Situação do crédito tributário."""

    LANCADO = "lancado"
    PAGO = "pago"
    INSCRITO_EM_DIVIDA_ATIVA = "inscrito_em_divida_ativa"
    CANCELADO = "cancelado"


@dataclass
class Lancamento:
    """Crédito tributário constituído pelo lançamento."""

    id: str = field(default_factory=lambda: str(uuid4()))
    contribuinte_id: str = ""
    imovel_id: str = ""
    tipo_tributo: TipoTributo = field(default=TipoTributo.TAXA)
    exercicio: int = 0
    numero_lancamento: str = ""
    descricao: str = ""
    base_calculo: float = 0.0
    aliquota: float = 0.0
    valor_tributo: float = 0.0
    juros: float = 0.0
    multa: float = 0.0
    valor_total: float = 0.0
    data_vencimento: date | None = None
    status: StatusLancamento = field(default=StatusLancamento.LANCADO)
    data_pagamento: date | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    def validar(self) -> None:
        """Valida regras estruturais do lançamento."""
        from ..exceptions import RegraNegocioError

        if not self.contribuinte_id:
            raise RegraNegocioError("Lançamento exige contribuinte (RN-TRI-020)")
        if not self.numero_lancamento:
            raise RegraNegocioError("Número do lançamento é obrigatório (RN-TRI-020)")
        if self.exercicio <= 0:
            raise RegraNegocioError("Exercício do lançamento é obrigatório")
        if self.valor_tributo < 0:
            raise RegraNegocioError("Valor do tributo não pode ser negativo")

    def recalcular_total(self) -> None:
        """Recompõe o valor total a partir de tributo, juros e multa."""
        self.valor_total = round(self.valor_tributo + self.juros + self.multa, 2)
        self.updated_at = datetime.utcnow()

    def registrar_pagamento(self, data_pagamento: date | None = None) -> None:
        """Registra a quitação total do crédito (RN-TRI-022)."""
        from ..exceptions import EstadoLancamentoInvalidoError

        if self.status not in (
            StatusLancamento.LANCADO,
            StatusLancamento.INSCRITO_EM_DIVIDA_ATIVA,
        ):
            raise EstadoLancamentoInvalidoError(
                f"Lançamento '{self.numero_lancamento}' não pode ser pago no "
                f"status '{self.status.value}' (RN-TRI-022)"
            )
        self.status = StatusLancamento.PAGO
        self.data_pagamento = data_pagamento or date.today()
        self.updated_at = datetime.utcnow()

    def inscrever_em_divida_ativa(self) -> None:
        """Inscreve o crédito vencido em dívida ativa."""
        from ..exceptions import EstadoLancamentoInvalidoError

        if self.status != StatusLancamento.LANCADO:
            raise EstadoLancamentoInvalidoError(
                f"Lançamento '{self.numero_lancamento}' não pode ser inscrito em "
                f"dívida ativa no status '{self.status.value}'"
            )
        self.status = StatusLancamento.INSCRITO_EM_DIVIDA_ATIVA
        self.updated_at = datetime.utcnow()

    def cancelar(self) -> None:
        """Cancela o lançamento (antes de pago)."""
        from ..exceptions import EstadoLancamentoInvalidoError

        if self.status == StatusLancamento.PAGO:
            raise EstadoLancamentoInvalidoError(
                "Lançamento pago não pode ser cancelado"
            )
        self.status = StatusLancamento.CANCELADO
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca o lançamento como excluído (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()


__all__ = ["TipoTributo", "StatusLancamento", "Lancamento"]