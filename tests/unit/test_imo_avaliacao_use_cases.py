"""Testes de casos de uso do DOM-IMO (Cadastro Imobiliário) — avaliação de valor venal."""

from __future__ import annotations

import pytest

from src.modules.sigmun_cadastro_imobiliario.application.use_cases import (
    AvaliarImovelInput,
    AvaliarImovelUseCase,
    CancelarAvaliacaoUseCase,
    ConcluirAvaliacaoUseCase,
    ocupacao_do_imovel,
)
from src.modules.sigmun_cadastro_imobiliario.domain.entities import SituacaoAvaliacao
from src.modules.sigmun_cadastro_imobiliario.domain.exceptions import (
    AvaliacaoNaoEncontradaError,
    ImovelNaoEncontradoError,
    RegraNegocioError,
)
from tests.unit.imo_fixtures import _avaliacao as avaliacao
from tests.unit.imo_fixtures import _imovel as imovel
from tests.unit.imo_fixtures import repo_avaliacao, repo_imovel


def _avaliar(repo_av, repo_im, **kwargs):
    dto = {
        "imovel_id": "imovel-1",
        "ano": 2026,
        "valor_terreno_m2_unitario": 180.0,
        "valor_construcao_m2_unitario": 950.0,
    }
    dto.update(kwargs)
    return AvaliarImovelUseCase(repo_av, repo_im).execute(AvaliarImovelInput(**dto))


class TestAvaliacao:
    def test_calcula_valor_venal(self) -> None:
        """RN-IMO-005: valor venal = área do terreno × Vt + área construída × Vc."""
        result = _avaliar(repo_avaliacao(), repo_imovel(imovel()), aliquota_percent=2.5)
        assert result.area_terreno_m2 == 200.0
        assert result.area_construida_m2 == 120.0
        assert result.valor_terreno == 36000.0
        assert result.valor_construcao == 114000.0
        assert result.valor_venal == 150000.0
        assert result.valor_lancamento == 3750.0
        assert result.situacao == SituacaoAvaliacao.CONCLUIDA

    def test_avaliacao_em_rascunho(self) -> None:
        result = _avaliar(repo_avaliacao(), repo_imovel(imovel()), concluir=False)
        assert result.situacao == SituacaoAvaliacao.RASCUNHO

    def test_exige_imovel_existente(self) -> None:
        with pytest.raises(ImovelNaoEncontradoError):
            _avaliar(repo_avaliacao(), repo_imovel(), imovel_id="imovel-9")

    def test_nao_reavalia_exercicio_concluido(self) -> None:
        """RN-IMO-005: um exercício concluído não pode ser reavaliado."""
        repo = repo_avaliacao(avaliacao(SituacaoAvaliacao.CONCLUIDA))
        with pytest.raises(AvaliacaoNaoEncontradaError):
            _avaliar(repo, repo_imovel(imovel()))

    def test_imovel_sem_area_nao_e_avaliado(self) -> None:
        alvo = imovel()
        alvo.area_terreno_m2 = 0.0
        alvo.area_construida_m2 = 0.0
        with pytest.raises(RegraNegocioError):
            _avaliar(repo_avaliacao(), repo_imovel(alvo))

    def test_valores_unitarios_negativos_rejeitados(self) -> None:
        with pytest.raises(RegraNegocioError):
            _avaliar(
                repo_avaliacao(), repo_imovel(imovel()), valor_terreno_m2_unitario=-1.0
            )

    def test_aliquota_fora_de_faixa_rejeitada(self) -> None:
        with pytest.raises(RegraNegocioError):
            _avaliar(repo_avaliacao(), repo_imovel(imovel()), aliquota_percent=200.0)

    def test_ano_invalido_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            _avaliar(repo_avaliacao(), repo_imovel(imovel()), ano=1800)

    def test_conclui_avaliacao_rascunho(self) -> None:
        alvo = avaliacao()
        alvo.id = "aval-1"
        result = ConcluirAvaliacaoUseCase(repo_avaliacao(alvo)).execute("aval-1")
        assert result.situacao == SituacaoAvaliacao.CONCLUIDA

    def test_nao_conclui_avaliacao_ja_concluida(self) -> None:
        alvo = avaliacao(SituacaoAvaliacao.CONCLUIDA)
        alvo.id = "aval-1"
        with pytest.raises(RegraNegocioError):
            ConcluirAvaliacaoUseCase(repo_avaliacao(alvo)).execute("aval-1")

    def test_conclui_avaliacao_inexistente(self) -> None:
        with pytest.raises(AvaliacaoNaoEncontradaError):
            ConcluirAvaliacaoUseCase(repo_avaliacao()).execute("aval-9")

    def test_cancela_avaliacao_rascunho(self) -> None:
        alvo = avaliacao()
        alvo.id = "aval-1"
        result = CancelarAvaliacaoUseCase(repo_avaliacao(alvo)).execute("aval-1", "erro")
        assert result.situacao == SituacaoAvaliacao.CANCELADA

    def test_nao_cancela_avaliacao_concluida(self) -> None:
        alvo = avaliacao(SituacaoAvaliacao.CONCLUIDA)
        alvo.id = "aval-1"
        with pytest.raises(RegraNegocioError):
            CancelarAvaliacaoUseCase(repo_avaliacao(alvo)).execute("aval-1", "motivo")

    def test_cancela_avaliacao_inexistente(self) -> None:
        with pytest.raises(AvaliacaoNaoEncontradaError):
            CancelarAvaliacaoUseCase(repo_avaliacao()).execute("aval-9", "motivo")


class TestOcupacao:
    @pytest.mark.parametrize(
        ("tipo", "obra", "esperado"),
        [
            ("casa", None, "residencial"),
            ("lote", None, "terreno"),
            ("loja", None, "comercial"),
            ("galpao", None, "industrial"),
            ("casa", "comercial", "comercial"),
            ("lote", "nao_aplicavel", "terreno"),
            ("apartamento", "mista", "misto"),
            ("outro", None, "misto"),
        ],
    )
    def test_resolve_ocupacao(self, tipo: str, obra: str | None, esperado: str) -> None:
        assert ocupacao_do_imovel(tipo, obra) == esperado
