"""Testes de casos de uso do DOM-IMO (Cadastro Imobiliário) — geometria do lote."""

from __future__ import annotations

import pytest

from src.modules.sigmun_cadastro_imobiliario.application.use_cases import (
    RegistrarCaracteristicaInput,
    RegistrarCaracteristicaUseCase,
    RegistrarGeometriaInput,
    RegistrarGeometriaUseCase,
)
from src.modules.sigmun_cadastro_imobiliario.domain.entities import TipoObra
from src.modules.sigmun_cadastro_imobiliario.domain.exceptions import (
    ImovelNaoEncontradoError,
    RegraNegocioError,
)
from tests.unit.imo_fixtures import _geometria as geometria
from tests.unit.imo_fixtures import _imovel as imovel
from tests.unit.imo_fixtures import repo_caracteristica, repo_geometria, repo_imovel

VERTICES = [
    {"latitude": -13.121, "longitude": -39.481},
    {"latitude": -13.122, "longitude": -39.482},
    {"latitude": -13.120, "longitude": -39.480},
]


def _registrar(repo_geo=None, repo_im=None, **kwargs):
    dto = {"imovel_id": "imovel-1"}
    dto.update(kwargs)
    return RegistrarGeometriaUseCase(
        repo_geo or repo_geometria(), repo_im or repo_imovel(imovel())
    ).execute(RegistrarGeometriaInput(**dto))


class TestGeometria:
    def test_registra_poligono_do_lote(self) -> None:
        result = _registrar(geometria="poligono", vertices=VERTICES)
        assert result.imovel_id == "imovel-1"
        assert result.geometria == "poligono"
        assert len(result.vertices) == 3

    def test_ponto_adota_vertice_como_coordenada(self) -> None:
        result = _registrar(
            geometria="ponto", vertices=[{"latitude": -13.5, "longitude": -39.9}]
        )
        assert result.latitude == pytest.approx(-13.5)
        assert result.longitude == pytest.approx(-39.9)

    def test_substitui_geometria_anterior(self) -> None:
        anterior = geometria()
        anterior.id = "geo-1"
        result = _registrar(
            repo_geo=repo_geometria(anterior), geometria="poligono", vertices=VERTICES
        )
        assert result.id == "geo-1"

    def test_exige_imovel_existente(self) -> None:
        with pytest.raises(ImovelNaoEncontradoError):
            _registrar(repo_im=repo_imovel(), imovel_id="imovel-9")

    def test_poligono_exige_tres_vertices(self) -> None:
        """RN-IMO-007: geometria poligonal exige ao menos 3 vértices."""
        with pytest.raises(RegraNegocioError):
            _registrar(geometria="poligono", vertices=VERTICES[:2])

    def test_linha_exige_dois_vertices(self) -> None:
        with pytest.raises(RegraNegocioError):
            _registrar(geometria="linha", vertices=VERTICES[:1])

    def test_geometria_invalida_rejeitada(self) -> None:
        with pytest.raises(RegraNegocioError):
            _registrar(geometria="circulo")

    def test_datum_invalido_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            _registrar(
                geometria="ponto",
                latitude=-13.1,
                longitude=-39.4,
                vertices=[{"latitude": -13.1, "longitude": -39.4}],
                datum="inexistente",
            )

    def test_coordenada_fora_de_faixa_rejeitada(self) -> None:
        with pytest.raises(RegraNegocioError):
            _registrar(latitude=95.0, longitude=-39.4)

    def test_vertice_fora_de_faixa_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            _registrar(
                geometria="poligono",
                vertices=[
                    {"latitude": -13.1, "longitude": -39.4},
                    {"latitude": -13.2, "longitude": -39.5},
                    {"latitude": 91.0, "longitude": -39.6},
                ],
            )

    def test_precisao_negativa_rejeitada(self) -> None:
        with pytest.raises(RegraNegocioError):
            _registrar(
                geometria="ponto",
                latitude=-13.1,
                longitude=-39.4,
                vertices=[{"latitude": -13.1, "longitude": -39.4}],
                precisao_m=-1.0,
            )


class TestCaracteristica:
    def test_registra_caracteristica(self) -> None:
        result = RegistrarCaracteristicaUseCase(
            repo_caracteristica(), repo_imovel(imovel())
        ).execute(
            RegistrarCaracteristicaInput(
                imovel_id="imovel-1", obra="residencial", numero_pavimentos=2
            )
        )
        assert result.obra == TipoObra.RESIDENCIAL
        assert result.numero_pavimentos == 2

    def test_exige_imovel_existente(self) -> None:
        with pytest.raises(ImovelNaoEncontradoError):
            RegistrarCaracteristicaUseCase(
                repo_caracteristica(), repo_imovel()
            ).execute(RegistrarCaracteristicaInput(imovel_id="imovel-9"))

    def test_obra_invalida_rejeitada(self) -> None:
        with pytest.raises(RegraNegocioError):
            RegistrarCaracteristicaUseCase(
                repo_caracteristica(), repo_imovel(imovel())
            ).execute(RegistrarCaracteristicaInput(imovel_id="imovel-1", obra="castelo"))

    def test_pavimentos_invalidos_rejeitados(self) -> None:
        with pytest.raises(RegraNegocioError):
            RegistrarCaracteristicaUseCase(
                repo_caracteristica(), repo_imovel(imovel())
            ).execute(
                RegistrarCaracteristicaInput(imovel_id="imovel-1", numero_pavimentos=0)
            )

    def test_ano_renovacao_invalido_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            RegistrarCaracteristicaUseCase(
                repo_caracteristica(), repo_imovel(imovel())
            ).execute(
                RegistrarCaracteristicaInput(imovel_id="imovel-1", ano_renovacao=1500)
            )

