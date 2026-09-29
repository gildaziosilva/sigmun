"""Entidades do DOM-IMO — Cadastro Imobiliário.

Regras de negócio implementadas:
- RN-IMO-001: a inscrição imobiliária é única no município.
- RN-IMO-002: o imóvel exige logradouro e bairro vinculados.
- RN-IMO-003: áreas não podem ser negativas e devem ser fisicamente coerentes.
- RN-IMO-004: a situação do imóvel obedece à máquina de estados declarada em
  `tipos.transicao_permitida`.
- RN-IMO-005: o valor venal é apurado a partir dos valores unitários vigentes
  da planta genérica de valores.
- RN-IMO-006: cada imóvel possui no máximo um proprietário titular principal e
  o CPF do titular deve ser válido.
- RN-IMO-007: a geometria do lote exige datum, coordenadas e vértices válidos.
"""

from .avaliacao import AvaliacaoImovel
from .geometria import (
    LATITUDE_MAX,
    LATITUDE_MIN,
    LONGITUDE_MAX,
    LONGITUDE_MIN,
    CaracteristicaImovel,
    GeometriaImovel,
)
from .imovel import Imovel
from .proprietario import ProprietarioImovel
from .tipos import (
    SituacaoAvaliacao,
    SituacaoImovel,
    TipoImovel,
    TipoObra,
    TipoPropriedade,
    TipoVinculo,
    transicao_permitida,
)

__all__ = [
    "LATITUDE_MIN",
    "LATITUDE_MAX",
    "LONGITUDE_MIN",
    "LONGITUDE_MAX",
    "TipoImovel",
    "SituacaoImovel",
    "TipoPropriedade",
    "TipoVinculo",
    "TipoObra",
    "SituacaoAvaliacao",
    "transicao_permitida",
    "Imovel",
    "ProprietarioImovel",
    "AvaliacaoImovel",
    "CaracteristicaImovel",
    "GeometriaImovel",
]
