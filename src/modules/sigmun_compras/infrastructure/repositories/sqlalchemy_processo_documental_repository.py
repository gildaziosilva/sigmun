"""Implementação SQLAlchemy do repositório de Processos Documentais.

Implementa o contrato ``ProcessoDocumentalRepository`` do domínio sobre a
tabela ``core.processos_documentais`` (migration 20260820_01).

Observações de projeto:
  - O repositório executa ``flush`` (não ``commit``); a transação é
    controlada pela sessão da requisição (ver core get_db).
  - ``deleted_at`` é gerado pelo servidor do banco (constraint
    ``ck_processos_documentais_deleted``).
"""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.sigmun_compras.domain.entities.processo_documental import (
    ProcessoDocumental,
)
from src.modules.sigmun_compras.domain.repositories.processo_documental_repository import (
    ProcessoDocumentalRepository,
)
from src.modules.sigmun_compras.infrastructure.database.models import (
    ProcessoDocumentalModel,
)

logger = logging.getLogger(__name__)


def _to_entity(model: ProcessoDocumentalModel) -> ProcessoDocumental:
    """Converte um registro ORM em entidade de domínio."""
    return ProcessoDocumental(
        id=model.id,
        unidade_id=model.unidade_id,
        numero=model.numero,
        ano=model.ano,
        assunto=model.assunto,
        descricao=model.descricao,
        created_at=model.created_at,
        created_by=model.created_by,
        updated_at=model.updated_at,
        updated_by=model.updated_by,
        deleted_at=model.deleted_at,
        deleted_by=model.deleted_by,
    )


class SqlAlchemyProcessoDocumentalRepository(ProcessoDocumentalRepository):
    """Repositório de processos documentais persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    # -- Contrato do domínio ---------------------------------------------------

    def save(self, processo: ProcessoDocumental) -> ProcessoDocumental:
        model = self._session.get(ProcessoDocumentalModel, processo.id)
        if model is None:
            model = ProcessoDocumentalModel(
                id=processo.id,
                unidade_id=processo.unidade_id,
                numero=processo.numero,
                ano=processo.ano,
                assunto=processo.assunto,
                descricao=processo.descricao,
                created_at=processo.created_at,
                created_by=processo.created_by,
                updated_at=processo.updated_at,
                updated_by=processo.updated_by,
            )
            self._session.add(model)
            logger.info("Processo documental inserido: %s", processo.id)
        else:
            model.unidade_id = processo.unidade_id
            model.numero = processo.numero
            model.ano = processo.ano
            model.assunto = processo.assunto
            model.descricao = processo.descricao
            model.updated_at = processo.updated_at
            model.updated_by = processo.updated_by
            model.deleted_at = processo.deleted_at
            model.deleted_by = processo.deleted_by
            logger.info("Processo documental atualizado: %s", processo.id)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def get_by_id(self, processo_id: UUID) -> ProcessoDocumental | None:
        model = self._session.get(ProcessoDocumentalModel, processo_id)
        return _to_entity(model) if model else None

    def list(
        self,
        unidade_id: UUID | None = None,
        ano: int | None = None,
        include_deleted: bool = False,
        limit: int | None = None,
        offset: int = 0,
    ) -> builtins.list[ProcessoDocumental]:
        stmt = select(ProcessoDocumentalModel).order_by(
            ProcessoDocumentalModel.ano.desc(), ProcessoDocumentalModel.numero
        )
        if not include_deleted:
            stmt = stmt.where(ProcessoDocumentalModel.deleted_at.is_(None))
        if unidade_id is not None:
            stmt = stmt.where(ProcessoDocumentalModel.unidade_id == unidade_id)
        if ano is not None:
            stmt = stmt.where(ProcessoDocumentalModel.ano == ano)
        if limit is not None:
            stmt = stmt.limit(limit)
        if offset:
            stmt = stmt.offset(offset)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models]

    def update(self, processo: ProcessoDocumental) -> ProcessoDocumental:
        return self.save(processo)

    def delete(self, processo_id: UUID, usuario_id: UUID) -> None:
        """Soft-delete: preserva histórico (auditoria)."""
        model = self._session.get(ProcessoDocumentalModel, processo_id)
        if model is None:
            return
        if model.deleted_at is None:
            model.deleted_at = func.now()
        model.deleted_by = usuario_id
        self._session.flush()
        logger.info("Processo documental marcado como excluído: %s", processo_id)

    def exists_unidade(self, unidade_id: UUID) -> bool:
        from src.modules.sigmun_compras.infrastructure.database.models import (
            UnidadeAdministrativaModel,
        )

        stmt = (
            select(UnidadeAdministrativaModel.id)
            .where(UnidadeAdministrativaModel.id == unidade_id)
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None

    def exists_numero_ano(
        self, numero: str, ano: int, excluir_id: UUID | None = None
    ) -> bool:
        stmt = select(ProcessoDocumentalModel.id).where(
            ProcessoDocumentalModel.numero == numero,
            ProcessoDocumentalModel.ano == ano,
        )
        if excluir_id is not None:
            stmt = stmt.where(ProcessoDocumentalModel.id != excluir_id)
        return self._session.scalars(stmt.limit(1)).first() is not None


__all__ = ["SqlAlchemyProcessoDocumentalRepository"]
