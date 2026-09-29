"""Router único do DOM-OBR — Obras e Infraestrutura (prefixo /api/v1/obr)."""

from fastapi import APIRouter

from ...domain.exceptions import (
    DespesaNaoEncontradaError,
    EtapaNaoEncontradaError,
    MedicaoNaoEncontradaError,
    ObraNaoEncontradaError,
    VistoriaNaoEncontradaError,
)

router = APIRouter(prefix="/api/v1/obr", tags=["Obras e Infraestrutura"])

# Exceções de "recurso referenciado inexistente", traduzidas para HTTP 404.
NAO_ENCONTRADOS = (
    ObraNaoEncontradaError,
    MedicaoNaoEncontradaError,
    EtapaNaoEncontradaError,
    DespesaNaoEncontradaError,
    VistoriaNaoEncontradaError,
)

__all__ = ["router", "NAO_ENCONTRADOS"]
