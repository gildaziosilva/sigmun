"""Testes de casos de uso do DOM-TRI (Administração Tributária)."""

from __future__ import annotations

from datetime import date, timedelta

import pytest
from unittest.mock import MagicMock

from src.modules.sigmun_tributos.application.interfaces import (
    RepositorioContribuinte,
    RepositorioImovel,
    RepositorioLancamento,
    RepositorioDividaAtiva,
    RepositorioCertidao,
)
from src.modules.sigmun_tributos.application.use_cases import (
    BaixarDividaAtivaUseCase,
    CadastrarContribuinteInput,
    CadastrarContribuinteUseCase,
    CadastrarImovelInput,
    CadastrarImovelUseCase,
    EmitirCertidaoUseCase,
    InscreverDividaAtivaUseCase,
    LancarTributoInput,
    LancarTributoUseCase,
    PagarLancamentoUseCase,
)
from src.modules.sigmun_tributos.domain.entities.certidao import TipoCertidao
from src.modules.sigmun_tributos.domain.entities.contribuinte import (
    Contribuinte,
    TipoContribuinte,
)
from src.modules.sigmun_tributos.domain.entities.imovel import Imovel
from src.modules.sigmun_tributos.domain.entities.lancamento import (
    Lancamento,
    StatusLancamento,
    TipoTributo,
)
from src.modules.sigmun_tributos.domain.exceptions import (
    ContribuinteJaExistenteError,
    ContribuinteNaoEncontradoError,
    ImovelJaExistenteError,
    LancamentoNaoEncontradoError,
    RegraNegocioError,
)


def _contribuinte(cpf: str = "11122233344") -> Contribuinte:
    return Contribuinte(cpf_cnpj=cpf, nome="Maria Silva",
                        tipo=TipoContribuinte.PESSOA_FISICA)


def _imovel(contribuinte_id: str = "c-1") -> Imovel:
    return Imovel(contribuinte_id=contribuinte_id,
                  inscricao_imobiliaria="INS-001", valor_venal=100000.0,
                  aliquota=0.01)


def _lancamento(contribuinte_id: str = "c-1") -> Lancamento:
    return Lancamento(
        contribuinte_id=contribuinte_id,
        tipo_tributo=TipoTributo.IPTU,
        exercicio=2026,
        numero_lancamento="2026IPTUABC123",
        valor_tributo=1000.0,
        juros=0.0, multa=0.0,
        data_vencimento=date.today() - timedelta(days=30),
    )


class TestContribuinte:
    """Cadastro de contribuintes."""

    def test_cadastra_contribuinte(self) -> None:
        repo = MagicMock(spec=RepositorioContribuinte)
        repo.get_by_cpf_cnpj = MagicMock(return_value=None)
        novo = _contribuinte()
        novo.id = "c-1"
        repo.save = MagicMock(return_value=novo)
        result = CadastrarContribuinteUseCase(repo).execute(
            CadastrarContribuinteInput(
                tipo="pf", nome="Maria Silva", cpf_cnpj="11122233344"
            )
        )
        assert result.cpf_cnpj == "11122233344"
        assert result.esta_ativo

    def test_nao_duplica_cpf(self) -> None:
        repo = MagicMock(spec=RepositorioContribuinte)
        repo.get_by_cpf_cnpj = MagicMock(return_value=_contribuinte())
        with pytest.raises(ContribuinteJaExistenteError):
            CadastrarContribuinteUseCase(repo).execute(
                CadastrarContribuinteInput(
                    tipo="pf", nome="Maria", cpf_cnpj="11122233344"
                )
            )


class TestImovel:
    """Cadastro de imóveis (IPTU)."""

    def test_cadastra_imovel(self) -> None:
        imoveis = MagicMock(spec=RepositorioImovel)
        imoveis.get_by_inscricao = MagicMock(return_value=None)
        cont = MagicMock(spec=RepositorioContribuinte)
        cont.get_by_id = MagicMock(return_value=_contribuinte())
        imovel = _imovel()
        imovel.id = "i-1"
        imoveis.save = MagicMock(return_value=imovel)
        result = CadastrarImovelUseCase(imoveis, cont).execute(
            CadastrarImovelInput(
                contribuinte_id="c-1", inscricao_imobiliaria="INS-001",
                valor_venal=100000.0, aliquota=0.01,
            )
        )
        assert result.inscricao_imobiliaria == "INS-001"
        assert result.calcular_iptu() == 1000.0

    def test_contribuinte_inexistente(self) -> None:
        imoveis = MagicMock(spec=RepositorioImovel)
        cont = MagicMock(spec=RepositorioContribuinte)
        cont.get_by_id = MagicMock(return_value=None)
        with pytest.raises(ContribuinteNaoEncontradoError):
            CadastrarImovelUseCase(imoveis, cont).execute(
                CadastrarImovelInput(
                    contribuinte_id="x", inscricao_imobiliaria="INS-001",
                    valor_venal=100000.0,
                )
            )

    def test_inscricao_duplicada(self) -> None:
        imoveis = MagicMock(spec=RepositorioImovel)
        imoveis.get_by_inscricao = MagicMock(return_value=_imovel())
        cont = MagicMock(spec=RepositorioContribuinte)
        cont.get_by_id = MagicMock(return_value=_contribuinte())
        with pytest.raises(ImovelJaExistenteError):
            CadastrarImovelUseCase(imoveis, cont).execute(
                CadastrarImovelInput(
                    contribuinte_id="c-1", inscricao_imobiliaria="INS-001",
                    valor_venal=100000.0,
                )
            )


