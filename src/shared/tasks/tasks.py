"""Tarefas Celery do SIGMUN (Fase VII — Processamento Assíncrono e Mensageria).

* `healthcheck` — sonda periódica do worker (usada pelo Beat + monitoramento).
* `despachar_outbox_gdo` — consome `gdo.eventos_outbox` pendentes e publica
  no Redis Pub/Sub (canal = tópico do evento).
* `expurgar_arquivos_gdo` — remove binários com descarte autorizado (RN-GDO-011).
"""

from __future__ import annotations

import contextlib
import logging
from typing import Any

from src.shared.config.celery_app import celery_app
from src.shared.config.settings import settings

logger = logging.getLogger(__name__)


@celery_app.task(name="sigmun.healthcheck", bind=True, max_retries=0)
def healthcheck(self: Any) -> dict[str, str]:
    """Sonda de saúde do worker: retorna status + metadados do worker."""
    import socket
    from datetime import datetime, timezone

    hostname = getattr(getattr(self, "request", None), "hostname", None) or socket.gethostname()
    return {
        "status": "ok",
        "worker": hostname,
        "service": "SIGMUN",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@celery_app.task(
    name="sigmun.gdo.despachar_outbox",
    bind=True,
    max_retries=3,
    autoretry_for=(Exception,),
    retry_backoff=30,
    retry_jitter=True,
)
def despachar_outbox_gdo(self: Any, lote: int | None = None) -> dict[str, int]:
    """Despacha eventos pendentes de `gdo.eventos_outbox` p/ Redis Pub/Sub."""
    import redis as redis_lib

    from src.core.infrastructure.database.session import SessionLocal
    from src.modules.sigmun_gdo.infrastructure.messaging.pubsub import DespachadorPubSub

    tamanho = lote or settings.OUTBOX_DISPATCH_BATCH
    cliente = redis_lib.Redis.from_url(settings.REDIS_URL, decode_responses=True)
    try:
        despachador = DespachadorPubSub(cliente, max_tentativas=settings.OUTBOX_MAX_TENTATIVAS)
        sessao = SessionLocal()
        try:
            resultado = despachador.despachar(sessao, lote=tamanho)
        finally:
            sessao.close()
    finally:
        with contextlib.suppress(Exception):  # higiene de socket
            cliente.close()
    logger.info("outbox GDO despachada via Pub/Sub", extra={"extra_data": resultado})
    return resultado


@celery_app.task(
    name="sigmun.gdo.expurgar_arquivos",
    bind=True,
    max_retries=2,
    autoretry_for=(Exception,),
    retry_backoff=60,
    retry_jitter=True,
)
def expurgar_arquivos_gdo(
    self: Any, dias_retencao: int = 30, dry_run: bool = False, limite: int = 500
) -> dict[str, Any]:
    """Expurga binários com descarte autorizado após carência temporal."""
    from src.core.infrastructure.database.session import SessionLocal
    from src.shared.tasks.expurgo import expurgar_arquivos

    sessao = SessionLocal()
    try:
        resultado = expurgar_arquivos(
            sessao,
            storage_root=settings.STORAGE_ROOT,
            dias_retencao=dias_retencao,
            dry_run=dry_run,
            limite=limite,
        )
    finally:
        sessao.close()
    resumo = resultado.to_dict()
    logger.info("expurgo GDO concluído", extra={"extra_data": resumo})
    return resumo


__all__ = ["healthcheck", "despachar_outbox_gdo", "expurgar_arquivos_gdo"]
