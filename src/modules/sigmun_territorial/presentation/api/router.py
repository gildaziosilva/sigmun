"""Router único do DOM-TEL — Gestão Territorial (prefixo /api/v1/tel)."""

from fastapi import APIRouter

from ...domain.exceptions import (
    BairroNaoEncontradoError,
    GeorreferenciaNaoEncontradaError,
    LogradouroNaoEncontradoError,
    PlantaValoresNaoEncontradaError,
)

router = APIRouter(prefix="/api/v1/tel", tags=["Gestão Territorial"])

# Exceções de "recurso referenciado inexistente", traduzidas para HTTP 404.
NAO_ENCONTRADOS = (
    BairroNaoEncontradoError,
    LogradouroNaoEncontradoError,
    PlantaValoresNaoEncontradaError,
    GeorreferenciaNaoEncontradaError,
)

__all__ = ["router", "NAO_ENCONTRADOS"]
