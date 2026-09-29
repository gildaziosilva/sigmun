"""Casos de uso do DOM-GEO — elementos geoespaciais (RN-GEO-003, RN-GEO-008)."""

from __future__ import annotations

from dataclasses import dataclass

from ..domain.entities import FeatureGeo
from . import interfaces as ports
from .conversores import datum, geometria


@dataclass
class RegistrarFeatureInput:
    """DTO de registro de elemento geoespacial (RN-GEO-003, RN-GEO-008)."""

    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    camada_id: str = ""
    geometria: str = "ponto"
    latitude: float = 0.0
    longitude: float = 0.0
    vertices: list[dict[str, float]] | None = None
    datum: str = "sirgas2000"
    atributos: dict[str, object] | None = None
    autor_id: str = ""


class RegistrarFeatureUseCase:
    """Registra um elemento geoespacial em uma camada cadastrada."""

    def __init__(
        self,
        repo: ports.RepositorioFeatureGeo,
        camadas: ports.RepositorioCamadaMapa,
    ) -> None:
        self._repo = repo
        self._camadas = camadas

    def execute(self, dto: RegistrarFeatureInput) -> FeatureGeo:
        """Executa o registro."""
        from ..domain.entities import SituacaoCamadaMapa
        from ..domain.exceptions import CamadaMapaNaoEncontradaError, FeatureGeoJaExistenteError

        camada = self._camadas.get_by_id(dto.camada_id)
        if camada is None:
            raise CamadaMapaNaoEncontradaError(
                "Camada não encontrada para o elemento geoespacial (RN-GEO-008)"
            )
        if camada.situacao == SituacaoCamadaMapa.DESATIVADA:
            from ..domain.exceptions import RegraNegocioError

            raise RegraNegocioError(
                "Camada desativada não recebe novos elementos geoespaciais (RN-GEO-006)"
            )
        if self._repo.get_by_codigo_camada(dto.codigo, dto.camada_id) is not None:
            raise FeatureGeoJaExistenteError(
                "Já existe elemento geoespacial com este código na camada (RN-GEO-003)"
            )

        tipo_geometria = geometria(dto.geometria)
        vertices = [dict(v) for v in (dto.vertices or [])]
        # Em geometria de ponto, o primeiro vértice é a própria coordenada
        # principal; adotá-lo evita divergência entre as duas representações.
        primeiro = vertices[0] if tipo_geometria.value == "ponto" and vertices else None
        latitude = float(primeiro["latitude"]) if primeiro else dto.latitude
        longitude = float(primeiro["longitude"]) if primeiro else dto.longitude

        feature = FeatureGeo(
            codigo=dto.codigo,
            nome=dto.nome,
            descricao=dto.descricao,
            camada_id=dto.camada_id,
            geometria=tipo_geometria,
            latitude=latitude,
            longitude=longitude,
            vertices=vertices,
            datum=datum(dto.datum),
            atributos=dict(dto.atributos or {}),
            criado_por=dto.autor_id,
            created_by=dto.autor_id,
        )
        feature.validar()
        return self._repo.save(feature)


class ExcluirFeatureUseCase:
    """Exclui (soft-delete) um elemento geoespacial."""

    def __init__(self, repo: ports.RepositorioFeatureGeo) -> None:
        self._repo = repo

    def execute(self, feature_id: str) -> FeatureGeo:
        """Executa a exclusão lógica."""
        from ..domain.exceptions import FeatureGeoNaoEncontradaError

        feature = self._repo.get_by_id(feature_id)
        if feature is None:
            raise FeatureGeoNaoEncontradaError("Elemento geoespacial não encontrado para exclusão")
        feature.excluir()
        return self._repo.save(feature)


__all__ = [
    "RegistrarFeatureInput",
    "RegistrarFeatureUseCase",
    "ExcluirFeatureUseCase",
]
