"""Enumerations e validações geográficas compartilhadas do DOM-GEO.

Concentradas em módulo próprio para evitar duplicação entre as entidades
`CamadaMapa`, `MapaSig`, `FeatureGeo` e `ServicoGeo`.
"""

from __future__ import annotations

from enum import Enum

# Limites globais de latitude e longitude (RN-GEO-003).
LATITUDE_MIN = -90.0
LATITUDE_MAX = 90.0
LONGITUDE_MIN = -180.0
LONGITUDE_MAX = 180.0

# Faixas de zoom aceitas pelos visores SIG (RN-GEO-005).
ZOOM_MINIMO = 0
ZOOM_MAXIMO = 24


class DatumGeografico(Enum):
    """Datums geodésicos aceitos no cadastro municipal."""

    SIRGAS2000 = "sirgas2000"
    SAD69 = "sad69"
    WGS84 = "wgs84"


class TipoGeometria(Enum):
    """Geometria representada por um elemento geoespacial (RN-GEO-003)."""

    PONTO = "ponto"
    LINHA = "linha"
    POLIGONO = "poligono"


class TipoCamadaMapa(Enum):
    """Espécie de camada que compõe um mapa SIG."""

    ORTOFOTO = "ortofoto"
    HIPSOMETRIA = "hipsometria"
    HIPSOGRAFIA = "hipsografia"
    TOPOGRAFIA = "topografia"
    HIDROGRAFIA = "hidrografia"
    USO_SOLO = "uso_solo"
    VEGETACAO = "vegetacao"
    MALHA_URBANA = "malha_urbana"
    INFRAESTRUTURA = "infraestrutura"
    CADASTRO_TERRITORIAL = "cadastro_territorial"
    OUTRO = "outro"


class FormatoCamada(Enum):
    """Formato técnico de armazenamento ou publicação da camada."""

    GEOTIFF = "geotiff"
    SHAPEFILE = "shapefile"
    GEOJSON = "geojson"
    KML = "kml"
    POSTGIS = "postgis"
    WMS = "wms"
    WFS = "wfs"
    WMTS = "wmts"
    XYZ = "xyz"
    VETORIAL = "vetorial"


class SituacaoCamadaMapa(Enum):
    """Ciclo de vida da camada de mapa (RN-GEO-006)."""

    RASCUNHO = "rascunho"
    ATIVA = "ativa"
    DESATIVADA = "desativada"


class TipoMapaSig(Enum):
    """Finalidade do mapa publicado no geoportal municipal."""

    TEMATICO = "tematico"
    CADASTRAL = "cadastral"
    BASEMAP = "basemap"
    INFRAESTRUTURA = "infraestrutura"
    AMBIENTAL = "ambiental"
    OUTRO = "outro"


class SituacaoMapaSig(Enum):
    """Ciclo de vida do mapa SIG (RN-GEO-004)."""

    RASCUNHO = "rascunho"
    PUBLICADO = "publicado"
    ARQUIVADO = "arquivado"


class TipoServicoGeo(Enum):
    """Protocolo do serviço geoespacial publicado (RN-GEO-007)."""

    WMS = "wms"
    WFS = "wfs"
    WMTS = "wmts"
    XYZ = "xyz"
    REST = "rest"


class SituacaoServicoGeo(Enum):
    """Situação operacional do serviço geoespacial."""

    ATIVO = "ativo"
    INATIVO = "inativo"
    MANUTENCAO = "manutencao"


# Quantidade mínima de vértices por tipo de geometria (RN-GEO-003).
VERTICES_MINIMOS: dict[TipoGeometria, int] = {
    TipoGeometria.PONTO: 1,
    TipoGeometria.LINHA: 2,
    TipoGeometria.POLIGONO: 3,
}

# Formatos de camada que exigem URL de serviço para publicação (RN-GEO-006).
FORMATOS_REQUEREM_URL: frozenset[FormatoCamada] = frozenset(
    {FormatoCamada.WMS, FormatoCamada.WFS, FormatoCamada.XYZ, FormatoCamada.WMTS}
)


def validar_coordenada(latitude: float, longitude: float, rotulo: str) -> None:
    """Valida a faixa de latitude/longitude de uma coordenada (RN-GEO-003)."""
    from ..exceptions import RegraNegocioError

    if not LATITUDE_MIN <= latitude <= LATITUDE_MAX:
        raise RegraNegocioError(
            f"{rotulo}: latitude deve estar entre {LATITUDE_MIN} e {LATITUDE_MAX} "
            "(RN-GEO-003)"
        )
    if not LONGITUDE_MIN <= longitude <= LONGITUDE_MAX:
        raise RegraNegocioError(
            f"{rotulo}: longitude deve estar entre {LONGITUDE_MIN} e {LONGITUDE_MAX} "
            "(RN-GEO-003)"
        )


def validar_zoom(zoom: int, rotulo: str) -> None:
    """Valida a faixa de zoom de um visor SIG (RN-GEO-005)."""
    from ..exceptions import RegraNegocioError

    if not ZOOM_MINIMO <= zoom <= ZOOM_MAXIMO:
        raise RegraNegocioError(
            f"{rotulo}: zoom deve estar entre {ZOOM_MINIMO} e {ZOOM_MAXIMO} (RN-GEO-005)"
        )


__all__ = [
    "LATITUDE_MIN",
    "LATITUDE_MAX",
    "LONGITUDE_MIN",
    "LONGITUDE_MAX",
    "ZOOM_MINIMO",
    "ZOOM_MAXIMO",
    "VERTICES_MINIMOS",
    "FORMATOS_REQUEREM_URL",
    "DatumGeografico",
    "TipoGeometria",
    "TipoCamadaMapa",
    "FormatoCamada",
    "SituacaoCamadaMapa",
    "TipoMapaSig",
    "SituacaoMapaSig",
    "TipoServicoGeo",
    "SituacaoServicoGeo",
    "validar_coordenada",
    "validar_zoom",
]
