"""Repositório SQLAlchemy para TramitacaoDocumento."""

from typing import List, Optional

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioTramitacao
from ...domain.entities import TramitacaoDocumento, TipoTramitacao
from ..database.models import TramitacaoDocumentoModel
import uuid


class SQLAlchemyTramitacaoRepository(RepositorioTramitacao):
    """Implementação de repositório para TramitacaoDocumento."""

    def __init__(self, session: Session):
        self._session = session

    def save(self, tramitacao: TramitacaoDocumento) -> TramitacaoDocumento:
        model = TramitacaoDocumentoModel(
            id=uuid.UUID(tramitacao.id),
            documento_id=uuid.UUID(tramitacao.documento_id),
            unidade_origem_id=tramitacao.unidade_origem_id,
            unidade_destino_id=tramitacao.unidade_destino_id,
            tipo=tramitacao.tipo.value,
            data_envio=tramitacao.data_envio,
            data_recebimento=tramitacao.data_recebimento,
            data_devolucao=tramitacao.data_devolucao,
            motivo=tramitacao.motivo,
            observacao=tramitacao.observacao,
            created_by=tramitacao.created_by,
        )
        self._session.add(model)
        self._session.flush()
        return tramitacao

    def get_by_id(self, id: str) -> Optional[TramitacaoDocumento]:
        model = self._session.query(TramitacaoDocumentoModel).filter(
            TramitacaoDocumentoModel.id == uuid.UUID(id)
        ).first()
        if not model:
            return None
        return self._to_entity(model)

    def find_by_documento(self, documento_id: str) -> List[TramitacaoDocumento]:
        models = self._session.query(TramitacaoDocumentoModel).filter(
            TramitacaoDocumentoModel.documento_id == uuid.UUID(documento_id)
        ).order_by(TramitacaoDocumentoModel.created_at.desc()).all()
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: TramitacaoDocumentoModel) -> TramitacaoDocumento:
        return TramitacaoDocumento(
            id=str(model.id),
            documento_id=str(model.documento_id),
            unidade_origem_id=model.unidade_origem_id,
            unidade_destino_id=model.unidade_destino_id,
            tipo=TipoTramitacao(model.tipo),
            data_envio=model.data_envio,
            data_recebimento=model.data_recebimento,
            data_devolucao=model.data_devolucao,
            motivo=model.motivo or "",
            observacao=model.observacao or "",
            created_by=model.created_by or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
        )