class TestLancamento:
    """Constituição de créditos tributários."""

    def test_lanca_issqn(self) -> None:
        repo = MagicMock(spec=RepositorioLancamento)
        cont = MagicMock(spec=RepositorioContribuinte)
        cont.get_by_id = MagicMock(return_value=_contribuinte())
        imoveis = MagicMock(spec=RepositorioImovel)
        repo.save = MagicMock(side_effect=lambda l: l)
        result = LancarTributoUseCase(repo, cont, imoveis).execute(
            LancarTributoInput(
                contribuinte_id="c-1", tipo_tributo="issqn", exercicio=2026,
                base_calculo=10000.0, aliquota=0.05,
            )
        )
        assert result.tipo_tributo == TipoTributo.ISSQN
        assert result.base_calculo == 10000.0

    def test_iptu_exige_imovel(self) -> None:
        repo = MagicMock(spec=RepositorioLancamento)
        cont = MagicMock(spec=RepositorioContribuinte)
        cont.get_by_id = MagicMock(return_value=_contribuinte())
        imoveis = MagicMock(spec=RepositorioImovel)
        with pytest.raises(RegraNegocioError):
            LancarTributoUseCase(repo, cont, imoveis).execute(
                LancarTributoInput(
                    contribuinte_id="c-1", tipo_tributo="iptu", exercicio=2026,
                    base_calculo=100000.0,
                )
            )

    def test_pagar_lancamento(self) -> None:
        repo = MagicMock(spec=RepositorioLancamento)
        lance = _lancamento()
        repo.get_by_id = MagicMock(return_value=lance)
        repo.save = MagicMock(return_value=lance)
        result = PagarLancamentoUseCase(repo).execute("l-1")
        assert result.status == StatusLancamento.PAGO
        assert result.data_pagamento is not None

    def test_pagar_inexistente(self) -> None:
        repo = MagicMock(spec=RepositorioLancamento)
        repo.get_by_id = MagicMock(return_value=None)
        with pytest.raises(LancamentoNaoEncontradoError):
            PagarLancamentoUseCase(repo).execute("l-x")


class TestDividaAtiva:
    """Inscrição e baixa de dívida ativa."""

    def test_inscreve_cobranca_vencida(self) -> None:
        dividas = MagicMock(spec=RepositorioDividaAtiva)
        lancamentos = MagicMock(spec=RepositorioLancamento)
        lance = _lancamento()
        lance.data_vencimento = date.today() - timedelta(days=10)
        lancamentos.get_by_id = MagicMock(return_value=lance)
        inscricao = MagicMock()
        inscricao.id = "da-1"
        dividas.save = MagicMock(return_value=inscricao)
        result = InscreverDividaAtivaUseCase(dividas, lancamentos).execute("l-1")
        assert lance.status == StatusLancamento.INSCRITO_EM_DIVIDA_ATIVA
        assert result.id == "da-1"

    def test_nao_inscreve_nao_vencida(self) -> None:
        dividas = MagicMock(spec=RepositorioDividaAtiva)
        lancamentos = MagicMock(spec=RepositorioLancamento)
        lance = _lancamento()
        lance.data_vencimento = date.today() + timedelta(days=30)
        lancamentos.get_by_id = MagicMock(return_value=lance)
        with pytest.raises(RegraNegocioError):
            InscreverDividaAtivaUseCase(dividas, lancamentos).execute("l-1")

    def test_baixa_inscricao(self) -> None:
        dividas = MagicMock(spec=RepositorioDividaAtiva)
        inscricao = MagicMock()
        inscricao.id = "da-1"
        dividas.get_by_id = MagicMock(return_value=inscricao)
        inscricao.baixar = MagicMock()
        dividas.save = MagicMock(return_value=inscricao)
        BaixarDividaAtivaUseCase(dividas).execute("da-1")
        inscricao.baixar.assert_called_once()


class TestCertidao:
    """Emissão de certidões de regularidade fiscal."""

    def test_emite_negativa_sem_debitos(self) -> None:
        certidoes = MagicMock(spec=RepositorioCertidao)
        lancamentos = MagicMock(spec=RepositorioLancamento)
        lancamentos.list_abertos_por_contribuinte = MagicMock(return_value=[])
        cont = MagicMock(spec=RepositorioContribuinte)
        cont.get_by_id = MagicMock(return_value=_contribuinte())
        cert = _certa_com_tipo(TipoCertidao.NEGATIVA)
        cert.id = "cert-1"
        certidoes.save = MagicMock(return_value=cert)
        result = EmitirCertidaoUseCase(certidoes, lancamentos, cont).execute("c-1")
        assert result.id == "cert-1"

    def test_emite_positiva_com_debitos(self) -> None:
        certidoes = MagicMock(spec=RepositorioCertidao)
        lancamentos = MagicMock(spec=RepositorioLancamento)
        lancamentos.list_abertos_por_contribuinte = MagicMock(
            return_value=[_lancamento()]
        )
        cont = MagicMock(spec=RepositorioContribuinte)
        cont.get_by_id = MagicMock(return_value=_contribuinte())
        certidoes.save = MagicMock(side_effect=lambda c: c)
        result = EmitirCertidaoUseCase(certidoes, lancamentos, cont).execute("c-1")
        assert result.tipo == TipoCertidao.POSITIVA


def _certa_com_tipo(tipo: TipoCertidao):
    from src.modules.sigmun_tributos.domain.entities.certidao import Certidao

    return Certidao(contribuinte_id="c-1", tipo=tipo, numero="CERT123")