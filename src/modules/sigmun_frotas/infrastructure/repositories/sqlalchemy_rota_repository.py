"""Repositório SQLAlchemy de rotas (DOM-FRO)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioRota
from ...domain.entities.operacional import Rota, StatusRota
from ..database.models import RotaModel


class SQLAlchemyRotaRepository(RepositorioRota):
    """Persistência de rotas."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, rota: Rota) -> Rota:
        """Persiste uma rota."""
        existente = self._session.get(RotaModel, uuid.UUID(rota.id))
        if existente is not None:
            existente.status = rota.status.value
            existente.distancia_km = rota.distancia_km
        else:
            self._session.add(
                RotaModel(
                    id=uuid.UUID(rota.id),
                    veiculo_id=rota.veiculo_id,
                    data=rota.data,
                    origem=rota.origem,
                    destino=rota.destino,
                    km_inicio=rota.km_inicio,
                    km_fim=rota.km_fim,
                    distancia_km=rota.distancia_km,
                    descricao=rota.descricao,
                    status=rota.status.value,
                    created_at=rota.created_at,
                    created_by=rota.created_by,
                )
            )
        self._session.flush()
        return rota

    def get_by_id(self, rota_id: str) -> Rota | None:
        """Busca rota por id."""
        model = self._session.get(RotaModel, uuid.UUID(rota_id))
        return self._to_entity(model) if model else None

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista rotas paginadas."""
        models = (
            self._session.query(RotaModel)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: RotaModel) -> Rota:
        return Rota(
            id=str(model.id),
            veiculo_id=model.veiculo_id or "",
            data=model.data,
            origem=model.origem or "",
            destino=model.destino or "",
            km_inicio=float(model.km_inicio or 0),
            km_fim=float(model.km_fim or 0),
            distancia_km=float(model.distancia_km or 0),
            descricao=model.descricao or "",
            status=StatusRota(model.status or "planejada"),
            created_at=model.created_at,
            created_by=model.created_by or "",
        )


__all__ = ["SQLAlchemyRotaRepository"]