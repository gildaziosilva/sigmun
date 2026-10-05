"""Revisão periódica do cadastro (ADR-0007, lacuna resolvida).

Pessoa é considerada desatualizada quando `updated_at` for anterior a 12 meses.
A verificação é mensal (Celery beat) e o resultado é divulgado como evento de
auditoria para os domínios consumidores (DOM-PES, DOM-ASS e DOM-IND).
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from datetime import datetime, timedelta, timezone
from typing import Any
from uuid import uuid4

from src.modules.sigmun_cadastro.domain.events.pessoa_events import (
    RevisaoCadastralDivulgadaEvent,
)
from src.modules.sigmun_cadastro.domain.repositories.pessoa_repository import (
    PessoaRepository,
)

logger = logging.getLogger(__name__)


class RevisarCadastralUseCase:
    """Localiza pessoas desatualizadas e divulga o evento de auditoria."""

    def __init__(
        self,
        repositorio: PessoaRepository,
        *,
        relogio: Callable[[], datetime] | None = None,
        auditoria: logging.Logger | None = None,
    ) -> None:
        self._repo = repositorio
        self._relogio = relogio or (lambda: datetime.now(timezone.utc))
        self._auditoria = auditoria or logger

    def execute(self, *, limite_meses: int = 12, limite: int = 1000) -> dict[str, Any]:
        """Executa a revisão e devolve o relatório com o evento divulgado."""
        agora = self._relogio()
        corte = agora - timedelta(days=30 * limite_meses)
        pessoas = tuple(self._repo.listar_desatualizadas(corte, limite=limite))
        evento = RevisaoCadastralDivulgadaEvent(
            event_id=uuid4(),
            pessoas_desatualizadas=pessoas,
            limite_meses=limite_meses,
            occurred_at=agora,
        )
        self._auditoria.info(
            "cadastro.revisao_divulgada",
            extra={
                "event_id": str(evento.event_id),
                "pessoas_desatualizadas": len(pessoas),
                "limite_meses": limite_meses,
                "corte": corte.isoformat(),
            },
        )
        return {
            "event_id": str(evento.event_id),
            "pessoas_desatualizadas": [str(pessoa) for pessoa in pessoas],
            "total": len(pessoas),
            "limite_meses": limite_meses,
        }


__all__ = ["RevisarCadastralUseCase"]
