"""Implementacao SQLAlchemy do repositorio de Chaves Criptograficas (DOM-SEG).

Implementa o contrato ChaveCriptograficaRepositoryInterface do dominio sobre a tabela
seg chaves_criptograficas (migracao correspondente).

Observacoes de projeto:
  - O repositorio executa flush (nao commit); a transacao e
    controlada pela sessao da requisicao (ver core get_db).
"""

import logging
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.sigmun_seg.application.interfaces import ChaveCriptograficaRepositoryInterface
from src.modules.sigmun_seg.domain.entities import ChaveCriptografica
from src.modules.sigmun_seg.infrastructure.database.models import ChaveCriptograficaModel

logger = logging.getLogger(__name__)


def _to_entity(model: ChaveCriptograficaModel):
    return ChaveCriptografica(
        id=str(model.id),
        nome=model.nome,
        algoritmo=model.algoritmo,
        tipo=model.tipo,
        tamanho_bits=model.tamanho_bits,
        status=model.status,
        data_expiracao=model.data_expiracao,
        responsavel_id=model.responsavel_id,
        created_at=model.created_at,
        updated_at=model.updated_at,
        is_deleted=model.is_deleted,
    )


def _to_model(entidade: ChaveCriptografica) -> ChaveCriptograficaModel:
    return ChaveCriptograficaModel(
        id=UUID(entidade.id),
        nome=entidade.nome,
        algoritmo=entidade.algoritmo,
        tipo=entidade.tipo,
        tamanho_bits=entidade.tamanho_bits,
        status=entidade.status,
        data_expiracao=entidade.data_expiracao,
        responsavel_id=entidade.responsavel_id,
        created_at=entidade.created_at,
        updated_at=entidade.updated_at,
        is_deleted=entidade.is_deleted,
    )


class SqlAlchemyChaveCriptograficaRepository(ChaveCriptograficaRepositoryInterface):
    """Repositorio de chaves criptograficas persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, chave_id: str) -> ChaveCriptografica | None:
        model = self._session.get(ChaveCriptograficaModel, UUID(chave_id))
        if model is None or model.is_deleted:
            return None
        return _to_entity(model)

    def get_by_nome(self, nome: str) -> ChaveCriptografica | None:
        stmt = select(ChaveCriptograficaModel).where(
            ChaveCriptograficaModel.nome == nome,
            ChaveCriptograficaModel.is_deleted.is_(False),
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        status: str | None = None,
    ) -> tuple[list[ChaveCriptografica], int]:
        stmt = select(ChaveCriptograficaModel).where(ChaveCriptograficaModel.is_deleted.is_(False))
        count_stmt = select(ChaveCriptograficaModel).where(
            ChaveCriptograficaModel.is_deleted.is_(False)
        )

        if status is not None:
            stmt = stmt.where(ChaveCriptograficaModel.status == status)
            count_stmt = count_stmt.where(ChaveCriptograficaModel.status == status)

        total = len(self._session.scalars(count_stmt).all())

        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def save(self, chave: ChaveCriptografica) -> ChaveCriptografica:
        model = self._session.get(ChaveCriptograficaModel, UUID(chave.id))
        if model is None:
            model = _to_model(chave)
            self._session.add(model)
            logger.info("Chave criptografica inserida: %s", chave.nome)
        else:
            model.nome = chave.nome
            model.algoritmo = chave.algoritmo
            model.tipo = chave.tipo
            model.tamanho_bits = chave.tamanho_bits
            model.status = chave.status
            model.data_expiracao = chave.data_expiracao
            model.responsavel_id = chave.responsavel_id
            model.updated_at = chave.updated_at
            logger.info("Chave criptografica atualizada: %s", chave.nome)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def delete(self, chave_id: str) -> bool:
        model = self._session.get(ChaveCriptograficaModel, UUID(chave_id))
        if model is None:
            return False
        if model.is_deleted is False:
            model.is_deleted = True
            model.updated_at = func.now()
        self._session.flush()
        logger.info("Chave criptografica marcada como excluida: %s", chave_id)
        return True

    def exists_by_nome(self, nome: str) -> bool:
        stmt = (
            select(ChaveCriptograficaModel.id)
            .where(ChaveCriptograficaModel.nome == nome)
            .where(ChaveCriptograficaModel.is_deleted.is_(False))
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None
