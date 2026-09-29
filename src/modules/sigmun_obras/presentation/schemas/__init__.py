"""Schemas Pydantic do DOM-OBR — Obras e Infraestrutura."""

from .acompanhamento import (
    DespesaCreateRequest,
    DespesaResponse,
    EtapaCreateRequest,
    EtapaResponse,
    EtapaUpdateRequest,
    MedicaoCreateRequest,
    MedicaoGlosaRequest,
    MedicaoResponse,
    ObraDetalheResponse,
    VistoriaCreateRequest,
    VistoriaResponse,
)
from .obras import ObraAcaoRequest, ObraCreateRequest, ObraResponse, ObraUpdateRequest

__all__ = [
    "ObraCreateRequest",
    "ObraUpdateRequest",
    "ObraResponse",
    "ObraAcaoRequest",
    "MedicaoCreateRequest",
    "MedicaoGlosaRequest",
    "MedicaoResponse",
    "DespesaCreateRequest",
    "DespesaResponse",
    "EtapaCreateRequest",
    "EtapaUpdateRequest",
    "EtapaResponse",
    "VistoriaCreateRequest",
    "VistoriaResponse",
    "ObraDetalheResponse",
]
