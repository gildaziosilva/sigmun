"""Repositório SQLAlchemy para VersaoDocumento."""

from typing import List, Optional
import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioVersaoDocumento
from ...domain.entities import VersaoDocumento, StatusDocumento
from ..database.models import VersaoDocumentoModel


class SQLAlchemyVersaoDocumentoRepository(RepositorioVersaoDocumento):
    """Implementação de repositório para VersaoDocumento."""

    def __init__(self, session: Session):
        self._session = session

    def save(self, versao: VersaoDocumento) -> VersaoDocumento:
        model = VersaoDocumentoModel(
            id=uuid.UUID(versao.id),
            documento_id=uuid.UUID(versao.documento_id),
            numero_versao=versao.numero_versao,
            conteudo_ref=versao.conteudo_ref,
            hash_integridade=versao.hash_integridade,
            data_versao=versao.data_versao,
            created_by=versao.created_by,
            deleted_at=None,
        )
        self._session.add(model)
        self._session.flush()
        return versao

    def get_by_id(self, id: str) -> Optional[VersaoDocumento]:
        model = self._session.query(VersaoDocumentoModel).filter(
            VersaoDocumentoModel.id == uuid.UUID(id),
            VersaoDocumentoModel.deleted_at.is_(None),
        ).first()
        if not model:
            return None
        return self._to_entity(model)

    def find_by_documento(self, documento_id: str) -> List[VersaoDocumento]:
        models = self._session.query(VersaoDocumentoModel).filter(
            VersaoDocumentoModel.documento_id == uuid.UUID(documento_id),
            VersaoDocumentoModel.deleted_at.is_(None),
        ).order_by(VersaoDocumentoModel.numero_versao.desc()).all()
        return [self._to_entity(m) for m in models]

    def get_ultima_versao(self, documento_id: str) -> Optional[VersaoDocumento]:
        model = self._session.query(VersaoDocumentoModel).filter(
            VersaoDocumentoModel.documento_id == uuid.UUID(documento_id),
            VersaoDocumentoModel.deleted_at.is_(None),
        ).order_by(VersaoDocumentoModel.numero_versao.desc()).first()
        if not model:
            return None
        return self._to_entity(model)

    def _to_entity(self, model: VersaoDocumentoModel) -> VersaoDocumento:
        return VersaoDocumento(
            id=str(model.id),
            documento_id=str(model.documento_id),
            numero_versao=model.numero_versao,
            conteudo_ref=model.conteudo_ref or "",
            hash_integridade=model.hash_integridade or "",
            data_versao=model.data_versao,
            created_by=model.created_by or "",
            is_deleted=model.deleted_at is not None,
        )
