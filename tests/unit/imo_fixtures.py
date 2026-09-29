"""Fixtures compartilhados pelos testes do DOM-IMO (Cadastro Imobiliário)."""

from __future__ import annotations

from unittest.mock import MagicMock

from src.modules.sigmun_cadastro_imobiliario.application.interfaces import (
    RepositorioAvaliacao,
    RepositorioCaracteristica,
    RepositorioGeometria,
    RepositorioImovel,
    RepositorioProprietario,
)
from src.modules.sigmun_cadastro_imobiliario.domain.entities import (
    AvaliacaoImovel,
    CaracteristicaImovel,
    GeometriaImovel,
    Imovel,
    ProprietarioImovel,
    SituacaoAvaliacao,
    SituacaoImovel,
)


def _imovel(inscricao: str = "INS-0001") -> Imovel:
    return Imovel(
        inscricao_imobiliaria=inscricao,
        logradouro_id="lg-1",
        bairro_id="bairro-1",
        numero="120",
        area_terreno_m2=200.0,
        area_construida_m2=120.0,
    )


def _imovel_demolid() -> Imovel:
    alvo = _imovel()
    alvo.situacao = SituacaoImovel.DEMOLIDO
    return alvo


def _proprietario(principal: bool = True) -> ProprietarioImovel:
    return ProprietarioImovel(
        imovel_id="imovel-1",
        nome="Maria Souza",
        cpf="12345678909",
        principal=principal,
    )


def _avaliacao(situacao: SituacaoAvaliacao = SituacaoAvaliacao.RASCUNHO) -> AvaliacaoImovel:
    return AvaliacaoImovel(
        imovel_id="imovel-1",
        ano=2026,
        valor_terreno_m2_unitario=180.0,
        valor_construcao_m2_unitario=950.0,
        aliquota_percent=2.5,
        area_terreno_m2=200.0,
        area_construida_m2=120.0,
        situacao=situacao,
    )


def _geometria() -> GeometriaImovel:
    return GeometriaImovel(
        imovel_id="imovel-1",
        geometria="poligono",
        latitude=-13.121,
        longitude=-39.481,
        vertices=[
            {"latitude": -13.121, "longitude": -39.481},
            {"latitude": -13.122, "longitude": -39.482},
            {"latitude": -13.120, "longitude": -39.480},
        ],
    )


def repo_imovel(imovel: Imovel | None = None) -> MagicMock:
    """Cria um port de imóveis simulado."""
    repo = MagicMock(spec=RepositorioImovel)
    repo.get_by_id = MagicMock(return_value=imovel)
    repo.get_by_inscricao = MagicMock(return_value=imovel)
    repo.save = MagicMock(side_effect=lambda i: i)
    repo.list_by_logradouro = MagicMock(return_value=[imovel] if imovel else [])
    repo.list_by_bairro = MagicMock(return_value=[imovel] if imovel else [])
    repo.list_all = MagicMock(return_value=[imovel] if imovel else [])
    return repo


def repo_proprietario(proprietario: ProprietarioImovel | None = None) -> MagicMock:
    """Cria um port de vínculos de propriedade simulado."""
    repo = MagicMock(spec=RepositorioProprietario)
    repo.get_by_id = MagicMock(return_value=proprietario)
    repo.get_by_imovel_e_cpf = MagicMock(return_value=None)
    repo.get_principal = MagicMock(return_value=None)
    repo.save = MagicMock(side_effect=lambda p: p)
    repo.list_by_imovel = MagicMock(return_value=[proprietario] if proprietario else [])
    repo.list_all = MagicMock(return_value=[proprietario] if proprietario else [])
    return repo


def repo_avaliacao(avaliacao: AvaliacaoImovel | None = None) -> MagicMock:
    """Cria um port de avaliações simulado."""
    repo = MagicMock(spec=RepositorioAvaliacao)
    repo.get_by_id = MagicMock(return_value=avaliacao)
    repo.get_by_imovel_e_ano = MagicMock(return_value=avaliacao)
    repo.save = MagicMock(side_effect=lambda a: a)
    repo.list_by_imovel = MagicMock(return_value=[avaliacao] if avaliacao else [])
    repo.list_all = MagicMock(return_value=[avaliacao] if avaliacao else [])
    return repo


def repo_caracteristica(caracteristica: CaracteristicaImovel | None = None) -> MagicMock:
    """Cria um port de características construtivas simulado."""
    repo = MagicMock(spec=RepositorioCaracteristica)
    repo.get_by_id = MagicMock(return_value=caracteristica)
    repo.get_by_imovel = MagicMock(return_value=caracteristica)
    repo.save = MagicMock(side_effect=lambda c: c)
    repo.list_by_imovel = MagicMock(return_value=[caracteristica] if caracteristica else [])
    repo.list_all = MagicMock(return_value=[caracteristica] if caracteristica else [])
    return repo


def repo_geometria(geometria: GeometriaImovel | None = None) -> MagicMock:
    """Cria um port de geometrias dos lotes simulado."""
    repo = MagicMock(spec=RepositorioGeometria)
    repo.get_by_id = MagicMock(return_value=geometria)
    repo.get_by_imovel = MagicMock(return_value=geometria)
    repo.save = MagicMock(side_effect=lambda g: g)
    repo.list_all = MagicMock(return_value=[geometria] if geometria else [])
    return repo
