"""Dependências e conversores compartilhados pelos endpoints do DOM-GEO."""

from __future__ import annotations

from typing import Annotated, Any, Protocol

from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db

from ...application.interfaces import (
    RepositorioCamadaMapa,
    RepositorioFeatureGeo,
    RepositorioMapaCamada,
    RepositorioMapaSig,
    RepositorioServicoGeo,
)
from ...domain.entities import (
    CamadaMapa,
    FeatureGeo,
    MapaCamada,
    MapaSig,
    ServicoGeo,
)
from ...infrastructure.repositories import (
    SQLAlchemyCamadaMapaRepository,
    SQLAlchemyFeatureGeoRepository,
    SQLAlchemyMapaCamadaRepository,
    SQLAlchemyMapaSigRepository,
    SQLAlchemyServicoGeoRepository,
)
from ..schemas import (
    CamadaResponse,
    FeatureResponse,
    MapaCamadaResponse,
    MapaResponse,
    ServicoResponse,
    VerticeGeo,
)


class RepoComId(Protocol):
    """Port mínimo com busca por identificador."""

    def get_by_id(self, entidade_id: str) -> Any:
        """Busca a entidade pelo identificador."""
        ...


def get_camada_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioCamadaMapa:
    """Fornece o port de camadas de mapa."""
    return SQLAlchemyCamadaMapaRepository(session)


def get_mapa_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioMapaSig:
    """Fornece o port de mapas SIG."""
    return SQLAlchemyMapaSigRepository(session)


def get_vinculo_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioMapaCamada:
    """Fornece o port de composição mapa ↔ camada."""
    return SQLAlchemyMapaCamadaRepository(session)


def get_feature_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioFeatureGeo:
    """Fornece o port de elementos geoespaciais."""
    return SQLAlchemyFeatureGeoRepository(session)


def get_servico_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioServicoGeo:
    """Fornece o port de serviços geoespaciais."""
    return SQLAlchemyServicoGeoRepository(session)


def obter(repo: RepoComId, entidade_id: str) -> Any:
    """Busca por id tolerando UUID malformado (evita 500 em input inválido)."""
    try:
        return repo.get_by_id(entidade_id)
    except (ValueError, AttributeError):
        return None


def to_camada(c: CamadaMapa) -> CamadaResponse:
    """Converte a entidade de camada na resposta da API."""
    return CamadaResponse(
        id=c.id,
        codigo=c.codigo,
        nome=c.nome,
        descricao=c.descricao,
        tipo=c.tipo.value,
        formato=c.formato.value,
        fonte=c.fonte,
        data_atualizacao=c.data_atualizacao,
        datum=c.datum.value,
        srid=c.srid,
        url_servico=c.url_servico,
        zoom_minimo=c.zoom_minimo,
        zoom_maximo=c.zoom_maximo,
        visivel=c.visivel,
        situacao=c.situacao.value,
        created_at=c.created_at,
        updated_at=c.updated_at,
    )


def to_mapa(m: MapaSig) -> MapaResponse:
    """Converte a entidade de mapa na resposta da API."""
    return MapaResponse(
        id=m.id,
        codigo=m.codigo,
        nome=m.nome,
        descricao=m.descricao,
        tipo=m.tipo.value,
        situacao=m.situacao.value,
        datum=m.datum.value,
        srid=m.srid,
        escala_denominador=m.escala_denominador,
        zoom_inicial=m.zoom_inicial,
        zoom_minimo=m.zoom_minimo,
        zoom_maximo=m.zoom_maximo,
        lat_min=m.lat_min,
        lon_min=m.lon_min,
        lat_max=m.lat_max,
        lon_max=m.lon_max,
        publicado_em=m.publicado_em,
        criado_por=m.criado_por,
        created_at=m.created_at,
        updated_at=m.updated_at,
    )


def to_vinculo(v: MapaCamada) -> MapaCamadaResponse:
    """Converte o vínculo de composição na resposta da API."""
    return MapaCamadaResponse(
        id=v.id,
        mapa_id=v.mapa_id,
        camada_id=v.camada_id,
        ordem=v.ordem,
        opacidade=v.opacidade,
        visivel=v.visivel,
        rotulo=v.rotulo,
        created_at=v.created_at,
    )


def to_feature(f: FeatureGeo) -> FeatureResponse:
    """Converte a entidade de elemento geoespacial na resposta da API."""
    return FeatureResponse(
        id=f.id,
        codigo=f.codigo,
        nome=f.nome,
        descricao=f.descricao,
        camada_id=f.camada_id,
        geometria=f.geometria.value,
        latitude=f.latitude,
        longitude=f.longitude,
        vertices=[VerticeGeo(**v) for v in f.vertices],
        datum=f.datum.value,
        atributos=f.atributos,
        criado_por=f.criado_por,
        created_at=f.created_at,
        updated_at=f.updated_at,
    )


def to_servico(s: ServicoGeo) -> ServicoResponse:
    """Converte a entidade de serviço geoespacial na resposta da API."""
    return ServicoResponse(
        id=s.id,
        codigo=s.codigo,
        nome=s.nome,
        descricao=s.descricao,
        tipo=s.tipo.value,
        situacao=s.situacao.value,
        url=s.url,
        camada=s.camada,
        datum=s.datum.value,
        srid=s.srid,
        zoom_minimo=s.zoom_minimo,
        zoom_maximo=s.zoom_maximo,
        publico=s.publico,
        created_at=s.created_at,
        updated_at=s.updated_at,
    )


__all__ = [
    "get_camada_repo",
    "get_mapa_repo",
    "get_vinculo_repo",
    "get_feature_repo",
    "get_servico_repo",
    "obter",
    "to_camada",
    "to_mapa",
    "to_vinculo",
    "to_feature",
    "to_servico",
]
