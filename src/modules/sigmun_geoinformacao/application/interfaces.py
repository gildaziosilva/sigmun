"""Interfaces (ports) dos repositórios do DOM-GEO — Geoinformação Municipal."""

from __future__ import annotations

from typing import Protocol

from ..domain.entities import CamadaMapa, FeatureGeo, MapaCamada, MapaSig, ServicoGeo


class RepositorioCamadaMapa(Protocol):
    """Port de persistência de camadas de mapa."""

    def save(self, camada: CamadaMapa) -> CamadaMapa:
        """Persiste uma camada de mapa."""
        ...

    def get_by_id(self, camada_id: str) -> CamadaMapa | None:
        """Busca camada de mapa por id."""
        ...

    def get_by_codigo(self, codigo: str) -> CamadaMapa | None:
        """Busca camada de mapa pelo código cadastral."""
        ...

    def list_all(
        self, page: int = 1, page_size: int = 20, tipo: str | None = None
    ) -> list[CamadaMapa]:
        """Lista camadas de mapa paginadas, opcionalmente por tipo."""
        ...


class RepositorioMapaSig(Protocol):
    """Port de persistência de mapas SIG."""

    def save(self, mapa: MapaSig) -> MapaSig:
        """Persiste um mapa SIG."""
        ...

    def get_by_id(self, mapa_id: str) -> MapaSig | None:
        """Busca mapa SIG por id."""
        ...

    def get_by_codigo(self, codigo: str) -> MapaSig | None:
        """Busca mapa SIG pelo código cadastral."""
        ...

    def list_all(
        self, page: int = 1, page_size: int = 20, situacao: str | None = None
    ) -> list[MapaSig]:
        """Lista mapas SIG paginados, opcionalmente por situação."""
        ...


class RepositorioMapaCamada(Protocol):
    """Port de persistência da composição mapa ↔ camada."""

    def save(self, vinculo: MapaCamada) -> MapaCamada:
        """Persiste um vínculo de composição."""
        ...

    def get_by_id(self, vinculo_id: str) -> MapaCamada | None:
        """Busca vínculo de composição por id."""
        ...

    def get_by_mapa_camada(self, mapa_id: str, camada_id: str) -> MapaCamada | None:
        """Busca o vínculo entre um mapa e uma camada específicos."""
        ...

    def list_by_mapa(self, mapa_id: str) -> list[MapaCamada]:
        """Lista as camadas que compõem um mapa."""
        ...

    def list_by_camada(self, camada_id: str) -> list[MapaCamada]:
        """Lista os mapas que referenciam uma camada."""
        ...

    def delete(self, vinculo_id: str) -> None:
        """Remove o vínculo de composição."""
        ...


class RepositorioFeatureGeo(Protocol):
    """Port de persistência de elementos geoespaciais."""

    def save(self, feature: FeatureGeo) -> FeatureGeo:
        """Persiste um elemento geoespacial."""
        ...

    def get_by_id(self, feature_id: str) -> FeatureGeo | None:
        """Busca elemento geoespacial por id."""
        ...

    def get_by_codigo_camada(self, codigo: str, camada_id: str) -> FeatureGeo | None:
        """Busca elemento geoespacial pelo código dentro da camada."""
        ...

    def list_by_camada(self, camada_id: str) -> list[FeatureGeo]:
        """Lista elementos geoespaciais de uma camada."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list[FeatureGeo]:
        """Lista elementos geoespaciais paginados."""
        ...


class RepositorioServicoGeo(Protocol):
    """Port de persistência de serviços geoespaciais."""

    def save(self, servico: ServicoGeo) -> ServicoGeo:
        """Persiste um serviço geoespacial."""
        ...

    def get_by_id(self, servico_id: str) -> ServicoGeo | None:
        """Busca serviço geoespacial por id."""
        ...

    def get_by_codigo(self, codigo: str) -> ServicoGeo | None:
        """Busca serviço geoespacial pelo código cadastral."""
        ...

    def list_all(
        self, page: int = 1, page_size: int = 20, tipo: str | None = None
    ) -> list[ServicoGeo]:
        """Lista serviços geoespaciais paginados, opcionalmente por tipo."""
        ...


__all__ = [
    "RepositorioCamadaMapa",
    "RepositorioMapaSig",
    "RepositorioMapaCamada",
    "RepositorioFeatureGeo",
    "RepositorioServicoGeo",
]
