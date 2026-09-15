"""Repositório SQLAlchemy para TipoDocumental."""

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioTipoDocumental
from ...domain.entities import TipoDocumental
from ..database.models import TipoDocumentalModel


class SQLAlchemyTipoDocumentalRepository(RepositorioTipoDocumental):
    """Implementação de repositório para TipoDocumental."""

    def __init__(self, session: Session):
        self._session = session

    def get_by_codigo(self, codigo: str) -> TipoDocumental | None:
        model = (
            self._session.query(TipoDocumentalModel)
            .filter(
                TipoDocumentalModel.codigo == codigo,
                TipoDocumentalModel.is_ativo.is_(True),
            )
            .first()
        )
        if not model:
            return None
        return self._to_entity(model)

    def find_ativos(self) -> list[TipoDocumental]:
        models = (
            self._session.query(TipoDocumentalModel)
            .filter(TipoDocumentalModel.is_ativo.is_(True))
            .order_by(TipoDocumentalModel.codigo)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def find_all(self) -> list[TipoDocumental]:
        models = self._session.query(TipoDocumentalModel).order_by(TipoDocumentalModel.codigo).all()
        return [self._to_entity(m) for m in models]

    def save(self, tipo: TipoDocumental) -> TipoDocumental:
        existente = (
            self._session.query(TipoDocumentalModel)
            .filter(TipoDocumentalModel.id == tipo.id)
            .first()
        )
        if existente:
            existente.codigo = tipo.codigo
            existente.nome = tipo.nome
            existente.descricao = tipo.descricao
            existente.is_ativo = tipo.is_ativo
            self._session.flush()
        else:
            model = TipoDocumentalModel(
                id=tipo.id,
                codigo=tipo.codigo,
                nome=tipo.nome,
                descricao=tipo.descricao,
                is_ativo=tipo.is_ativo,
            )
            self._session.add(model)
            self._session.flush()
        return tipo

    def _to_entity(self, model: TipoDocumentalModel) -> TipoDocumental:
        return TipoDocumental(
            id=str(model.id),
            codigo=model.codigo,
            nome=model.nome,
            descricao=model.descricao or "",
            is_ativo=model.is_ativo,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )
