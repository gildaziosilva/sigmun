"""Repositório SQLAlchemy de divisões territoriais (DOM-TEL)."""

from __future__ import annotations

import uuid
from typing import TypeVar

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioBairro
from ...domain.entities import Bairro, SituacaoBairro, TipoBairro
from ..database.models import BairroModel


def to_uuid(valor: str) -> uuid.UUID | None:
    """Converte o identificador textual em UUID.

    Retorna `None` quando o valor não é um UUID válido. O identificador é opaco
    na borda HTTP, então um valor malformado equivale a um recurso inexistente:
    propagar `ValueError` aqui produziria HTTP 500 nas operações de escrita,
    que não traduzem essa exceção. Com `None`, os repositórios seguem o mesmo
    caminho de "não encontrado" e a API responde 404.
    """
    try:
        return uuid.UUID(valor)
    except (ValueError, AttributeError, TypeError):
        return None


T = TypeVar("T")


def buscar_ou_um(session: Session, model: type[T], valor: str) -> T | None:
    """Busca a linha pelo identificador, tolerando valor malformado.

    `session.get` exige uma chave primária válida; um identificador opaco que
    não é UUID equivale a registro inexistente e devolve `None`.
    """
    chave = to_uuid(valor)
    if chave is None:
        return None
    return session.get(model, chave)


class SQLAlchemyBairroRepository(RepositorioBairro):
    """Persistência de divisões territoriais."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, bairro: Bairro) -> Bairro:
        """Insere ou atualiza uma divisão territorial."""
        existente = self._session.get(BairroModel, to_uuid(bairro.id))
        if existente is not None:
            existente.codigo = bairro.codigo
            existente.nome = bairro.nome
            existente.tipo = bairro.tipo.value
            existente.populacao_estimada = bairro.populacao_estimada
            existente.area_km2 = bairro.area_km2
            existente.situacao = bairro.situacao.value
            existente.updated_at = bairro.updated_at
            existente.is_deleted = bairro.is_deleted
        else:
            self._session.add(
                BairroModel(
                    id=to_uuid(bairro.id),
                    codigo=bairro.codigo,
                    nome=bairro.nome,
                    tipo=bairro.tipo.value,
                    populacao_estimada=bairro.populacao_estimada,
                    area_km2=bairro.area_km2,
                    situacao=bairro.situacao.value,
                    created_at=bairro.created_at,
                    updated_at=bairro.updated_at,
                    created_by=bairro.created_by,
                    is_deleted=bairro.is_deleted,
                )
            )
        self._session.flush()
        return bairro

    def get_by_id(self, bairro_id: str) -> Bairro | None:
        """Busca divisão territorial por id."""
        model = buscar_ou_um(self._session, BairroModel, bairro_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_codigo(self, codigo: str) -> Bairro | None:
        """Busca divisão territorial pelo código cadastral."""
        model = (
            self._session.query(BairroModel)
            .filter(BairroModel.codigo == codigo, BairroModel.is_deleted.is_(False))
            .first()
        )
        return self._to_entity(model) if model else None

    def list_all(self, page: int = 1, page_size: int = 20) -> list[Bairro]:
        """Lista divisões territoriais paginadas."""
        models = (
            self._session.query(BairroModel)
            .filter(BairroModel.is_deleted.is_(False))
            .order_by(BairroModel.codigo)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: BairroModel) -> Bairro:
        return Bairro(
            id=str(model.id),
            codigo=model.codigo or "",
            nome=model.nome or "",
            tipo=TipoBairro(model.tipo or "bairro"),
            populacao_estimada=int(model.populacao_estimada or 0),
            area_km2=float(model.area_km2 or 0),
            situacao=SituacaoBairro(model.situacao or "ativo"),
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyBairroRepository", "to_uuid"]
