"""Dados demonstrativos (DEMO) do DOM-GEO — Geoinformação Municipal.

Os registros aqui definidos são FICTÍCIOS, criados apenas para demonstrar as
telas administrativas. Não representam cadastro real de camadas, mapas ou
serviços do Município de Camacan-BA.

Classificação da Informação: Pública
Responsável: Equipe SIGMUN
Status da revisão: Vigente
"""

from __future__ import annotations

from dataclasses import dataclass

AUTOR_SEED = "seed-geo"


@dataclass(frozen=True)
class CamadaSeed:
    """Camada cartográfica a ser criada."""

    codigo: str
    nome: str
    descricao: str
    tipo: str
    formato: str
    fonte: str
    url_servico: str
    ativar: bool


CAMADAS_DEMO: tuple[CamadaSeed, ...] = (
    CamadaSeed(
        "CAM-ORTO-2025",
        "Ortofoto municipal 2025",
        "Ortofoto area urbana do sede, resolucao 0,20 m/pixel.",
        "ortofoto",
        "wms",
        "Prefeitura Municipal",
        "https://geoportal.exemplo.gov.br/geo/ortofoto",
        True,
    ),
    CamadaSeed(
        "CAM-HIPSO",
        "Hipsometria",
        "Modelo digital de elevacao com curvas de nivel de 10 m.",
        "hipsometria",
        "geotiff",
        "IBGE",
        "",
        True,
    ),
    CamadaSeed(
        "CAM-HIDRO",
        "Hidrografia",
        "Cursos d'agua, lagoas e reservatorios do municipio.",
        "hidrografia",
        "geojson",
        "IBGE",
        "",
        True,
    ),
    CamadaSeed(
        "CAM-USO-SOLO",
        "Uso do solo",
        "Classificacao de uso do solo vigente no Plano Diretor.",
        "uso_solo",
        "postgis",
        "Prefeitura Municipal",
        "",
        True,
    ),
    CamadaSeed(
        "CAM-CAD-TERR",
        "Cadastro territorial",
        "Malha de setores censitarios e malha de bairros.",
        "cadastro_territorial",
        "shapefile",
        "IBGE",
        "",
        True,
    ),
    CamadaSeed(
        "CAM-INFRA",
        "Infraestrutura urbana",
        "Rede de agua, esgoto e energia. Camada em preparo, ainda nao publicada.",
        "infraestrutura",
        "postgis",
        "Prefeitura Municipal",
        "",
        False,
    ),
)


@dataclass(frozen=True)
class MapaSeed:
    """Mapa SIG a ser criado."""

    codigo: str
    nome: str
    descricao: str
    tipo: str
    escala: int
    camadas: tuple[str, ...]
    publicar: bool


MAPAS_DEMO: tuple[MapaSeed, ...] = (
    MapaSeed(
        "MAP-USO-SOLO",
        "Mapa de uso do solo",
        "Coberto do solo conforme o Plano Diretor Municipal.",
        "tematico",
        25_000,
        ("CAM-ORTO-2025", "CAM-USO-SOLO"),
        True,
    ),
    MapaSeed(
        "MAP-HIDROGRAFIA",
        "Mapa de hidrografia",
        "Rede hidrografica e areas de preservacao.",
        "ambiental",
        50_000,
        ("CAM-HIPSO", "CAM-HIDRO"),
        True,
    ),
    MapaSeed(
        "MAP-CADASTRO",
        "Mapa cadastral municipal",
        "Sedes, lotes e malha urbana para consulta publica.",
        "cadastral",
        5_000,
        ("CAM-CAD-TERR",),
        False,
    ),
)


@dataclass(frozen=True)
class FeatureSeed:
    """Elemento geoespacial a ser criado."""

    codigo: str
    nome: str
    descricao: str
    camada_codigo: str
    geometria: str
    latitude: float
    longitude: float


FEATURES_DEMO: tuple[FeatureSeed, ...] = (
    FeatureSeed(
        "PT-PREFEITURA",
        "Prefeitura Municipal",
        "Paaco central do municipio.",
        "CAM-USO-SOLO",
        "ponto",
        -13.1289,
        -39.4906,
    ),
    FeatureSeed(
        "PT-PRACA-MATRIZ",
        "Praca da Matriz",
        "Praca central com area verde para convivencia.",
        "CAM-USO-SOLO",
        "ponto",
        -13.1301,
        -39.4912,
    ),
    FeatureSeed(
        "PT-PARQUE",
        "Parque Municipal",
        "Area de lazer e preservacao urbana.",
        "CAM-HIDRO",
        "ponto",
        -13.1345,
        -39.4975,
    ),
    FeatureSeed(
        "PT-CEMITERIO",
        "Cemiterio Municipal",
        "Cemiterio da cidade.",
        "CAM-USO-SOLO",
        "ponto",
        -13.1225,
        -39.4832,
    ),
)


@dataclass(frozen=True)
class ServicoSeed:
    """Serviço geoespacial a ser criado."""

    codigo: str
    nome: str
    descricao: str
    tipo: str
    url: str
    camada: str


SERVICOS_DEMO: tuple[ServicoSeed, ...] = (
    ServicoSeed(
        "WMS-ORTOFOTO",
        "WMS de ortofoto",
        "Servico de consulta de ortofoto municipal.",
        "wms",
        "https://geoportal.exemplo.gov.br/geoserver/wms",
        "sigmun:ortofoto_2025",
    ),
    ServicoSeed(
        "WMS-ORTOFOTO-XYZ",
        "Basemap de imagens (XYZ)",
        "Servico de tiles para o visor web.",
        "xyz",
        "https://geoportal.exemplo.gov.br/tiles/{z}/{x}/{y}.png",
        "",
    ),
)
