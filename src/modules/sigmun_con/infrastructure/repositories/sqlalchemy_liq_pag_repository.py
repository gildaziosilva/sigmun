"""Repositórios SQLAlchemy de liquidação/pagamento (DOM-CON)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioLiquidacao, RepositorioPagamento
from ...domain.entities.liquidacao import Liquidacao, StatusLiquidacao
from ...domain.entities.pagamento import Pagamento, StatusPagamento
from ..database.models import LiquidacaoModel, PagamentoModel


class SQLAlchemyLiquidacaoRepository(RepositorioLiquidacao):
    """Persistência de liquidações."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, liq: Liquidacao) -> Liquidacao:
        """Insere ou atualiza liquidação."""
        ex = self._session.get(LiquidacaoModel, uuid.UUID(liq.id))
        if ex is not None:
            ex.status = liq.status.value
            ex.motivo_cancelamento = liq.motivo_cancelamento
            ex.updated_at = liq.updated_at
            ex.updated_by = liq.updated_by
            ex.is_deleted = liq.is_deleted
        else:
            self._session.add(LiquidacaoModel(
                id=uuid.UUID(liq.id), empenho_id=uuid.UUID(liq.empenho_id),
                numero=liq.numero,
                valor=liq.valor, documento_fiscal=liq.documento_fiscal,
                status=liq.status.value, created_at=liq.created_at,
                created_by=liq.created_by, is_deleted=liq.is_deleted))
        self._session.flush()
        return liq

    def get_by_id(self, liquidacao_id: str) -> Liquidacao | None:
        """Busca liquidação por id."""
        m = self._session.get(LiquidacaoModel, uuid.UUID(liquidacao_id))
        if m is None or m.is_deleted:
            return None
        return Liquidacao(id=str(m.id),
                          empenho_id=str(m.empenho_id) if m.empenho_id else "",
                          numero=m.numero or "", valor=float(m.valor or 0),
                          documento_fiscal=m.documento_fiscal or "",
                          status=StatusLiquidacao(m.status or "registrada"),
                          created_at=m.created_at, updated_at=m.updated_at,
                          created_by=m.created_by or "",
                          updated_by=m.updated_by or "",
                          is_deleted=bool(m.is_deleted))


class SQLAlchemyPagamentoRepository(RepositorioPagamento):
    """Persistência de pagamentos."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, pag: Pagamento) -> Pagamento:
        """Insere ou atualiza pagamento."""
        ex = self._session.get(PagamentoModel, uuid.UUID(pag.id))
        if ex is not None:
            ex.status = pag.status.value
            ex.motivo_cancelamento = pag.motivo_cancelamento
            ex.updated_at = pag.updated_at
            ex.updated_by = pag.updated_by
            ex.is_deleted = pag.is_deleted
        else:
            self._session.add(PagamentoModel(
                id=uuid.UUID(pag.id),
                liquidacao_id=uuid.UUID(pag.liquidacao_id),
                empenho_id=uuid.UUID(pag.empenho_id),
                numero_ob=pag.numero_ob,
                valor=pag.valor, conta_bancaria=pag.conta_bancaria,
                status=pag.status.value, created_at=pag.created_at,
                created_by=pag.created_by, is_deleted=pag.is_deleted))
        self._session.flush()
        return pag

    def get_by_id(self, pagamento_id: str) -> Pagamento | None:
        """Busca pagamento por id."""
        m = self._session.get(PagamentoModel, uuid.UUID(pagamento_id))
        if m is None or m.is_deleted:
            return None
        return Pagamento(id=str(m.id),
                         liquidacao_id=str(m.liquidacao_id) if m.liquidacao_id else "",
                         empenho_id=str(m.empenho_id) if m.empenho_id else "",
                         numero_ob=m.numero_ob or "",
                         valor=float(m.valor or 0),
                         conta_bancaria=m.conta_bancaria or "",
                         status=StatusPagamento(m.status or "programado"),
                         created_at=m.created_at, updated_at=m.updated_at,
                         created_by=m.created_by or "",
                         updated_by=m.updated_by or "",
                         is_deleted=bool(m.is_deleted))


__all__ = ["SQLAlchemyLiquidacaoRepository", "SQLAlchemyPagamentoRepository"]
