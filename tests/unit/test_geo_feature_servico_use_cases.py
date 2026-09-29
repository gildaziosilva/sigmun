"""Testes de casos de uso do DOM-GEO — elementos e serviços (RN-GEO-003/007/008)."""

from __future__ import annotations

import pytest

from src.modules.sigmun_geoinformacao.application.use_cases import (
    AtualizarServicoInput,
    AtualizarServicoUseCase,
    CadastrarServicoInput,
    CadastrarServicoUseCase,
    ExcluirFeatureUseCase,
    ExcluirServicoUseCase,
    InativarServicoUseCase,
    RegistrarFeatureInput,
    RegistrarFeatureUseCase,
)
from src.modules.sigmun_geoinformacao.domain.entities import (
    SituacaoCamadaMapa,
    TipoGeometria,
)
from src.modules.sigmun_geoinformacao.domain.exceptions import (
    CamadaMapaNaoEncontradaError,
    FeatureGeoJaExistenteError,
    FeatureGeoNaoEncontradaError,
    RegraNegocioError,
    ServicoGeoJaExistenteError,
    ServicoGeoNaoEncontradoError,
)
from tests.unit.geo_fixtures import (
    _camada,
    _camada_ativa,
    _feature,
    _servico,
    repo_camada,
    repo_feature,
    repo_servico,
)


def _camada_cadastrada(ativa=True, camada_id="camada-1"):
    camada = _camada_ativa() if ativa else _camada()
    if not ativa:
        camada.situacao = SituacaoCamadaMapa.RASCUNHO
    camada.id = camada_id
    return camada


def _registrar(features=None, **kwargs):
    dto = {
        "codigo": "PT-01",
        "nome": "Prefeitura Municipal",
        "camada_id": "camada-1",
        "vertices": [{"latitude": -13.1289, "longitude": -39.4906}],
    }
    dto.update(kwargs)
    return RegistrarFeatureUseCase(
        repo_feature(*(features or ())), repo_camada(_camada_cadastrada())
    ).execute(RegistrarFeatureInput(**dto))


class TestElementosGeoespaciais:
    def test_registra_ponto_de_interesse(self) -> None:
        """RN-GEO-003: ponto com um vértice."""
        feature = _registrar()
        assert feature.geometria is TipoGeometria.PONTO
        assert feature.latitude == pytest.approx(-13.1289)

    def test_ponto_adota_primeiro_vertice_como_coordenada(self) -> None:
        feature = _registrar(
            vertices=[{"latitude": -13.2, "longitude": -39.4}],
            latitude=0.0,
            longitude=0.0,
        )
        assert feature.latitude == pytest.approx(-13.2)
        assert feature.longitude == pytest.approx(-39.4)

    def test_registra_poligono(self) -> None:
        """RN-GEO-003: polígono exige três vértices."""
        feature = _registrar(
            geometria="poligono",
            vertices=[
                {"latitude": -13.12, "longitude": -39.48},
                {"latitude": -13.13, "longitude": -39.49},
                {"latitude": -13.11, "longitude": -39.47},
            ],
        )
        assert feature.geometria is TipoGeometria.POLIGONO
        assert len(feature.vertices) == 3

    def test_poligono_com_vertices_insuficientes_rejeitado(self) -> None:
        """RN-GEO-003: vértices consistentes com o tipo de geometria."""
        with pytest.raises(RegraNegocioError):
            _registrar(geometria="poligono")

    def test_elemento_exige_camada(self) -> None:
        """RN-GEO-008: todo elemento pertence a uma camada cadastrada."""
        with pytest.raises(RegraNegocioError):
            _registrar(camada_id="")

    def test_elemento_em_camada_inexistente(self) -> None:
        """RN-GEO-008: a camada referenciada precisa existir."""
        repo = repo_camada()
        repo.get_by_id = lambda _id: None
        with pytest.raises(CamadaMapaNaoEncontradaError):
            RegistrarFeatureUseCase(repo_feature(), repo).execute(
                RegistrarFeatureInput(
                    codigo="PT-9",
                    nome="X",
                    camada_id="camada-9",
                    vertices=[{"latitude": -13.1, "longitude": -39.4}],
                )
            )

    def test_codigo_duplicado_na_camada_rejeitado(self) -> None:
        with pytest.raises(FeatureGeoJaExistenteError):
            _registrar(features=(_feature(),))

    def test_latitude_fora_de_faixa_rejeitada(self) -> None:
        """RN-GEO-003: coordenadas dentro do intervalo do datum."""
        with pytest.raises(RegraNegocioError):
            _registrar(vertices=[{"latitude": 95.0, "longitude": -39.4}])

    def test_exclui_elemento(self) -> None:
        alvo = _feature()
        alvo.id = "feat-1"
        assert ExcluirFeatureUseCase(repo_feature(alvo)).execute("feat-1").is_deleted is True

    def test_exclui_elemento_inexistente(self) -> None:
        with pytest.raises(FeatureGeoNaoEncontradaError):
            ExcluirFeatureUseCase(repo_feature()).execute("feat-9")


