"""Repositorio SQLAlchemy de lotacoes (DOM-PES)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioLotacao
from ...domain.entities.lotacao import Lotacao
from ..database.models import LotacaoModel


class SQLAlchemyLotacaoRepository(RepositorioLotacao):
    """Persistencia de lotacoes."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, lotacao: Lotacao) -> Lotacao:
        """Insere ou atualiza lotacao."""
        existente = self._session.get(LotacaoModel, uuid.UUID(lotacao.id))
        if existente is not None:
            existente.servidor_id = lotacao.servidor_id
            existente.unidade_id = lotacao.unidade_id
            existente.cargo_id = lotacao.cargo_id
            existente.data_inicio = lotacao.data_inicio
            existente.data_fim = lotacao.data_fim
            existente.vigente = lotacao.vigente
            existente.motivo = lotacao.motivo
            existente.updated_at = lotacao.updated_at
            existente.is_deleted = lotacao.is_deleted
        else:
            self._session.add(
                LotacaoModel(
                    id=uuid.UUID(lotacao.id),
                    servidor_id=lotacao.servidor_id,
                    unidade_id=lotacao.unidade_id,
                    cargo_id=lotacao.cargo_id,
                    data_inicio=lotacao.data_inicio,
                    data_fim=lotacao.data_fim,
                    vigente=lotacao.vigente,
                    motivo=lotacao.motivo,
                    created_at=lotacao.created_at,
                    updated_at=lotacao.updated_at,
                    created_by=lotacao.created_by,
                    is_deleted=lotacao.is_deleted,
                )
            )
        self._session.flush()
        return lotacao

    def get_by_id(self, lotacao_id: str) -> Lotacao | None:
        """Busca lotacao por id."""
        model = self._session.get(LotacaoModel, uuid.UUID(lotacao_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def list_vigentes_por_servidor(self, servidor_id: str) -> list[Lotacao]:
        """Lista lotacoes vigentes do servidor."""
        models = (
            self._session.query(LotacaoModel)
            .filter(
                LotacaoModel.servidor_id == servidor_id,
                LotacaoModel.vigente == True,  # noqa: E712
                LotacaoModel.is_deleted == False,  # noqa: E712
            )
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: LotacaoModel) -> Lotacao:
        return Lotacao(
            id=str(model.id),
            servidor_id=model.servidor_id or "",
            unidade_id=model.unidade_id or "",
            cargo_id=model.cargo_id or "",
            data_inicio=model.data_inicio,
            data_fim=model.data_fim,
            vigente=bool(model.vigente),
            motivo=model.motivo or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyLotacaoRepository"]
