"""Testes de empenho/liquidação/pagamento (DOM-CON)."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from src.modules.sigmun_con.application.interfaces import (
    RepositorioEmpenho,
    RepositorioLiquidacao,
    RepositorioPagamento,
)
from src.modules.sigmun_con.application.use_cases_execucao import (
    AnularEmpenhoUseCase,
    EmitirEmpenhoInput,
    EmitirEmpenhoUseCase,
    LiquidarEmpenhoUseCase,
    PagarLiquidacaoUseCase,
)
from src.modules.sigmun_con.domain.entities.empenho import Empenho, StatusEmpenho
from src.modules.sigmun_con.domain.entities.liquidacao import (
    Liquidacao,
    StatusLiquidacao,
)
from src.modules.sigmun_orc.domain.entities.dotacao import Dotacao
from src.modules.sigmun_orc.domain.exceptions import DotacaoSemSaldoError


def _dotacao() -> Dotacao:
    return Dotacao(id="dot-1", loa_id="loa-1", exercicio=2026,
                   codigo="01.01.01", valor_inicial=1000.0)


def _empenho() -> Empenho:
    return Empenho(id="emp-1", exercicio=2026, numero="2026NE0001",
                   dotacao_id="dot-1", valor_empenhado=500.0)


class TestExecucao:
    """Ciclo empenho → liquidação → pagamento."""

    def test_ciclo(self) -> None:
        """Emite, liquida e paga integralmente."""
        dot = _dotacao()
        emps = MagicMock(spec=RepositorioEmpenho)
        emps.get_by_numero_exercicio = MagicMock(return_value=None)
        emp = _empenho()
        emps.save = MagicMock(return_value=emp)
        EmitirEmpenhoUseCase(emps).execute(
            EmitirEmpenhoInput(exercicio=2026, numero="2026NE0001", valor=500.0), dot)
        assert dot.valor_empenhado == 500.0
        emps.get_by_id = MagicMock(return_value=emp)
        liqs = MagicMock(spec=RepositorioLiquidacao)
        liq = Liquidacao(id="liq-1", empenho_id="emp-1", valor=500.0,
                         status=StatusLiquidacao.CONFIRMADA)
        liqs.save = MagicMock(return_value=liq)
        LiquidarEmpenhoUseCase(emps, liqs).execute("emp-1", 500.0)
        assert emp.status == StatusEmpenho.LIQUIDADO
        liqs.get_by_id = MagicMock(return_value=liq)
        pags = MagicMock(spec=RepositorioPagamento)
        pags.save = MagicMock(return_value=MagicMock())
        PagarLiquidacaoUseCase(emps, liqs, pags).execute("liq-1", 500.0)
        assert emp.status == StatusEmpenho.PAGO

    def test_empenho_sem_saldo(self) -> None:
        """Emissão acima do saldo gera erro."""
        dot = _dotacao()
        emps = MagicMock(spec=RepositorioEmpenho)
        emps.get_by_numero_exercicio = MagicMock(return_value=None)
        with pytest.raises(DotacaoSemSaldoError):
            EmitirEmpenhoUseCase(emps).execute(
                EmitirEmpenhoInput(exercicio=2026, numero="X", valor=5000.0), dot)

    def test_anular_devolve_saldo(self) -> None:
        """Anulação devolve saldo à dotação."""
        dot = _dotacao()
        dot.empenhar_direto(500.0)
        emp = _empenho()
        emps = MagicMock(spec=RepositorioEmpenho)
        emps.get_by_id = MagicMock(return_value=emp)
        emps.save = MagicMock(return_value=emp)
        AnularEmpenhoUseCase(emps).execute("emp-1", 500.0, dot)
        assert dot.valor_empenhado == 0.0
