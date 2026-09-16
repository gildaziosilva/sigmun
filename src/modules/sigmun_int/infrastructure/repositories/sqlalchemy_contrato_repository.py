"""Repositório SQLAlchemy de contratos de integração (DOM-INT)."""

import logging
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.sigmun_int.application.interfaces import RepositorioContratoIntegracao
from src.modules.sigmun_int.domain.entities import ContratoIntegracao, EstadoContrato
from src.modules.sigmun_int.infrastructure.database.models import ContratoIntegracaoModel

logger = logging.getLogger(__name__)


def _to_entity(model: ContratoIntegracaoModel) -> ContratoIntegracao:
    return ContratoIntegracao(
        id=str(model.id),
        codigo=model.codigo,
        nome=model.nome,
        descricao=model.descricao or "",
        versao_formato=model.versao_formato,
        esquema_ref=model.esquema_ref or "",
        api_externa_id=str(model.api_externa_id) if model.api_externa_id else "",
        estado=EstadoContrato(model.estado),
        criado_em=model.criado_em,
        atualizado_em=model.atualizado_em,
        is_deleted=model.is_deleted,
    )


class SqlAlchemyContratoIntegracaoRepository(RepositorioContratoIntegracao):
    """Repositório de contratos de integração persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, contrato: ContratoIntegracao) -> ContratoIntegracao:
        model = self._session.get(ContratoIntegracaoModel, UUID(contrato.id))
        if model is None:
            model = ContratoIntegracaoModel(
                id=UUID(contrato.id),
                codigo=contrato.codigo,
                nome=contrato.nome,
                descricao=contrato.descricao or None,
                versao_formato=contrato.versao_formato,
                esquema_ref=contrato.esquema_ref or None,
                api_externa_id=UUID(contrato.api_externa_id) if contrato.api_externa_id else None,
                estado=contrato.estado.value,
                is_deleted=contrato.is_deleted,
            )
            self._session.add(model)
        else:
            model.codigo = contrato.codigo
            model.nome = contrato.nome
            model.descricao = contrato.descricao or None
            model.versao_formato = contrato.versao_formato
            model.esquema_ref = contrato.esquema_ref or None
            model.api_externa_id = (
                UUID(contrato.api_externa_id) if contrato.api_externa_id else None
            )
            model.estado = contrato.estado.value
            model.atualizado_em = func.now()
        self._session.flush()
        return contrato

    def get_by_id(self, contrato_id: str) -> ContratoIntegracao | None:
        model = self._session.get(ContratoIntegracaoModel, UUID(contrato_id))
        if model is None or model.is_deleted:
            return None
        return _to_entity(model)

    def get_by_codigo(self, codigo: str) -> ContratoIntegracao | None:
        stmt = select(ContratoIntegracaoModel).where(
            ContratoIntegracaoModel.codigo == codigo,
            ContratoIntegracaoModel.is_deleted.is_(False),
        )
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def exists_by_codigo(self, codigo: str) -> bool:
        stmt = (
            select(ContratoIntegracaoModel.id)
            .where(
                ContratoIntegracaoModel.codigo == codigo,
                ContratoIntegracaoModel.is_deleted.is_(False),
            )
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        estado: str | None = None,
        api_externa_id: str | None = None,
    ) -> tuple[list[ContratoIntegracao], int]:
        base = select(ContratoIntegracaoModel).where(ContratoIntegracaoModel.is_deleted.is_(False))
        if estado:
            base = base.where(ContratoIntegracaoModel.estado == estado)
        if api_externa_id:
            base = base.where(ContratoIntegracaoModel.api_externa_id == UUID(api_externa_id))
        total = len(self._session.scalars(base).all())
        stmt = (
            base.order_by(ContratoIntegracaoModel.codigo).offset(page * page_size).limit(page_size)
        )
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def delete(self, contrato_id: str) -> bool:
        model = self._session.get(ContratoIntegracaoModel, UUID(contrato_id))
        if model is None:
            return False
        if not model.is_deleted:
            model.is_deleted = True
            model.atualizado_em = func.now()
        self._session.flush()
        return True
