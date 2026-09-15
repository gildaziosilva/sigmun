"""Repositório SQLAlchemy do catálogo de APIs externas (DOM-INT).

Segue o padrão do DOM-SEG: ``flush`` sem ``commit`` (a transação é
controlada pela sessão da requisição) e exclusão lógica por ``is_deleted``.
"""

import logging
from uuid import UUID

from sqlalchemy import func, select

from src.modules.sigmun_int.application.interfaces import RepositorioApiExterna
from src.modules.sigmun_int.domain.entities import ApiExterna, AutenticacaoApi, EstadoApi, TipoApi
from src.modules.sigmun_int.infrastructure.database.models import ApiExternaModel

logger = logging.getLogger(__name__)


def _para_entidade(model: ApiExternaModel) -> ApiExterna:
    return ApiExterna(
        id=str(model.id),
        codigo=model.codigo,
        nome=model.nome,
        descricao=model.descricao or "",
        provedor=model.provedor or "",
        url_base=model.url_base or "",
        tipo=TipoApi(model.tipo),
        autenticacao=AutenticacaoApi(model.autenticacao),
        estado=EstadoApi(model.estado),
        versao=model.versao,
        limite_por_minuto=model.limite_por_minuto,
        timeout_seg=model.timeout_seg,
        criado_em=model.criado_em,
        atualizado_em=model.atualizado_em,
        is_deleted=model.is_deleted,
    )


def _para_model(api: ApiExterna) -> ApiExternaModel:
    return ApiExternaModel(
        id=UUID(api.id),
        codigo=api.codigo,
        nome=api.nome,
        descricao=api.descricao or None,
        provedor=api.provedor or None,
        url_base=api.url_base or None,
        tipo=api.tipo.value,
        autenticacao=api.autenticacao.value,
        estado=api.estado.value,
        versao=api.versao,
        limite_por_minuto=api.limite_por_minuto,
        timeout_seg=api.timeout_seg,
        is_deleted=api.is_deleted,
    )


class SqlAlchemyApiExternaRepository(RepositorioApiExterna):
    """Repositório de APIs externas persistido via SQLAlchemy."""

    def __init__(self, session) -> None:
        self._session = session

    def save(self, api: ApiExterna) -> ApiExterna:
        model = self._session.get(ApiExternaModel, UUID(api.id))
        if model is None:
            model = _para_model(api)
            self._session.add(model)
            logger.info("API externa inserida: %s", api.codigo)
        else:
            model.codigo = api.codigo
            model.nome = api.nome
            model.descricao = api.descricao or None
            model.provedor = api.provedor or None
            model.url_base = api.url_base or None
            model.tipo = api.tipo.value
            model.autenticacao = api.autenticacao.value
            model.estado = api.estado.value
            model.versao = api.versao
            model.limite_por_minuto = api.limite_por_minuto
            model.timeout_seg = api.timeout_seg
            model.atualizado_em = func.now()
            logger.info("API externa atualizada: %s", api.codigo)
        self._session.flush()
        return api

    def get_by_id(self, api_id: str) -> ApiExterna | None:
        model = self._session.get(ApiExternaModel, UUID(api_id))
        if model is None or model.is_deleted:
            return None
        return _para_entidade(model)

    def get_by_codigo(self, codigo: str) -> ApiExterna | None:
        stmt = select(ApiExternaModel).where(
            ApiExternaModel.codigo == codigo, ApiExternaModel.is_deleted.is_(False)
        )
        model = self._session.scalars(stmt).first()
        return _para_entidade(model) if model else None

    def exists_by_codigo(self, codigo: str) -> bool:
        stmt = (
            select(ApiExternaModel.id)
            .where(ApiExternaModel.codigo == codigo, ApiExternaModel.is_deleted.is_(False))
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        estado: str | None = None,
        tipo: str | None = None,
    ) -> tuple[list[ApiExterna], int]:
        base = select(ApiExternaModel).where(ApiExternaModel.is_deleted.is_(False))
        if estado:
            base = base.where(ApiExternaModel.estado == estado)
        if tipo:
            base = base.where(ApiExternaModel.tipo == tipo)
        total = len(self._session.scalars(base).all())
        stmt = base.order_by(ApiExternaModel.codigo).offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_para_entidade(m) for m in models], total

    def delete(self, api_id: str) -> bool:
        model = self._session.get(ApiExternaModel, UUID(api_id))
        if model is None:
            return False
        if not model.is_deleted:
            model.is_deleted = True
            model.atualizado_em = func.now()
        self._session.flush()
        logger.info("API externa marcada como excluída: %s", api_id)
        return True
