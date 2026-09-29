"""Georreferência territorial do DOM-TEL.

RN-TEL-005: a georreferência exige datum suportado, coordenadas no intervalo
    do datum e vértices consistentes com o tipo de geometria informada.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import uuid4

from .tipos import (
    VERTICES_MINIMOS,
    DatumGeorreferencia,
    TipoGeometria,
    validar_coordenada,
)


@dataclass
class Georreferencia:
    """Georreferência territorial vinculada a bairro ou logradouro (RN-TEL-005)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    bairro_id: str = ""
    logradouro_id: str = ""
    geometria: TipoGeometria = field(default=TipoGeometria.PONTO)
    latitude: float = 0.0
    longitude: float = 0.0
    altitude_m: float | None = None
    vertices: list[dict[str, float]] = field(default_factory=list)
    datum: DatumGeorreferencia = field(default=DatumGeorreferencia.SIRGAS2000)
    precisao_m: float = 0.0
    data_levantamento: date = field(default_factory=date.today)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    def excluir(self) -> None:
        """Marca a georreferência como excluída (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida as regras estruturais da georreferência (RN-TEL-005)."""
        from ..exceptions import RegraNegocioError

        if not self.bairro_id and not self.logradouro_id:
            raise RegraNegocioError(
                "Georreferência deve estar vinculada a um bairro ou logradouro (RN-TEL-005)"
            )
        if self.bairro_id and self.logradouro_id:
            raise RegraNegocioError(
                "Georreferência deve estar vinculada a um bairro OU a um logradouro, "
                "não a ambos (RN-TEL-005)"
            )
        validar_coordenada(
            self.latitude, self.longitude, "Coordenada principal da georreferência"
        )

        minimo = VERTICES_MINIMOS[self.geometria]
        if len(self.vertices) < minimo:
            raise RegraNegocioError(
                f"Geometria {self.geometria.value} exige ao menos {minimo} vértice(s) "
                "(RN-TEL-005)"
            )
        for vertice in self.vertices:
            validar_coordenada(
                float(vertice.get("latitude", 0.0)),
                float(vertice.get("longitude", 0.0)),
                "Vértice da georreferência",
            )

        if self.precisao_m < 0:
            raise RegraNegocioError("Precisão da georreferência não pode ser negativa")
        if self.altitude_m is not None and not -500 <= self.altitude_m <= 9000:
            raise RegraNegocioError("Altitude informada está fora da faixa terrestre admitida")


__all__ = ["Georreferencia"]
