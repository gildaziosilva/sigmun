"""Repositórios SQLAlchemy do DOM-GEO — Geoinformação Municipal.

Reexporta as implementações concretas separadas por agregado.
"""

from .camada_mapa import SQLAlchemyCamadaMapaRepository, SQLAlchemyMapaSigRepository
from .helpers import buscar_ou_um, to_uuid
from .mapa_camada import (
    SQLAlchemyFeatureGeoRepository,
    SQLAlchemyMapaCamadaRepository,
    SQLAlchemyServicoGeoRepository,
)

__all__ = [
    "SQLAlchemyCamadaMapaRepository",
    "SQLAlchemyMapaSigRepository",
    "SQLAlchemyMapaCamadaRepository",
    "SQLAlchemyFeatureGeoRepository",
    "SQLAlchemyServicoGeoRepository",
    "to_uuid",
    "buscar_ou_um",
]
