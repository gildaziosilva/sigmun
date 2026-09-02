"""Implementação SQLAlchemy do repositório de Contratos.

Implementa o contrato ``ContratoRepository`` do domínio sobre a tabela
``compras.contratos`` (migration 20260820_01).

Observações de projeto:
  - O repositório executa ``flush`` (não ``commit``); a transação é
    controlada pela sessão da requisição (ver core get_db).
  - ``deleted_at`` é gerado pelo servidor do banco (constraint
    ``ck_contratos_deleted``).
"""

from __future__ import annotations

import logging
from typing import List, Optional
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.sigmun_compras.domain.entities.contrato import (
    Contrato,
    SituacaoContrato,
)
from src.modules.sigmun_compras.domain.repositories.contrato_repository import (
    ContratoRepository,
)
from src.modules.sigmun_compras.infrastructure.database.models import (
    ContratoModel,
    FornecedorModel,
)

logger = logging.getLogger(__name__)


def _to_entity(model: ContratoModel) -> Contrato:
    """Converte um registro ORM em entidade de domínio."""
    return Contrato(
        id=model.id,
        processo_documental_id=model.processo_documental_id,
        fornecedor_id=model.fornecedor_id,
        unidade_id=model.unidade_id,
        licitacao_master_id=model.licitacao_master_id,
        compra_id=model.compra_id,
        numero=model.numero,
        data_inicio=model.data_inicio,
        data_fim=model.data_fim,
        valor=model.valor,
        objeto=model.objeto,
        situacao=SituacaoContrato(model.situacao),
        created_at=model.created_at,
        created_by=model.created_by,
        updated_at=model.updated_at,
        updated_by=model.updated_by,
        deleted_at=model.deleted_at,
        deleted_by=model.deleted_by,
    )


class SqlAlchemyContratoRepository(ContratoRepository):
    """Repositório de contratos persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    # -- Contrato do domínio ---------------------------------------------------

    def save(self, contrato: Contrato) -> Contrato:
        model = self._session.get(ContratoModel, contrato.id)
        if model is None:
            model = ContratoModel(
                id=contrato.id,
                processo_documental_id=contrato.processo_documental_id,
                fornecedor_id=contrato.fornecedor_id,
                unidade_id=contrato.unidade_id,
                licitacao_master_id=contrato.licitacao_master_id,
                compra_id=contrato.compra_id,
                numero=contrato.numero,
                data_inicio=contrato.data_inicio,
                data_fim=contrato.data_fim,
                valor=contrato.valor,
                objeto=contrato.objeto,
                situacao=contrato.situacao.value,
                created_at=contrato.created_at,
                created_by=contrato.created_by,
                updated_at=contrato.updated_at,
                updated_by=contrato.updated_by,
            )
            self._session.add(model)
            logger.info("Contrato inserido: %s", contrato.id)
        else:
            model.processo_documental_id = contrato.processo_documental_id
            model.fornecedor_id = contrato.fornecedor_id
            model.unidade_id = contrato.unidade_id
            model.licitacao_master_id = contrato.licitacao_master_id
            model.compra_id = contrato.compra_id
            model.numero = contrato.numero
            model.data_inicio = contrato.data_inicio
            model.data_fim = contrato.data_fim
            model.valor = contrato.valor
            model.objeto = contrato.objeto
            model.situacao = contrato.situacao.value
            model.updated_at = contrato.updated_at
            model.updated_by = contrato.updated_by
            model.deleted_at = contrato.deleted_at
            model.deleted_by = contrato.deleted_by
            logger.info("Contrato atualizado: %s", contrato.id)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def get_by_id(self, contrato_id: UUID) -> Optional[Contrato]:
        model = self._session.get(ContratoModel, contrato_id)
        return _to_entity(model) if model else None

    def list(
        self,
        situacao: Optional[SituacaoContrato] = None,
        fornecedor_id: Optional[UUID] = None,
        unidade_id: Optional[UUID] = None,
        include_deleted: bool = False,
        limit: Optional[int] = None,
        offset: int = 0,
    ) -> List[Contrato]:
        stmt = select(ContratoModel).order_by(ContratoModel.created_at.desc())
        if not include_deleted:
            stmt = stmt.where(ContratoModel.deleted_at.is_(None))
        if situacao is not None:
            stmt = stmt.where(ContratoModel.situacao == situacao.value)
        if fornecedor_id is not None:
            stmt = stmt.where(ContratoModel.fornecedor_id == fornecedor_id)
        if unidade_id is not None:
            stmt = stmt.where(ContratoModel.unidade_id == unidade_id)
        if limit is not None:
            stmt = stmt.limit(limit)
        if offset:
            stmt = stmt.offset(offset)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models]

    def update(self, contrato: Contrato) -> Contrato:
        return self.save(contrato)

    def delete(self, contrato_id: UUID, usuario_id: UUID) -> None:
        """Soft-delete: preserva histórico (auditoria)."""
        model = self._session.get(ContratoModel, contrato_id)
        if model is None:
            return
        if model.deleted_at is None:
            model.deleted_at = func.now()
        model.deleted_by = usuario_id
        self._session.flush()
        logger.info("Contrato marcado como excluído: %s", contrato_id)

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

    def exists_numero(self, numero: str, excluir_id: Optional[UUID] = None) -> bool:
        """RN-COMPRAS-036: identificação única entre não excluídos."""
        stmt = select(ContratoModel.id).where(
            ContratoModel.numero == numero,
            ContratoModel.deleted_at.is_(None),
        )
        if excluir_id is not None:
            stmt = stmt.where(ContratoModel.id != excluir_id)
        return self._session.scalars(stmt.limit(1)).first() is not None

    def exists_compra(self, compra_id: UUID) -> bool:
        """RN-COMPRAS-025: a compra referenciada deve existir."""
        from src.modules.sigmun_compras.infrastructure.database.models import (
            CompraModel,
        )

        stmt = (
            select(CompraModel.id)
            .where(
                CompraModel.id == compra_id,
                CompraModel.deleted_at.is_(None),
            )
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None


__all__ = ["SqlAlchemyContratoRepository"]
