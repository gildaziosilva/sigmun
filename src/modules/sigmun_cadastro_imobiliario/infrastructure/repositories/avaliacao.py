"""Repositórios SQLAlchemy das avaliações, características e geometrias (DOM-IMO)."""

from __future__ import annotations

from sqlalchemy.orm import Session

from ...application.interfaces import (
    RepositorioAvaliacao,
    RepositorioCaracteristica,
    RepositorioGeometria,
)
from ...domain.entities import (
    AvaliacaoImovel,
    CaracteristicaImovel,
    GeometriaImovel,
    SituacaoAvaliacao,
    TipoObra,
)
from ..database.models import (
    AvaliacaoImovelModel,
    CaracteristicaImovelModel,
    GeometriaImovelModel,
)
from .imovel import buscar_ou_um
from .imovel import to_uuid


class SQLAlchemyAvaliacaoRepository(RepositorioAvaliacao):
    """Persistência das avaliações de valor venal."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, avaliacao: AvaliacaoImovel) -> AvaliacaoImovel:
        """Insere ou atualiza uma avaliação."""
        existente = self._session.get(AvaliacaoImovelModel, to_uuid(avaliacao.id))
        if existente is not None:
            existente.imovel_id = avaliacao.imovel_id
            existente.ano = avaliacao.ano
            existente.valor_terreno_m2_unitario = avaliacao.valor_terreno_m2_unitario
            existente.valor_construcao_m2_unitario = avaliacao.valor_construcao_m2_unitario
            existente.aliquota_percent = avaliacao.aliquota_percent
            existente.area_terreno_m2 = avaliacao.area_terreno_m2
            existente.area_construida_m2 = avaliacao.area_construida_m2
            existente.situacao = avaliacao.situacao.value
            existente.data_avaliacao = avaliacao.data_avaliacao
            existente.updated_at = avaliacao.updated_at
            existente.is_deleted = avaliacao.is_deleted
        else:
            self._session.add(
                AvaliacaoImovelModel(
                    id=to_uuid(avaliacao.id),
                    imovel_id=avaliacao.imovel_id,
                    ano=avaliacao.ano,
                    valor_terreno_m2_unitario=avaliacao.valor_terreno_m2_unitario,
                    valor_construcao_m2_unitario=avaliacao.valor_construcao_m2_unitario,
                    aliquota_percent=avaliacao.aliquota_percent,
                    area_terreno_m2=avaliacao.area_terreno_m2,
                    area_construida_m2=avaliacao.area_construida_m2,
                    situacao=avaliacao.situacao.value,
                    data_avaliacao=avaliacao.data_avaliacao,
                    created_at=avaliacao.created_at,
                    updated_at=avaliacao.updated_at,
                    created_by=avaliacao.created_by,
                    is_deleted=avaliacao.is_deleted,
                )
            )
        self._session.flush()
        return avaliacao

    def get_by_id(self, avaliacao_id: str) -> AvaliacaoImovel | None:
        """Busca avaliação por id."""
        model = buscar_ou_um(self._session, AvaliacaoImovelModel, avaliacao_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_imovel_e_ano(self, imovel_id: str, ano: int) -> AvaliacaoImovel | None:
        """Busca avaliação do imóvel para o exercício."""
        model = (
            self._session.query(AvaliacaoImovelModel)
            .filter(
                AvaliacaoImovelModel.imovel_id == imovel_id,
                AvaliacaoImovelModel.ano == ano,
                AvaliacaoImovelModel.is_deleted.is_(False),
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def list_by_imovel(self, imovel_id: str) -> list[AvaliacaoImovel]:
        """Lista avaliações de um imóvel."""
        models = (
            self._session.query(AvaliacaoImovelModel)
            .filter(
                AvaliacaoImovelModel.imovel_id == imovel_id,
                AvaliacaoImovelModel.is_deleted.is_(False),
            )
            .order_by(AvaliacaoImovelModel.ano.desc())
            .all()
        )
        return [self._to_entity(m) for m in models]

    def list_all(self, page: int = 1, page_size: int = 20) -> list[AvaliacaoImovel]:
        """Lista avaliações paginadas."""
        models = (
            self._session.query(AvaliacaoImovelModel)
            .filter(AvaliacaoImovelModel.is_deleted.is_(False))
            .order_by(AvaliacaoImovelModel.ano.desc(), AvaliacaoImovelModel.imovel_id)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: AvaliacaoImovelModel) -> AvaliacaoImovel:
        return AvaliacaoImovel(
            id=str(model.id),
            imovel_id=model.imovel_id or "",
            ano=int(model.ano or 0),
            valor_terreno_m2_unitario=float(model.valor_terreno_m2_unitario or 0),
            valor_construcao_m2_unitario=float(model.valor_construcao_m2_unitario or 0),
            aliquota_percent=float(model.aliquota_percent or 0),
            area_terreno_m2=float(model.area_terreno_m2 or 0),
            area_construida_m2=float(model.area_construida_m2 or 0),
            situacao=SituacaoAvaliacao(model.situacao or "rascunho"),
            data_avaliacao=model.data_avaliacao,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


class SQLAlchemyCaracteristicaRepository(RepositorioCaracteristica):
    """Persistência das características construtivas."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, caracteristica: CaracteristicaImovel) -> CaracteristicaImovel:
        """Insere ou atualiza a característica construtiva."""
        existente = self._session.get(CaracteristicaImovelModel, to_uuid(caracteristica.id))
        if existente is not None:
            existente.imovel_id = caracteristica.imovel_id
            existente.obra = caracteristica.obra.value
            existente.numero_pavimentos = caracteristica.numero_pavimentos
            existente.ano_renovacao = caracteristica.ano_renovacao
            existente.observacao = caracteristica.observacao
            existente.updated_at = caracteristica.updated_at
        else:
            self._session.add(
                CaracteristicaImovelModel(
                    id=to_uuid(caracteristica.id),
                    imovel_id=caracteristica.imovel_id,
                    obra=caracteristica.obra.value,
                    numero_pavimentos=caracteristica.numero_pavimentos,
                    ano_renovacao=caracteristica.ano_renovacao,
                    observacao=caracteristica.observacao,
                    created_at=caracteristica.created_at,
                    updated_at=caracteristica.updated_at,
                    created_by=caracteristica.created_by,
                )
            )
        self._session.flush()
        return caracteristica

    def get_by_id(self, caracteristica_id: str) -> CaracteristicaImovel | None:
        """Busca característica por id."""
        model = buscar_ou_um(self._session, CaracteristicaImovelModel, caracteristica_id)
        return self._to_entity(model) if model else None

    def get_by_imovel(self, imovel_id: str) -> CaracteristicaImovel | None:
        """Busca a característica construtiva vigente do imóvel."""
        model = (
            self._session.query(CaracteristicaImovelModel)
            .filter(CaracteristicaImovelModel.imovel_id == imovel_id)
            .first()
        )
        return self._to_entity(model) if model else None

    def list_by_imovel(self, imovel_id: str) -> list[CaracteristicaImovel]:
        """Lista características de um imóvel."""
        models = (
            self._session.query(CaracteristicaImovelModel)
            .filter(CaracteristicaImovelModel.imovel_id == imovel_id)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def list_all(self, page: int = 1, page_size: int = 20) -> list[CaracteristicaImovel]:
        """Lista características paginadas."""
        models = (
            self._session.query(CaracteristicaImovelModel)
            .order_by(CaracteristicaImovelModel.imovel_id)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: CaracteristicaImovelModel) -> CaracteristicaImovel:
        return CaracteristicaImovel(
            id=str(model.id),
            imovel_id=model.imovel_id or "",
            obra=TipoObra(model.obra or "residencial"),
            numero_pavimentos=int(model.numero_pavimentos or 1),
            ano_renovacao=model.ano_renovacao,
            observacao=model.observacao or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
        )



class SQLAlchemyGeometriaRepository(RepositorioGeometria):
    """Persistência das geometrias georreferenciadas dos lotes."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, geometria: GeometriaImovel) -> GeometriaImovel:
        """Insere ou atualiza a geometria do lote."""
        existente = self._session.get(GeometriaImovelModel, to_uuid(geometria.id))
        if existente is not None:
            existente.imovel_id = geometria.imovel_id
            existente.geometria = geometria.geometria
            existente.latitude = geometria.latitude
            existente.longitude = geometria.longitude
            existente.vertices = geometria.vertices
            existente.datum = geometria.datum
            existente.precisao_m = geometria.precisao_m
            existente.data_levantamento = geometria.data_levantamento
            existente.updated_at = geometria.updated_at
            existente.is_deleted = geometria.is_deleted
        else:
            self._session.add(
                GeometriaImovelModel(
                    id=to_uuid(geometria.id),
                    imovel_id=geometria.imovel_id,
                    geometria=geometria.geometria,
                    latitude=geometria.latitude,
                    longitude=geometria.longitude,
                    vertices=geometria.vertices,
                    datum=geometria.datum,
                    precisao_m=geometria.precisao_m,
                    data_levantamento=geometria.data_levantamento,
                    created_at=geometria.created_at,
                    updated_at=geometria.updated_at,
                    created_by=geometria.created_by,
                    is_deleted=geometria.is_deleted,
                )
            )
        self._session.flush()
        return geometria

    def get_by_id(self, geometria_id: str) -> GeometriaImovel | None:
        """Busca geometria por id."""
        model = buscar_ou_um(self._session, GeometriaImovelModel, geometria_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_imovel(self, imovel_id: str) -> GeometriaImovel | None:
        """Busca a geometria vigente do lote (RN-IMO-007)."""
        model = (
            self._session.query(GeometriaImovelModel)
            .filter(
                GeometriaImovelModel.imovel_id == imovel_id,
                GeometriaImovelModel.is_deleted.is_(False),
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def list_all(self, page: int = 1, page_size: int = 20) -> list[GeometriaImovel]:
        """Lista geometrias paginadas."""
        models = (
            self._session.query(GeometriaImovelModel)
            .filter(GeometriaImovelModel.is_deleted.is_(False))
            .order_by(GeometriaImovelModel.imovel_id)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: GeometriaImovelModel) -> GeometriaImovel:
        return GeometriaImovel(
            id=str(model.id),
            imovel_id=model.imovel_id or "",
            geometria=model.geometria or "ponto",
            latitude=float(model.latitude or 0),
            longitude=float(model.longitude or 0),
            vertices=list(model.vertices or []),
            datum=model.datum or "sirgas2000",
            precisao_m=float(model.precisao_m or 0),
            data_levantamento=model.data_levantamento,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = [
    "SQLAlchemyAvaliacaoRepository",
    "SQLAlchemyCaracteristicaRepository",
    "SQLAlchemyGeometriaRepository",
]

