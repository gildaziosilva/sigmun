"""Caso de uso: Consultar Trilha de Auditoria.

Baseado em:
  - 017-Modelo-de-Auditoria (seção 42 – filtros de consulta; seção 40 –
    acesso restrito a perfis autorizados; seção 41 – o acesso à auditoria
    também deve ser auditado).
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.queries.consultar_trilha_auditoria_query import (
    ConsultarTrilhaAuditoriaQuery,
)
from src.modules.sigmun_compras.domain.entities.registro_auditoria import (
    RegistroAuditoria,
)
from src.modules.sigmun_compras.domain.repositories.trilha_auditoria_repository import (
    TrilhaAuditoriaRepository,
)

logger = logging.getLogger(__name__)


class ConsultarTrilhaAuditoriaUseCase:
    """Orquestra a consulta paginada e filtrada da trilha de auditoria."""

    def __init__(self, repository: TrilhaAuditoriaRepository) -> None:
        self._repository = repository

    def execute(self, query: ConsultarTrilhaAuditoriaQuery) -> list[RegistroAuditoria]:
        logger.info("Consultando trilha de auditoria – categoria=%s", query.categoria)

        offset = query.page * query.page_size

        return self._repository.list(
            data_inicio=query.data_inicio,
            data_fim=query.data_fim,
            usuario_id=query.usuario_id,
            categoria=query.categoria,
            recurso_tipo=query.recurso_tipo,
            recurso_id=query.recurso_id,
            correlation_id=query.correlation_id,
            limit=query.page_size,
            offset=offset,
        )


__all__ = ["ConsultarTrilhaAuditoriaUseCase"]
