"""Testes de PCASP, lançamentos e conciliação (DOM-CON)."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from src.modules.sigmun_con.application.interfaces import (
    RepositorioConciliacao,
    RepositorioContaContabil,
    RepositorioLancamento,
)
from src.modules.sigmun_con.application.use_cases_contabil import (
    ConciliarContaUseCase,
    ConciliarInput,
    CriarContaInput,
    CriarContaUseCase,
    LancarContabilUseCase,
    LancarInput,
    PartidaInput,
)
from src.modules.sigmun_con.domain.entities.conta import ContaContabil
from src.modules.sigmun_con.domain.entities.lancamento import StatusLancamento
from src.modules.sigmun_con.domain.exceptions import LancamentoDesequilibradoError


def _conta(codigo: str) -> ContaContabil:
    return ContaContabil(id=f"id-{codigo}", codigo=codigo, nome=f"Conta {codigo}")


class TestContabil:
    """PCASP, partidas dobradas e conciliação."""

    def test_lancamento_balanceado(self) -> None:
        """Lançamento débito == crédito é lançado."""
        contas = MagicMock(spec=RepositorioContaContabil)
        contas.get_by_id = MagicMock(side_effect=lambda cid: _conta(cid))
        lancs = MagicMock(spec=RepositorioLancamento)
        lancs.save = MagicMock(side_effect=lambda x: x)
        lanc = LancarContabilUseCase(lancs, contas).execute(
            LancarInput(exercicio=2026, historico="Empenho",
                        partidas=[PartidaInput(conta_id="a", codigo_conta="a",
                                               tipo="debito", valor=100.0),
                                  PartidaInput(conta_id="b", codigo_conta="b",
                                               tipo="credito", valor=100.0)]))
        assert lanc.status == StatusLancamento.LANCADO

    def test_desequilibrado(self) -> None:
        """Débito ≠ crédito gera erro."""
        contas = MagicMock(spec=RepositorioContaContabil)
        contas.get_by_id = MagicMock(side_effect=lambda cid: _conta(cid))
        lancs = MagicMock(spec=RepositorioLancamento)
        with pytest.raises(LancamentoDesequilibradoError):
            LancarContabilUseCase(lancs, contas).execute(
                LancarInput(exercicio=2026, historico="X",
                            partidas=[PartidaInput(conta_id="a", codigo_conta="a",
                                                   tipo="debito", valor=100.0),
                                      PartidaInput(conta_id="b", codigo_conta="b",
                                                   tipo="credito", valor=50.0)]))

    def test_conta_e_conciliacao(self) -> None:
        """Cria conta e concilia sem divergência."""
        contas = MagicMock(spec=RepositorioContaContabil)
        contas.get_by_codigo = MagicMock(return_value=None)
        contas.save = MagicMock(return_value=_conta("1.1.1"))
        conta = CriarContaUseCase(contas).execute(
            CriarContaInput(codigo="1.1.1", nome="Caixa"))
        assert conta.codigo == "1.1.1"
        concs = MagicMock(spec=RepositorioConciliacao)
        concs.save = MagicMock(side_effect=lambda c: c)
        conc = ConciliarContaUseCase(concs).execute(
            ConciliarInput(conta_id="x", codigo_conta="1.1.1", ano=2026, mes=1,
                           saldo_contabil=100.0, saldo_extrato=100.0))
        assert conc.status.value == "conciliada"
