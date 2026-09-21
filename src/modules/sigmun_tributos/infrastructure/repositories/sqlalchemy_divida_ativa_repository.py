"""Repositório SQLAlchemy de dívida ativa (DOM-TRI)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioDividaAtiva
from ...domain.entities.divida_ativa import (
    InscricaoDividaAtiva,
    StatusDividaAtiva,
)
from ..database.models import DividaAtivaModel


class SQLAlchemyDividaAtivaRepository(RepositorioDividaAtiva):
    """Persistência de inscrições em dívida ativa."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, inscricao: InscricaoDividaAtiva) -> InscricaoDividaAtiva:
        """Insere ou atualiza uma inscrição."""
        existente = self._session.get(DividaAtivaModel, uuid.UUID(inscricao.id))
        if existente is not None:
            existente.lancamento_id = inscricao.lancamento_id
            existente.numero_inscricao = inscricao.numero_inscricao
            existente.data_inscricao = inscricao.data_inscricao
            existente.valor_original = inscricao.valor_original
            existente.valor_atualizado = inscricao.valor_atualizado
            existente.status = inscricao.status.value
            existente.updated_at = inscricao.updated_at
            existente.is_deleted = inscricao.is_deleted
        else:
            self._session.add(
                DividaAtivaModel(
                    id=uuid.UUID(inscricao.id),
                    lancamento_id=inscricao.lancamento_id,
                    numero_inscricao=inscricao.numero_inscricao,
                    data_inscricao=inscricao.data_inscricao,
                    valor_original=inscricao.valor_original,
                    valor_atualizado=inscricao.valor_atualizado,
                    status=inscricao.status.value,
                    created_at=inscricao.created_at,
                    updated_at=inscricao.updated_at,
                    created_by=inscricao.created_by,
                    is_deleted=inscricao.is_deleted,
                )
            )
        self._session.flush()
        return inscricao

    def get_by_id(self, inscricao_id: str) -> InscricaoDividaAtiva | None:
        """Busca inscrição por id."""
        model = self._session.get(DividaAtivaModel, uuid.UUID(inscricao_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_numero(self, numero: str) -> InscricaoDividaAtiva | None:
        """Busca inscrição pelo número."""
        model = (
            self._session.query(DividaAtivaModel)
            .filter(
                DividaAtivaModel.numero_inscricao == numero,
                DividaAtivaModel.is_deleted == False,  # noqa: E712
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista inscrições paginadas."""
        models = (
            self._session.query(DividaAtivaModel)
            .filter(DividaAtivaModel.is_deleted == False)  # noqa: E712
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: DividaAtivaModel) -> InscricaoDividaAtiva:
        return InscricaoDividaAtiva(
            id=str(model.id),
            lancamento_id=model.lancamento_id or "",
            numero_inscricao=model.numero_inscricao or "",
            data_inscricao=model.data_inscricao,
            valor_original=float(model.valor_original or 0),
            valor_atualizado=float(model.valor_atualizado or 0),
            status=StatusDividaAtiva(model.status or "ativa"),
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyDividaAtivaRepository"]