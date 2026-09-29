"""Router único do DOM-IMO — Cadastro Imobiliário (prefixo /api/v1/imo)."""

from fastapi import APIRouter

from ...domain.exceptions import (
    AvaliacaoNaoEncontradaError,
    CaracteristicaNaoEncontradaError,
    GeometriaNaoEncontradaError,
    ImovelNaoEncontradoError,
    ProprietarioNaoEncontradoError,
)

router = APIRouter(prefix="/api/v1/imo", tags=["Cadastro Imobiliário"])

# Exceções de "recurso inexistente", traduzidas para HTTP 404.
NAO_ENCONTRADOS = (
    ImovelNaoEncontradoError,
    ProprietarioNaoEncontradoError,
    AvaliacaoNaoEncontradaError,
    CaracteristicaNaoEncontradaError,
    GeometriaNaoEncontradaError,
)

__all__ = ["router", "NAO_ENCONTRADOS"]
