"""Repositórios SQLAlchemy de lançamentos/conciliação (DOM-CON)."""

from __future__ import annotations

import json
import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioConciliacao, RepositorioLancamento
from ...domain.entities.lancamento import (
    ConciliacaoContabil,
    LancamentoContabil,
    Partida,
    StatusConciliacao,
    StatusLancamento,
    TipoPartida,
)
from ..database.models_contabil import ConciliacaoModel, LancamentoModel


class SQLAlchemyLancamentoRepository(RepositorioLancamento):
    """Persistência de lançamentos (partidas em JSON)."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, lanc: LancamentoContabil) -> LancamentoContabil:
        """Insere ou atualiza lançamento."""
        payload = json.dumps([{"conta_id": p.conta_id, "codigo": p.codigo_conta,
                               "tipo": p.tipo.value, "valor": p.valor}
                              for p in lanc.partidas])
        ex = self._session.get(LancamentoModel, uuid.UUID(lanc.id))
        if ex is not None:
            ex.exercicio = lanc.exercicio
            ex.numero = lanc.numero
            ex.historico = lanc.historico
            ex.origem = lanc.origem
            ex.origem_id = lanc.origem_id
            ex.partidas = payload
            ex.total_debito = lanc.total_debito
            ex.total_credito = lanc.total_credito
            ex.status = lanc.status.value
            ex.is_deleted = lanc.is_deleted
        else:
            self._session.add(LancamentoModel(
                id=uuid.UUID(lanc.id), exercicio=lanc.exercicio, numero=lanc.numero,
                historico=lanc.historico, origem=lanc.origem, origem_id=lanc.origem_id,
                partidas=payload, total_debito=lanc.total_debito,
                total_credito=lanc.total_credito, status=lanc.status.value,
                created_at=lanc.created_at, created_by=lanc.created_by,
                is_deleted=lanc.is_deleted))
        self._session.flush()
        return lanc

    def get_by_id(self, lancamento_id: str) -> LancamentoContabil | None:
        """Busca lançamento por id."""
        m = self._session.get(LancamentoModel, uuid.UUID(lancamento_id))
        if m is None or m.is_deleted:
            return None
        raw = json.loads(m.partidas or "[]")
        partidas = [Partida(conta_id=p.get("conta_id", ""),
                            codigo_conta=p.get("codigo", ""),
                            tipo=TipoPartida(p.get("tipo", "debito")),
                            valor=float(p.get("valor", 0))) for p in raw]
        return LancamentoContabil(id=str(m.id), exercicio=int(m.exercicio or 0),
                                  numero=m.numero or "", historico=m.historico or "",
                                  origem=m.origem or "", origem_id=m.origem_id or "",
                                  partidas=partidas,
                                  status=StatusLancamento(m.status or "rascunho"),
                                  created_at=m.created_at,
                                  created_by=m.created_by or "",
                                  is_deleted=bool(m.is_deleted))


class SQLAlchemyConciliacaoRepository(RepositorioConciliacao):
    """Persistência de conciliações."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, conc: ConciliacaoContabil) -> ConciliacaoContabil:
        """Insere ou atualiza conciliação."""
        ex = self._session.get(ConciliacaoModel, uuid.UUID(conc.id))
        if ex is not None:
            ex.saldo_contabil = conc.saldo_contabil
            ex.saldo_extrato = conc.saldo_extrato
            ex.diferenca = conc.diferenca
            ex.status = conc.status.value
            ex.justificativa = conc.justificativa
            ex.data_conciliacao = conc.data_conciliacao
            ex.is_deleted = conc.is_deleted
        else:
            self._session.add(ConciliacaoModel(
                id=uuid.UUID(conc.id), conta_id=conc.conta_id,
                codigo_conta=conc.codigo_conta, competencia_ano=conc.competencia_ano,
                competencia_mes=conc.competencia_mes,
                saldo_contabil=conc.saldo_contabil, saldo_extrato=conc.saldo_extrato,
                diferenca=conc.diferenca, status=conc.status.value,
                justificativa=conc.justificativa,
                data_conciliacao=conc.data_conciliacao,
                created_at=conc.created_at, created_by=conc.created_by,
                is_deleted=conc.is_deleted))
        self._session.flush()
        return conc

    def get_by_id(self, conciliacao_id: str) -> ConciliacaoContabil | None:
        """Busca conciliação por id."""
        m = self._session.get(ConciliacaoModel, uuid.UUID(conciliacao_id))
        if m is None or m.is_deleted:
            return None
        return ConciliacaoContabil(
            id=str(m.id), conta_id=m.conta_id or "",
            codigo_conta=m.codigo_conta or "",
            competencia_ano=int(m.competencia_ano or 0),
            competencia_mes=int(m.competencia_mes or 0),
            saldo_contabil=float(m.saldo_contabil or 0),
            saldo_extrato=float(m.saldo_extrato or 0),
            diferenca=float(m.diferenca or 0),
            status=StatusConciliacao(m.status or "aberta"),
            justificativa=m.justificativa or "",
            data_conciliacao=m.data_conciliacao,
            created_at=m.created_at, created_by=m.created_by or "",
            is_deleted=bool(m.is_deleted))


__all__ = ["SQLAlchemyLancamentoRepository", "SQLAlchemyConciliacaoRepository"]
