"""Enumerations e validações geográficas compartilhadas do DOM-TEL.

Concentradas em módulo próprio para evitar duplicação entre as entidades
`Bairro`, `Logradouro`, `PlantaGenericaValores` e `Georreferencia`.
"""

from __future__ import annotations

from enum import Enum

# Limites globais de latitude e longitude (RN-TEL-005).
LATITUDE_MIN = -90.0
LATITUDE_MAX = 90.0
LONGITUDE_MIN = -180.0
LONGITUDE_MAX = 180.0


class TipoBairro(Enum):
    """Espécie de divisão territorial."""

    BAIRRO = "bairro"
    DISTRITO = "distrito"
    SETOR = "setor"
    ZONA_RURAL = "zona_rural"


class SituacaoBairro(Enum):
    """Situação cadastral da divisão territorial."""

    ATIVO = "ativo"
    INATIVO = "inativo"


class TipoLogradouro(Enum):
    """Classificação do logradouro público."""

    RUA = "rua"
    AVENIDA = "avenida"
    TRAVESSA = "travessa"
    PRACA = "praca"
    RODOVIA = "rodovia"
    ESTRADA = "estrada"
    ALAMEDA = "alameda"
    PARQUE = "parque"
    OUTRO = "outro"


class SituacaoLogradouro(Enum):
    """Situação cadastral do logradouro."""

    ATIVO = "ativo"
    INATIVO = "inativo"
    EM_OBRA = "em_obra"


class TipoOcupacaoImovel(Enum):
    """Segmento de ocupação usado na planta genérica de valores."""

    RESIDENCIAL = "residencial"
    COMERCIAL = "comercial"
    INDUSTRIAL = "industrial"
    INSTITUCIONAL = "institucional"
    MISTO = "misto"
    TERRENO = "terreno"


class SituacaoPlantaValores(Enum):
    """Ciclo de vida da planta genérica de valores (RN-TEL-004)."""

    RASCUNHO = "rascunho"
    VIGENTE = "vigente"
    REVOGADA = "revogada"


class DatumGeorreferencia(Enum):
    """Datums geodésicos aceitos no cadastro municipal."""

    SIRGAS2000 = "sirgas2000"
    SAD69 = "sad69"
    WGS84 = "wgs84"


class TipoGeometria(Enum):
    """Geometria representada pela georreferência."""

    PONTO = "ponto"
    LINHA = "linha"
    POLIGONO = "poligono"


# Quantidade mínima de vértices por tipo de geometria (RN-TEL-005).
VERTICES_MINIMOS: dict[TipoGeometria, int] = {
    TipoGeometria.PONTO: 1,
    TipoGeometria.LINHA: 2,
    TipoGeometria.POLIGONO: 3,
}


def validar_coordenada(latitude: float, longitude: float, rotulo: str) -> None:
    """Valida a faixa de latitude/longitude de uma coordenada (RN-TEL-005)."""
    from ..exceptions import RegraNegocioError

    if not LATITUDE_MIN <= latitude <= LATITUDE_MAX:
        raise RegraNegocioError(
            f"{rotulo}: latitude deve estar entre {LATITUDE_MIN} e {LATITUDE_MAX} "
            "(RN-TEL-005)"
        )
    if not LONGITUDE_MIN <= longitude <= LONGITUDE_MAX:
        raise RegraNegocioError(
            f"{rotulo}: longitude deve estar entre {LONGITUDE_MIN} e {LONGITUDE_MAX} "
            "(RN-TEL-005)"
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
    "validar_coordenada",
]
