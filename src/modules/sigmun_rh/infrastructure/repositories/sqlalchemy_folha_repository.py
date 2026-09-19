"""Repositorio SQLAlchemy de folhas (DOM-PES)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioFolha
from ...domain.entities.folha import FolhaPagamento, StatusFolha
from ..database.models_folha import FolhaPagamentoModel


class SQLAlchemyFolhaRepository(RepositorioFolha):
    """Persistencia de folhas."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, folha: FolhaPagamento) -> FolhaPagamento:
        """Insere ou atualiza folha."""
        existente = self._session.get(FolhaPagamentoModel, uuid.UUID(folha.id))
        if existente is not None:
            existente.status = folha.status.value
            existente.total_proventos = folha.total_proventos
            existente.total_descontos = folha.total_descontos
            existente.total_liquido = folha.total_liquido
            existente.quantidade_servidores = folha.quantidade_servidores
            existente.data_fechamento = folha.data_fechamento
            existente.data_homologacao = folha.data_homologacao
            existente.data_pagamento = folha.data_pagamento
            existente.updated_at = folha.updated_at
            existente.updated_by = folha.updated_by
            existente.is_deleted = folha.is_deleted
        else:
            self._session.add(
                FolhaPagamentoModel(
                    id=uuid.UUID(folha.id),
                    competencia_ano=folha.competencia_ano,
                    competencia_mes=folha.competencia_mes,
                    descricao=folha.descricao,
                    status=folha.status.value,
                    total_proventos=folha.total_proventos,
                    total_descontos=folha.total_descontos,
                    total_liquido=folha.total_liquido,
                    quantidade_servidores=folha.quantidade_servidores,
                    data_fechamento=folha.data_fechamento,
                    data_homologacao=folha.data_homologacao,
                    data_pagamento=folha.data_pagamento,
                    created_at=folha.created_at,
                    updated_at=folha.updated_at,
                    created_by=folha.created_by,
                    updated_by=folha.updated_by,
                    is_deleted=folha.is_deleted,
                )
            )
        self._session.flush()
        return folha

    def get_by_id(self, folha_id: str) -> FolhaPagamento | None:
        """Busca folha por id."""
        model = self._session.get(FolhaPagamentoModel, uuid.UUID(folha_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_competencia(self, ano: int, mes: int) -> FolhaPagamento | None:
        """Busca folha por competencia."""
        model = (
            self._session.query(FolhaPagamentoModel)
            .filter(
                FolhaPagamentoModel.competencia_ano == ano,
                FolhaPagamentoModel.competencia_mes == mes,
                FolhaPagamentoModel.is_deleted == False,  # noqa: E712
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def _to_entity(self, model: FolhaPagamentoModel) -> FolhaPagamento:
        return FolhaPagamento(
            id=str(model.id),
            competencia_ano=int(model.competencia_ano or 0),
            competencia_mes=int(model.competencia_mes or 0),
            descricao=model.descricao or "",
            status=StatusFolha(model.status or "aberta"),
            total_proventos=float(model.total_proventos or 0),
            total_descontos=float(model.total_descontos or 0),
            total_liquido=float(model.total_liquido or 0),
            quantidade_servidores=int(model.quantidade_servidores or 0),
            data_fechamento=model.data_fechamento,
            data_homologacao=model.data_homologacao,
            data_pagamento=model.data_pagamento,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            updated_by=model.updated_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyFolhaRepository"]
