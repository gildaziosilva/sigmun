"""Repositório SQLAlchemy da planta genérica de valores (DOM-TEL)."""

from __future__ import annotations

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioPlantaValores
from ...domain.entities import PlantaGenericaValores, SituacaoPlantaValores, TipoOcupacaoImovel
from ..database.models import PlantaGenericaValoresModel
from .bairro import buscar_ou_um
from .bairro import to_uuid


class SQLAlchemyPlantaValoresRepository(RepositorioPlantaValores):
    """Persistência da planta genérica de valores."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, planta: PlantaGenericaValores) -> PlantaGenericaValores:
        """Insere ou atualiza uma planta genérica de valores."""
        existente = self._session.get(PlantaGenericaValoresModel, to_uuid(planta.id))
        if existente is not None:
            existente.ano = planta.ano
            existente.bairro_id = planta.bairro_id
            existente.ocupacao = planta.ocupacao.value
            existente.valor_terreno_m2 = planta.valor_terreno_m2
            existente.valor_construcao_m2 = planta.valor_construcao_m2
            existente.aliquota_percent = planta.aliquota_percent
            existente.situacao = planta.situacao.value
            existente.legislacao = planta.legislacao
            existente.updated_at = planta.updated_at
            existente.is_deleted = planta.is_deleted
        else:
            self._session.add(
                PlantaGenericaValoresModel(
                    id=to_uuid(planta.id),
                    ano=planta.ano,
                    bairro_id=planta.bairro_id,
                    ocupacao=planta.ocupacao.value,
                    valor_terreno_m2=planta.valor_terreno_m2,
                    valor_construcao_m2=planta.valor_construcao_m2,
                    aliquota_percent=planta.aliquota_percent,
                    situacao=planta.situacao.value,
                    legislacao=planta.legislacao,
                    created_at=planta.created_at,
                    updated_at=planta.updated_at,
                    created_by=planta.created_by,
                    is_deleted=planta.is_deleted,
                )
            )
        self._session.flush()
        return planta

    def get_by_id(self, planta_id: str) -> PlantaGenericaValores | None:
        """Busca planta genérica de valores por id."""
        model = buscar_ou_um(self._session, PlantaGenericaValoresModel, planta_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_vigente(
        self, ano: int, bairro_id: str, ocupacao: str
    ) -> PlantaGenericaValores | None:
        """Busca a planta vigente para ano, bairro e ocupação (RN-TEL-003)."""
        model = (
            self._session.query(PlantaGenericaValoresModel)
            .filter(
                PlantaGenericaValoresModel.ano == ano,
                PlantaGenericaValoresModel.bairro_id == bairro_id,
                PlantaGenericaValoresModel.ocupacao == ocupacao,
                PlantaGenericaValoresModel.situacao == SituacaoPlantaValores.VIGENTE.value,
                PlantaGenericaValoresModel.is_deleted.is_(False),
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def get_by_ano_bairro_ocupacao(
        self, ano: int, bairro_id: str, ocupacao: str
    ) -> PlantaGenericaValores | None:
        """Busca a planta de uma combinação, independente da situação."""
        model = (
            self._session.query(PlantaGenericaValoresModel)
            .filter(
                PlantaGenericaValoresModel.ano == ano,
                PlantaGenericaValoresModel.bairro_id == bairro_id,
                PlantaGenericaValoresModel.ocupacao == ocupacao,
                PlantaGenericaValoresModel.is_deleted.is_(False),
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def list_all(
        self, page: int = 1, page_size: int = 20, bairro_id: str | None = None
    ) -> list[PlantaGenericaValores]:
        """Lista plantas genéricas de valores, opcionalmente por bairro."""
        query = self._session.query(PlantaGenericaValoresModel).filter(
            PlantaGenericaValoresModel.is_deleted.is_(False)
        )
        if bairro_id:
            query = query.filter(PlantaGenericaValoresModel.bairro_id == bairro_id)
        models = (
            query.order_by(
                PlantaGenericaValoresModel.ano.desc(),
                PlantaGenericaValoresModel.bairro_id,
            )
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: PlantaGenericaValoresModel) -> PlantaGenericaValores:
        return PlantaGenericaValores(
            id=str(model.id),
            ano=int(model.ano or 0),
            bairro_id=model.bairro_id or "",
            ocupacao=TipoOcupacaoImovel(model.ocupacao or "residencial"),
            valor_terreno_m2=float(model.valor_terreno_m2 or 0),
            valor_construcao_m2=float(model.valor_construcao_m2 or 0),
            aliquota_percent=float(model.aliquota_percent or 0),
            situacao=SituacaoPlantaValores(model.situacao or "rascunho"),
            legislacao=model.legislacao or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyPlantaValoresRepository"]
