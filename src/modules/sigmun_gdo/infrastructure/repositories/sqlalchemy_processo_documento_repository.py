"""Repositório SQLAlchemy para ProcessoDocumento."""

from typing import List, Optional
import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioProcessoDocumento
from ...domain.entities import ProcessoDocumento
from ..database.models import ProcessoDocumentoModel


class SQLAlchemyProcessoDocumentoRepository(RepositorioProcessoDocumento):
    """Implementação de repositório para ProcessoDocumento."""

    def __init__(self, session: Session):
        self._session = session

    def save(self, processo: ProcessoDocumento) -> ProcessoDocumento:
        model = ProcessoDocumentoModel(
            id=uuid.UUID(processo.id),
            numero=processo.numero,
            ano=processo.ano,
            tipo_processo_id=processo.tipo_processo_id,
            titulo=processo.titulo,
            descricao=processo.descricao,
            unidade_autor_id=processo.unidade_autor_id,
            data_abertura=processo.data_abertura,
            data_encerramento=processo.data_encerramento,
            status=processo.status,
            created_by=processo.created_by,
        )
        self._session.add(model)
        self._session.flush()
        return processo

    def get_by_id(self, id: str) -> Optional[ProcessoDocumento]:
        model = self._session.query(ProcessoDocumentoModel).filter(
            ProcessoDocumentoModel.id == uuid.UUID(id),
            ProcessoDocumentoModel.deleted_at.is_(None),
        ).first()
        if not model:
            return None
        return self._to_entity(model)

    def find_all_abertos(self) -> List[ProcessoDocumento]:
        models = self._session.query(ProcessoDocumentoModel).filter(
            ProcessoDocumentoModel.deleted_at.is_(None),
            ProcessoDocumentoModel.status != "encerrado",
        ).all()
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: ProcessoDocumentoModel) -> ProcessoDocumento:
        return ProcessoDocumento(
            id=str(model.id),
            numero=model.numero,
            ano=model.ano,
            tipo_processo_id=model.tipo_processo_id,
            titulo=model.titulo,
            descricao=model.descricao or "",
            unidade_autor_id=model.unidade_autor_id,
            data_abertura=model.data_abertura,
            data_encerramento=model.data_encerramento,
            status=model.status,
            created_by=model.created_by or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            is_deleted=model.deleted_at is not None,
        )
