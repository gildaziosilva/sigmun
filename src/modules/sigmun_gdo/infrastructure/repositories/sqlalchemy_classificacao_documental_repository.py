"""Repositório SQLAlchemy para ClassificacaoDocumental."""

from typing import List, Optional

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioClassificacaoDocumental
from ...domain.entities import ClassificacaoDocumental
from ..database.models import ClassificacaoDocumentalModel


class SQLAlchemyClassificacaoDocumentalRepository(RepositorioClassificacaoDocumental):
    """Implementação de repositório para ClassificacaoDocumental."""

    def __init__(self, session: Session):
        self._session = session

    def save(self, classificacao: ClassificacaoDocumental) -> ClassificacaoDocumental:
        model = ClassificacaoDocumentalModel(
            id=classificacao.id,
            codigo=classificacao.codigo,
            nome=classificacao.nome,
            descricao=classificacao.descricao,
            nivel=classificacao.nivel,
            classificacao_pai_id=classificacao.classificacao_pai_id or None,
            prazo_retencao=classificacao.prazo_retencao,
            unidade_destino_id=classificacao.unidade_destino_id or None,
        )
        self._session.add(model)
        self._session.flush()
        return classificacao

    def get_by_id(self, id: str) -> Optional[ClassificacaoDocumental]:
        model = self._session.query(ClassificacaoDocumentalModel).filter(
            ClassificacaoDocumentalModel.id == id,
            ClassificacaoDocumentalModel.deleted_at.is_(None),
        ).first()
        if not model:
            return None
        return self._to_entity(model)

    def get_by_codigo(self, codigo: str) -> Optional[ClassificacaoDocumental]:
        model = self._session.query(ClassificacaoDocumentalModel).filter(
            ClassificacaoDocumentalModel.codigo == codigo,
            ClassificacaoDocumentalModel.deleted_at.is_(None),
        ).first()
        if not model:
            return None
        return self._to_entity(model)

    def find_all(self) -> List[ClassificacaoDocumental]:
        models = self._session.query(ClassificacaoDocumentalModel).filter(
            ClassificacaoDocumentalModel.deleted_at.is_(None)
        ).order_by(ClassificacaoDocumentalModel.nivel, ClassificacaoDocumentalModel.codigo).all()
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: ClassificacaoDocumentalModel) -> ClassificacaoDocumental:
        return ClassificacaoDocumental(
            id=str(model.id),
            codigo=model.codigo,
            nome=model.nome,
            descricao=model.descricao or "",
            nivel=model.nivel,
            classificacao_pai_id=model.classificacao_pai_id or "",
            prazo_retencao=model.prazo_retencao,
            unidade_destino_id=model.unidade_destino_id or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            is_deleted=model.deleted_at is not None,
        )
