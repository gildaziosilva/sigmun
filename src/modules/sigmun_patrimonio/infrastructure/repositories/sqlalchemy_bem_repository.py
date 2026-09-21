"""Repositório SQLAlchemy de bens patrimoniais (DOM-PAT)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioBem
from ...domain.entities.bem import Bem, StatusBem, TipoBem
from ..database.models import BemModel


class SQLAlchemyBemRepository(RepositorioBem):
    """Persistência de bens."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, bem: Bem) -> Bem:
        """Insere ou atualiza um bem."""
        existente = self._session.get(BemModel, uuid.UUID(bem.id))
        if existente is not None:
            existente.codigo = bem.codigo
            existente.tipo = bem.tipo.value
            existente.descricao = bem.descricao
            existente.categoria = bem.categoria
            existente.valor_aquisicao = bem.valor_aquisicao
            existente.data_aquisicao = bem.data_aquisicao
            existente.valor_residual = bem.valor_residual
            existente.vida_util_anos = bem.vida_util_anos
            existente.valor_contabil = bem.valor_contabil
            existente.status = bem.status.value
            existente.localizacao = bem.localizacao
            existente.responsavel_id = bem.responsavel_id
            existente.updated_at = bem.updated_at
            existente.is_deleted = bem.is_deleted
        else:
            self._session.add(
                BemModel(
                    id=uuid.UUID(bem.id),
                    codigo=bem.codigo,
                    tipo=bem.tipo.value,
                    descricao=bem.descricao,
                    categoria=bem.categoria,
                    valor_aquisicao=bem.valor_aquisicao,
                    data_aquisicao=bem.data_aquisicao,
                    valor_residual=bem.valor_residual,
                    vida_util_anos=bem.vida_util_anos,
                    valor_contabil=bem.valor_contabil,
                    status=bem.status.value,
                    localizacao=bem.localizacao,
                    responsavel_id=bem.responsavel_id,
                    created_at=bem.created_at,
                    updated_at=bem.updated_at,
                    created_by=bem.created_by,
                    is_deleted=bem.is_deleted,
                )
            )
        self._session.flush()
        return bem

    def get_by_id(self, bem_id: str) -> Bem | None:
        """Busca bem por id."""
        model = self._session.get(BemModel, uuid.UUID(bem_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_codigo(self, codigo: str) -> Bem | None:
        """Busca bem pelo tombo/código."""
        model = (
            self._session.query(BemModel)
            .filter(
                BemModel.codigo == codigo,
                BemModel.is_deleted == False,  # noqa: E712
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista bens paginados."""
        models = (
            self._session.query(BemModel)
            .filter(BemModel.is_deleted == False)  # noqa: E712
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: BemModel) -> Bem:
        return Bem(
            id=str(model.id),
            codigo=model.codigo or "",
            tipo=TipoBem(model.tipo or "movel"),
            descricao=model.descricao or "",
            categoria=model.categoria or "",
            valor_aquisicao=float(model.valor_aquisicao or 0),
            data_aquisicao=model.data_aquisicao,
            valor_residual=float(model.valor_residual or 0),
            vida_util_anos=model.vida_util_anos or 0,
            valor_contabil=float(model.valor_contabil or 0),
            status=StatusBem(model.status or "em_uso"),
            localizacao=model.localizacao or "",
            responsavel_id=model.responsavel_id or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyBemRepository"]