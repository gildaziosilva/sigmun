"""Repositório SQLAlchemy para ArquivamentoDocumento."""

from typing import List, Optional
import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioArquivamento
from ...domain.entities import ArquivamentoDocumento
from ..database.models import ArquivamentoDocumentoModel


class SQLAlchemyArquivamentoRepository(RepositorioArquivamento):
    """Implementação de repositório para ArquivamentoDocumento."""

    def __init__(self, session: Session):
        self._session = session

    def save(self, arquivamento: ArquivamentoDocumento) -> ArquivamentoDocumento:
        model = ArquivamentoDocumentoModel(
            id=uuid.UUID(arquivamento.id),
            documento_id=uuid.UUID(arquivamento.documento_id),
            data_arquivamento=arquivamento.data_arquivamento,
            data_restauracao=arquivamento.data_restauracao,
            created_by=arquivamento.created_by,
            observacao=arquivamento.observacao,
        )
        self._session.add(model)
        self._session.flush()
        return arquivamento

    def get_by_id(self, id: str) -> Optional[ArquivamentoDocumento]:
        model = self._session.query(ArquivamentoDocumentoModel).filter(
            ArquivamentoDocumentoModel.id == uuid.UUID(id)
        ).first()
        if not model:
            return None
        return self._to_entity(model)

    def find_by_documento(self, documento_id: str) -> List[ArquivamentoDocumento]:
        models = self._session.query(ArquivamentoDocumentoModel).filter(
            ArquivamentoDocumentoModel.documento_id == uuid.UUID(documento_id)
        ).order_by(ArquivamentoDocumentoModel.data_arquivamento.desc()).all()
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: ArquivamentoDocumentoModel) -> ArquivamentoDocumento:
        return ArquivamentoDocumento(
            id=str(model.id),
            documento_id=str(model.documento_id),
            data_arquivamento=model.data_arquivamento,
            data_restauracao=model.data_restauracao,
            created_by=model.created_by or "",
            observacao=model.observacao or "",
            is_restaurado=model.data_restauracao is not None,
        )
