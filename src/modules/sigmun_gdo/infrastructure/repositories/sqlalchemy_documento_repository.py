"""Repositório SQLAlchemy para Documento."""

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioDocumento
from ...domain.entities import Documento
from ..database.models import DocumentoModel


class SQLAlchemyDocumentoRepository(RepositorioDocumento):
    """Implementação de repositório para Documento."""

    def __init__(self, session: Session):
        self._session = session

    def save(self, documento: Documento) -> Documento:
        """Insere ou atualiza um documento (insert-or-update)."""
        model_existente = self._session.get(DocumentoModel, uuid.UUID(documento.id))
        if model_existente is not None:
            model_existente.codigo = documento.codigo
            model_existente.numero = documento.numero
            model_existente.ano = documento.ano
            model_existente.tipo_documental_id = documento.tipo_documental_id
            model_existente.titulo = documento.titulo
            model_existente.descricao = documento.descricao
            model_existente.data_criacao = documento.data_criacao
            model_existente.data_recebimento = documento.data_recebimento
            model_existente.data_arquivamento = documento.data_arquivamento
            model_existente.data_encerramento = documento.data_encerramento
            model_existente.data_eliminacao = documento.data_eliminacao
            model_existente.unidade_autor_id = documento.unidade_autor_id
            model_existente.unidade_arquivo_id = documento.unidade_arquivo_id
            model_existente.processo_id = documento.processo_id
            model_existente.status = documento.status.value
            model_existente.is_sigiloso = documento.is_sigiloso
            model_existente.conteudo_ref = documento.conteudo_ref
            model_existente.hash_integridade = documento.hash_integridade
            model_existente.updated_at = documento.updated_at  # type: ignore[assignment]
            model_existente.updated_by = documento.updated_by
        else:
            model = DocumentoModel(
                id=uuid.UUID(documento.id),
                codigo=documento.codigo,
                numero=documento.numero,
                ano=documento.ano,
                tipo_documental_id=documento.tipo_documental_id,
                titulo=documento.titulo,
                descricao=documento.descricao,
                data_criacao=documento.data_criacao,
                data_recebimento=documento.data_recebimento,
                data_arquivamento=documento.data_arquivamento,
                data_encerramento=documento.data_encerramento,
                data_eliminacao=documento.data_eliminacao,
                unidade_autor_id=documento.unidade_autor_id,
                unidade_arquivo_id=documento.unidade_arquivo_id,
                processo_id=documento.processo_id,
                status=documento.status.value,
                is_sigiloso=documento.is_sigiloso,
                conteudo_ref=documento.conteudo_ref,
                hash_integridade=documento.hash_integridade,
                created_at=documento.created_at,
                created_by=documento.created_by,
                updated_at=documento.updated_at,
                updated_by=documento.updated_by,
            )
            self._session.add(model)
        self._session.flush()
        return documento

    def get_by_id(self, id: str) -> Documento | None:
        """Busca documento por ID."""
        model = (
            self._session.query(DocumentoModel)
            .filter(DocumentoModel.id == uuid.UUID(id), DocumentoModel.deleted_at.is_(None))
            .first()
        )
        if not model:
            return None
        return self._to_entity(model)

    def get_by_codigo(self, codigo: str, ano: int) -> Documento | None:
        """Busca documento por código e ano."""
        model = (
            self._session.query(DocumentoModel)
            .filter(
                DocumentoModel.codigo == codigo,
                DocumentoModel.ano == ano,
                DocumentoModel.deleted_at.is_(None),
            )
            .first()
        )
        if not model:
            return None
        return self._to_entity(model)

    def find_by_processo(self, processo_id: str) -> list[Documento]:
        """Busca documentos vinculados a um processo."""
        models = (
            self._session.query(DocumentoModel)
            .filter(DocumentoModel.processo_id == processo_id, DocumentoModel.deleted_at.is_(None))
            .all()
        )
        return [self._to_entity(m) for m in models]

    def find_ativos(self) -> list[Documento]:
        """Lista documentos ativos."""
        models = (
            self._session.query(DocumentoModel).filter(DocumentoModel.deleted_at.is_(None)).all()
        )
        return [self._to_entity(m) for m in models]

    def delete(self, id: str) -> None:
        """Remove logicamente um documento."""
        from datetime import datetime, timezone

        self._session.query(DocumentoModel).filter(DocumentoModel.id == uuid.UUID(id)).update(
            {
                DocumentoModel.deleted_at: datetime.now(timezone.utc),
                DocumentoModel.deleted_by: "system",
            }
        )
        self._session.flush()

    def _to_entity(self, model: DocumentoModel) -> Documento:
        """Converte modelo para entidade de domínio."""
        from ...domain.entities import StatusDocumento

        return Documento(
            id=str(model.id),
            codigo=model.codigo,
            numero=model.numero,
            ano=model.ano,
            tipo_documental_id=model.tipo_documental_id,
            titulo=model.titulo,
            descricao=model.descricao or "",
            data_criacao=model.data_criacao,
            data_recebimento=model.data_recebimento,
            data_arquivamento=model.data_arquivamento,
            data_encerramento=model.data_encerramento,
            data_eliminacao=model.data_eliminacao,
            unidade_autor_id=model.unidade_autor_id,
            unidade_arquivo_id=model.unidade_arquivo_id or "",
            processo_id=model.processo_id or "",
            status=StatusDocumento(model.status),
            is_sigiloso=model.is_sigiloso,
            conteudo_ref=model.conteudo_ref or "",
            hash_integridade=model.hash_integridade or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            updated_by=model.updated_by or "",
            is_deleted=model.deleted_at is not None,
        )
