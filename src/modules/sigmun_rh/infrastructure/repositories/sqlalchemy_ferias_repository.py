"""Repositorio SQLAlchemy de ferias (DOM-PES)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioFerias
from ...domain.entities.ferias import Ferias, StatusFerias
from ..database.models_folha import FeriasModel


class SQLAlchemyFeriasRepository(RepositorioFerias):
    """Persistencia de ferias."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, ferias: Ferias) -> Ferias:
        """Insere ou atualiza ferias."""
        existente = self._session.get(FeriasModel, uuid.UUID(ferias.id))
        if existente is not None:
            existente.status = ferias.status.value
            existente.dias = ferias.dias
            existente.parcela = ferias.parcela
            existente.data_aprovacao = ferias.data_aprovacao
            existente.data_cancelamento = ferias.data_cancelamento
            existente.motivo_cancelamento = ferias.motivo_cancelamento
            existente.updated_at = ferias.updated_at
            existente.is_deleted = ferias.is_deleted
        else:
            self._session.add(
                FeriasModel(
                    id=uuid.UUID(ferias.id),
                    servidor_id=ferias.servidor_id,
                    periodo_aquisitivo_inicio=ferias.periodo_aquisitivo_inicio,
                    periodo_aquisitivo_fim=ferias.periodo_aquisitivo_fim,
                    data_inicio_gozo=ferias.data_inicio_gozo,
                    data_fim_gozo=ferias.data_fim_gozo,
                    dias=ferias.dias,
                    parcela=ferias.parcela,
                    status=ferias.status.value,
                    data_aprovacao=ferias.data_aprovacao,
                    data_cancelamento=ferias.data_cancelamento,
                    motivo_cancelamento=ferias.motivo_cancelamento,
                    created_at=ferias.created_at,
                    updated_at=ferias.updated_at,
                    created_by=ferias.created_by,
                    is_deleted=ferias.is_deleted,
                )
            )
        self._session.flush()
        return ferias

    def get_by_id(self, ferias_id: str) -> Ferias | None:
        """Busca ferias por id."""
        model = self._session.get(FeriasModel, uuid.UUID(ferias_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def _to_entity(self, model: FeriasModel) -> Ferias:
        return Ferias(
            id=str(model.id),
            servidor_id=model.servidor_id or "",
            periodo_aquisitivo_inicio=model.periodo_aquisitivo_inicio,
            periodo_aquisitivo_fim=model.periodo_aquisitivo_fim,
            data_inicio_gozo=model.data_inicio_gozo,
            data_fim_gozo=model.data_fim_gozo,
            dias=int(model.dias or 0),
            parcela=int(model.parcela or 1),
            status=StatusFerias(model.status or "planejada"),
            data_aprovacao=model.data_aprovacao,
            data_cancelamento=model.data_cancelamento,
            motivo_cancelamento=model.motivo_cancelamento or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyFeriasRepository"]
