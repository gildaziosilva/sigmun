"""Repositórios SQLAlchemy do DOM-GEO — camadas de mapa e mapas SIG."""

from __future__ import annotations

from datetime import date

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioCamadaMapa, RepositorioMapaSig
from ...domain.entities import (
    CamadaMapa,
    DatumGeografico,
    FormatoCamada,
    MapaSig,
    SituacaoCamadaMapa,
    SituacaoMapaSig,
    TipoCamadaMapa,
    TipoMapaSig,
)
from ..database.models import CamadaMapaModel, MapaSigModel
from .helpers import buscar_ou_um, to_uuid


class SQLAlchemyCamadaMapaRepository(RepositorioCamadaMapa):
    """Persistência de camadas cartográficas do geoportal."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, camada: CamadaMapa) -> CamadaMapa:
        """Insere ou atualiza uma camada de mapa."""
        existente = buscar_ou_um(self._session, CamadaMapaModel, camada.id)
        if existente is not None:
            existente.codigo = camada.codigo
            existente.nome = camada.nome
            existente.descricao = camada.descricao or None
            existente.tipo = camada.tipo.value
            existente.formato = camada.formato.value
            existente.fonte = camada.fonte or None
            existente.data_atualizacao = camada.data_atualizacao
            existente.datum = camada.datum.value
            existente.srid = camada.srid
            existente.url_servico = camada.url_servico or None
            existente.zoom_minimo = camada.zoom_minimo
            existente.zoom_maximo = camada.zoom_maximo
            existente.visivel = camada.visivel
            existente.situacao = camada.situacao.value
            existente.updated_at = camada.updated_at
            existente.is_deleted = camada.is_deleted
        else:
            self._session.add(
                CamadaMapaModel(
                    id=to_uuid(camada.id),
                    codigo=camada.codigo,
                    nome=camada.nome,
                    descricao=camada.descricao or None,
                    tipo=camada.tipo.value,
                    formato=camada.formato.value,
                    fonte=camada.fonte or None,
                    data_atualizacao=camada.data_atualizacao,
                    datum=camada.datum.value,
                    srid=camada.srid,
                    url_servico=camada.url_servico or None,
                    zoom_minimo=camada.zoom_minimo,
                    zoom_maximo=camada.zoom_maximo,
                    visivel=camada.visivel,
                    situacao=camada.situacao.value,
                    created_at=camada.created_at,
                    updated_at=camada.updated_at,
                    created_by=camada.created_by or None,
                    is_deleted=camada.is_deleted,
                )
            )
        self._session.flush()
        return camada

    def get_by_id(self, camada_id: str) -> CamadaMapa | None:
        """Busca camada de mapa por id."""
        model = buscar_ou_um(self._session, CamadaMapaModel, camada_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_codigo(self, codigo: str) -> CamadaMapa | None:
        """Busca camada de mapa pelo código cadastral."""
        model = (
            self._session.query(CamadaMapaModel)
            .filter(CamadaMapaModel.codigo == codigo, CamadaMapaModel.is_deleted.is_(False))
            .first()
        )
        return self._to_entity(model) if model else None

    def list_all(
        self, page: int = 1, page_size: int = 20, tipo: str | None = None
    ) -> list[CamadaMapa]:
        """Lista camadas de mapa paginadas, opcionalmente por tipo."""
        query = self._session.query(CamadaMapaModel).filter(
            CamadaMapaModel.is_deleted.is_(False)
        )
        if tipo:
            query = query.filter(CamadaMapaModel.tipo == tipo)
        models = (
            query.order_by(CamadaMapaModel.codigo)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: CamadaMapaModel) -> CamadaMapa:
        return CamadaMapa(
            id=str(model.id),
            codigo=model.codigo,
            nome=model.nome,
            descricao=model.descricao or "",
            tipo=TipoCamadaMapa(model.tipo or "outro"),
            formato=FormatoCamada(model.formato or "geojson"),
            fonte=model.fonte or "",
            data_atualizacao=model.data_atualizacao or date.today(),
            datum=DatumGeografico(model.datum or "sirgas2000"),
            srid=int(model.srid or 4326),
            url_servico=model.url_servico or "",
            zoom_minimo=int(model.zoom_minimo or 0),
            zoom_maximo=int(model.zoom_maximo or 24),
            visivel=bool(model.visivel),
            situacao=SituacaoCamadaMapa(model.situacao or "rascunho"),
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


class SQLAlchemyMapaSigRepository(RepositorioMapaSig):
    """Persistência de mapas SIG do geoportal municipal."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, mapa: MapaSig) -> MapaSig:
        """Insere ou atualiza um mapa SIG."""
        existente = buscar_ou_um(self._session, MapaSigModel, mapa.id)
        if existente is not None:
            existente.codigo = mapa.codigo
            existente.nome = mapa.nome
            existente.descricao = mapa.descricao or None
            existente.tipo = mapa.tipo.value
            existente.situacao = mapa.situacao.value
            existente.datum = mapa.datum.value
            existente.srid = mapa.srid
            existente.escala_denominador = mapa.escala_denominador
            existente.zoom_inicial = mapa.zoom_inicial
            existente.zoom_minimo = mapa.zoom_minimo
            existente.zoom_maximo = mapa.zoom_maximo
            existente.lat_min = mapa.lat_min
            existente.lon_min = mapa.lon_min
            existente.lat_max = mapa.lat_max
            existente.lon_max = mapa.lon_max
            existente.publicado_em = mapa.publicado_em
            existente.updated_at = mapa.updated_at
            existente.is_deleted = mapa.is_deleted
        else:
            self._session.add(
                MapaSigModel(
                    id=to_uuid(mapa.id),
                    codigo=mapa.codigo,
                    nome=mapa.nome,
                    descricao=mapa.descricao or None,
                    tipo=mapa.tipo.value,
                    situacao=mapa.situacao.value,
                    datum=mapa.datum.value,
                    srid=mapa.srid,
                    escala_denominador=mapa.escala_denominador,
                    zoom_inicial=mapa.zoom_inicial,
                    zoom_minimo=mapa.zoom_minimo,
                    zoom_maximo=mapa.zoom_maximo,
                    lat_min=mapa.lat_min,
                    lon_min=mapa.lon_min,
                    lat_max=mapa.lat_max,
                    lon_max=mapa.lon_max,
                    publicado_em=mapa.publicado_em,
                    criado_por=mapa.criado_por or None,
                    created_at=mapa.created_at,
                    updated_at=mapa.updated_at,
                    created_by=mapa.created_by or None,
                    is_deleted=mapa.is_deleted,
                )
            )
        self._session.flush()
        return mapa

    def get_by_id(self, mapa_id: str) -> MapaSig | None:
        """Busca mapa SIG por id."""
        model = buscar_ou_um(self._session, MapaSigModel, mapa_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_codigo(self, codigo: str) -> MapaSig | None:
        """Busca mapa SIG pelo código cadastral."""
        model = (
            self._session.query(MapaSigModel)
            .filter(MapaSigModel.codigo == codigo, MapaSigModel.is_deleted.is_(False))
            .first()
        )
        return self._to_entity(model) if model else None

    def list_all(
        self, page: int = 1, page_size: int = 20, situacao: str | None = None
    ) -> list[MapaSig]:
        """Lista mapas SIG paginados, opcionalmente por situação."""
        query = self._session.query(MapaSigModel).filter(MapaSigModel.is_deleted.is_(False))
        if situacao:
            query = query.filter(MapaSigModel.situacao == situacao)
        models = (
            query.order_by(MapaSigModel.codigo)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: MapaSigModel) -> MapaSig:
        return MapaSig(
            id=str(model.id),
            codigo=model.codigo,
            nome=model.nome,
            descricao=model.descricao or "",
            tipo=TipoMapaSig(model.tipo or "tematico"),
            situacao=SituacaoMapaSig(model.situacao or "rascunho"),
            datum=DatumGeografico(model.datum or "sirgas2000"),
            srid=int(model.srid or 4326),
            escala_denominador=int(model.escala_denominador or 0),
            zoom_inicial=int(model.zoom_inicial or 13),
            zoom_minimo=int(model.zoom_minimo or 0),
            zoom_maximo=int(model.zoom_maximo or 24),
            lat_min=model.lat_min,
            lon_min=model.lon_min,
            lat_max=model.lat_max,
            lon_max=model.lon_max,
            publicado_em=model.publicado_em,
            criado_por=model.criado_por or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyCamadaMapaRepository", "SQLAlchemyMapaSigRepository"]
