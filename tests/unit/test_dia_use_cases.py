"""Testes unitários dos use cases de Diárias, Viagens e Deslocamentos (DOM-DIA)."""

import pytest
from datetime import date, datetime
from unittest.mock import MagicMock

from src.modules.sigmun_dia.application.use_cases import (
    CriarDiariaUseCase,
    CriarViagemUseCase,
    SolicitarViagemInput,
    SolicitacaoDiariaInput,
    AutorizarDiariaUseCase,
    PagarDiariaUseCase,
    CriarPrestacaoContasUseCase,
    CriarPrestacaoContasInputDTO,
    AprovarPrestacaoUseCase,
    AprovacaoPrestacaoInputDTO,
    GlosarPrestacaoUseCase,
    GlosagemPrestacaoInputDTO,
    RestituirPrestacaoUseCase,
    RestituicaPrestacaoInputDTO,
    ConfirmarConcessaoUseCase,
    ReverterParaPagamentoUseCase,
)
from src.modules.sigmun_dia.application.interfaces import (
    RepositorioViagem,
    RepositorioDiaria,
    RepositorioPrestacaoContas,
)
from src.modules.sigmun_dia.domain.entities import (
    Viagem,
    Diaria,
    StatusDiaria,
    CategoriaDiaria,
    PrestacaoContas,
)



def _diaria(status=StatusDiaria.SOLICITADA):
    return Diaria(
        id="diaria-1", viagem_id="viagem-1", servidor_id="servidor-1", dota_id="dota-1",
        categoria=CategoriaDiaria.EVENTO, descricao="Diária",
        valor_diaria=150.0, valor_total=150.0, status=status,
    )


def _prestacao(status="aberta"):
    return PrestacaoContas(
        id="prestacao-1", diaria_id="diaria-1", servidor_id="servidor-1", dota_id="dota-1",
        data_emissao=datetime(2024, 1, 10), documento_id="doc-1",
        valor_previsto=150.0, valor_apresentado=150.0, valor_glosado=0.0, valor_liquido=150.0,
        status=status,
    )


class TestViagem:
    def test_criar_viagem(self):
        repo = MagicMock(spec=RepositorioViagem)
        repo.save = MagicMock(return_value=Viagem(
            id="vid", servidor_id="s1", dota_id="d1", motivo="negócios",
            cargo_ocupado="Analista", unidade_origem_id="o1", unidade_destino_id="o2",
            data_inicio=date(2024, 1, 15), data_fim=date(2024, 1, 20), destino="SP",
            created_by="u1",
        ))
        uc = CriarViagemUseCase(repo)
        dto = SolicitarViagemInput(
            servidor_id="s1", dota_id="d1", motivo="negócios", cargo_ocupado="Analista",
            unidade_origem_id="o1", unidade_destino_id="o2",
            data_inicio=date(2024, 1, 15), data_fim=date(2024, 1, 20),
            destino="SP", autor_id="u1",
        )
        v = uc.execute(dto)
        assert v.id == "vid"
        repo.save.assert_called_once()


class TestDiaria:
    def test_criar_diaria(self):
        repo = MagicMock(spec=RepositorioDiaria)
        repo.save = MagicMock(return_value=_diaria())
        uc = CriarDiariaUseCase(repo, MagicMock(spec=RepositorioViagem))
        dto = SolicitacaoDiariaInput(
            viagem_id="viagem-1", servidor_id="servidor-1", dota_id="dota-1",
            categoria="evento", descricao="Diária", valor_diaria=150.0,
        )
        d = uc.execute(dto)
        assert d.id == "diaria-1"
        repo.save.assert_called_once()


class TestTransicoes:
    def test_autorizar(self):
        d = _diaria()
        repo = MagicMock(spec=RepositorioDiaria); repo.get_by_id=MagicMock(return_value=d); repo.save=MagicMock(return_value=d)
        r = AutorizarDiariaUseCase(repo).execute("diaria-1", "")
        assert r.status == StatusDiaria.AUTORIZADA

    def test_pagar_invalida(self):
        d = _diaria(StatusDiaria.AUTORIZADA)
        repo = MagicMock(spec=RepositorioDiaria); repo.get_by_id=MagicMock(return_value=d)
        with pytest.raises(Exception):
            PagarDiariaUseCase(repo).execute("diaria-1")


class TestConcessaoPagamento:
    def test_confirmar_concessao(self):
        d = _diaria(StatusDiaria.CALCULADA)
        repo = MagicMock(spec=RepositorioDiaria); repo.get_by_id=MagicMock(return_value=d); repo.save=MagicMock(return_value=d)
        r = ConfirmarConcessaoUseCase(repo).execute("diaria-1", date(2024,1,15), date(2024,1,16), "")
        assert r.status == StatusDiaria.CONCEDIDA

    def test_reverter_pagamento(self):
        d = _diaria(StatusDiaria.EM_PRESTACAO)
        repo = MagicMock(spec=RepositorioDiaria); repo.get_by_id=MagicMock(return_value=d); repo.save=MagicMock(return_value=d)
        r = ReverterParaPagamentoUseCase(repo).execute("diaria-1")
        assert r.status == StatusDiaria.PAGA


def _paga():
    return _diaria(StatusDiaria.PAGA)


class TestPrestacao:
    def test_criar(self):
        rp = MagicMock(spec=RepositorioPrestacaoContas); rp.save=MagicMock(return_value=_prestacao())
        rd = MagicMock(spec=RepositorioDiaria); rd.get_by_id=MagicMock(return_value=_paga())
        uc = CriarPrestacaoContasUseCase(rp, rd)
        dto = CriarPrestacaoContasInputDTO(diaria_id="diaria-1", servidor_id="s", dota_id="d", documento_id="doc", valor_previsto=150.0, valor_apresentado=150.0)
        p = uc.execute(dto)
        assert p.id == "prestacao-1"

    def test_aprovar(self):
        rp = MagicMock(spec=RepositorioPrestacaoContas); rp.get_by_diaria=MagicMock(return_value=_prestacao()); rp.save=MagicMock(return_value=_prestacao())
        rd = MagicMock(spec=RepositorioDiaria); rd.get_by_id=MagicMock(return_value=_paga())
        uc = AprovarPrestacaoUseCase(rd, rp)
        uc.execute(AprovacaoPrestacaoInputDTO(diaria_id="diaria-1", autor_id="u"))
        rp.save.assert_called_once()

    def test_glosar(self):
        prest = _prestacao()
        rp = MagicMock(spec=RepositorioPrestacaoContas); rp.get_by_diaria=MagicMock(return_value=prest); rp.save=MagicMock(return_value=prest)
        rd = MagicMock(spec=RepositorioDiaria); rd.get_by_id=MagicMock(return_value=_paga())
        uc = GlosarPrestacaoUseCase(rd, rp)
        r = uc.execute(GlosagemPrestacaoInputDTO(diaria_id="diaria-1", motivo="não comprovado", valor_glosado=50.0, autor_id="u"))
        assert r.status == "glosa"
        assert r.valor_glosado == 50.0

    def test_restituir(self):
        prest = _prestacao("glosa"); prest.valor_glosado = 50.0
        rp = MagicMock(spec=RepositorioPrestacaoContas); rp.get_by_diaria=MagicMock(return_value=prest); rp.save=MagicMock(return_value=prest)
        rd = MagicMock(spec=RepositorioDiaria); rd.get_by_id=MagicMock(return_value=_paga())
        uc = RestituirPrestacaoUseCase(rd, rp)
        r = uc.execute(RestituicaPrestacaoInputDTO(diaria_id="diaria-1", autor_id="u"))
        assert r.status == "restituida"
