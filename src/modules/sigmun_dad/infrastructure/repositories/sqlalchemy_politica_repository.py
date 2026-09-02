"""Implementação SQLAlchemy do repositório de Políticas (DOM-DAD)."""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.modules.sigmun_dad.application.interfaces import PoliticaRepositoryInterface
from src.modules.sigmun_dad.domain.entities import PoliticaDado
from src.modules.sigmun_dad.infrastructure.database.models import PoliticaDadoModel

logger = logging.getLogger(__name__)


def _parse_list(value: str | None) -> list[str]:
    if not value:
        return []
    return [v.strip() for v in value.split(",") if v.strip()]


def _format_list(values: list[str]) -> str:
    return ",".join(values)


def _to_entity(model: PoliticaDadoModel) -> PoliticaDado:
    return PoliticaDado(
        id=str(model.id),
        codigo=model.codigo,
        nome=model.nome,
        descricao=model.descricao or "",
        tipo=model.tipo or "",
        regras=_parse_list(model.regras),
        created_at=model.created_at,
        updated_at=model.updated_at,
        is_deleted=model.deleted_at is not None,
    )


class SqlAlchemyPoliticaRepository(PoliticaRepositoryInterface):
    """Repositório de políticas persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, politica_id: str) -> PoliticaDado | None:
        model = self._session.get(PoliticaDadoModel, UUID(politica_id))
        if model is None or model.deleted_at is not None:
            return None
        return _to_entity(model)

    def get_by_codigo(self, codigo: str) -> PoliticaDado | None:
        stmt = select(PoliticaDadoModel).where(
            PoliticaDadoModel.codigo == codigo,
            PoliticaDadoModel.deleted_at.is_(None),
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
    ) -> tuple[builtins.list[PoliticaDado], int]:
        stmt = select(PoliticaDadoModel).where(PoliticaDadoModel.deleted_at.is_(None))
        total = len(self._session.scalars(stmt).all())
        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def save(self, politica: PoliticaDado) -> PoliticaDado:
        model = self._session.get(PoliticaDadoModel, UUID(politica.id))
        if model is None:
            model = PoliticaDadoModel(
                id=UUID(politica.id),
                codigo=politica.codigo,
                nome=politica.nome,
                descricao=politica.descricao,
                tipo=politica.tipo,
                regras=_format_list(politica.regras),
                created_at=politica.created_at,
            )
            self._session.add(model)
            logger.info("Política inserida: %s", politica.id)
        else:
            model.codigo = politica.codigo
            model.nome = politica.nome
            model.descricao = politica.descricao
            model.tipo = politica.tipo
            model.regras = _format_list(politica.regras)
            model.updated_at = politica.updated_at
            logger.info("Política atualizada: %s", politica.id)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def delete(self, politica_id: str) -> bool:
        from sqlalchemy import func
        model = self._session.get(PoliticaDadoModel, UUID(politica_id))
        if model is None:
            return False
        if model.deleted_at is None:
            model.deleted_at = func.now()
        self._session.flush()
        return True

    def exists_by_codigo(self, codigo: str) -> bool:
        stmt = select(PoliticaDadoModel.id).where(
            PoliticaDadoModel.codigo == codigo,
            PoliticaDadoModel.deleted_at.is_(None),
        ).limit(1)
        return self._session.scalars(stmt).first() is not None


__all__ = ["SqlAlchemyPoliticaRepository"]
