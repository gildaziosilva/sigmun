"""Repositório SQLAlchemy para AssinaturaDocumento."""

from typing import List, Optional
import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioAssinatura
from ...domain.entities import AssinaturaDocumento
from ..database.models import AssinaturaDocumentoModel


class SQLAlchemyAssinaturaRepository(RepositorioAssinatura):
    """Implementação de repositório para AssinaturaDocumento."""

    def __init__(self, session: Session):
        self._session = session

    def save(self, assinatura: AssinaturaDocumento) -> AssinaturaDocumento:
        model = AssinaturaDocumentoModel(
            id=uuid.UUID(assinatura.id),
            documento_id=uuid.UUID(assinatura.documento_id),
            signatario_id=assinatura.signatario_id,
            data_assinatura=assinatura.data_assinatura,
            hash_assinatura=assinatura.hash_assinatura,
            certificado_id=assinatura.certificado_id,
            is_valida=assinatura.is_valida,
            is_revogada=assinatura.is_revogada,
        )
        self._session.add(model)
        self._session.flush()
        return assinatura

    def get_by_id(self, id: str) -> Optional[AssinaturaDocumento]:
        model = self._session.query(AssinaturaDocumentoModel).filter(
            AssinaturaDocumentoModel.id == uuid.UUID(id)
        ).first()
        if not model:
            return None
        return self._to_entity(model)

    def find_by_documento(self, documento_id: str) -> List[AssinaturaDocumento]:
        models = self._session.query(AssinaturaDocumentoModel).filter(
            AssinaturaDocumentoModel.documento_id == uuid.UUID(documento_id)
        ).order_by(AssinaturaDocumentoModel.data_assinatura.desc()).all()
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: AssinaturaDocumentoModel) -> AssinaturaDocumento:
        return AssinaturaDocumento(
            id=str(model.id),
            documento_id=str(model.documento_id),
            signatario_id=model.signatario_id,
            data_assinatura=model.data_assinatura,
            hash_assinatura=model.hash_assinatura,
            certificado_id=model.certificado_id or "",
            is_valida=model.is_valida,
            is_revogada=model.is_revogada,
        )
