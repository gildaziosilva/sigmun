"""Testes de PPA/LDO/LOA/dotação/reserva (DOM-ORC)."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from src.modules.sigmun_orc.application.interfaces import (
    RepositorioDotacao,
    RepositorioLDO,
    RepositorioLOA,
    RepositorioPPA,
    RepositorioReserva,
)
from src.modules.sigmun_orc.application.use_cases_dotacao import (
    AnularDotacaoUseCase,
    CancelarReservaUseCase,
    CriarDotacaoInput,
    CriarDotacaoUseCase,
    ReservarSaldoInput,
    ReservarSaldoUseCase,
    SuplementarDotacaoUseCase,
)
from src.modules.sigmun_orc.application.use_cases_planejamento import (
    CriarLDOInput,
    CriarLDOUseCase,
    CriarLOAInput,
    CriarLOAUseCase,
    CriarPPAInput,
    CriarPPAUseCase,
    PublicarLOAUseCase,
    PublicarPPAUseCase,
    SancionarLDOUseCase,
)
from src.modules.sigmun_orc.domain.entities.dotacao import Dotacao
from src.modules.sigmun_orc.domain.entities.ldo import LDO, StatusLDO
from src.modules.sigmun_orc.domain.entities.loa import LOA, StatusLOA
from src.modules.sigmun_orc.domain.entities.ppa import PPA, StatusPPA
from src.modules.sigmun_orc.domain.entities.reserva import ReservaSaldo
from src.modules.sigmun_orc.domain.exceptions import (
    DotacaoSemSaldoError,
    RegraNegocioError,
)


def _ppa(status=StatusPPA.ELABORACAO) -> PPA:
    return PPA(id="ppa-1", ano_inicial=2026, ano_final=2029, status=status)


def _ldo(status=StatusLDO.ELABORACAO) -> LDO:
    return LDO(id="ldo-1", exercicio=2026, ppa_id="ppa-1", status=status)


def _loa(status=StatusLOA.ELABORACAO) -> LOA:
    return LOA(id="loa-1", exercicio=2026, ldo_id="ldo-1",
               valor_receita_prevista=1000.0, valor_despesa_fixada=900.0,
               status=status)


def _dotacao() -> Dotacao:
    return Dotacao(id="dot-1", loa_id="loa-1", exercicio=2026,
                   codigo="01.01.01", valor_inicial=1000.0)


class TestPlanejamento:
    """Ciclo PPA → LDO → LOA."""

    def test_ciclo(self) -> None:
        """Cria e publica PPA, aprova/sanciona LDO, aprova/publica LOA."""
        ppas = MagicMock(spec=RepositorioPPA)
        ppas.get_by_quadrienio = MagicMock(return_value=None)
        ppas.save = MagicMock(return_value=_ppa())
        ppa = CriarPPAUseCase(ppas).execute(CriarPPAInput(2026, 2029))
        assert ppa.quadrienio == "2026-2029"
        ppas.get_by_id = MagicMock(return_value=ppa)
        PublicarPPAUseCase(ppas).execute("ppa-1")
        assert ppa.status == StatusPPA.VIGENTE

        ldos = MagicMock(spec=RepositorioLDO)
        ldos.get_by_exercicio = MagicMock(return_value=None)
        ldos.save = MagicMock(return_value=_ldo())
        ldo = CriarLDOUseCase(ldos, ppas).execute(
            CriarLDOInput(exercicio=2026, ppa_id="ppa-1"))
        assert ldo.exercicio == 2026
        ldos.get_by_id = MagicMock(return_value=ldo)
        SancionarLDOUseCase(ldos).execute("ldo-1", sancionar=True)
        assert ldo.status == StatusLDO.SANCIONADA

        loas = MagicMock(spec=RepositorioLOA)
        loas.get_by_exercicio = MagicMock(return_value=None)
        loas.save = MagicMock(return_value=_loa())
        loa = CriarLOAUseCase(loas, ldos).execute(
            CriarLOAInput(exercicio=2026, ldo_id="ldo-1",
                          receita=1000.0, despesa=900.0))
        loas.get_by_id = MagicMock(return_value=loa)
        PublicarLOAUseCase(loas).execute("loa-1", publicar=True)
        assert loa.status == StatusLOA.PUBLICADA

    def test_ppa_quadrienio_invalido(self) -> None:
        """Quadriênio diferente de 4 anos gera erro."""
        ppas = MagicMock(spec=RepositorioPPA)
        with pytest.raises(RegraNegocioError):
            CriarPPAUseCase(ppas).execute(CriarPPAInput(2026, 2027))


class TestDotacao:
    """Dotação e reserva de saldo."""

    def test_dotacao_e_reserva(self) -> None:
        """Cria, suplementa e reserva saldo."""
        dots = MagicMock(spec=RepositorioDotacao)
        dots.get_by_codigo_exercicio = MagicMock(return_value=None)
        dot = _dotacao()
        dots.save = MagicMock(return_value=dot)
        loas = MagicMock(spec=RepositorioLOA)
        loas.get_by_id = MagicMock(return_value=_loa(StatusLOA.PUBLICADA))
        CriarDotacaoUseCase(dots, loas).execute(
            CriarDotacaoInput(loa_id="loa-1", exercicio=2026,
                              codigo="01.01.01", valor_inicial=1000.0))
        dots.get_by_id = MagicMock(return_value=dot)
        SuplementarDotacaoUseCase(dots).execute("dot-1", 200.0)
        assert dot.valor_atualizado == 1200.0
        res_repo = MagicMock(spec=RepositorioReserva)
        res_repo.save = MagicMock(
            return_value=ReservaSaldo(id="r1", dotacao_id="dot-1", valor=300.0))
        ReservarSaldoUseCase(res_repo, dots).execute(
            ReservarSaldoInput(dotacao_id="dot-1", valor=300.0))
        assert dot.saldo_disponivel == 900.0

    def test_reserva_sem_saldo(self) -> None:
        """Reserva acima do saldo gera erro."""
        dot = _dotacao()
        dots = MagicMock(spec=RepositorioDotacao)
        dots.get_by_id = MagicMock(return_value=dot)
        res_repo = MagicMock(spec=RepositorioReserva)
        with pytest.raises(DotacaoSemSaldoError):
            ReservarSaldoUseCase(res_repo, dots).execute(
                ReservarSaldoInput(dotacao_id="dot-1", valor=5000.0))

    def test_anular_e_cancelar(self) -> None:
        """Anulação e cancelamento de reserva devolvem saldo."""
        dot = _dotacao()
        dot.reservar(300.0)
        dots = MagicMock(spec=RepositorioDotacao)
        dots.get_by_id = MagicMock(return_value=dot)
        dots.save = MagicMock(return_value=dot)
        AnularDotacaoUseCase(dots).execute("dot-1", 100.0)
        assert dot.valor_atualizado == 900.0
        res = ReservaSaldo(id="r1", dotacao_id="dot-1", valor=300.0)
        res_repo = MagicMock(spec=RepositorioReserva)
        res_repo.get_by_id = MagicMock(return_value=res)
        res_repo.save = MagicMock(return_value=res)
        CancelarReservaUseCase(res_repo, dots).execute("r1")
        assert dot.valor_reservado == 0.0
