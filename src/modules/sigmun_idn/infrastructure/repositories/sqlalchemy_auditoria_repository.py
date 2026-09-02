"""Implementação SQLAlchemy do repositório de Auditoria de Login (DOM-IDN)."""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.modules.sigmun_idn.domain.entities import AuditoriaLogin
from src.modules.sigmun_idn.application.interfaces import AuditoriaLoginRepositoryInterface
from src.modules.sigmun_idn.infrastructure.database.models import AuditoriaLoginModel

logger = logging.getLogger(__name__)


def _to_entity(model: AuditoriaLoginModel) -> AuditoriaLogin:
    """Converte um registro ORM em entidade de domínio."""
    return AuditoriaLogin(
        id=str(model.id),
        usuario_id=str(model.usuario_id) if model.usuario_id else "",
        login=model.login,
        ip_origem=model.ip_origem or "",
        user_agent=model.user_agent or "",
        sucesso=model.sucesso,
        motivo_falha=model.motivo_falha or "",
        created_at=model.created_at,
    )


class SqlAlchemyAuditoriaLoginRepository(AuditoriaLoginRepositoryInterface):
    """Repositório de auditoria de login persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, auditoria: AuditoriaLogin) -> AuditoriaLogin:
        model = AuditoriaLoginModel(
            id=UUID(auditoria.id),
            usuario_id=UUID(auditoria.usuario_id) if auditoria.usuario_id else None,
            login=auditoria.login,
            ip_origem=auditoria.ip_origem,
            user_agent=auditoria.user_agent,
            sucesso=auditoria.sucesso,
            motivo_falha=auditoria.motivo_falha,
            created_at=auditoria.created_at,
        )
        self._session.add(model)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def get_by_usuario(
        self,
        usuario_id: str,
        page: int = 0,
        page_size: int = 50,
    ) -> tuple[builtins.list[AuditoriaLogin], int]:
        stmt = select(AuditoriaLoginModel).where(
            AuditoriaLoginModel.usuario_id == UUID(usuario_id)
        ).order_by(AuditoriaLoginModel.created_at.desc())
        total = len(self._session.scalars(stmt).all())
        stmt = stmt.offset(page * page_size).limit(page_size)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models], total

    def count_failed_recent(self, login: str, minutes: int = 30) -> int:
        """Conta falhas recentes de login."""
        from datetime import datetime, timedelta
        from sqlalchemy import func
        cutoff = datetime.utcnow() - timedelta(minutes=minutes)
        stmt = select(func.count(AuditoriaLoginModel.id)).where(
            AuditoriaLoginModel.login == login,
            AuditoriaLoginModel.sucesso == False,
            AuditoriaLoginModel.created_at >= cutoff,
        )
        return self._session.scalar(stmt) or 0


__all__ = ["SqlAlchemyAuditoriaLoginRepository"]
