"""Fixtures compartilhados pelos testes do DOM-TEL (Gestão Territorial)."""

from __future__ import annotations

from unittest.mock import MagicMock

from src.modules.sigmun_territorial.application.interfaces import (
    RepositorioBairro,
    RepositorioGeorreferencia,
    RepositorioLogradouro,
    RepositorioPlantaValores,
)
from src.modules.sigmun_territorial.domain.entities import (
    Bairro,
    Georreferencia,
    Logradouro,
    PlantaGenericaValores,
    SituacaoPlantaValores,
)


def _bairro(codigo: str = "BR-01") -> Bairro:
    return Bairro(codigo=codigo, nome="Centro")


def _logradouro(bairro_id: str = "bairro-1") -> Logradouro:
    return Logradouro(codigo="LG-01", nome="Rua da Matriz", bairro_id=bairro_id)


def _planta(
    situacao: SituacaoPlantaValores = SituacaoPlantaValores.RASCUNHO,
) -> PlantaGenericaValores:
    return PlantaGenericaValores(
        ano=2026,
        bairro_id="bairro-1",
        valor_terreno_m2=180.0,
        valor_construcao_m2=950.0,
        aliquota_percent=2.5,
        situacao=situacao,
    )


def _georreferencia() -> Georreferencia:
    return Georreferencia(
        bairro_id="bairro-1",
        geometria="ponto",
        latitude=-13.13,
        longitude=-39.49,
        vertices=[{"latitude": -13.13, "longitude": -39.49}],
    )


def repo_bairro(bairro: Bairro | None = None) -> MagicMock:
    """Cria um port de bairros simulado."""
    repo = MagicMock(spec=RepositorioBairro)
    repo.get_by_codigo = MagicMock(return_value=bairro)
    repo.get_by_id = MagicMock(return_value=bairro)
    repo.save = MagicMock(side_effect=lambda b: b)
    repo.list_all = MagicMock(return_value=[bairro] if bairro else [])
    return repo


def repo_logradouro(logradouro: Logradouro | None = None) -> MagicMock:
    """Cria um port de logradouros simulado."""
    repo = MagicMock(spec=RepositorioLogradouro)
    repo.get_by_codigo = MagicMock(return_value=logradouro)
    repo.get_by_id = MagicMock(return_value=logradouro)
    repo.save = MagicMock(side_effect=lambda lg: lg)
    repo.list_by_bairro = MagicMock(return_value=[logradouro] if logradouro else [])
    repo.list_all = MagicMock(return_value=[logradouro] if logradouro else [])
    return repo


def repo_planta(planta: PlantaGenericaValores | None = None) -> MagicMock:
    """Cria um port de plantas genéricas de valores simulado."""
    repo = MagicMock(spec=RepositorioPlantaValores)
    repo.get_by_id = MagicMock(return_value=planta)
    repo.get_vigente = MagicMock(return_value=None)
    repo.save = MagicMock(side_effect=lambda p: p)
    repo.list_all = MagicMock(return_value=[planta] if planta else [])
    return repo


def repo_geo(geo: Georreferencia | None = None) -> MagicMock:
    """Cria um port de georreferências simulado."""
    repo = MagicMock(spec=RepositorioGeorreferencia)
    repo.get_by_id = MagicMock(return_value=geo)
    repo.save = MagicMock(side_effect=lambda g: g)
    repo.list_all = MagicMock(return_value=[geo] if geo else [])
    repo.list_by_referencia = MagicMock(return_value=[geo] if geo else [])
    return repo
