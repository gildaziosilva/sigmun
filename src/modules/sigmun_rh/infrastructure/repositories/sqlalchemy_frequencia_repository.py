"""Repositorio SQLAlchemy de frequencia (DOM-PES)."""

from __future__ import annotations

import uuid
from datetime import date

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioFrequencia
from ...domain.entities.frequencia import Frequencia, TipoFrequencia
from ..database.models_folha import FrequenciaModel


class SQLAlchemyFrequenciaRepository(RepositorioFrequencia):
    """Persistencia de frequencia."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, frequencia: Frequencia) -> Frequencia:
        """Insere ou atualiza frequencia."""
        existente = self._session.get(FrequenciaModel, uuid.UUID(frequencia.id))
        if existente is not None:
            existente.tipo = frequencia.tipo.value
            existente.hora_entrada = frequencia.hora_entrada
            existente.hora_saida = frequencia.hora_saida
            existente.minutos_atraso = frequencia.minutos_atraso
            existente.justificativa = frequencia.justificativa
            existente.desconto_folha = frequencia.desconto_folha
            existente.updated_at = frequencia.updated_at
            existente.is_deleted = frequencia.is_deleted
        else:
            self._session.add(
                FrequenciaModel(
                    id=uuid.UUID(frequencia.id),
                    servidor_id=frequencia.servidor_id,
                    data=frequencia.data,
                    tipo=frequencia.tipo.value,
                    hora_entrada=frequencia.hora_entrada,
                    hora_saida=frequencia.hora_saida,
                    minutos_atraso=frequencia.minutos_atraso,
                    justificativa=frequencia.justificativa,
                    desconto_folha=frequencia.desconto_folha,
                    created_at=frequencia.created_at,
                    updated_at=frequencia.updated_at,
                    created_by=frequencia.created_by,
                    is_deleted=frequencia.is_deleted,
                )
            )
        self._session.flush()
        return frequencia

    def get_by_id(self, frequencia_id: str) -> Frequencia | None:
        """Busca frequencia por id."""
        model = self._session.get(FrequenciaModel, uuid.UUID(frequencia_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_por_servidor_data(
        self, servidor_id: str, data: date
    ) -> Frequencia | None:
        """Busca registro por servidor/data."""
        model = (
            self._session.query(FrequenciaModel)
            .filter(
                FrequenciaModel.servidor_id == servidor_id,
                FrequenciaModel.data == data,
                FrequenciaModel.is_deleted == False,  # noqa: E712
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def _to_entity(self, model: FrequenciaModel) -> Frequencia:
        return Frequencia(
            id=str(model.id),
            servidor_id=model.servidor_id or "",
            data=model.data,
            tipo=TipoFrequencia(model.tipo or "presenca"),
            hora_entrada=model.hora_entrada,
            hora_saida=model.hora_saida,
            minutos_atraso=int(model.minutos_atraso or 0),
            justificativa=model.justificativa or "",
            desconto_folha=bool(model.desconto_folha),
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyFrequenciaRepository"]
