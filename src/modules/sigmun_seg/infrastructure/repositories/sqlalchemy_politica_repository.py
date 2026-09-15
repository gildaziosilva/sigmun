"""Implementacao SQLAlchemy do repositorio de Politicas de Seguranca (DOM-SEG).

Implementa o contrato PoliticaSegurancaRepositoryInterface do dominio sobre a tabela
seg politicas seguranca (migracao correspondente).

Observacoes de projeto:
  - O repositorio executa flush (nao commit); a transacao e
    controlada pela sessao da requisicao (ver core get_db).
"""
import logging
from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

from src.modules.sigmun_seg.application.interfaces import PoliticaSegurancaRepositoryInterface
from src.modules.sigmun_seg.domain.entities import PoliticaSeguranca
from src.modules.sigmun_seg.infrastructure.database.models import PoliticaSegurancaModel

def _to_entity(model: PoliticaSegurancaModel):
    return PoliticaSeguranca(
        id=str(model.id),
        codigo=model.codigo,
        titulo=model.titulo,
        conteudo=model.conteudo,
        versao=model.versao,
        aprovador_id=model.aprovador_id,
        data_aprovacao=model.data_aprovacao,
        data_revisao=model.data_revisao,
        ativa=model.ativa,
        created_at=model.created_at,
        updated_at=model.updated_at,
        is_deleted=model.is_deleted,
    )


def _to_model(entidade: PoliticaSeguranca) -> PoliticaSegurancaModel:
    return PoliticaSegurancaModel(
        id=UUID(entidade.id),
        codigo=entidade.codigo,
        titulo=entidade.titulo,
        conteudo=entidade.conteudo,
        versao=entidade.versao,
        aprovador_id=entidade.aprovador_id,
        data_aprovacao=entidade.data_aprovacao,
        data_revisao=entidade.data_revisao,
        ativa=entidade.ativa,
        created_at=entidade.created_at,
        updated_at=entidade.updated_at,
        is_deleted=entidade.is_deleted,
    )


class SqlAlchemyPoliticaSegurancaRepository(PoliticaSegurancaRepositoryInterface):
    """Repositorio de politicas de seguranca persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, politica_id: str) -> PoliticaSeguranca | None:
        model = self._session.get(PoliticaSegurancaModel, UUID(politica_id))
        if model is None or model.is_deleted:
            return None
        return _to_entity(model)

    def get_by_codigo(self, codigo: str) -> PoliticaSeguranca | None:
        stmt = select(PoliticaSegurancaModel).where(
            PoliticaSegurancaModel.codigo == codigo,
            PoliticaSegurancaModel.is_deleted.is_(False),
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        ativa: bool | None = None,
    ) -> tuple[list[PoliticaSeguranca], int]:
        stmt = select(PoliticaSegurancaModel).where(PoliticaSegurancaModel.is_deleted.is_(False))
        count_stmt = select(PoliticaSegurancaModel).where(PoliticaSegurancaModel.is_deleted.is_(False))

        if ativa is not None:
            stmt = stmt.where(PoliticaSegurancaModel.ativa == ativa)
            count_stmt = count_stmt.where(PoliticaSegurancaModel.ativa == ativa)

        total = len(self._session.scalars(count_stmt).all())

        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def save(self, politica: PoliticaSeguranca) -> PoliticaSeguranca:
        model = self._session.get(PoliticaSegurancaModel, UUID(politica.id))
        if model is None:
            model = _to_model(politica)
            self._session.add(model)
            logger.info("Politica inserida: %s", politica.codigo)
        else:
            model.codigo = politica.codigo
            model.titulo = politica.titulo
            model.conteudo = politica.conteudo
            model.versao = politica.versao
            model.aprovador_id = politica.aprovador_id
            model.data_aprovacao = politica.data_aprovacao
            model.data_revisao = politica.data_revisao
            model.ativa = politica.ativa
            model.updated_at = politica.updated_at
            logger.info("Politica atualizada: %s", politica.codigo)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def delete(self, politica_id: str) -> bool:
        from sqlalchemy import func
        model = self._session.get(PoliticaSegurancaModel, UUID(politica_id))
        if model is None:
            return False
        if model.is_deleted is False:
            model.is_deleted = True
            model.updated_at = func.now()
        self._session.flush()
        logger.info("Politica marcada como excluida: %s", politica_id)
        return True

    def exists_by_codigo(self, codigo: str) -> bool:
        stmt = (
            select(PoliticaSegurancaModel.id)
            .where(PoliticaSegurancaModel.codigo == codigo)
            .where(PoliticaSegurancaModel.is_deleted.is_(False))
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None