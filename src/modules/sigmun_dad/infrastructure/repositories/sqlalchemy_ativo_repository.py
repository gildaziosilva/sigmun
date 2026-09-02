"""Implementação SQLAlchemy do repositório de Ativos de Dados (DOM-DAD)."""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.modules.sigmun_dad.application.interfaces import AtivoRepositoryInterface
from src.modules.sigmun_dad.domain.entities import (
    AtivoDado,
    QualidadeNivel,
    StatusAtivo,
    TipoAtivoDado,
)
from src.modules.sigmun_dad.infrastructure.database.models import AtivoDadoModel

logger = logging.getLogger(__name__)


def _parse_list(value: str | None) -> list[str]:
    if not value:
        return []
    return [v.strip() for v in value.split(",") if v.strip()]


def _format_list(values: list[str]) -> str:
    return ",".join(values)


def _to_entity(model: AtivoDadoModel) -> AtivoDado:
    return AtivoDado(
        id=str(model.id),
        nome=model.nome,
        descricao=model.descricao or "",
        tipo=TipoAtivoDado(model.tipo),
        status=StatusAtivo(model.status),
        qualidade=QualidadeNivel(model.qualidade),
        dono_id=model.dono_id or "",
        steward_id=model.steward_id or "",
        schema_origem=model.schema_origem or "",
        tabela_origem=model.tabela_origem or "",
        classificacao=model.classificacao or "",
        tags=_parse_list(model.tags),
        metadata=model.metadata_json or {},
        created_at=model.created_at,
        updated_at=model.updated_at,
        is_deleted=model.deleted_at is not None,
    )


class SqlAlchemyAtivoRepository(AtivoRepositoryInterface):
    """Repositório de ativos de dados persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, ativo_id: str) -> AtivoDado | None:
        model = self._session.get(AtivoDadoModel, UUID(ativo_id))
        if model is None or model.deleted_at is not None:
            return None
        return _to_entity(model)

    def get_by_nome(self, nome: str) -> AtivoDado | None:
        stmt = select(AtivoDadoModel).where(
            AtivoDadoModel.nome == nome,
            AtivoDadoModel.deleted_at.is_(None),
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        tipo: str | None = None,
        status: str | None = None,
    ) -> tuple[builtins.list[AtivoDado], int]:
        stmt = select(AtivoDadoModel).where(AtivoDadoModel.deleted_at.is_(None))
        if tipo:
            stmt = stmt.where(AtivoDadoModel.tipo == tipo)
        if status:
            stmt = stmt.where(AtivoDadoModel.status == status)
        total = len(self._session.scalars(stmt).all())
        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def save(self, ativo: AtivoDado) -> AtivoDado:
        model = self._session.get(AtivoDadoModel, UUID(ativo.id))
        if model is None:
            model = AtivoDadoModel(
                id=UUID(ativo.id),
                nome=ativo.nome,
                descricao=ativo.descricao,
                tipo=ativo.tipo.value,
                status=ativo.status.value,
                qualidade=ativo.qualidade.value,
                dono_id=ativo.dono_id,
                steward_id=ativo.steward_id,
                schema_origem=ativo.schema_origem,
                tabela_origem=ativo.tabela_origem,
                classificacao=ativo.classificacao,
                tags=_format_list(ativo.tags),
                metadata_json=ativo.metadata,
                created_at=ativo.created_at,
            )
            self._session.add(model)
            logger.info("Ativo de dado inserido: %s", ativo.id)
        else:
            model.nome = ativo.nome
            model.descricao = ativo.descricao
            model.tipo = ativo.tipo.value
            model.status = ativo.status.value
            model.qualidade = ativo.qualidade.value
            model.dono_id = ativo.dono_id
            model.steward_id = ativo.steward_id
            model.schema_origem = ativo.schema_origem
            model.tabela_origem = ativo.tabela_origem
            model.classificacao = ativo.classificacao
            model.tags = _format_list(ativo.tags)
            model.metadata_json = ativo.metadata
            model.updated_at = ativo.updated_at
            logger.info("Ativo de dado atualizado: %s", ativo.id)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def delete(self, ativo_id: str) -> bool:
        from sqlalchemy import func
        model = self._session.get(AtivoDadoModel, UUID(ativo_id))
        if model is None:
            return False
        if model.deleted_at is None:
            model.deleted_at = func.now()
        self._session.flush()
        return True

    def exists_by_nome(self, nome: str) -> bool:
        stmt = select(AtivoDadoModel.id).where(
            AtivoDadoModel.nome == nome,
            AtivoDadoModel.deleted_at.is_(None),
        ).limit(1)
        return self._session.scalars(stmt).first() is not None


__all__ = ["SqlAlchemyAtivoRepository"]
