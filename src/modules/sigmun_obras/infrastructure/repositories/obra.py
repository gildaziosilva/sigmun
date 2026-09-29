"""Repositório SQLAlchemy das obras públicas (DOM-OBR)."""

from __future__ import annotations

import uuid
from typing import TypeVar

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioObra
from ...domain.entities import (
    FonteRecurso,
    Obra,
    SituacaoObra,
    TipoContratacao,
    TipoObra,
)
from ..database.models import ObraModel


def to_uuid(valor: str) -> uuid.UUID | None:
    """Converte o identificador textual em UUID, tolerando valor malformado."""
    try:
        return uuid.UUID(valor)
    except (ValueError, AttributeError, TypeError):
        return None


T = TypeVar("T")


def buscar_ou_um(session: Session, model: type[T], valor: str) -> T | None:
    """Busca a linha pelo identificador, tolerando valor malformado."""
    chave = to_uuid(valor)
    if chave is None:
        return None
    return session.get(model, chave)


class SQLAlchemyObraRepository(RepositorioObra):
    """Persistência de obras públicas."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, obra: Obra) -> Obra:
        """Insere ou atualiza uma obra."""
        existente = buscar_ou_um(self._session, ObraModel, obra.id)
        if existente is not None:
            existente.nome = obra.nome
            existente.descricao = obra.descricao or None
            existente.tipo = obra.tipo.value
            existente.situacao = obra.situacao.value
            existente.tipo_contratacao = obra.tipo_contratacao.value
            existente.fonte_recurso = obra.fonte_recurso.value
            existente.valor_orcado = obra.valor_orcado
            existente.valor_contratado = obra.valor_contratado
            existente.valor_mediado = obra.valor_mediado
            existente.valor_pago = obra.valor_pago
            existente.percentual_fisico = obra.percentual_fisico
            existente.percentual_financeiro = obra.percentual_financeiro
            existente.empresa_contratada = obra.empresa_contratada or None
            existente.numero_contrato = obra.numero_contrato or None
            existente.responsavel_tecnico = obra.responsavel_tecnico or None
            existente.endereco = obra.endereco or None
            existente.bairro = obra.bairro or None
            existente.data_inicio_prevista = obra.data_inicio_prevista
            existente.data_fim_prevista = obra.data_fim_prevista
            existente.data_inicio_real = obra.data_inicio_real
            existente.data_fim_real = obra.data_fim_real
            existente.observacao = obra.observacao or None
            existente.updated_at = obra.updated_at
            existente.is_deleted = obra.is_deleted
        else:
            self._session.add(
                ObraModel(
                    id=to_uuid(obra.id),
                    numero=obra.numero,
                    nome=obra.nome,
                    descricao=obra.descricao or None,
                    tipo=obra.tipo.value,
                    situacao=obra.situacao.value,
                    tipo_contratacao=obra.tipo_contratacao.value,
                    fonte_recurso=obra.fonte_recurso.value,
                    valor_orcado=obra.valor_orcado,
                    valor_contratado=obra.valor_contratado,
                    valor_mediado=obra.valor_mediado,
                    valor_pago=obra.valor_pago,
                    percentual_fisico=obra.percentual_fisico,
                    percentual_financeiro=obra.percentual_financeiro,
                    empresa_contratada=obra.empresa_contratada or None,
                    numero_contrato=obra.numero_contrato or None,
                    responsavel_tecnico=obra.responsavel_tecnico or None,
                    endereco=obra.endereco or None,
                    bairro=obra.bairro or None,
                    data_inicio_prevista=obra.data_inicio_prevista,
                    data_fim_prevista=obra.data_fim_prevista,
                    data_inicio_real=obra.data_inicio_real,
                    data_fim_real=obra.data_fim_real,
                    observacao=obra.observacao or None,
                    created_at=obra.created_at,
                    updated_at=obra.updated_at,
                    created_by=obra.created_by or None,
                    is_deleted=obra.is_deleted,
                )
            )
        self._session.flush()
        return obra

    def get_by_id(self, obra_id: str) -> Obra | None:
        """Busca obra por id."""
        model = buscar_ou_um(self._session, ObraModel, obra_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_numero(self, numero: str) -> Obra | None:
        """Busca obra pelo número cadastral."""
        model = (
            self._session.query(ObraModel)
            .filter(ObraModel.numero == numero, ObraModel.is_deleted.is_(False))
            .first()
        )
        return self._to_entity(model) if model else None

    def list_all(
        self, page: int = 1, page_size: int = 20, situacao: str | None = None
    ) -> list[Obra]:
        """Lista obras paginadas, opcionalmente por situação."""
        query = self._session.query(ObraModel).filter(ObraModel.is_deleted.is_(False))
        if situacao:
            query = query.filter(ObraModel.situacao == situacao)
        models = (
            query.order_by(ObraModel.numero)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: ObraModel) -> Obra:
        return Obra(
            id=str(model.id),
            numero=model.numero,
            nome=model.nome,
            descricao=model.descricao or "",
            tipo=TipoObra(model.tipo or "outro"),
            situacao=SituacaoObra(model.situacao or "planejada"),
            tipo_contratacao=TipoContratacao(model.tipo_contratacao or "licitacao"),
            fonte_recurso=FonteRecurso(model.fonte_recurso or "orcamento_proprio"),
            valor_orcado=float(model.valor_orcado or 0),
            valor_contratado=float(model.valor_contratado or 0),
            valor_mediado=float(model.valor_mediado or 0),
            valor_pago=float(model.valor_pago or 0),
            percentual_fisico=float(model.percentual_fisico or 0),
            percentual_financeiro=float(model.percentual_financeiro or 0),
            empresa_contratada=model.empresa_contratada or "",
            numero_contrato=model.numero_contrato or "",
            responsavel_tecnico=model.responsavel_tecnico or "",
            endereco=model.endereco or "",
            bairro=model.bairro or "",
            data_inicio_prevista=model.data_inicio_prevista,
            data_fim_prevista=model.data_fim_prevista,
            data_inicio_real=model.data_inicio_real,
            data_fim_real=model.data_fim_real,
            observacao=model.observacao or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyObraRepository", "to_uuid", "buscar_ou_um"]
