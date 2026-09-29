"""Repositório SQLAlchemy de georreferências territoriais (DOM-TEL)."""

from __future__ import annotations

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioGeorreferencia
from ...domain.entities import (
    DatumGeorreferencia,
    Georreferencia,
    TipoGeometria,
)
from ..database.models import GeorreferenciaModel
from .bairro import buscar_ou_um
from .bairro import to_uuid


class SQLAlchemyGeorreferenciaRepository(RepositorioGeorreferencia):
    """Persistência de georreferências territoriais."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, georreferencia: Georreferencia) -> Georreferencia:
        """Insere ou atualiza uma georreferência.

        Referências oplas são normalizadas para NULL antes da gravação, pois a
        constraint `ck_tel_geo_referencia` (RN-TEL-005) exige que exatamente um
        dos campos `bairro_id`/`logradouro_id` esteja preenchido.
        """
        existente = self._session.get(GeorreferenciaModel, to_uuid(georreferencia.id))
        if existente is not None:
            existente.bairro_id = georreferencia.bairro_id or None
            existente.logradouro_id = georreferencia.logradouro_id or None
            existente.geometria = georreferencia.geometria.value
            existente.latitude = georreferencia.latitude
            existente.longitude = georreferencia.longitude
            existente.altitude_m = georreferencia.altitude_m
            existente.vertices = georreferencia.vertices
            existente.datum = georreferencia.datum.value
            existente.precisao_m = georreferencia.precisao_m
            existente.data_levantamento = georreferencia.data_levantamento
            existente.updated_at = georreferencia.updated_at
            existente.is_deleted = georreferencia.is_deleted
        else:
            self._session.add(
                GeorreferenciaModel(
                    id=to_uuid(georreferencia.id),
                    bairro_id=georreferencia.bairro_id or None,
                    logradouro_id=georreferencia.logradouro_id or None,
                    geometria=georreferencia.geometria.value,
                    latitude=georreferencia.latitude,
                    longitude=georreferencia.longitude,
                    altitude_m=georreferencia.altitude_m,
                    vertices=georreferencia.vertices,
                    datum=georreferencia.datum.value,
                    precisao_m=georreferencia.precisao_m,
                    data_levantamento=georreferencia.data_levantamento,
                    created_at=georreferencia.created_at,
                    updated_at=georreferencia.updated_at,
                    created_by=georreferencia.created_by,
                    is_deleted=georreferencia.is_deleted,
                )
            )
        self._session.flush()
        return georreferencia

    def get_by_id(self, georreferencia_id: str) -> Georreferencia | None:
        """Busca georreferência por id."""
        model = buscar_ou_um(self._session, GeorreferenciaModel, georreferencia_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def list_by_referencia(
        self, bairro_id: str | None = None, logradouro_id: str | None = None
    ) -> list[Georreferencia]:
        """Lista georreferências por bairro ou logradouro."""
        query = self._session.query(GeorreferenciaModel).filter(
            GeorreferenciaModel.is_deleted.is_(False)
        )
        if bairro_id:
            query = query.filter(GeorreferenciaModel.bairro_id == bairro_id)
        if logradouro_id:
            query = query.filter(GeorreferenciaModel.logradouro_id == logradouro_id)
        return [self._to_entity(m) for m in query.order_by(GeorreferenciaModel.id).all()]

    def list_all(self, page: int = 1, page_size: int = 20) -> list[Georreferencia]:
        """Lista georreferências paginadas."""
        models = (
            self._session.query(GeorreferenciaModel)
            .filter(GeorreferenciaModel.is_deleted.is_(False))
            .order_by(GeorreferenciaModel.id)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: GeorreferenciaModel) -> Georreferencia:
        return Georreferencia(
            id=str(model.id),
            bairro_id=model.bairro_id or "",
            logradouro_id=model.logradouro_id or "",
            geometria=TipoGeometria(model.geometria or "ponto"),
            latitude=float(model.latitude or 0),
            longitude=float(model.longitude or 0),
            altitude_m=model.altitude_m,
            vertices=list(model.vertices or []),
            datum=DatumGeorreferencia(model.datum or "sirgas2000"),
            precisao_m=float(model.precisao_m or 0),
            data_levantamento=model.data_levantamento,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyGeorreferenciaRepository"]
