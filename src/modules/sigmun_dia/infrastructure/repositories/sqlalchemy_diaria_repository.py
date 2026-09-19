"""Repositório SQLAlchemy para Diária."""

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioDiaria
from ...domain.entities import CategoriaDiaria, Diaria, StatusDiaria
from ..database.models import DiariaModel


class SQLAlchemyDiariaRepository(RepositorioDiaria):
    """Implementação de repositório para Diaria."""

    def __init__(self, session: Session):
        self._session = session

    def save(self, diaria: Diaria) -> Diaria:
        """Insere ou atualiza uma diária (insert-or-update)."""
        model_existente = self._session.get(DiariaModel, uuid.UUID(diaria.id))
        if model_existente is not None:
            model_existente.viagem_id = diaria.viagem_id
            model_existente.servidor_id = diaria.servidor_id
            model_existente.dota_id = diaria.dota_id
            model_existente.categoria = diaria.categoria.value
            model_existente.descricao = diaria.descricao
            model_existente.data_inicio = diaria.data_inicio
            model_existente.data_fim = diaria.data_fim
            model_existente.valor_diaria = diaria.valor_diaria
            model_existente.valor_total = diaria.valor_total
            model_existente.status = diaria.status.value
            model_existente.data_autorizacao = diaria.data_autorizacao
            model_existente.data_calculo = diaria.data_calculo
            model_existente.data_concessao = diaria.data_concessao
            model_existente.data_inicio_prestacao = diaria.data_inicio_prestacao
            model_existente.data_fim_prestacao = diaria.data_fim_prestacao
            model_existente.data_pagamento = diaria.data_pagamento
            model_existente.data_aprovacao = diaria.data_aprovacao
            model_existente.data_glosa = diaria.data_glosa
            model_existente.data_restituicao = diaria.data_restituicao
            model_existente.data_cancelamento = diaria.data_cancelamento
            model_existente.motivo_cancelamento = diaria.motivo_cancelamento
            model_existente.motivo_glosa = diaria.motivo_glosa
            model_existente.valor_glosado = diaria.valor_glosado
            model_existente.documento_prestacao_id = diaria.documento_prestacao_id
            model_existente.updated_at = diaria.updated_at
            model_existente.updated_by = diaria.updated_by
            model_existente.is_deleted = diaria.is_deleted
        else:
            model = DiariaModel(
                id=uuid.UUID(diaria.id),
                viagem_id=diaria.viagem_id,
                servidor_id=diaria.servidor_id,
                dota_id=diaria.dota_id,
                categoria=diaria.categoria.value,
                descricao=diaria.descricao,
                data_inicio=diaria.data_inicio,
                data_fim=diaria.data_fim,
                valor_diaria=diaria.valor_diaria,
                valor_total=diaria.valor_total,
                status=diaria.status.value,
                data_solicitacao=diaria.data_solicitacao,
                data_autorizacao=diaria.data_autorizacao,
                data_calculo=diaria.data_calculo,
                data_concessao=diaria.data_concessao,
                data_inicio_prestacao=diaria.data_inicio_prestacao,
                data_fim_prestacao=diaria.data_fim_prestacao,
                data_pagamento=diaria.data_pagamento,
                data_aprovacao=diaria.data_aprovacao,
                data_glosa=diaria.data_glosa,
                data_restituicao=diaria.data_restituicao,
                data_cancelamento=diaria.data_cancelamento,
                motivo_cancelamento=diaria.motivo_cancelamento,
                motivo_glosa=diaria.motivo_glosa,
                valor_glosado=diaria.valor_glosado,
                documento_prestacao_id=diaria.documento_prestacao_id,
                created_at=diaria.created_at,
                created_by=diaria.created_by,
                updated_at=diaria.updated_at,
                updated_by=diaria.updated_by,
                is_deleted=diaria.is_deleted,
            )
            self._session.add(model)
        self._session.flush()
        return diaria

    def get_by_id(self, id: str) -> Diaria | None:
        """Busca diária por ID."""
        model = (
            self._session.query(DiariaModel)
            .filter(DiariaModel.id == uuid.UUID(id), DiariaModel.is_deleted == False)
            .first()
        )
        if not model:
            return None
        return self._to_entity(model)

    def get_by_viagem(self, viagem_id: str) -> Diaria | None:
        """Busca diária por ID de viagem."""
        model = (
            self._session.query(DiariaModel)
            .filter(DiariaModel.viagem_id == viagem_id, DiariaModel.is_deleted == False)
            .first()
        )
        if not model:
            return None
        return self._to_entity(model)

    def find_by_servidor(self, servidor_id: str) -> list[Diaria]:
        """Busca diárias por servidor."""
        models = (
            self._session.query(DiariaModel)
            .filter(DiariaModel.servidor_id == servidor_id, DiariaModel.is_deleted == False)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def find_by_dota(self, dota_id: str) -> list[Diaria]:
        """Busca diárias por dotação."""
        models = (
            self._session.query(DiariaModel)
            .filter(DiariaModel.dota_id == dota_id, DiariaModel.is_deleted == False)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def find_by_status(self, status: str) -> list[Diaria]:
        """Busca diárias por status."""
        models = (
            self._session.query(DiariaModel)
            .filter(DiariaModel.status == status, DiariaModel.is_deleted == False)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def find_ativas(self) -> list[Diaria]:
        """Lista diárias ativas."""
        models = (
            self._session.query(DiariaModel)
            .filter(DiariaModel.is_deleted == False)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def delete(self, id: str) -> None:
        """Remove logicamente uma diária."""
        self._session.query(DiariaModel).filter(DiariaModel.id == uuid.UUID(id)).update(
            {DiariaModel.is_deleted: True}
        )
        self._session.flush()

    def _to_entity(self, model: DiariaModel) -> Diaria:
        """Converte modelo para entidade de domínio."""
        return Diaria(
            id=str(model.id),
            viagem_id=model.viagem_id,
            servidor_id=model.servidor_id,
            dota_id=model.dota_id,
            categoria=CategoriaDiaria(model.categoria),
            descricao=model.descricao or "",
            data_inicio=model.data_inicio,
            data_fim=model.data_fim,
            valor_diaria=model.valor_diaria,
            valor_total=model.valor_total,
            status=StatusDiaria(model.status),
            data_solicitacao=model.data_solicitacao,
            data_autorizacao=model.data_autorizacao,
            data_calculo=model.data_calculo,
            data_concessao=model.data_concessao,
            data_inicio_prestacao=model.data_inicio_prestacao,
            data_fim_prestacao=model.data_fim_prestacao,
            data_pagamento=model.data_pagamento,
            data_aprovacao=model.data_aprovacao,
            data_glosa=model.data_glosa,
            data_restituicao=model.data_restituicao,
            data_cancelamento=model.data_cancelamento,
            motivo_cancelamento=model.motivo_cancelamento or "",
            motivo_glosa=model.motivo_glosa or "",
            valor_glosado=model.valor_glosado,
            documento_prestacao_id=model.documento_prestacao_id,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            updated_by=model.updated_by or "",
            is_deleted=model.is_deleted,
        )
