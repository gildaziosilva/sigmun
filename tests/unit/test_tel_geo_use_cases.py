"""Testes de casos de uso do DOM-TEL (Gestão Territorial) — georreferenciamento."""

from __future__ import annotations

import pytest

from src.modules.sigmun_territorial.application.use_cases import (
    ExcluirGeorreferenciaUseCase,
    RegistrarGeorreferenciaInput,
    RegistrarGeorreferenciaUseCase,
)
from src.modules.sigmun_territorial.domain.entities import TipoGeometria
from src.modules.sigmun_territorial.domain.exceptions import (
    BairroNaoEncontradoError,
    GeorreferenciaNaoEncontradaError,
    LogradouroNaoEncontradoError,
    RegraNegocioError,
)
from tests.unit.tel_fixtures import _bairro as bairro
from tests.unit.tel_fixtures import _georreferencia as georreferencia
from tests.unit.tel_fixtures import _logradouro as logradouro
from tests.unit.tel_fixtures import repo_bairro, repo_geo, repo_logradouro


def _bairro_cadastrado():
    alvo = bairro()
    alvo.id = "bairro-1"
    return alvo


def _logradouro_cadastrado():
    alvo = logradouro()
    alvo.id = "lg-1"
    return alvo


def _use_case(geo_repo=None, bairros=None, logradouros=None):
    return RegistrarGeorreferenciaUseCase(
        geo_repo or repo_geo(),
        bairros if bairros is not None else repo_bairro(_bairro_cadastrado()),
        logradouros if logradouros is not None else repo_logradouro(),
    )


class TestGeorreferencia:
    def test_registra_ponto_de_bairro(self) -> None:
        result = _use_case().execute(
            RegistrarGeorreferenciaInput(
                bairro_id="bairro-1",
                latitude=-13.13,
                longitude=-39.49,
                vertices=[{"latitude": -13.13, "longitude": -39.49}],
            )
        )
        assert result.bairro_id == "bairro-1"
        assert result.logradouro_id == ""
        assert result.geometria == TipoGeometria.PONTO

    def test_registra_poligono_de_logradouro(self) -> None:
        result = _use_case(logradouros=repo_logradouro(_logradouro_cadastrado())).execute(
            RegistrarGeorreferenciaInput(
                logradouro_id="lg-1",
                geometria="poligono",
                vertices=[
                    {"latitude": -13.12, "longitude": -39.48},
                    {"latitude": -13.13, "longitude": -39.49},
                    {"latitude": -13.11, "longitude": -39.47},
                ],
            )
        )
        assert result.logradouro_id == "lg-1"
        assert len(result.vertices) == 3

    def test_ponto_adota_primeiro_vertice_como_coordenada(self) -> None:
        result = _use_case().execute(
            RegistrarGeorreferenciaInput(
                bairro_id="bairro-1",
                vertices=[{"latitude": -13.20, "longitude": -39.40}],
            )
        )
        assert result.latitude == pytest.approx(-13.20)
        assert result.longitude == pytest.approx(-39.40)

    def test_exige_bairro_ou_logradouro(self) -> None:
        """RN-TEL-005: georreferência exige referência territorial."""
        with pytest.raises(RegraNegocioError):
            _use_case().execute(
                RegistrarGeorreferenciaInput(latitude=-13.13, longitude=-39.49)
            )

    def test_recusa_bairro_e_logradouro_simultaneos(self) -> None:
        with pytest.raises(RegraNegocioError):
            _use_case().execute(
                RegistrarGeorreferenciaInput(bairro_id="bairro-1", logradouro_id="lg-1")
            )

    def test_exige_bairro_existente(self) -> None:
        with pytest.raises(BairroNaoEncontradoError):
            _use_case(bairros=repo_bairro()).execute(
                RegistrarGeorreferenciaInput(bairro_id="bairro-9", latitude=-13.1)
            )

    def test_exige_logradouro_existente(self) -> None:
        with pytest.raises(LogradouroNaoEncontradoError):
            _use_case(logradouros=repo_logradouro()).execute(
                RegistrarGeorreferenciaInput(logradouro_id="lg-9", latitude=-13.1)
            )

    def test_latitude_fora_de_faixa_rejeitada(self) -> None:
        """Sem vértices, a coordenada principal é validada (RN-TEL-005)."""
        with pytest.raises(RegraNegocioError):
            _use_case().execute(
                RegistrarGeorreferenciaInput(
                    bairro_id="bairro-1", latitude=95.0, longitude=-39.49
                )
            )

    def test_longitude_fora_de_faixa_rejeitada(self) -> None:
        """Sem vértices, a coordenada principal é validada (RN-TEL-005)."""
        with pytest.raises(RegraNegocioError):
            _use_case().execute(
                RegistrarGeorreferenciaInput(
                    bairro_id="bairro-1", latitude=-13.13, longitude=-200.0
                )
            )

    def test_vertice_fora_de_faixa_rejeitado(self) -> None:
        """Com vértices, cada vértice também é validado (RN-TEL-005)."""
        with pytest.raises(RegraNegocioError):
            _use_case().execute(
                RegistrarGeorreferenciaInput(
                    bairro_id="bairro-1",
                    latitude=-13.13,
                    longitude=-39.49,
                    vertices=[{"latitude": 95.0, "longitude": -39.49}],
                )
            )


    def test_poligono_exige_tres_vertices(self) -> None:
        with pytest.raises(RegraNegocioError):
            _use_case().execute(
                RegistrarGeorreferenciaInput(
                    bairro_id="bairro-1",
                    geometria="poligono",
                    vertices=[{"latitude": -13.12, "longitude": -39.48}],
                )
            )

    def test_vertice_invalido_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            _use_case().execute(
                RegistrarGeorreferenciaInput(
                    bairro_id="bairro-1",
                    geometria="poligono",
                    vertices=[
                        {"latitude": -13.12, "longitude": -39.48},
                        {"latitude": -13.13, "longitude": -39.49},
                        {"latitude": 91.0, "longitude": -39.47},
                    ],
                )
            )

    def test_geometria_invalida_rejeitada(self) -> None:
        with pytest.raises(RegraNegocioError):
            _use_case().execute(
                RegistrarGeorreferenciaInput(bairro_id="bairro-1", geometria="circulo")
            )

    def test_datum_invalido_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            _use_case().execute(
                RegistrarGeorreferenciaInput(
                    bairro_id="bairro-1",
                    latitude=-13.13,
                    longitude=-39.49,
                    vertices=[{"latitude": -13.13, "longitude": -39.49}],
                    datum="inexistente",
                )
            )

    def test_precisao_negativa_rejeitada(self) -> None:
        with pytest.raises(RegraNegocioError):
            _use_case().execute(
                RegistrarGeorreferenciaInput(
                    bairro_id="bairro-1",
                    latitude=-13.13,
                    longitude=-39.49,
                    vertices=[{"latitude": -13.13, "longitude": -39.49}],
                    precisao_m=-1.0,
                )
            )

    def test_exclui_logicamente(self) -> None:
        alvo = georreferencia()
        alvo.id = "geo-1"
        repo = repo_geo(alvo)
        assert ExcluirGeorreferenciaUseCase(repo).execute("geo-1").is_deleted is True

    def test_exclui_georreferencia_inexistente(self) -> None:
        with pytest.raises(GeorreferenciaNaoEncontradaError):
            ExcluirGeorreferenciaUseCase(repo_geo()).execute("geo-9")

