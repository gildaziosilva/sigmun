"""Repositórios SQLAlchemy de depreciações e transferências (DOM-PAT)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioDepreciacao, RepositorioTransferencia
from ...domain.entities.depreciacao import Depreciacao
from ...domain.entities.transferencia import (
    StatusTransferencia,
    Transferencia,
)
from ..database.models import DepreciacaoModel, TransferenciaModel


class SQLAlchemyDepreciacaoRepository(RepositorioDepreciacao):
    """Persistência de depreciações."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, depreciacao: Depreciacao) -> Depreciacao:
        """Persiste uma depreciação."""
        self._session.add(
            DepreciacaoModel(
                id=uuid.UUID(depreciacao.id),
                bem_id=depreciacao.bem_id,
                data=depreciacao.data,
                valor_depreciado=depreciacao.valor_depreciado,
                valor_acumulado=depreciacao.valor_acumulado,
                valor_liquido=depreciacao.valor_liquido,
                created_at=depreciacao.created_at,
                created_by=depreciacao.created_by,
            )
        )
        self._session.flush()
        return depreciacao

    def list_by_bem(self, bem_id: str) -> list:
        """Lista depreciações de um bem."""
        models = (
            self._session.query(DepreciacaoModel)
            .filter(DepreciacaoModel.bem_id == bem_id)
            .all()
        )
        return [
            Depreciacao(
                id=str(m.id), bem_id=m.bem_id, data=m.data,
                valor_depreciado=float(m.valor_depreciado or 0),
                valor_acumulado=float(m.valor_acumulado or 0),
                valor_liquido=float(m.valor_liquido or 0),
                created_at=m.created_at, created_by=m.created_by or "",
            )
            for m in models
        ]


class SQLAlchemyTransferenciaRepository(RepositorioTransferencia):
    """Persistência de transferências."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, transferencia: Transferencia) -> Transferencia:
        """Persiste uma transferência."""
        existente = self._session.get(
            TransferenciaModel, uuid.UUID(transferencia.id)
        )
        if existente is not None:
            existente.status = transferencia.status.value
            existente.para_localizacao = transferencia.para_localizacao
        else:
            self._session.add(
                TransferenciaModel(
                    id=uuid.UUID(transferencia.id),
                    bem_id=transferencia.bem_id,
                    de_localizacao=transferencia.de_localizacao,
                    para_localizacao=transferencia.para_localizacao,
                    de_responsavel_id=transferencia.de_responsavel_id,
                    para_responsavel_id=transferencia.para_responsavel_id,
                    data_transferencia=transferencia.data_transferencia,
                    motivo=transferencia.motivo,
                    status=transferencia.status.value,
                    created_at=transferencia.created_at,
                    created_by=transferencia.created_by,
                )
            )
        self._session.flush()
        return transferencia

    def get_by_id(self, transferencia_id: str) -> Transferencia | None:
        """Busca transferência por id."""
        model = self._session.get(
            TransferenciaModel, uuid.UUID(transferencia_id)
        )
        return self._to_entity(model) if model else None

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista transferências paginadas."""
        models = (
            self._session.query(TransferenciaModel)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: TransferenciaModel) -> Transferencia:
        return Transferencia(
            id=str(model.id),
            bem_id=model.bem_id or "",
            de_localizacao=model.de_localizacao or "",
            para_localizacao=model.para_localizacao or "",
            de_responsavel_id=model.de_responsavel_id or "",
            para_responsavel_id=model.para_responsavel_id or "",
            data_transferencia=model.data_transferencia,
            motivo=model.motivo or "",
            status=StatusTransferencia(model.status or "pendente"),
            created_at=model.created_at,
            created_by=model.created_by or "",
        )


__all__ = [
    "SQLAlchemyDepreciacaoRepository",
    "SQLAlchemyTransferenciaRepository",
]