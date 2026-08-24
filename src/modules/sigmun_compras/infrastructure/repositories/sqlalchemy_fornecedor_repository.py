"""Implementação SQLAlchemy do repositório de Fornecedores.

Implementa o contrato ``FornecedorRepository`` do domínio sobre a tabela
``core.fornecedores`` (migration 20260820_01).

Observações de projeto:
  - O repositório executa ``flush`` (não ``commit``); a transação é
    controlada pela sessão da requisição (ver core get_db).
  - RN-COMPRAS-031: a unicidade cadastral considera também registros
    logicamente excluídos, espelhando a constraint UNIQUE da tabela.
"""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.sigmun_compras.domain.entities.fornecedor import (
    Fornecedor,
    SituacaoFornecedor,
)
from src.modules.sigmun_compras.domain.repositories.fornecedor_repository import (
    FornecedorRepository,
)
from src.modules.sigmun_compras.infrastructure.database.models import FornecedorModel

logger = logging.getLogger(__name__)


def _to_entity(model: FornecedorModel) -> Fornecedor:
    """Converte um registro ORM em entidade de domínio."""
    return Fornecedor(
        id=model.id,
        pessoa_juridica_id=model.pessoa_juridica_id,
        situacao_cadastro=SituacaoFornecedor(model.situacao_cadastro),
        macro_categoria=model.macro_categoria,
        created_at=model.created_at,
        created_by=model.created_by,
        updated_at=model.updated_at,
        updated_by=model.updated_by,
        deleted_at=model.deleted_at,
        deleted_by=model.deleted_by,
    )


class SqlAlchemyFornecedorRepository(FornecedorRepository):
    """Repositório de fornecedores persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    # -- Helpers -------------------------------------------------------------

    def _get_model(self, fornecedor_id: UUID) -> FornecedorModel | None:
        return self._session.get(FornecedorModel, fornecedor_id)

    # -- Contrato do domínio ---------------------------------------------------

    def save(self, fornecedor: Fornecedor) -> Fornecedor:
        model = self._get_model(fornecedor.id)
        if model is None:
            model = FornecedorModel(
                id=fornecedor.id,
                pessoa_juridica_id=fornecedor.pessoa_juridica_id,
                situacao_cadastro=fornecedor.situacao_cadastro.value,
                macro_categoria=fornecedor.macro_categoria,
                created_at=fornecedor.created_at,
                created_by=fornecedor.created_by,
                updated_at=fornecedor.updated_at,
                updated_by=fornecedor.updated_by,
            )
            self._session.add(model)
            logger.info("Fornecedor inserido: %s", fornecedor.id)
        else:
            model.situacao_cadastro = fornecedor.situacao_cadastro.value
            model.macro_categoria = fornecedor.macro_categoria
            model.updated_at = fornecedor.updated_at
            model.updated_by = fornecedor.updated_by
            model.deleted_at = fornecedor.deleted_at
            model.deleted_by = fornecedor.deleted_by
            logger.info("Fornecedor atualizado: %s", fornecedor.id)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def get_by_id(self, fornecedor_id: UUID) -> Fornecedor | None:
        model = self._get_model(fornecedor_id)
        return _to_entity(model) if model else None

    def get_by_pessoa_juridica_id(self, pessoa_juridica_id: UUID) -> Fornecedor | None:
        stmt = select(FornecedorModel).where(
            FornecedorModel.pessoa_juridica_id == pessoa_juridica_id
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def list(
        self,
        situacao: SituacaoFornecedor | None = None,
        include_deleted: bool = False,
        limit: int | None = None,
        offset: int = 0,
    ) -> builtins.list[Fornecedor]:
        stmt = select(FornecedorModel).order_by(FornecedorModel.created_at)
        if not include_deleted:
            stmt = stmt.where(FornecedorModel.deleted_at.is_(None))
        if situacao is not None:
            stmt = stmt.where(FornecedorModel.situacao_cadastro == situacao.value)
        if limit is not None:
            stmt = stmt.limit(limit)
        if offset:
            stmt = stmt.offset(offset)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models]

    def update(self, fornecedor: Fornecedor) -> Fornecedor:
        return self.save(fornecedor)

    def delete(self, fornecedor_id: UUID, usuario_id: UUID) -> None:
        """Soft-delete (RN-COMPRAS-032): preserva histórico.

        ``deleted_at`` é gerado pelo servidor do banco (``NOW()``) para
        satisfazer a constraint ``ck_fornecedores_deleted`` mesmo em
        presença de defasagem de relógio entre aplicação e banco.
        """
        model = self._get_model(fornecedor_id)
        if model is None:
            return
        if model.deleted_at is None:
            model.deleted_at = func.now()
        model.deleted_by = usuario_id
        self._session.flush()
        logger.info("Fornecedor marcado como excluído: %s", fornecedor_id)

    def exists_pessoa_juridica(self, pessoa_juridica_id: UUID) -> bool:
        stmt = (
            select(FornecedorModel.id)
            .where(FornecedorModel.pessoa_juridica_id == pessoa_juridica_id)
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None


__all__ = ["SqlAlchemyFornecedorRepository"]
