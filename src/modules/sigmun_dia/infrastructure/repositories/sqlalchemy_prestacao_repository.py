"""Repositório SQLAlchemy para PrestacaoContas."""

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioPrestacaoContas
from ...domain.entities import PrestacaoContas
from ..database.models import PrestacaoContasModel


class SQLAlchemyPrestacaoContasRepository(RepositorioPrestacaoContas):
    """Implementação de repositório para PrestacaoContas."""

    def __init__(self, session: Session):
        self._session = session

    def save(self, prestacao: PrestacaoContas) -> PrestacaoContas:
        """Insere ou atualiza uma prestação de contas."""
        model_existente = self._session.get(PrestacaoContasModel, uuid.UUID(prestacao.id))
        if model_existente is not None:
            model_existente.diaria_id = prestacao.diaria_id
            model_existente.servidor_id = prestacao.servidor_id
            model_existente.dota_id = prestacao.dota_id
            model_existente.data_vencimento = prestacao.data_vencimento
            model_existente.documento_id = prestacao.documento_id
            model_existente.valor_previsto = prestacao.valor_previsto
            model_existente.valor_apresentado = prestacao.valor_apresentado
            model_existente.valor_glosado = prestacao.valor_glosado
            model_existente.valor_liquido = prestacao.valor_liquido
            model_existente.status = prestacao.status
            model_existente.motivo_glosa = prestacao.motivo_glosa
            model_existente.updated_at = prestacao.updated_at
            model_existente.is_deleted = prestacao.is_deleted
        else:
            model = PrestacaoContasModel(
                id=uuid.UUID(prestacao.id),
                diaria_id=prestacao.diaria_id,
                servidor_id=prestacao.servidor_id,
                dota_id=prestacao.dota_id,
                data_emissao=prestacao.data_emissao,
                data_vencimento=prestacao.data_vencimento,
                documento_id=prestacao.documento_id,
                valor_previsto=prestacao.valor_previsto,
                valor_apresentado=prestacao.valor_apresentado,
                valor_glosado=prestacao.valor_glosado,
                valor_liquido=prestacao.valor_liquido,
                status=prestacao.status,
                motivo_glosa=prestacao.motivo_glosa,
                created_at=prestacao.created_at,
                created_by=prestacao.created_by,
                is_deleted=prestacao.is_deleted,
            )
            self._session.add(model)
        self._session.flush()
        return prestacao

    def get_by_id(self, id: str) -> PrestacaoContas | None:
        """Busca prestação por ID."""
        model = (
            self._session.query(PrestacaoContasModel)
            .filter(PrestacaoContasModel.id == uuid.UUID(id), PrestacaoContasModel.is_deleted == False)
            .first()
        )
        if not model:
            return None
        return self._to_entity(model)

    def get_by_diaria(self, diaria_id: str) -> PrestacaoContas | None:
        """Busca prestação por ID de diária."""
        model = (
            self._session.query(PrestacaoContasModel)
            .filter(PrestacaoContasModel.diaria_id == diaria_id, PrestacaoContasModel.is_deleted == False)
            .first()
        )
        if not model:
            return None
        return self._to_entity(model)

    def find_authors(self) -> list[PrestacaoContas]:
        """Lista prestações abertas."""
        models = (
            self._session.query(PrestacaoContasModel)
            .filter(PrestacaoContasModel.status == "aberta", PrestacaoContasModel.is_deleted == False)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def delete(self, id: str) -> None:
        """Remove logicamente uma prestação."""
        self._session.query(PrestacaoContasModel).filter(PrestacaoContasModel.id == uuid.UUID(id)).update(
            {PrestacaoContasModel.is_deleted: True}
        )
        self._session.flush()

    def _to_entity(self, model: PrestacaoContasModel) -> PrestacaoContas:
        """Converte modelo para entidade de domínio."""
        return PrestacaoContas(
            id=str(model.id),
            diaria_id=model.diaria_id,
            servidor_id=model.servidor_id,
            dota_id=model.dota_id,
            data_emissao=model.data_emissao,
            data_vencimento=model.data_vencimento,
            documento_id=model.documento_id,
            valor_previsto=model.valor_previsto,
            valor_apresentado=model.valor_apresentado,
            valor_glosado=model.valor_glosado,
            valor_liquido=model.valor_liquido,
            status=model.status,
            motivo_glosa=model.motivo_glosa or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=model.is_deleted,
        )
