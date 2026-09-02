"""Implementação SQLAlchemy do repositório da trilha de auditoria.

Implementa o contrato ``TrilhaAuditoriaRepository`` do domínio sobre a
tabela ``auditoria.eventos`` (migration 20260822_01).

Observações de projeto:
  - append-only: apenas INSERT (registrar) e SELECT (list/count);
  - a tabela possui trigger que bloqueia UPDATE/DELETE no banco;
  - o repositório executa ``flush``; a transação é controlada pela sessão
    da requisição (ver core get_db).
"""

from __future__ import annotations

import builtins
import logging
from datetime import datetime
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.sigmun_compras.domain.entities.registro_auditoria import (
    CategoriaEventoAuditoria,
    RegistroAuditoria,
    ResultadoEventoAuditoria,
)
from src.modules.sigmun_compras.domain.repositories.trilha_auditoria_repository import (
    TrilhaAuditoriaRepository,
)
from src.modules.sigmun_compras.infrastructure.database.models import (
    TrilhaAuditoriaModel,
)

logger = logging.getLogger(__name__)


def _to_entity(model: TrilhaAuditoriaModel) -> RegistroAuditoria:
    """Converte um registro ORM em entidade de domínio."""
    return RegistroAuditoria(
        id=model.id,
        ocorrido_em=model.ocorrido_em,
        categoria=CategoriaEventoAuditoria(model.categoria),
        tipo_evento=model.tipo_evento,
        ator_id=model.ator_id,
        ator_perfil=model.ator_perfil,
        origem=model.origem,
        operacao=model.operacao,
        recurso_tipo=model.recurso_tipo,
        recurso_id=model.recurso_id,
        chave_negocio=model.chave_negocio,
        resultado=ResultadoEventoAuditoria(model.resultado),
        correlation_id=model.correlation_id,
        justificativa=model.justificativa,
        detalhes=model.detalhes,
        created_at=model.created_at,
    )


class SqlAlchemyTrilhaAuditoriaRepository(TrilhaAuditoriaRepository):
    """Repositório da trilha de auditoria persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    # -- Contrato do domínio ---------------------------------------------------

    def registrar(self, registro: RegistroAuditoria) -> RegistroAuditoria:
        model = TrilhaAuditoriaModel(
            id=registro.id,
            ocorrido_em=registro.ocorrido_em,
            categoria=registro.categoria.value,
            tipo_evento=registro.tipo_evento,
            ator_id=registro.ator_id,
            ator_perfil=registro.ator_perfil,
            origem=registro.origem,
            operacao=registro.operacao,
            recurso_tipo=registro.recurso_tipo,
            recurso_id=registro.recurso_id,
            chave_negocio=registro.chave_negocio,
            resultado=registro.resultado.value,
            correlation_id=registro.correlation_id,
            justificativa=registro.justificativa,
            detalhes=registro.detalhes,
            created_at=registro.created_at,
        )
        self._session.add(model)
        self._session.flush()
        logger.info("Evento inserido na trilha: %s", registro.tipo_evento)
        return registro

    def list(
        self,
        *,
        data_inicio: datetime | None = None,
        data_fim: datetime | None = None,
        usuario_id: UUID | None = None,
        categoria: CategoriaEventoAuditoria | None = None,
        recurso_tipo: str | None = None,
        recurso_id: UUID | None = None,
        correlation_id: UUID | None = None,
        limit: int | None = None,
        offset: int = 0,
    ) -> builtins.list[RegistroAuditoria]:
        stmt = select(TrilhaAuditoriaModel).order_by(
            TrilhaAuditoriaModel.ocorrido_em.desc()
        )
        if data_inicio is not None:
            stmt = stmt.where(TrilhaAuditoriaModel.ocorrido_em >= data_inicio)
        if data_fim is not None:
            stmt = stmt.where(TrilhaAuditoriaModel.ocorrido_em <= data_fim)
        if usuario_id is not None:
            stmt = stmt.where(TrilhaAuditoriaModel.ator_id == usuario_id)
        if categoria is not None:
            stmt = stmt.where(TrilhaAuditoriaModel.categoria == categoria.value)
        if recurso_tipo is not None:
            stmt = stmt.where(TrilhaAuditoriaModel.recurso_tipo == recurso_tipo)
        if recurso_id is not None:
            stmt = stmt.where(TrilhaAuditoriaModel.recurso_id == recurso_id)
        if correlation_id is not None:
            stmt = stmt.where(TrilhaAuditoriaModel.correlation_id == correlation_id)
        if limit is not None:
            stmt = stmt.limit(limit)
        if offset:
            stmt = stmt.offset(offset)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models]

    def count(
        self,
        *,
        data_inicio: datetime | None = None,
        data_fim: datetime | None = None,
        usuario_id: UUID | None = None,
        categoria: CategoriaEventoAuditoria | None = None,
        recurso_tipo: str | None = None,
        recurso_id: UUID | None = None,
        correlation_id: UUID | None = None,
    ) -> int:
        """Total de eventos para os filtros (envelope de paginação)."""
        stmt = select(func.count()).select_from(TrilhaAuditoriaModel)
        if data_inicio is not None:
            stmt = stmt.where(TrilhaAuditoriaModel.ocorrido_em >= data_inicio)
        if data_fim is not None:
            stmt = stmt.where(TrilhaAuditoriaModel.ocorrido_em <= data_fim)
        if usuario_id is not None:
            stmt = stmt.where(TrilhaAuditoriaModel.ator_id == usuario_id)
        if categoria is not None:
            stmt = stmt.where(TrilhaAuditoriaModel.categoria == categoria.value)
        if recurso_tipo is not None:
            stmt = stmt.where(TrilhaAuditoriaModel.recurso_tipo == recurso_tipo)
        if recurso_id is not None:
            stmt = stmt.where(TrilhaAuditoriaModel.recurso_id == recurso_id)
        if correlation_id is not None:
            stmt = stmt.where(TrilhaAuditoriaModel.correlation_id == correlation_id)
        return int(self._session.scalar(stmt) or 0)


__all__ = ["SqlAlchemyTrilhaAuditoriaRepository"]
