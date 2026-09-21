"""Repositório SQLAlchemy de lançamentos (DOM-TRI)."""

from __future__ import annotations

import uuid

from sqlalchemy import or_
from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioLancamento
from ...domain.entities.lancamento import (
    Lancamento,
    StatusLancamento,
    TipoTributo,
)
from ..database.models import LancamentoModel


class SQLAlchemyLancamentoRepository(RepositorioLancamento):
    """Persistência de lançamentos."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, lancamento: Lancamento) -> Lancamento:
        """Insere ou atualiza um lançamento."""
        existente = self._session.get(LancamentoModel, uuid.UUID(lancamento.id))
        if existente is not None:
            existente.contribuinte_id = lancamento.contribuinte_id
            existente.imovel_id = lancamento.imovel_id
            existente.tipo_tributo = lancamento.tipo_tributo.value
            existente.exercicio = lancamento.exercicio
            existente.numero_lancamento = lancamento.numero_lancamento
            existente.descricao = lancamento.descricao
            existente.base_calculo = lancamento.base_calculo
            existente.aliquota = lancamento.aliquota
            existente.valor_tributo = lancamento.valor_tributo
            existente.juros = lancamento.juros
            existente.multa = lancamento.multa
            existente.valor_total = lancamento.valor_total
            existente.data_vencimento = lancamento.data_vencimento
            existente.status = lancamento.status.value
            existente.data_pagamento = lancamento.data_pagamento
            existente.updated_at = lancamento.updated_at
            existente.is_deleted = lancamento.is_deleted
        else:
            self._session.add(
                LancamentoModel(
                    id=uuid.UUID(lancamento.id),
                    contribuinte_id=lancamento.contribuinte_id,
                    imovel_id=lancamento.imovel_id,
                    tipo_tributo=lancamento.tipo_tributo.value,
                    exercicio=lancamento.exercicio,
                    numero_lancamento=lancamento.numero_lancamento,
                    descricao=lancamento.descricao,
                    base_calculo=lancamento.base_calculo,
                    aliquota=lancamento.aliquota,
                    valor_tributo=lancamento.valor_tributo,
                    juros=lancamento.juros,
                    multa=lancamento.multa,
                    valor_total=lancamento.valor_total,
                    data_vencimento=lancamento.data_vencimento,
                    status=lancamento.status.value,
                    data_pagamento=lancamento.data_pagamento,
                    created_at=lancamento.created_at,
                    updated_at=lancamento.updated_at,
                    created_by=lancamento.created_by,
                    is_deleted=lancamento.is_deleted,
                )
            )
        self._session.flush()
        return lancamento

    def get_by_id(self, lancamento_id: str) -> Lancamento | None:
        """Busca lançamento por id."""
        model = self._session.get(LancamentoModel, uuid.UUID(lancamento_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_numero(self, numero: str) -> Lancamento | None:
        """Busca lançamento pelo número."""
        model = (
            self._session.query(LancamentoModel)
            .filter(
                LancamentoModel.numero_lancamento == numero,
                LancamentoModel.is_deleted == False,  # noqa: E712
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista lançamentos paginados."""
        models = (
            self._session.query(LancamentoModel)
            .filter(LancamentoModel.is_deleted == False)  # noqa: E712
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def list_abertos_por_contribuinte(self, contribuinte_id: str) -> list:
        """Lista débitos abertos (lançados ou inscritos) do contribuinte."""
        models = (
            self._session.query(LancamentoModel)
            .filter(
                LancamentoModel.contribuinte_id == contribuinte_id,
                LancamentoModel.is_deleted == False,  # noqa: E712
                or_(
                    LancamentoModel.status == StatusLancamento.LANCADO.value,
                    LancamentoModel.status
                    == StatusLancamento.INSCRITO_EM_DIVIDA_ATIVA.value,
                ),
            )
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: LancamentoModel) -> Lancamento:
        return Lancamento(
            id=str(model.id),
            contribuinte_id=model.contribuinte_id or "",
            imovel_id=model.imovel_id or "",
            tipo_tributo=TipoTributo(model.tipo_tributo or "taxa"),
            exercicio=model.exercicio or 0,
            numero_lancamento=model.numero_lancamento or "",
            descricao=model.descricao or "",
            base_calculo=float(model.base_calculo or 0),
            aliquota=float(model.aliquota or 0),
            valor_tributo=float(model.valor_tributo or 0),
            juros=float(model.juros or 0),
            multa=float(model.multa or 0),
            valor_total=float(model.valor_total or 0),
            data_vencimento=model.data_vencimento,
            status=StatusLancamento(model.status or "lancado"),
            data_pagamento=model.data_pagamento,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyLancamentoRepository"]