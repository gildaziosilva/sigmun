"""Router único do DOM-GEO — Geoinformação Municipal (prefixo /api/v1/geo)."""

from fastapi import APIRouter

from ...domain.exceptions import (
    CamadaMapaNaoEncontradaError,
    FeatureGeoNaoEncontradaError,
    MapaSigNaoEncontradoError,
    ServicoGeoNaoEncontradoError,
)

router = APIRouter(prefix="/api/v1/geo", tags=["Geoinformação Municipal"])

# Exceções de "recurso referenciado inexistente", traduzidas para HTTP 404.
NAO_ENCONTRADOS = (
    CamadaMapaNaoEncontradaError,
    MapaSigNaoEncontradoError,
    FeatureGeoNaoEncontradaError,
    ServicoGeoNaoEncontradoError,
)

__all__ = ["router", "NAO_ENCONTRADOS"]
