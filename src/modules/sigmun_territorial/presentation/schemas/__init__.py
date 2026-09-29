"""Schemas Pydantic do DOM-TEL — Gestão Territorial."""

from .territoriais import (
    BairroCreateRequest,
    BairroResponse,
    BairroUpdateRequest,
    LogradouroCreateRequest,
    LogradouroResponse,
    LogradouroUpdateRequest,
)
from .valores_geo import (
    GeorreferenciaCreateRequest,
    GeorreferenciaResponse,
    PlantaValoresCreateRequest,
    PlantaValoresResponse,
    PlantaValoresRevogarRequest,
    PlantaValoresUpdateRequest,
    VerticeGeometria,
)

__all__ = [
    "BairroCreateRequest",
    "BairroUpdateRequest",
    "BairroResponse",
    "LogradouroCreateRequest",
    "LogradouroUpdateRequest",
    "LogradouroResponse",
    "PlantaValoresCreateRequest",
    "PlantaValoresUpdateRequest",
    "PlantaValoresRevogarRequest",
    "PlantaValoresResponse",
    "GeorreferenciaCreateRequest",
    "GeorreferenciaResponse",
    "VerticeGeometria",
]
