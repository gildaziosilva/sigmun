"""Implementacao SQLAlchemy do repositorio de Credenciais (DOM-SEG).

Implementa o contrato CredencialRepositoryInterface do dominio sobre a tabela
seg credenciais (migracao correspondente).

Observacoes de projeto:
  - O repositorio executa flush (nao commit); a transacao e
    controlada pela sessao da requisicao (ver core get_db).
"""

import logging
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.sigmun_seg.application.interfaces import CredencialRepositoryInterface
from src.modules.sigmun_seg.domain.entities import Credencial
from src.modules.sigmun_seg.infrastructure.database.models import CredencialModel

logger = logging.getLogger(__name__)


def _to_entity(model: CredencialModel):
    return Credencial(
        id=str(model.id),
        usuario_id=model.usuario_id,
        tipo=model.tipo,
        identificador=model.identificador,
        status=model.status,
        validade=model.validade,
        ultimo_uso=model.ultimo_uso,
        tentativas_falhas=model.tentativas_falhas,
        created_at=model.created_at,
        updated_at=model.updated_at,
        is_deleted=model.is_deleted,
    )


def _to_model(entidade: Credencial) -> CredencialModel:
    return CredencialModel(
        id=UUID(entidade.id),
        usuario_id=entidade.usuario_id,
        tipo=entidade.tipo,
        identificador=entidade.identificador,
        status=entidade.status,
        validade=entidade.validade,
        ultimo_uso=entidade.ultimo_uso,
        tentativas_falhas=entidade.tentativas_falhas,
        created_at=entidade.created_at,
        updated_at=entidade.updated_at,
        is_deleted=entidade.is_deleted,
    )


class SqlAlchemyCredencialRepository(CredencialRepositoryInterface):
    """Repositorio de credenciais persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, credencial_id: str) -> Credencial | None:
        model = self._session.get(CredencialModel, UUID(credencial_id))
        if model is None or model.is_deleted:
            return None
        return _to_entity(model)

    def get_by_usuario(self, usuario_id: str) -> list[Credencial]:
        stmt = select(CredencialModel).where(
            CredencialModel.usuario_id == usuario_id,
            CredencialModel.is_deleted.is_(False),
        )
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models]

    def get_by_tipo_e_status(self, tipo: str, status: str) -> list[Credencial]:
        stmt = select(CredencialModel).where(
            CredencialModel.tipo == tipo,
            CredencialModel.status == status,
            CredencialModel.is_deleted.is_(False),
        )
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models]

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        status: str | None = None,
        tipo: str | None = None,
    ) -> tuple[list[Credencial], int]:
        stmt = select(CredencialModel).where(CredencialModel.is_deleted.is_(False))
        count_stmt = select(CredencialModel).where(CredencialModel.is_deleted.is_(False))

        if status is not None:
            stmt = stmt.where(CredencialModel.status == status)
            count_stmt = count_stmt.where(CredencialModel.status == status)

        if tipo is not None:
            stmt = stmt.where(CredencialModel.tipo == tipo)
            count_stmt = count_stmt.where(CredencialModel.tipo == tipo)

        total = len(self._session.scalars(count_stmt).all())

        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def save(self, credencial: Credencial) -> Credencial:
        model = self._session.get(CredencialModel, UUID(credencial.id))
        if model is None:
            model = _to_model(credencial)
            self._session.add(model)
            logger.info("Credencial inserida: %s", credencial.tipo)
        else:
            model.usuario_id = credencial.usuario_id
            model.tipo = credencial.tipo
            model.identificador = credencial.identificador
            model.status = credencial.status
            model.validade = credencial.validade
            model.ultimo_uso = credencial.ultimo_uso
            model.tentativas_falhas = credencial.tentativas_falhas
            model.updated_at = credencial.updated_at
            logger.info("Credencial atualizada: %s", credencial.tipo)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def delete(self, credencial_id: str) -> bool:
        model = self._session.get(CredencialModel, UUID(credencial_id))
        if model is None:
            return False
        if model.is_deleted is False:
            model.is_deleted = True
            model.updated_at = func.now()
        self._session.flush()
        logger.info("Credencial marcada como excluida: %s", credencial_id)
        return True

    def exists_by_identificador(self, identificador: str) -> bool:
        stmt = (
            select(CredencialModel.id)
            .where(CredencialModel.identificador == identificador)
            .where(CredencialModel.is_deleted.is_(False))
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None
