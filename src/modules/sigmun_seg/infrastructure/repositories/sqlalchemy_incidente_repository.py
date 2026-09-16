"""Implementacao SQLAlchemy do repositorio de Incidentes de Seguranca (DOM-SEG).

Implementa o contrato IncidenteSegurancaRepositoryInterface do dominio sobre a tabela
seg incidentes seguranca (migracao correspondente).

Observacoes de projeto:
  - O repositorio executa flush (nao commit); a transacao e
    controlada pela sessao da requisicao (ver core get_db).
"""

import logging
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.sigmun_seg.application.interfaces import IncidenteSegurancaRepositoryInterface
from src.modules.sigmun_seg.domain.entities import (
    IncidenteSeguranca,
    SeveridadeIncidente,
    StatusIncidente,
)
from src.modules.sigmun_seg.infrastructure.database.models import IncidenteSegurancaModel

logger = logging.getLogger(__name__)


def _to_entity(model: IncidenteSegurancaModel) -> IncidenteSeguranca:
    return IncidenteSeguranca(
        id=str(model.id),
        titulo=model.titulo,
        descricao=model.descricao,
        severidade=SeveridadeIncidente(model.severidade),
        impacto=model.impacto,
        categoria=model.categoria,
        relator_id=model.relator_id,
        atribuido_a=model.atribuido_a,
        status=StatusIncidente(model.status),
        created_at=model.created_at,
        updated_at=model.updated_at,
        data_resolucao=model.data_resolucao,
        is_deleted=model.is_deleted,
    )


def _to_model(entidade: IncidenteSeguranca) -> IncidenteSegurancaModel:
    return IncidenteSegurancaModel(
        id=UUID(entidade.id),
        titulo=entidade.titulo,
        descricao=entidade.descricao,
        severidade=entidade.severidade.value,
        impacto=entidade.impacto,
        categoria=entidade.categoria,
        relator_id=entidade.relator_id,
        atribuido_a=entidade.atribuido_a,
        status=entidade.status.value,
        created_at=entidade.created_at,
        updated_at=entidade.updated_at,
        data_resolucao=entidade.data_resolucao,
        is_deleted=entidade.is_deleted,
    )


class SqlAlchemyIncidenteSegurancaRepository(IncidenteSegurancaRepositoryInterface):
    """Repositorio de incidentes de seguranca persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, incidente_id: str) -> IncidenteSeguranca | None:
        model = self._session.get(IncidenteSegurancaModel, UUID(incidente_id))
        if model is None or model.is_deleted:
            return None
        return _to_entity(model)

    def get_by_titulo(self, titulo: str) -> IncidenteSeguranca | None:
        stmt = select(IncidenteSegurancaModel).where(
            IncidenteSegurancaModel.titulo == titulo,
            IncidenteSegurancaModel.is_deleted.is_(False),
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        severidade: str | None = None,
        status: str | None = None,
    ) -> tuple[list[IncidenteSeguranca], int]:
        stmt = select(IncidenteSegurancaModel).where(IncidenteSegurancaModel.is_deleted.is_(False))
        count_stmt = select(IncidenteSegurancaModel).where(
            IncidenteSegurancaModel.is_deleted.is_(False)
        )

        if severidade is not None:
            stmt = stmt.where(IncidenteSegurancaModel.severidade == severidade)
            count_stmt = count_stmt.where(IncidenteSegurancaModel.severidade == severidade)

        if status is not None:
            stmt = stmt.where(IncidenteSegurancaModel.status == status)
            count_stmt = count_stmt.where(IncidenteSegurancaModel.status == status)

        total = len(self._session.scalars(count_stmt).all())

        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def save(self, incidente: IncidenteSeguranca) -> IncidenteSeguranca:
        model = self._session.get(IncidenteSegurancaModel, UUID(incidente.id))
        if model is None:
            model = _to_model(incidente)
            self._session.add(model)
            logger.info("Incidente registrado: %s", incidente.titulo)
        else:
            model.titulo = incidente.titulo
            model.descricao = incidente.descricao
            model.severidade = incidente.severidade.value
            model.impacto = incidente.impacto
            model.categoria = incidente.categoria
            model.relator_id = incidente.relator_id
            model.atribuido_a = incidente.atribuido_a
            model.status = incidente.status.value
            model.updated_at = incidente.updated_at  # type: ignore[assignment]
            logger.info("Incidente atualizado: %s", incidente.titulo)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def delete(self, incidente_id: str) -> bool:
        model = self._session.get(IncidenteSegurancaModel, UUID(incidente_id))
        if model is None:
            return False
        if model.is_deleted is False:
            model.is_deleted = True
            model.updated_at = func.now()  # type: ignore[assignment]
        self._session.flush()
        logger.info("Incidente marcado como excluido: %s", incidente_id)
        return True

    def exists_by_titulo(self, titulo: str) -> bool:
        stmt = (
            select(IncidenteSegurancaModel.id)
            .where(IncidenteSegurancaModel.titulo == titulo)
            .where(IncidenteSegurancaModel.is_deleted.is_(False))
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None
