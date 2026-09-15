"""Implementacao SQLAlchemy do repositorio de Controles de Seguranca (DOM-SEG).

Implementa o contrato ControleSegurancaRepositoryInterface do dominio sobre a tabela
seg controles seguranca (migracao correspondente).

Observacoes de projeto:
  - O repositorio executa flush (nao commit); a transacao e
    controlada pela sessao da requisicao (ver core get_db).
"""
import logging
from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from src.modules.sigmun_seg.application.interfaces import ControleSegurancaRepositoryInterface
from src.modules.sigmun_seg.domain.entities import ControleSeguranca, StatusControle
from src.modules.sigmun_seg.infrastructure.database.models import ControleSegurancaModel

def _to_entity(model: ControleSegurancaModel):
    return ControleSeguranca(
        id=str(model.id),
        codigo=model.codigo,
        nome=model.nome,
        descricao=model.descricao,
        tipo=model.tipo,
        categoria=model.categoria,
        status=StatusControle(model.status),
        responsavel_id=model.responsavel_id,
        nivel_risco=model.nivel_risco if model.nivel_risco else "medio",
        created_at=model.created_at,
        updated_at=model.updated_at,
        is_deleted=model.is_deleted,
    )


logger = logging.getLogger(__name__)


class SqlAlchemyControleSegurancaRepository(ControleSegurancaRepositoryInterface):
    """Repositorio de controles de seguranca persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, controle_id: str):
        model = self._session.get(ControleSegurancaModel, UUID(controle_id))
        if model is None or model.is_deleted:
            return None
        return _to_entity(model)

    def get_by_codigo(self, codigo: str):
        stmt = select(ControleSegurancaModel).where(
            ControleSegurancaModel.codigo == codigo,
            ControleSegurancaModel.is_deleted.is_(False),
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def list_all(self, page=0, page_size=50, status=None, tipo=None, categoria=None):
        stmt = select(ControleSegurancaModel).where(ControleSegurancaModel.is_deleted.is_(False))
        count_stmt = select(ControleSegurancaModel).where(ControleSegurancaModel.is_deleted.is_(False))

        if status is not None:
            stmt = stmt.where(ControleSegurancaModel.status == status)
            count_stmt = count_stmt.where(ControleSegurancaModel.status == status)

        if tipo is not None:
            stmt = stmt.where(ControleSegurancaModel.tipo == tipo)
            count_stmt = count_stmt.where(ControleSegurancaModel.tipo == tipo)

        if categoria is not None:
            stmt = stmt.where(ControleSegurancaModel.categoria == categoria)
            count_stmt = count_stmt.where(ControleSegurancaModel.categoria == categoria)

        total = len(self._session.scalars(count_stmt).all())

        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def save(self, controle: ControleSeguranca) -> ControleSeguranca:
        model = self._session.get(ControleSegurancaModel, UUID(controle.id))
        if model is None:
            model = _to_model(controle)
            self._session.add(model)
            logger.info("Controle inserido: %s", controle.codigo)
        else:
            model.codigo = controle.codigo
            model.nome = controle.nome
            model.descricao = controle.descricao
            model.tipo = controle.tipo
            model.categoria = controle.categoria
            model.status = controle.status.value
            model.nivel_risco = controle.nivel_risco
            model.responsavel_id = controle.responsavel_id
            model.updated_at = controle.updated_at
            logger.info("Controle atualizado: %s", controle.codigo)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def delete(self, controle_id: str) -> bool:
        from sqlalchemy import func
        model = self._session.get(ControleSegurancaModel, UUID(controle_id))
        if model is None:
            return False
        if model.is_deleted is False:
            model.is_deleted = True
            model.updated_at = func.now()
        self._session.flush()
        logger.info("Controle marcado como excluido: %s", controle_id)
        return True

    def exists_by_codigo(self, codigo: str) -> bool:
        stmt = (
            select(ControleSegurancaModel.id)
            .where(ControleSegurancaModel.codigo == codigo)
            .where(ControleSegurancaModel.is_deleted.is_(False))
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None