"""Schemas Pydantic do DOM-IMO — Cadastro Imobiliário."""

from .avaliacoes import (
    AvaliacaoCancelarRequest,
    AvaliacaoCreateRequest,
    AvaliacaoResponse,
    CaracteristicaCreateRequest,
    CaracteristicaResponse,
    GeometriaCreateRequest,
    GeometriaResponse,
    VerticeGeometria,
)
from .imoveis import (
    ImovelCreateRequest,
    ImovelResponse,
    ImovelSituacaoRequest,
    ImovelUpdateRequest,
    ProprietarioCreateRequest,
    ProprietarioResponse,
)

__all__ = [
    "ImovelCreateRequest",
    "ImovelUpdateRequest",
    "ImovelSituacaoRequest",
    "ImovelResponse",
    "ProprietarioCreateRequest",
    "ProprietarioResponse",
    "AvaliacaoCreateRequest",
    "AvaliacaoCancelarRequest",
    "AvaliacaoResponse",
    "CaracteristicaCreateRequest",
    "CaracteristicaResponse",
    "GeometriaCreateRequest",
    "GeometriaResponse",
    "VerticeGeometria",
]
