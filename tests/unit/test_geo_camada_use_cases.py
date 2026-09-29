"""Testes de casos de uso do DOM-GEO — camadas de mapa (RN-GEO-001, RN-GEO-006)."""

from __future__ import annotations

import pytest

from src.modules.sigmun_geoinformacao.application.use_cases import (
    AtivarCamadaUseCase,
    AtualizarCamadaInput,
    AtualizarCamadaUseCase,
    CadastrarCamadaInput,
    CadastrarCamadaUseCase,
    DesativarCamadaUseCase,
    ExcluirCamadaUseCase,
)
from src.modules.sigmun_geoinformacao.domain.entities import SituacaoCamadaMapa
from src.modules.sigmun_geoinformacao.domain.exceptions import (
    CamadaMapaJaExistenteError,
    CamadaMapaNaoEncontradaError,
    MapaComCamadasError,
    RegraNegocioError,
)
from tests.unit.geo_fixtures import (
    _camada,
    _publicado,
    _vinculo,
    repo_camada,
    repo_mapa,
    repo_vinculo,
)


def _cadastrar(repo=None):
    return CadastrarCamadaUseCase(repo or repo_camada()).execute(
        CadastrarCamadaInput(codigo="CAM-01", nome="Base hipsometrica", tipo="hipsometria")
    )


class TestCadastroCamada:
    def test_cadastra_camada_em_rascunho(self) -> None:
        camada = _cadastrar()
        assert camada.codigo == "CAM-01"
        assert camada.situacao is SituacaoCamadaMapa.RASCUNHO

    def test_codigo_duplicado_rejeitado(self) -> None:
        """RN-GEO-001: o código da camada é único."""
        repo = repo_camada(_camada())
        with pytest.raises(CamadaMapaJaExistenteError):
            _cadastrar(repo)

    def test_tipo_invalido_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarCamadaUseCase(repo_camada()).execute(
                CadastrarCamadaInput(codigo="CAM-9", nome="X", tipo="mapa_thermal")
            )

    def test_zoom_invertido_rejeitado(self) -> None:
        """RN-GEO-005: zoom mínimo não pode superar o máximo."""
        with pytest.raises(RegraNegocioError):
            CadastrarCamadaUseCase(repo_camada()).execute(
                CadastrarCamadaInput(
                    codigo="CAM-9", nome="X", zoom_minimo=20, zoom_maximo=5
                )
            )

    def test_zoom_fora_de_faixa_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarCamadaUseCase(repo_camada()).execute(
                CadastrarCamadaInput(codigo="CAM-9", nome="X", zoom_maximo=99)
            )


class TestCicloCamada:
    def test_ativa_camada(self) -> None:
        """RN-GEO-006: RASCUNHO -> ATIVA."""
        alvo = _camada()
        alvo.id = "cam-1"
        resultado = AtivarCamadaUseCase(repo_camada(alvo)).execute("cam-1")
        assert resultado.situacao is SituacaoCamadaMapa.ATIVA

    def test_ativar_camada_inexistente(self) -> None:
        with pytest.raises(CamadaMapaNaoEncontradaError):
            AtivarCamadaUseCase(repo_camada()).execute("cam-9")

    def test_desativa_camada(self) -> None:
        """RN-GEO-006: ATIVA -> DESATIVADA."""
        alvo = _camada(situacao=SituacaoCamadaMapa.ATIVA)
        alvo.id = "cam-1"
        resultado = DesativarCamadaUseCase(repo_camada(alvo)).execute("cam-1")
        assert resultado.situacao is SituacaoCamadaMapa.DESATIVADA
        assert resultado.visivel is False

    def test_camada_desativada_nao_e_reativada(self) -> None:
        """RN-GEO-006: a desativação é terminal."""
        alvo = _camada(situacao=SituacaoCamadaMapa.DESATIVADA)
        alvo.id = "cam-1"
        with pytest.raises(RegraNegocioError):
            AtivarCamadaUseCase(repo_camada(alvo)).execute("cam-1")

    def test_camada_de_servico_ativa_exige_url(self) -> None:
        """RN-GEO-006: formato WMS ativo exige URL de serviço."""
        from src.modules.sigmun_geoinformacao.domain.entities import CamadaMapa, FormatoCamada

        alvo = CamadaMapa(
            codigo="CAM-1",
            nome="OrtServico",
            formato=FormatoCamada.WMS,
            situacao=SituacaoCamadaMapa.ATIVA,
        )
        alvo.id = "cam-1"
        with pytest.raises(RegraNegocioError):
            AtivarCamadaUseCase(repo_camada(alvo)).execute("cam-1")


class TestAtualizacaoCamada:
    def test_atualiza_campos(self) -> None:
        alvo = _camada()
        alvo.id = "cam-1"
        resultado = AtualizarCamadaUseCase(repo_camada(alvo)).execute(
            AtualizarCamadaInput(camada_id="cam-1", nome="Novo nome", fonte="IBGE")
        )
        assert resultado.nome == "Novo nome"
        assert resultado.fonte == "IBGE"

    def test_atualiza_camada_inexistente(self) -> None:
        with pytest.raises(CamadaMapaNaoEncontradaError):
            AtualizarCamadaUseCase(repo_camada()).execute(
                AtualizarCamadaInput(camada_id="cam-9", nome="X")
            )

    def test_codigo_duplicado_na_atualizacao_rejeitado(self) -> None:
        """RN-GEO-001: não trocar para um código já usado por outra camada."""
        alvo = _camada()
        alvo.id = "cam-1"
        outra = _camada("CAM-99")
        repo = repo_camada(alvo)
        repo.get_by_codigo = lambda codigo: outra if codigo == "CAM-99" else None
        with pytest.raises(RegraNegocioError):
            AtualizarCamadaUseCase(repo).execute(
                AtualizarCamadaInput(camada_id="cam-1", codigo="CAM-99")
            )


class TestExclusaoCamada:
    def test_exclui_camada_sem_mapa_publicado(self) -> None:
        alvo = _camada()
        alvo.id = "cam-1"
        resultado = ExcluirCamadaUseCase(
            repo_camada(alvo), repo_vinculo(), repo_mapa()
        ).execute("cam-1")
        assert resultado.is_deleted is True

    def test_exclui_camada_inexistente(self) -> None:
        with pytest.raises(CamadaMapaNaoEncontradaError):
            ExcluirCamadaUseCase(repo_camada(), repo_vinculo(), repo_mapa()).execute("cam-9")

    def test_camada_de_mapa_publicado_nao_pode_ser_excluida(self) -> None:
        """RN-GEO-004: a composição publicada não pode ser desfeita."""
        alvo = _camada()
        alvo.id = "cam-1"
        mapa = _publicado()
        mapa.id = "mapa-1"
        with pytest.raises(MapaComCamadasError):
            ExcluirCamadaUseCase(
                repo_camada(alvo), repo_vinculo(_vinculo()), repo_mapa(mapa)
            ).execute("cam-1")

    def test_camada_de_mapa_rascunho_pode_ser_excluida(self) -> None:
        alvo = _camada()
        alvo.id = "cam-1"
        from src.modules.sigmun_geoinformacao.domain.entities import MapaSig

        mapa = MapaSig(codigo="MAP-1", nome="Rascunho")
        mapa.id = "mapa-1"
        resultado = ExcluirCamadaUseCase(
            repo_camada(alvo), repo_vinculo(_vinculo()), repo_mapa(mapa)
        ).execute("cam-1")
        assert resultado.is_deleted is True
