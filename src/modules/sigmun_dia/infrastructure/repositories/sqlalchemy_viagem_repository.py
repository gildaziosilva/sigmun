"""Repositório SQLAlchemy para Viagem."""

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioViagem
from ...domain.entities import Viagem
from ..database.models import ViagemModel


class SQLAlchemyViagemRepository(RepositorioViagem):
    """Implementação de repositório para Viagem."""

    def __init__(self, session: Session):
        self._session = session

    def save(self, viagem: Viagem) -> Viagem:
        """Insere ou atualiza uma viagem (insert-or-update)."""
        model_existente = self._session.get(ViagemModel, uuid.UUID(viagem.id))
        if model_existente is not None:
            model_existente.servidor_id = viagem.servidor_id
            model_existente.dota_id = viagem.dota_id
            model_existente.motivo = viagem.motivo
            model_existente.cargo_ocupado = viagem.cargo_ocupado
            model_existente.unidade_origem_id = viagem.unidade_origem_id
            model_existente.unidade_destino_id = viagem.unidade_destino_id
            model_existente.data_inicio = viagem.data_inicio
            model_existente.data_fim = viagem.data_fim
            model_existente.destino = viagem.destino
            model_existente.is_antecipacao = viagem.is_antecipacao
            model_existente.updated_at = viagem.updated_at
            model_existente.is_deleted = viagem.is_deleted
        else:
            model = ViagemModel(
                id=uuid.UUID(viagem.id),
                servidor_id=viagem.servidor_id,
                dota_id=viagem.dota_id,
                motivo=viagem.motivo,
                cargo_ocupado=viagem.cargo_ocupado,
                unidade_origem_id=viagem.unidade_origem_id,
                unidade_destino_id=viagem.unidade_destino_id,
                data_inicio=viagem.data_inicio,
                data_fim=viagem.data_fim,
                destino=viagem.destino,
                is_antecipacao=viagem.is_antecipacao,
                created_at=viagem.created_at,
                created_by=viagem.created_by,
                is_deleted=viagem.is_deleted,
            )
            self._session.add(model)
        self._session.flush()
        return viagem

    def get_by_id(self, id: str) -> Viagem | None:
        """Busca viagem por ID."""
        model = (
            self._session.query(ViagemModel)
            .filter(ViagemModel.id == uuid.UUID(id), ViagemModel.is_deleted == False)
            .first()
        )
        if not model:
            return None
        return self._to_entity(model)

    def find_by_servidor(self, servidor_id: str) -> list[Viagem]:
        """Busca viagens por servidor."""
        models = (
            self._session.query(ViagemModel)
            .filter(ViagemModel.servidor_id == servidor_id, ViagemModel.is_deleted == False)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def find_by_dota(self, dota_id: str) -> list[Viagem]:
        """Busca viagens por dotação orçamentária."""
        models = (
            self._session.query(ViagemModel)
            .filter(ViagemModel.dota_id == dota_id, ViagemModel.is_deleted == False)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def find_ativos(self) -> list[Viagem]:
        """Lista viagens ativas."""
        models = (
            self._session.query(ViagemModel)
            .filter(ViagemModel.is_deleted == False)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def delete(self, id: str) -> None:
        """Remove logicamente uma viagem."""
        self._session.query(ViagemModel).filter(ViagemModel.id == uuid.UUID(id)).update(
            {ViagemModel.is_deleted: True}
        )
        self._session.flush()

    def _to_entity(self, model: ViagemModel) -> Viagem:
        """Converte modelo para entidade de domínio."""
        return Viagem(
            id=str(model.id),
            servidor_id=model.servidor_id,
            dota_id=model.dota_id,
            motivo=model.motivo,
            cargo_ocupado=model.cargo_ocupado or "",
            unidade_origem_id=model.unidade_origem_id,
            unidade_destino_id=model.unidade_destino_id,
            data_inicio=model.data_inicio,
            data_fim=model.data_fim,
            destino=model.destino,
            is_antecipacao=model.is_antecipacao,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=model.is_deleted,
        )
