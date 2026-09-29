"""Entidades do DOM-TEL — Gestão Territorial.

Regras de negócio implementadas (ver também o docstring de cada entidade):
- RN-TEL-001: código do bairro é único no cadastro territorial municipal.
- RN-TEL-002: código do logradouro é único e todo logradouro pertence a um
  bairro cadastrado.
- RN-TEL-003: existe no máximo uma planta genérica de valores vigente por
  combinação de ano, bairro e tipo de ocupação.
- RN-TEL-004: a planta genérica de valores obedece ao ciclo
  RASCUNHO -> VIGENTE -> REVOGADA, sem retorno a partir de REVOGADA.
- RN-TEL-005: a georreferência exige datum suportado, coordenadas no intervalo
  do datum e vértices consistentes com o tipo de geometria informada.
- RN-TEL-006: bairro com logradouros ativos não pode ser excluído.
"""

from .bairro import Bairro
from .georreferencia import Georreferencia
from .logradouro import Logradouro
from .planta_valores import PlantaGenericaValores
from .tipos import (
    LATITUDE_MAX,
    LATITUDE_MIN,
    LONGITUDE_MAX,
    LONGITUDE_MIN,
    VERTICES_MINIMOS,
    DatumGeorreferencia,
    SituacaoBairro,
    SituacaoLogradouro,
    SituacaoPlantaValores,
    TipoBairro,
    TipoGeometria,
    TipoLogradouro,
    TipoOcupacaoImovel,
    validar_coordenada,
)

__all__ = [
    "LATITUDE_MIN",
    "LATITUDE_MAX",
    "LONGITUDE_MIN",
    "LONGITUDE_MAX",
    "VERTICES_MINIMOS",
    "TipoBairro",
    "SituacaoBairro",
    "TipoLogradouro",
    "SituacaoLogradouro",
    "TipoOcupacaoImovel",
    "SituacaoPlantaValores",
    "DatumGeorreferencia",
    "TipoGeometria",
    "Bairro",
    "Logradouro",
    "PlantaGenericaValores",
    "Georreferencia",
    "validar_coordenada",
]
