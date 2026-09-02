"""Implementação SQLAlchemy do repositório de Metadados (DOM-MET)."""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.sigmun_met.application.interfaces import MetadadoRepositoryInterface
from src.modules.sigmun_met.domain.entities import (
    Metadado,
    StatusMetadado,
    TipoDadoMetadado,
)
from src.modules.sigmun_met.infrastructure.database.models import MetadadoModel

logger = logging.getLogger(__name__)


def _parse_list(value: str | None) -> list[str]:
    if not value:
        return []
    return [v.strip() for v in value.split(",") if v.strip()]


def _format_list(values: list[str]) -> str:
    return ",".join(values)


def _to_entity(model: MetadadoModel) -> Metadado:
    return Metadado(
        id=str(model.id),
        codigo=model.codigo,
        nome=model.nome,
        descricao=model.descricao or "",
        tipo_dado=TipoDadoMetadado(model.tipo_dado),
        obrigatorio=model.obrigatorio,
        multi_valor=model.multi_valor,
        aplicavel_a=_parse_list(model.aplicavel_a),
        valor_padrao=model.valor_padrao or "",
        status=StatusMetadado(model.status),
        created_at=model.created_at,
        updated_at=model.updated_at,
        is_deleted=model.deleted_at is not None,
    )


class SqlAlchemyMetadadoRepository(MetadadoRepositoryInterface):
    """Repositório de metadados persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, metadado_id: str) -> Metadado | None:
        model = self._session.get(MetadadoModel, UUID(metadado_id))
        if model is None or model.deleted_at is not None:
            return None
        return _to_entity(model)

    def get_by_codigo(self, codigo: str) -> Metadado | None:
        stmt = select(MetadadoModel).where(
            MetadadoModel.codigo == codigo,
            MetadadoModel.deleted_at.is_(None),
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        status: str | None = None,
        tipo_dado: str | None = None,
    ) -> tuple[builtins.list[Metadado], int]:
        stmt = select(MetadadoModel).where(MetadadoModel.deleted_at.is_(None))
        if status:
            stmt = stmt.where(MetadadoModel.status == status)
        if tipo_dado:
            stmt = stmt.where(MetadadoModel.tipo_dado == tipo_dado)
        total = len(self._session.scalars(stmt).all())
        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def save(self, metadado: Metadado) -> Metadado:
        model = self._session.get(MetadadoModel, UUID(metadado.id))
        if model is None:
            model = MetadadoModel(
                id=UUID(metadado.id),
                codigo=metadado.codigo,
                nome=metadado.nome,
                descricao=metadado.descricao,
                tipo_dado=metadado.tipo_dado.value,
                obrigatorio=metadado.obrigatorio,
                multi_valor=metadado.multi_valor,
                aplicavel_a=_format_list(metadado.aplicavel_a),
                valor_padrao=metadado.valor_padrao,
                status=metadado.status.value,
                created_at=metadado.created_at,
            )
            self._session.add(model)
            logger.info("Metadado inserido: %s", metadado.id)
        else:
            model.nome = metadado.nome
            model.descricao = metadado.descricao
            model.tipo_dado = metadado.tipo_dado.value
            model.obrigatorio = metadado.obrigatorio
            model.multi_valor = metadado.multi_valor
            model.aplicavel_a = _format_list(metadado.aplicavel_a)
            model.valor_padrao = metadado.valor_padrao
            model.status = metadado.status.value
            model.updated_at = metadado.updated_at
            logger.info("Metadado atualizado: %s", metadado.id)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def delete(self, metadado_id: str) -> bool:
        model = self._session.get(MetadadoModel, UUID(metadado_id))
        if model is None:
            return False
        if model.deleted_at is None:
            model.deleted_at = func.now()
        self._session.flush()
        return True

    def exists_by_codigo(self, codigo: str) -> bool:
        stmt = select(MetadadoModel.id).where(
            MetadadoModel.codigo == codigo,
            MetadadoModel.deleted_at.is_(None),
        ).limit(1)
        return self._session.scalars(stmt).first() is not None


__all__ = ["SqlAlchemyMetadadoRepository"]
