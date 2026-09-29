"""Schemas Pydantic do DOM-GEO — Geoinformação Municipal."""

from .camadas import (
    CamadaCreateRequest,
    CamadaResponse,
    CamadaUpdateRequest,
)
from .mapas import (
    MapaCamadaResponse,
    MapaComposicaoRequest,
    MapaComposicaoResponse,
    MapaCreateRequest,
    MapaResponse,
    MapaUpdateRequest,
)
from .servicos import (
    FeatureCreateRequest,
    FeatureResponse,
    ServicoCreateRequest,
    ServicoResponse,
    ServicoUpdateRequest,
    VerticeGeo,
)

__all__ = [
    "CamadaCreateRequest",
    "CamadaUpdateRequest",
    "CamadaResponse",
    "MapaCreateRequest",
    "MapaUpdateRequest",
    "MapaResponse",
    "MapaComposicaoRequest",
    "MapaCamadaResponse",
    "MapaComposicaoResponse",
    "FeatureCreateRequest",
    "FeatureResponse",
    "ServicoCreateRequest",
    "ServicoUpdateRequest",
    "ServicoResponse",
    "VerticeGeo",
]
