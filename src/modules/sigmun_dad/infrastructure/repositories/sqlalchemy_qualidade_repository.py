"""Implementação SQLAlchemy do repositório de Qualidade de Dados (DOM-DAD)."""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.modules.sigmun_dad.application.interfaces import QualidadeRepositoryInterface
from src.modules.sigmun_dad.domain.entities import QualidadeDado, QualidadeNivel
from src.modules.sigmun_dad.infrastructure.database.models import QualidadeDadoModel

logger = logging.getLogger(__name__)


def _parse_list(value: str | None) -> list[str]:
    if not value:
        return []
    return [v.strip() for v in value.split(",") if v.strip()]


def _format_list(values: list[str]) -> str:
    return ",".join(values)


def _to_entity(model: QualidadeDadoModel) -> QualidadeDado:
    return QualidadeDado(
        id=str(model.id),
        ativo_id=str(model.ativo_id),
        nivel=QualidadeNivel(model.nivel),
        score=float(model.score),
        criterios=_parse_list(model.criterios),
        observacao=model.observacao or "",
        created_at=model.created_at,
        updated_at=model.updated_at,
        is_deleted=model.deleted_at is not None,
    )


class SqlAlchemyQualidadeRepository(QualidadeRepositoryInterface):
    """Repositório de qualidade de dados persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, qualidade_id: str) -> QualidadeDado | None:
        model = self._session.get(QualidadeDadoModel, UUID(qualidade_id))
        if model is None or model.deleted_at is not None:
            return None
        return _to_entity(model)

    def get_by_ativo(self, ativo_id: str) -> QualidadeDado | None:
        stmt = select(QualidadeDadoModel).where(
            QualidadeDadoModel.ativo_id == UUID(ativo_id),
            QualidadeDadoModel.deleted_at.is_(None),
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
    ) -> tuple[builtins.list[QualidadeDado], int]:
        stmt = select(QualidadeDadoModel).where(QualidadeDadoModel.deleted_at.is_(None))
        total = len(self._session.scalars(stmt).all())
        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def save(self, qualidade: QualidadeDado) -> QualidadeDado:
        model = self._session.get(QualidadeDadoModel, UUID(qualidade.id))
        if model is None:
            model = QualidadeDadoModel(
                id=UUID(qualidade.id),
                ativo_id=UUID(qualidade.ativo_id),
                nivel=qualidade.nivel.value,
                score=qualidade.score,
                criterios=_format_list(qualidade.criterios),
                observacao=qualidade.observacao,
                created_at=qualidade.created_at,
            )
            self._session.add(model)
            logger.info("Qualidade de dados inserida: %s", qualidade.id)
        else:
            model.ativo_id = UUID(qualidade.ativo_id)
            model.nivel = qualidade.nivel.value
            model.score = qualidade.score
            model.criterios = _format_list(qualidade.criterios)
            model.observacao = qualidade.observacao
            model.updated_at = qualidade.updated_at
            logger.info("Qualidade de dados atualizada: %s", qualidade.id)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def delete(self, qualidade_id: str) -> bool:
        from sqlalchemy import func
        model = self._session.get(QualidadeDadoModel, UUID(qualidade_id))
        if model is None:
            return False
        if model.deleted_at is None:
            model.deleted_at = func.now()
        self._session.flush()
        return True

    def exists_by_ativo(self, ativo_id: str) -> bool:
        stmt = select(QualidadeDadoModel.id).where(
            QualidadeDadoModel.ativo_id == UUID(ativo_id),
            QualidadeDadoModel.deleted_at.is_(None),
        ).limit(1)
        return self._session.scalars(stmt).first() is not None


__all__ = ["SqlAlchemyQualidadeRepository"]
