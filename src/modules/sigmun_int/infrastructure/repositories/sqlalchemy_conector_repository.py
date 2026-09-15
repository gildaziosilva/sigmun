"""Repositorio SQLAlchemy de conectores oficiales (DOM-INT)."""

import logging
from uuid import UUID

from sqlalchemy import func, select

from src.modules.sigmun_int.application.interfaces import RepositorioConector
from src.modules.sigmun_int.domain.entities import Conector, EstadoConector
from src.modules.sigmun_int.infrastructure.database.models import ConectorModel

logger = logging.getLogger(__name__)


def _to_entity(model: ConectorModel) -> Conector:
    return Conector(
        id=str(model.id),
        codigo=model.codigo,
        nome=model.nome,
        descricao=model.descricao or "",
        provedor=model.provedor or "",
        url_base=model.url_base or "",
        autenticacao_tipo=model.autenticacao_tipo,
        estado=EstadoConector(model.estado),
        config=model.config or {},
        criado_em=model.criado_em,
        atualizado_em=model.atualizado_em,
        is_deleted=model.is_deleted,
    )


class SqlAlchemyConectorRepository(RepositorioConector):
    """Repositorio de conectores oficiales persistido via SQLAlchemy."""

    def __init__(self, session) -> None:
        self._session = session

    def save(self, conector: Conector) -> Conector:
        model = self._session.get(ConectorModel, UUID(conector.id))
        if model is None:
            model = ConectorModel(
                id=UUID(conector.id),
                codigo=conector.codigo,
                nome=conector.nome,
                descricao=conector.descricao or None,
                provedor=conector.provedor or None,
                url_base=conector.url_base or None,
                autenticacao_tipo=conector.autenticacao_tipo,
                estado=conector.estado.value,
                config=conector.config or {},
                is_deleted=conector.is_deleted,
            )
            self._session.add(model)
        else:
            model.codigo = conector.codigo
            model.nome = conector.nome
            model.descricao = conector.descricao or None
            model.provedor = conector.provedor or None
            model.url_base = conector.url_base or None
            model.autenticacao_tipo = conector.autenticacao_tipo
            model.estado = conector.estado.value
            model.config = conector.config or {}
            model.atualizado_em = func.now()
        self._session.flush()
        return conector

    def get_by_id(self, conector_id: str) -> Conector | None:
        model = self._session.get(ConectorModel, UUID(conector_id))
        if model is None or model.is_deleted:
            return None
        return _to_entity(model)

    def get_by_codigo(self, codigo: str) -> Conector | None:
        stmt = select(ConectorModel).where(
            ConectorModel.codigo == codigo, ConectorModel.is_deleted.is_(False)
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def exists_by_codigo(self, codigo: str) -> bool:
        stmt = (
            select(ConectorModel.id)
            .where(ConectorModel.codigo == codigo, ConectorModel.is_deleted.is_(False))
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None

    def list_all(
        self, page: int = 0, page_size: int = 50, estado: str | None = None
    ) -> tuple[list[Conector], int]:
        base = select(ConectorModel).where(ConectorModel.is_deleted.is_(False))
        if estado:
            base = base.where(ConectorModel.estado == estado)
        total = len(self._session.scalars(base).all())
        stmt = base.order_by(ConectorModel.codigo).offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def delete(self, conector_id: str) -> bool:
        model = self._session.get(ConectorModel, UUID(conector_id))
        if model is None:
            return False
        if not model.is_deleted:
            model.is_deleted = True
            model.atualizado_em = func.now()
        self._session.flush()
        return True