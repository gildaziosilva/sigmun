"""Elemento geoespacial do DOM-GEO — Geoinformação Municipal.

RN-GEO-003: o elemento exige geometria suportada dentro do datum, com vértices
    consistentes com o tipo de geometria informado.
RN-GEO-008: todo elemento geoespacial pertence a uma camada cadastrada.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from .tipos import (
    VERTICES_MINIMOS,
    DatumGeografico,
    TipoGeometria,
    validar_coordenada,
)


@dataclass
class FeatureGeo:
    """Elemento geoespacial (ponto de interesse) associate a uma camada."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    camada_id: str = ""
    geometria: TipoGeometria = field(default=TipoGeometria.PONTO)
    latitude: float = 0.0
    longitude: float = 0.0
    vertices: list[dict[str, float]] = field(default_factory=list)
    datum: DatumGeografico = field(default=DatumGeografico.SIRGAS2000)
    atributos: dict[str, object] = field(default_factory=dict)
    criado_por: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    def excluir(self) -> None:
        """Marca o elemento como excluído (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida as regras estruturais do elemento (RN-GEO-003, RN-GEO-008)."""
        from ..exceptions import RegraNegocioError

        if not self.codigo:
            raise RegraNegocioError("Código do elemento geoespacial é obrigatório")
        if not self.nome:
            raise RegraNegocioError("Nome do elemento geoespacial é obrigatório")
        if not self.camada_id:
            raise RegraNegocioError(
                "Elemento geoespacial deve estar vinculado a uma camada (RN-GEO-008)"
            )

        validar_coordenada(
            self.latitude, self.longitude, "Coordenada principal do elemento geoespacial"
        )

        minimo = VERTICES_MINIMOS[self.geometria]
        if len(self.vertices) < minimo:
            raise RegraNegocioError(
                f"Geometria {self.geometria.value} exige ao menos {minimo} vértice(s) "
                "(RN-GEO-003)"
            )
        for vertice in self.vertices:
            validar_coordenada(
                float(vertice.get("latitude", 0.0)),
                float(vertice.get("longitude", 0.0)),
                "Vértice do elemento geoespacial",
            )


__all__ = ["FeatureGeo"]
