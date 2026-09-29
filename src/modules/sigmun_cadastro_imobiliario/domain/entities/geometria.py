"""Característica construtiva e geometria georreferenciada do lote (DOM-IMO).

RN-IMO-007: a geometria do lote exige datum suportado, coordenadas no intervalo
    admissível e vértices compatíveis com o tipo de geometria informada.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import uuid4

from .tipos import TipoObra

# Limites globais de latitude e longitude (RN-IMO-007).
LATITUDE_MIN = -90.0
LATITUDE_MAX = 90.0
LONGITUDE_MIN = -180.0
LONGITUDE_MAX = 180.0

_VERTICES_MINIMOS: dict[str, int] = {"ponto": 1, "linha": 2, "poligono": 3}


@dataclass
class CaracteristicaImovel:
    """Descrição da construção existente na unidade imobiliária."""

    id: str = field(default_factory=lambda: str(uuid4()))
    imovel_id: str = ""
    obra: TipoObra = field(default=TipoObra.RESIDENCIAL)
    numero_pavimentos: int = 1
    ano_renovacao: int | None = None
    observacao: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""

    def validar(self) -> None:
        """Valida as regras estruturais da característica construtiva."""
        from ..exceptions import RegraNegocioError

        if not self.imovel_id:
            raise RegraNegocioError("Característica exige imóvel vinculado")
        if self.numero_pavimentos < 1:
            raise RegraNegocioError("Número de pavimentos deve ser maior que zero")
        if self.ano_renovacao is not None and not 1800 <= self.ano_renovacao <= 2200:
            raise RegraNegocioError("Ano de renovação inválido")


@dataclass
class GeometriaImovel:
    """Geometria georreferenciada do lote (RN-IMO-007)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    imovel_id: str = ""
    geometria: str = "ponto"
    latitude: float = 0.0
    longitude: float = 0.0
    vertices: list[dict[str, float]] = field(default_factory=list)
    datum: str = "sirgas2000"
    precisao_m: float = 0.0
    data_levantamento: date = field(default_factory=date.today)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    def validar(self) -> None:
        """Valida as regras estruturais da geometria do lote (RN-IMO-007)."""
        from ..exceptions import RegraNegocioError

        if not self.imovel_id:
            raise RegraNegocioError("Geometria exige imóvel vinculado (RN-IMO-007)")
        if self.geometria not in _VERTICES_MINIMOS:
            raise RegraNegocioError(f"Tipo de geometria inválido: {self.geometria}")
        if self.datum not in ("sirgas2000", "sad69", "wgs84"):
            raise RegraNegocioError(f"Datum geodésico inválido: {self.datum} (RN-IMO-007)")

        for rotulo, latitude, longitude in [
            ("Coordenada principal da geometria", self.latitude, self.longitude),
            *[
                (
                    "Vértice da geometria",
                    float(v.get("latitude", 0.0)),
                    float(v.get("longitude", 0.0)),
                )
                for v in self.vertices
            ],
        ]:
            if not LATITUDE_MIN <= latitude <= LATITUDE_MAX:
                raise RegraNegocioError(
                    f"{rotulo} inválida: latitude fora do intervalo (RN-IMO-007)"
                )
            if not LONGITUDE_MIN <= longitude <= LONGITUDE_MAX:
                raise RegraNegocioError(
                    f"{rotulo} inválida: longitude fora do intervalo (RN-IMO-007)"
                )

        minimo = _VERTICES_MINIMOS[self.geometria]
        if len(self.vertices) < minimo:
            raise RegraNegocioError(
                f"Geometria {self.geometria} exige ao menos {minimo} vértice(s) "
                "(RN-IMO-007)"
            )
        if self.precisao_m < 0:
            raise RegraNegocioError("Precisão da geometria não pode ser negativa")

    def remover(self) -> None:
        """Marca a geometria como removida (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()


__all__ = [
    "LATITUDE_MIN",
    "LATITUDE_MAX",
    "LONGITUDE_MIN",
    "LONGITUDE_MAX",
    "CaracteristicaImovel",
    "GeometriaImovel",
]
