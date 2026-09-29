"""Repositório SQLAlchemy de logradouros públicos (DOM-TEL)."""

from __future__ import annotations

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioLogradouro
from ...domain.entities import Logradouro, SituacaoLogradouro, TipoLogradouro
from ..database.models import LogradouroModel
from .bairro import buscar_ou_um
from .bairro import to_uuid


class SQLAlchemyLogradouroRepository(RepositorioLogradouro):
    """Persistência de logradouros públicos."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, logradouro: Logradouro) -> Logradouro:
        """Insere ou atualiza um logradouro."""
        existente = self._session.get(LogradouroModel, to_uuid(logradouro.id))
        if existente is not None:
            existente.codigo = logradouro.codigo
            existente.nome = logradouro.nome
            existente.tipo = logradouro.tipo.value
            existente.bairro_id = logradouro.bairro_id
            existente.cep = logradouro.cep
            existente.numero_inicial = logradouro.numero_inicial
            existente.numero_final = logradouro.numero_final
            existente.situacao = logradouro.situacao.value
            existente.updated_at = logradouro.updated_at
            existente.is_deleted = logradouro.is_deleted
        else:
            self._session.add(
                LogradouroModel(
                    id=to_uuid(logradouro.id),
                    codigo=logradouro.codigo,
                    nome=logradouro.nome,
                    tipo=logradouro.tipo.value,
                    bairro_id=logradouro.bairro_id,
                    cep=logradouro.cep,
                    numero_inicial=logradouro.numero_inicial,
                    numero_final=logradouro.numero_final,
                    situacao=logradouro.situacao.value,
                    created_at=logradouro.created_at,
                    updated_at=logradouro.updated_at,
                    created_by=logradouro.created_by,
                    is_deleted=logradouro.is_deleted,
                )
            )
        self._session.flush()
        return logradouro

    def get_by_id(self, logradouro_id: str) -> Logradouro | None:
        """Busca logradouro por id."""
        model = buscar_ou_um(self._session, LogradouroModel, logradouro_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_codigo(self, codigo: str) -> Logradouro | None:
        """Busca logradouro pelo código cadastral."""
        model = (
            self._session.query(LogradouroModel)
            .filter(LogradouroModel.codigo == codigo, LogradouroModel.is_deleted.is_(False))
            .first()
        )
        return self._to_entity(model) if model else None

    def list_by_bairro(self, bairro_id: str) -> list[Logradouro]:
        """Lista logradouros de um bairro."""
        models = (
            self._session.query(LogradouroModel)
            .filter(
                LogradouroModel.bairro_id == bairro_id,
                LogradouroModel.is_deleted.is_(False),
            )
            .order_by(LogradouroModel.codigo)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def list_all(self, page: int = 1, page_size: int = 20) -> list[Logradouro]:
        """Lista logradouros paginados."""
        models = (
            self._session.query(LogradouroModel)
            .filter(LogradouroModel.is_deleted.is_(False))
            .order_by(LogradouroModel.codigo)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: LogradouroModel) -> Logradouro:
        return Logradouro(
            id=str(model.id),
            codigo=model.codigo or "",
            nome=model.nome or "",
            tipo=TipoLogradouro(model.tipo or "rua"),
            bairro_id=model.bairro_id or "",
            cep=model.cep or "",
            numero_inicial=int(model.numero_inicial or 0),
            numero_final=int(model.numero_final or 0),
            situacao=SituacaoLogradouro(model.situacao or "ativo"),
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyLogradouroRepository"]
