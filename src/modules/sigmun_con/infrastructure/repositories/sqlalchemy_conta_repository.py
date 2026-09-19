"""Repositórios SQLAlchemy de PCASP e lançamentos (DOM-CON)."""

from __future__ import annotations

import json
import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioContaContabil, RepositorioLancamento
from ...domain.entities.conta import ContaContabil
from ...domain.entities.lancamento import (
    LancamentoContabil,
    Partida,
    StatusLancamento,
    TipoPartida,
)
from ..database.models_contabil import ContaContabilModel, LancamentoModel


class SQLAlchemyContaRepository(RepositorioContaContabil):
    """Persistência do PCASP."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, conta: ContaContabil) -> ContaContabil:
        """Insere ou atualiza conta."""
        ex = self._session.get(ContaContabilModel, uuid.UUID(conta.id))
        if ex is not None:
            ex.nome = conta.nome
            ex.ativa = conta.ativa
            ex.aceita_lancamento = conta.aceita_lancamento
        else:
            self._session.add(ContaContabilModel(
                id=uuid.UUID(conta.id), codigo=conta.codigo, nome=conta.nome,
                classe=conta.classe, natureza_saldo=conta.natureza_saldo,
                tipo=conta.tipo, aceita_lancamento=conta.aceita_lancamento,
                ativa=conta.ativa, conta_pai_id=conta.conta_pai_id,
                created_at=conta.created_at, created_by=conta.created_by,
                is_deleted=conta.is_deleted))
        self._session.flush()
        return conta

    def get_by_id(self, conta_id: str) -> ContaContabil | None:
        """Busca conta por id."""
        m = self._session.get(ContaContabilModel, uuid.UUID(conta_id))
        if m is None or m.is_deleted:
            return None
        return self._to_entity(m)

    def get_by_codigo(self, codigo: str) -> ContaContabil | None:
        """Busca conta por código."""
        m = (self._session.query(ContaContabilModel).filter(
            ContaContabilModel.codigo == codigo,
            ContaContabilModel.is_deleted == False).first())  # noqa: E712
        return self._to_entity(m) if m else None

    def _to_entity(self, m: ContaContabilModel) -> ContaContabil:
        return ContaContabil(id=str(m.id), codigo=m.codigo or "",
                             nome=m.nome or "", classe=m.classe or "",
                             natureza_saldo=m.natureza_saldo or "devedora",
                             tipo=m.tipo or "analitica",
                             aceita_lancamento=bool(m.aceita_lancamento),
                             ativa=bool(m.ativa),
                             conta_pai_id=m.conta_pai_id or "",
                             created_at=m.created_at, updated_at=m.updated_at,
                             created_by=m.created_by or "",
                             is_deleted=bool(m.is_deleted))
