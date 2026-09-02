"""Implementação SQLAlchemy do repositório de Compras (processos).

Implementa o contrato ``CompraRepository`` do domínio sobre a tabela
``compras.compras`` (migration 20260820_01).

Observações de projeto:
  - O repositório executa ``flush`` (não ``commit``); a transação é
    controlada pela sessão da requisição (ver core get_db).
  - ``deleted_at`` é gerado pelo servidor do banco (constraint
    ``ck_compras_deleted``).
"""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.sigmun_compras.domain.entities.compra import Compra, SituacaoCompra
from src.modules.sigmun_compras.domain.repositories.compra_repository import (
    CompraRepository,
)
from src.modules.sigmun_compras.infrastructure.database.models import (
    CompraModel,
    FornecedorModel,
)

logger = logging.getLogger(__name__)


def _to_entity(model: CompraModel) -> Compra:
    """Converte um registro ORM em entidade de domínio."""
    return Compra(
        id=model.id,
        processo_documental_id=model.processo_documental_id,
        fornecedor_id=model.fornecedor_id,
        unidade_id=model.unidade_id,
        numero=model.numero,
        data=model.data,
        valor_total=model.valor_total,
        situacao=SituacaoCompra(model.situacao),
        pendencias_impeditivas=model.pendencias_impeditivas,
        created_at=model.created_at,
        created_by=model.created_by,
        updated_at=model.updated_at,
        updated_by=model.updated_by,
        deleted_at=model.deleted_at,
        deleted_by=model.deleted_by,
    )


class SqlAlchemyCompraRepository(CompraRepository):
    """Repositório de compras persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    # -- Contrato do domínio ---------------------------------------------------

    def save(self, compra: Compra) -> Compra:
        model = self._session.get(CompraModel, compra.id)
        if model is None:
            model = CompraModel(
                id=compra.id,
                processo_documental_id=compra.processo_documental_id,
                fornecedor_id=compra.fornecedor_id,
                unidade_id=compra.unidade_id,
                numero=compra.numero,
                data=compra.data,
                valor_total=compra.valor_total,
                situacao=compra.situacao.value,
                pendencias_impeditivas=compra.pendencias_impeditivas,
                created_at=compra.created_at,
                created_by=compra.created_by,
                updated_at=compra.updated_at,
                updated_by=compra.updated_by,
            )
            self._session.add(model)
            logger.info("Compra inserida: %s", compra.id)
        else:
            model.processo_documental_id = compra.processo_documental_id
            model.fornecedor_id = compra.fornecedor_id
            model.unidade_id = compra.unidade_id
            model.numero = compra.numero
            model.data = compra.data
            model.valor_total = compra.valor_total
            model.situacao = compra.situacao.value
            model.pendencias_impeditivas = compra.pendencias_impeditivas
            model.updated_at = compra.updated_at
            model.updated_by = compra.updated_by
            model.deleted_at = compra.deleted_at
            model.deleted_by = compra.deleted_by
            logger.info("Compra atualizada: %s", compra.id)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def get_by_id(self, compra_id: UUID) -> Compra | None:
        model = self._session.get(CompraModel, compra_id)
        return _to_entity(model) if model else None

    def list(
        self,
        situacao: SituacaoCompra | None = None,
        include_deleted: bool = False,
        limit: int | None = None,
        offset: int = 0,
    ) -> builtins.list[Compra]:
        stmt = select(CompraModel).order_by(CompraModel.created_at.desc())
        if not include_deleted:
            stmt = stmt.where(CompraModel.deleted_at.is_(None))
        if situacao is not None:
            stmt = stmt.where(CompraModel.situacao == situacao.value)
        if limit is not None:
            stmt = stmt.limit(limit)
        if offset:
            stmt = stmt.offset(offset)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models]

    def update(self, compra: Compra) -> Compra:
        return self.save(compra)

    def delete(self, compra_id: UUID, usuario_id: UUID) -> None:
        """Soft-delete: preserva histórico (auditoria)."""
        model = self._session.get(CompraModel, compra_id)
        if model is None:
            return
        if model.deleted_at is None:
            model.deleted_at = func.now()
        model.deleted_by = usuario_id
        self._session.flush()
        logger.info("Compra marcada como excluída: %s", compra_id)

    # -- Verificações de vínculo ------------------------------------------------

    def exists_processo_documental(self, processo_documental_id: UUID) -> bool:
        from src.modules.sigmun_compras.infrastructure.database.models import (
            ProcessoDocumentalModel,
        )

        stmt = (
            select(ProcessoDocumentalModel.id)
            .where(ProcessoDocumentalModel.id == processo_documental_id)
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None

    def exists_fornecedor_ativo(self, fornecedor_id: UUID) -> bool:
        stmt = (
            select(FornecedorModel.id)
            .where(
                FornecedorModel.id == fornecedor_id,
                FornecedorModel.situacao_cadastro == "ATIVO",
                FornecedorModel.deleted_at.is_(None),
            )
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None

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


__all__ = ["SqlAlchemyCompraRepository"]
