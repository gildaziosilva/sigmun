"""Entidades do DOM-GEO — Geoinformação Municipal.

Regras de negócio implementadas (ver também o docstring de cada entidade):
- RN-GEO-001: código da camada de mapa é único no geoportal municipal.
- RN-GEO-002: código do mapa SIG é único no geoportal municipal.
- RN-GEO-003: o elemento geoespacial exige geometria suportada, coordenadas no
  intervalo do datum e vértices consistentes com o tipo de geometria.
- RN-GEO-004: o mapa obedece ao ciclo RASCUNHO -> PUBLICADO -> ARQUIVADO; a
  publicação exige ao menos uma camada ativa e mapas publicados não aceitam
  nova composição de camadas.
- RN-GEO-005: extensão (bbox), SRID e níveis de zoom são validados no mapa,
  na camada e no serviço geoespacial.
- RN-GEO-006: a camada de mapa obedece ao ciclo RASCUNHO -> ATIVA -> DESATIVADA;
  camadas ativas exigem URL quando o formato é de serviço.
- RN-GEO-007: o serviço geoespacial exige URL válida, código único e parâmetros
  de publicação coerentes com o protocolo declarado.
- RN-GEO-008: todo elemento geoespacial pertence a uma camada cadastrada, e
  todo mapa publicado é composto por camadas cadastradas.
"""

from .camada_mapa import CamadaMapa
from .feature_geo import FeatureGeo
from .mapa_camada import MapaCamada
from .mapa_sig import MapaSig
from .servico_geo import ServicoGeo
from .tipos import (
    FORMATOS_REQUEREM_URL,
    LATITUDE_MAX,
    LATITUDE_MIN,
    LONGITUDE_MAX,
    LONGITUDE_MIN,
    VERTICES_MINIMOS,
    ZOOM_MAXIMO,
    ZOOM_MINIMO,
    DatumGeografico,
    FormatoCamada,
    SituacaoCamadaMapa,
    SituacaoMapaSig,
    SituacaoServicoGeo,
    TipoCamadaMapa,
    TipoGeometria,
    TipoMapaSig,
    TipoServicoGeo,
    validar_coordenada,
    validar_zoom,
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
    "CamadaMapa",
    "MapaSig",
    "MapaCamada",
    "FeatureGeo",
    "ServicoGeo",
    "validar_coordenada",
    "validar_zoom",
]
