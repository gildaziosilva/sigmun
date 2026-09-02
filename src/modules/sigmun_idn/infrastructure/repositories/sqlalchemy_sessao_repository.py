"""Implementação SQLAlchemy do repositório de Sessões (DOM-IDN)."""

from __future__ import annotations

import logging
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.modules.sigmun_idn.domain.entities import Sessao
from src.modules.sigmun_idn.application.interfaces import SessaoRepositoryInterface
from src.modules.sigmun_idn.infrastructure.database.models import SessaoModel

logger = logging.getLogger(__name__)


def _to_entity(model: SessaoModel) -> Sessao:
    """Converte um registro ORM em entidade de domínio."""
    return Sessao(
        id=str(model.id),
        usuario_id=str(model.usuario_id),
        token=model.token,
        ip_origem=model.ip_origem or "",
        user_agent=model.user_agent or "",
        created_at=model.created_at,
        expires_at=model.expires_at,
        is_active=model.is_active,
    )


class SqlAlchemySessaoRepository(SessaoRepositoryInterface):
    """Repositório de sessões persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_token(self, token: str) -> Sessao | None:
        stmt = select(SessaoModel).where(SessaoModel.token == token)
        model = self._session.scalars(stmt).first()
        return _to_entity(model) if model else None

    def get_by_usuario(self, usuario_id: str) -> list[Sessao]:
        stmt = select(SessaoModel).where(
            SessaoModel.usuario_id == UUID(usuario_id),
            SessaoModel.is_active == True,
        )
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models]

    def save(self, sessao: Sessao) -> Sessao:
        model = SessaoModel(
            id=UUID(sessao.id),
            usuario_id=UUID(sessao.usuario_id),
            token=sessao.token,
            ip_origem=sessao.ip_origem,
            user_agent=sessao.user_agent,
            is_active=sessao.is_active,
            expires_at=sessao.expires_at,
            created_at=sessao.created_at,
        )
        self._session.add(model)
        self._session.flush()
        self._session.refresh(model)
        logger.info("Sessão criada: %s", sessao.id)
        return _to_entity(model)

    def invalidate(self, token: str) -> bool:
        """Invalida sessão (logout)."""
        stmt = select(SessaoModel).where(SessaoModel.token == token)
        model = self._session.scalars(stmt).first()
        if model is None:
            return False
        model.is_active = False
        self._session.flush()
        logger.info("Sessão invalidada: %s", token[:16] + "...")
        return True

    def invalidate_all_for_usuario(self, usuario_id: str) -> int:
        """Invalida todas as sessões ativas do usuário."""
        from sqlalchemy import update
        stmt = (
            update(SessaoModel)
            .where(
                SessaoModel.usuario_id == UUID(usuario_id),
                SessaoModel.is_active == True,
            )
            .values(is_active=False)
        )
        result = self._session.execute(stmt)
        self._session.flush()
        count = result.rowcount
        logger.info("%d sessões invalidadas para usuário: %s", count, usuario_id)
        return count


__all__ = ["SqlAlchemySessaoRepository"]
