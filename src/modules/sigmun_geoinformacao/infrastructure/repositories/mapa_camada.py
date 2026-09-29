"""Repositórios SQLAlchemy do DOM-GEO — composição, elementos e serviços."""

from __future__ import annotations

from sqlalchemy.orm import Session

from ...application.interfaces import (
    RepositorioFeatureGeo,
    RepositorioMapaCamada,
    RepositorioServicoGeo,
)
from ...domain.entities import (
    DatumGeografico,
    FeatureGeo,
    MapaCamada,
    ServicoGeo,
    SituacaoServicoGeo,
    TipoGeometria,
    TipoServicoGeo,
)
from ..database.models import FeatureGeoModel, MapaCamadaModel, ServicoGeoModel
from .helpers import buscar_ou_um, to_uuid


class SQLAlchemyMapaCamadaRepository(RepositorioMapaCamada):
    """Persistência da composição mapa ↔ camada (RN-GEO-004)."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, vinculo: MapaCamada) -> MapaCamada:
        """Insere ou atualiza um vínculo de composição."""
        existente = buscar_ou_um(self._session, MapaCamadaModel, vinculo.id)
        if existente is not None:
            existente.mapa_id = vinculo.mapa_id
            existente.camada_id = vinculo.camada_id
            existente.ordem = vinculo.ordem
            existente.opacidade = vinculo.opacidade
            existente.visivel = vinculo.visivel
            existente.rotulo = vinculo.rotulo or None
            existente.is_deleted = vinculo.is_deleted
        else:
            self._session.add(
                MapaCamadaModel(
                    id=to_uuid(vinculo.id),
                    mapa_id=vinculo.mapa_id,
                    camada_id=vinculo.camada_id,
                    ordem=vinculo.ordem,
                    opacidade=vinculo.opacidade,
                    visivel=vinculo.visivel,
                    rotulo=vinculo.rotulo or None,
                    created_at=vinculo.created_at,
                    created_by=vinculo.created_by or None,
                    is_deleted=vinculo.is_deleted,
                )
            )
        self._session.flush()
        return vinculo

    def get_by_id(self, vinculo_id: str) -> MapaCamada | None:
        """Busca vínculo de composição por id."""
        model = buscar_ou_um(self._session, MapaCamadaModel, vinculo_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_mapa_camada(self, mapa_id: str, camada_id: str) -> MapaCamada | None:
        """Busca o vínculo entre um mapa e uma camada específicos."""
        model = (
            self._session.query(MapaCamadaModel)
            .filter(
                MapaCamadaModel.mapa_id == mapa_id,
                MapaCamadaModel.camada_id == camada_id,
                MapaCamadaModel.is_deleted.is_(False),
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def list_by_mapa(self, mapa_id: str) -> list[MapaCamada]:
        """Lista as camadas que compõem um mapa."""
        models = (
            self._session.query(MapaCamadaModel)
            .filter(MapaCamadaModel.mapa_id == mapa_id, MapaCamadaModel.is_deleted.is_(False))
            .order_by(MapaCamadaModel.ordem, MapaCamadaModel.camada_id)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def list_by_camada(self, camada_id: str) -> list[MapaCamada]:
        """Lista os mapas que referenciam uma camada."""
        models = (
            self._session.query(MapaCamadaModel)
            .filter(
                MapaCamadaModel.camada_id == camada_id, MapaCamadaModel.is_deleted.is_(False)
            )
            .all()
        )
        return [self._to_entity(m) for m in models]

    def delete(self, vinculo_id: str) -> None:
        """Remove o vínculo de composição (exclusão física)."""
        model = buscar_ou_um(self._session, MapaCamadaModel, vinculo_id)
        if model is not None:
            self._session.delete(model)
            self._session.flush()

    def _to_entity(self, model: MapaCamadaModel) -> MapaCamada:
        return MapaCamada(
            id=str(model.id),
            mapa_id=model.mapa_id or "",
            camada_id=model.camada_id or "",
            ordem=int(model.ordem or 0),
            opacidade=float(model.opacidade or 100),
            visivel=bool(model.visivel),
            rotulo=model.rotulo or "",
            created_at=model.created_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


class SQLAlchemyFeatureGeoRepository(RepositorioFeatureGeo):
    """Persistência de elementos geoespaciais do geoportal."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, feature: FeatureGeo) -> FeatureGeo:
        """Insere ou atualiza um elemento geoespacial."""
        existente = buscar_ou_um(self._session, FeatureGeoModel, feature.id)
        if existente is not None:
            existente.codigo = feature.codigo
            existente.nome = feature.nome
            existente.descricao = feature.descricao or None
            existente.camada_id = feature.camada_id
            existente.geometria = feature.geometria.value
            existente.latitude = feature.latitude
            existente.longitude = feature.longitude
            existente.vertices = feature.vertices
            existente.datum = feature.datum.value
            existente.atributos = feature.atributos
            existente.updated_at = feature.updated_at
            existente.is_deleted = feature.is_deleted
        else:
            self._session.add(
                FeatureGeoModel(
                    id=to_uuid(feature.id),
                    codigo=feature.codigo,
                    nome=feature.nome,
                    descricao=feature.descricao or None,
                    camada_id=feature.camada_id,
                    geometria=feature.geometria.value,
                    latitude=feature.latitude,
                    longitude=feature.longitude,
                    vertices=feature.vertices,
                    datum=feature.datum.value,
                    atributos=feature.atributos,
                    criado_por=feature.criado_por or None,
                    created_at=feature.created_at,
                    updated_at=feature.updated_at,
                    created_by=feature.created_by or None,
                    is_deleted=feature.is_deleted,
                )
            )
        self._session.flush()
        return feature

    def get_by_id(self, feature_id: str) -> FeatureGeo | None:
        """Busca elemento geoespacial por id."""
        model = buscar_ou_um(self._session, FeatureGeoModel, feature_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_codigo_camada(self, codigo: str, camada_id: str) -> FeatureGeo | None:
        """Busca elemento geoespacial pelo código dentro da camada."""
        model = (
            self._session.query(FeatureGeoModel)
            .filter(
                FeatureGeoModel.codigo == codigo,
                FeatureGeoModel.camada_id == camada_id,
                FeatureGeoModel.is_deleted.is_(False),
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def list_by_camada(self, camada_id: str) -> list[FeatureGeo]:
        """Lista elementos geoespaciais de uma camada."""
        models = (
            self._session.query(FeatureGeoModel)
            .filter(
                FeatureGeoModel.camada_id == camada_id, FeatureGeoModel.is_deleted.is_(False)
            )
            .order_by(FeatureGeoModel.codigo)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def list_all(self, page: int = 1, page_size: int = 20) -> list[FeatureGeo]:
        """Lista elementos geoespaciais paginados."""
        models = (
            self._session.query(FeatureGeoModel)
            .filter(FeatureGeoModel.is_deleted.is_(False))
            .order_by(FeatureGeoModel.codigo)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: FeatureGeoModel) -> FeatureGeo:
        return FeatureGeo(
            id=str(model.id),
            codigo=model.codigo,
            nome=model.nome,
            descricao=model.descricao or "",
            camada_id=model.camada_id or "",
            geometria=TipoGeometria(model.geometria or "ponto"),
            latitude=float(model.latitude or 0),
            longitude=float(model.longitude or 0),
            vertices=[dict(v) for v in (model.vertices or [])],
            datum=DatumGeografico(model.datum or "sirgas2000"),
            atributos=dict(model.atributos or {}),
            criado_por=model.criado_por or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


class SQLAlchemyServicoGeoRepository(RepositorioServicoGeo):
    """Persistência de serviços geoespaciais publicados (RN-GEO-007)."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, servico: ServicoGeo) -> ServicoGeo:
        """Insere ou atualiza um serviço geoespacial."""
        existente = buscar_ou_um(self._session, ServicoGeoModel, servico.id)
        if existente is not None:
            existente.codigo = servico.codigo
            existente.nome = servico.nome
            existente.descricao = servico.descricao or None
            existente.tipo = servico.tipo.value
            existente.situacao = servico.situacao.value
            existente.url = servico.url or None
            existente.camada = servico.camada or None
            existente.datum = servico.datum.value
            existente.srid = servico.srid
            existente.zoom_minimo = servico.zoom_minimo
            existente.zoom_maximo = servico.zoom_maximo
            existente.publico = servico.publico
            existente.updated_at = servico.updated_at
            existente.is_deleted = servico.is_deleted
        else:
            self._session.add(
                ServicoGeoModel(
                    id=to_uuid(servico.id),
                    codigo=servico.codigo,
                    nome=servico.nome,
                    descricao=servico.descricao or None,
                    tipo=servico.tipo.value,
                    situacao=servico.situacao.value,
                    url=servico.url or None,
                    camada=servico.camada or None,
                    datum=servico.datum.value,
                    srid=servico.srid,
                    zoom_minimo=servico.zoom_minimo,
                    zoom_maximo=servico.zoom_maximo,
                    publico=servico.publico,
                    created_at=servico.created_at,
                    updated_at=servico.updated_at,
                    created_by=servico.created_by or None,
                    is_deleted=servico.is_deleted,
                )
            )
        self._session.flush()
        return servico

    def get_by_id(self, servico_id: str) -> ServicoGeo | None:
        """Busca serviço geoespacial por id."""
        model = buscar_ou_um(self._session, ServicoGeoModel, servico_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_codigo(self, codigo: str) -> ServicoGeo | None:
        """Busca serviço geoespacial pelo código cadastral."""
        model = (
            self._session.query(ServicoGeoModel)
            .filter(ServicoGeoModel.codigo == codigo, ServicoGeoModel.is_deleted.is_(False))
            .first()
        )
        return self._to_entity(model) if model else None

    def list_all(
        self, page: int = 1, page_size: int = 20, tipo: str | None = None
    ) -> list[ServicoGeo]:
        """Lista serviços geoespaciais paginados, opcionalmente por tipo."""
        query = self._session.query(ServicoGeoModel).filter(
            ServicoGeoModel.is_deleted.is_(False)
        )
        if tipo:
            query = query.filter(ServicoGeoModel.tipo == tipo)
        models = (
            query.order_by(ServicoGeoModel.codigo)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: ServicoGeoModel) -> ServicoGeo:
        return ServicoGeo(
            id=str(model.id),
            codigo=model.codigo,
            nome=model.nome,
            descricao=model.descricao or "",
            tipo=TipoServicoGeo(model.tipo or "wms"),
            situacao=SituacaoServicoGeo(model.situacao or "ativo"),
            url=model.url or "",
            camada=model.camada or "",
            datum=DatumGeografico(model.datum or "sirgas2000"),
            srid=int(model.srid or 4326),
            zoom_minimo=int(model.zoom_minimo or 0),
            zoom_maximo=int(model.zoom_maximo or 24),
            publico=bool(model.publico),
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = [
    "SQLAlchemyMapaCamadaRepository",
    "SQLAlchemyFeatureGeoRepository",
    "SQLAlchemyServicoGeoRepository",
]
