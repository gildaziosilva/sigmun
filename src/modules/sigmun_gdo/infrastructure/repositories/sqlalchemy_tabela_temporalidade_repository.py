"""Repositório SQLAlchemy para TabelaTemporalidade."""

from typing import List, Optional

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioTabelaTemporalidade
from ...domain.entities import TabelaTemporalidade, TipoDestinacao
from ..database.models import TabelaTemporalidadeModel


class SQLAlchemyTabelaTemporalidadeRepository(RepositorioTabelaTemporalidade):
    """Implementação de repositório para TabelaTemporalidade."""

    def __init__(self, session: Session):
        self._session = session

    def save(self, tabela: TabelaTemporalidade) -> TabelaTemporalidade:
        model = TabelaTemporalidadeModel(
            id=tabela.id,
            codigo=tabela.codigo,
            nome=tabela.nome,
            prazo_tempo=tabela.prazo_tempo,
            unidade_tempo=tabela.unidade_tempo,
            evento_fim=tabela.evento_fim,
            tipo_destinacao=tabela.tipo_destinacao.value,
            is_ativo=tabela.is_ativo,
        )
        self._session.add(model)
        self._session.flush()
        return tabela

    def get_by_id(self, id: str) -> Optional[TabelaTemporalidade]:
        model = self._session.query(TabelaTemporalidadeModel).filter(
            TabelaTemporalidadeModel.id == id,
            TabelaTemporalidadeModel.deleted_at.is_(None),
            TabelaTemporalidadeModel.is_ativo == True,
        ).first()
        if not model:
            return None
        return self._to_entity(model)

    def get_by_codigo(self, codigo: str) -> Optional[TabelaTemporalidade]:
        model = self._session.query(TabelaTemporalidadeModel).filter(
            TabelaTemporalidadeModel.codigo == codigo,
            TabelaTemporalidadeModel.deleted_at.is_(None),
            TabelaTemporalidadeModel.is_ativo == True,
        ).first()
        if not model:
            return None
        return self._to_entity(model)

    def _to_entity(self, model: TabelaTemporalidadeModel) -> TabelaTemporalidade:
        return TabelaTemporalidade(
            id=str(model.id),
            codigo=model.codigo,
            nome=model.nome,
            prazo_tempo=model.prazo_tempo,
            unidade_tempo=model.unidade_tempo,
            evento_fim=model.evento_fim,
            tipo_destinacao=TipoDestinacao(model.tipo_destinacao),
            is_ativo=model.is_ativo,
            created_at=model.created_at,
            updated_at=model.updated_at,
            is_deleted=model.deleted_at is not None,
        )
