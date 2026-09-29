"""Fixtures compartilhados pelos testes do DOM-GEO (Geoinformação Municipal)."""

from __future__ import annotations

from unittest.mock import MagicMock

from src.modules.sigmun_geoinformacao.application.interfaces import (
    RepositorioCamadaMapa,
    RepositorioFeatureGeo,
    RepositorioMapaCamada,
    RepositorioMapaSig,
    RepositorioServicoGeo,
)
from src.modules.sigmun_geoinformacao.domain.entities import (
    CamadaMapa,
    FeatureGeo,
    FormatoCamada,
    MapaCamada,
    MapaSig,
    ServicoGeo,
    SituacaoCamadaMapa,
    SituacaoMapaSig,
    TipoCamadaMapa,
)


def _camada(codigo: str = "CAM-01", situacao: SituacaoCamadaMapa = SituacaoCamadaMapa.RASCUNHO):
    return CamadaMapa(
        codigo=codigo,
        nome="Base hipsometrica",
        tipo=TipoCamadaMapa.HIPSOMETRIA,
        formato=FormatoCamada.GEOTIFF,
        situacao=situacao,
    )


def _camada_ativa(codigo: str = "CAM-01") -> CamadaMapa:
    return _camada(codigo, SituacaoCamadaMapa.ATIVA)


def _mapa(
    codigo: str = "MAP-01", situacao: SituacaoMapaSig = SituacaoMapaSig.RASCUNHO
) -> MapaSig:
    return MapaSig(codigo=codigo, nome="Mapa de uso do solo", situacao=situacao)


def _publicado() -> MapaSig:
    """Mapa publicado, para verificar o congelamento da composição (RN-GEO-004)."""
    return _mapa(situacao=SituacaoMapaSig.PUBLICADO)


def _vinculo(mapa_id: str = "mapa-1", camada_id: str = "camada-1") -> MapaCamada:
    return MapaCamada(mapa_id=mapa_id, camada_id=camada_id)


def _feature(camada_id: str = "camada-1") -> FeatureGeo:
    return FeatureGeo(
        codigo="PT-01",
        nome="Prefeitura Municipal",
        camada_id=camada_id,
        latitude=-13.1289,
        longitude=-39.4906,
        vertices=[{"latitude": -13.1289, "longitude": -39.4906}],
    )


def _servico() -> ServicoGeo:
    return ServicoGeo(
        codigo="WMS-01",
        nome="Servico de ortofoto",
        tipo="wms",
        url="https://geo.exemplo.gov.br/wms",
        camada="ortofoto",
    )


def repo_camada(camada: CamadaMapa | None = None) -> MagicMock:
    """Cria um port de camadas simulado."""
    repo = MagicMock(spec=RepositorioCamadaMapa)
    repo.get_by_id = MagicMock(return_value=camada)
    repo.get_by_codigo = MagicMock(return_value=camada)
    repo.save = MagicMock(side_effect=lambda c: c)
    repo.list_all = MagicMock(return_value=[camada] if camada else [])
    return repo


def repo_mapa(mapa: MapaSig | None = None) -> MagicMock:
    """Cria um port de mapas simulado."""
    repo = MagicMock(spec=RepositorioMapaSig)
    repo.get_by_id = MagicMock(return_value=mapa)
    repo.get_by_codigo = MagicMock(return_value=mapa)
    repo.save = MagicMock(side_effect=lambda m: m)
    repo.list_all = MagicMock(return_value=[mapa] if mapa else [])
    return repo


def repo_vinculo(vinculo: MapaCamada | None = None) -> MagicMock:
    """Cria um port de composição simulado."""
    repo = MagicMock(spec=RepositorioMapaCamada)
    repo.get_by_id = MagicMock(return_value=vinculo)
    repo.get_by_mapa_camada = MagicMock(return_value=vinculo)
    repo.save = MagicMock(side_effect=lambda v: v)
    repo.delete = MagicMock(return_value=None)
    repo.list_by_mapa = MagicMock(return_value=[vinculo] if vinculo else [])
    repo.list_by_camada = MagicMock(return_value=[vinculo] if vinculo else [])
    return repo


def repo_feature(feature: FeatureGeo | None = None) -> MagicMock:
    """Cria um port de elementos geoespaciais simulado."""
    repo = MagicMock(spec=RepositorioFeatureGeo)
    repo.get_by_id = MagicMock(return_value=feature)
    repo.get_by_codigo_camada = MagicMock(return_value=feature)
    repo.save = MagicMock(side_effect=lambda f: f)
    repo.list_by_camada = MagicMock(return_value=[feature] if feature else [])
    repo.list_all = MagicMock(return_value=[feature] if feature else [])
    return repo


def repo_servico(servico: ServicoGeo | None = None) -> MagicMock:
    """Cria um port de serviços geoespaciais simulado."""
    repo = MagicMock(spec=RepositorioServicoGeo)
    repo.get_by_id = MagicMock(return_value=servico)
    repo.get_by_codigo = MagicMock(return_value=servico)
    repo.save = MagicMock(side_effect=lambda s: s)
    repo.list_all = MagicMock(return_value=[servico] if servico else [])
    return repo