class TestServicosGeoespaciais:
    def test_cadastra_servico_wms(self) -> None:
        """RN-GEO-007: serviço WMS exige URL e nome de camada."""
        servico = CadastrarServicoUseCase(repo_servico()).execute(
            CadastrarServicoInput(
                codigo="WMS-01",
                nome="Ortofoto",
                tipo="wms",
                url="https://geo.exemplo.gov.br/wms",
                camada="ortofoto",
            )
        )
        assert servico.codigo == "WMS-01"

    def test_codigo_duplicado_rejeitado(self) -> None:
        with pytest.raises(ServicoGeoJaExistenteError):
            CadastrarServicoUseCase(repo_servico(_servico())).execute(
                CadastrarServicoInput(
                    codigo="WMS-01", nome="X", url="https://x.gov.br", camada="c"
                )
            )

    def test_servico_ativo_sem_url_rejeitado(self) -> None:
        """RN-GEO-007: serviço ativo exige URL de acesso."""
        with pytest.raises(RegraNegocioError):
            CadastrarServicoUseCase(repo_servico()).execute(
                CadastrarServicoInput(codigo="WMS-9", nome="X", url="")
            )

    def test_servico_com_url_invalida_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarServicoUseCase(repo_servico()).execute(
                CadastrarServicoInput(
                    codigo="WMS-9", nome="X", url="ftp://geo.exemplo.gov.br", camada="c"
                )
            )

    def test_wms_sem_nome_de_camada_rejeitado(self) -> None:
        """RN-GEO-007: WMS/WFS exigem a camada publicada."""
        with pytest.raises(RegraNegocioError):
            CadastrarServicoUseCase(repo_servico()).execute(
                CadastrarServicoInput(
                    codigo="WMS-9", nome="X", tipo="wms", url="https://x.gov.br"
                )
            )

    def test_tipo_invalido_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarServicoUseCase(repo_servico()).execute(
                CadastrarServicoInput(
                    codigo="S-9", nome="X", tipo="soap", url="https://x.gov.br"
                )
            )

    def test_zoom_invertido_rejeitado(self) -> None:
        """RN-GEO-005: coerência dos níveis de zoom."""
        with pytest.raises(RegraNegocioError):
            CadastrarServicoUseCase(repo_servico()).execute(
                CadastrarServicoInput(
                    codigo="S-9",
                    nome="X",
                    url="https://x.gov.br",
                    camada="c",
                    zoom_minimo=20,
                    zoom_maximo=5,
                )
            )

    def test_atualiza_servico(self) -> None:
        servico = _servico()
        servico.id = "srv-1"
        resultado = AtualizarServicoUseCase(repo_servico(servico)).execute(
            AtualizarServicoInput(servico_id="srv-1", nome="Novo nome", publico=True)
        )
        assert resultado.nome == "Novo nome"
        assert resultado.publico is True

    def test_atualiza_servico_inexistente(self) -> None:
        with pytest.raises(ServicoGeoNaoEncontradoError):
            AtualizarServicoUseCase(repo_servico()).execute(
                AtualizarServicoInput(servico_id="srv-9", nome="X")
            )

    def test_inativa_servico(self) -> None:
        servico = _servico()
        servico.id = "srv-1"
        resultado = InativarServicoUseCase(repo_servico(servico)).execute("srv-1")
        assert resultado.situacao.value == "inativo"

    def test_exclui_servico(self) -> None:
        servico = _servico()
        servico.id = "srv-1"
        assert ExcluirServicoUseCase(repo_servico(servico)).execute("srv-1").is_deleted is True
