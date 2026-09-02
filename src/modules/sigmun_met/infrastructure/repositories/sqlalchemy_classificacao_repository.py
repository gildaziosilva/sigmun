"""Implementação SQLAlchemy do repositório de Classificações (DOM-MET)."""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.sigmun_met.application.interfaces import (
    ClassificacaoRepositoryInterface,
)
from src.modules.sigmun_met.domain.entities import Classificacao, TipoClassificacao
from src.modules.sigmun_met.infrastructure.database.models import ClassificacaoModel

logger = logging.getLogger(__name__)


def _to_entity(model: ClassificacaoModel) -> Classificacao:
    return Classificacao(
        id=str(model.id),
        codigo=model.codigo,
        nome=model.nome,
        descricao=model.descricao or "",
        tipo=TipoClassificacao(model.tipo),
        nivel=model.nivel,
        cor=model.cor or "",
        created_at=model.created_at,
        updated_at=model.updated_at,
        is_deleted=model.deleted_at is not None,
    )


class SqlAlchemyClassificacaoRepository(ClassificacaoRepositoryInterface):
    """Repositório de classificações persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, classificacao_id: str) -> Classificacao | None:
        model = self._session.get(ClassificacaoModel, UUID(classificacao_id))
        if model is None or model.deleted_at is not None:
            return None
        return _to_entity(model)

    def get_by_codigo(self, codigo: str) -> Classificacao | None:
        stmt = select(ClassificacaoModel).where(
            ClassificacaoModel.codigo == codigo,
            ClassificacaoModel.deleted_at.is_(None),
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def list_all(
        self, page: int = 0, page_size: int = 50, tipo: str | None = None,
    ) -> tuple[builtins.list[Classificacao], int]:
        stmt = select(ClassificacaoModel).where(ClassificacaoModel.deleted_at.is_(None))
        if tipo:
            stmt = stmt.where(ClassificacaoModel.tipo == tipo)
        total = len(self._session.scalars(stmt).all())
        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def save(self, classificacao: Classificacao) -> Classificacao:
        model = self._session.get(ClassificacaoModel, UUID(classificacao.id))
        if model is None:
            model = ClassificacaoModel(
                id=UUID(classificacao.id),
                codigo=classificacao.codigo,
                nome=classificacao.nome,
                descricao=classificacao.descricao,
                tipo=classificacao.tipo.value,
                nivel=classificacao.nivel,
                cor=classificacao.cor,
                created_at=classificacao.created_at,
            )
            self._session.add(model)
            logger.info("Classificação inserida: %s", classificacao.id)
        else:
            model.nome = classificacao.nome
            model.descricao = classificacao.descricao
            model.tipo = classificacao.tipo.value
            model.nivel = classificacao.nivel
            model.cor = classificacao.cor
            model.updated_at = classificacao.updated_at
            logger.info("Classificação atualizada: %s", classificacao.id)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def delete(self, classificacao_id: str) -> bool:
        model = self._session.get(ClassificacaoModel, UUID(classificacao_id))
        if model is None:
            return False
        if model.deleted_at is None:
            model.deleted_at = func.now()
        self._session.flush()
        return True

    def exists_by_codigo(self, codigo: str) -> bool:
        stmt = select(ClassificacaoModel.id).where(
            ClassificacaoModel.codigo == codigo,
            ClassificacaoModel.deleted_at.is_(None),
        ).limit(1)
        return self._session.scalars(stmt).first() is not None


__all__ = ["SqlAlchemyClassificacaoRepository"]
