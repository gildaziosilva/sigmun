"""Configuracao do Celery (Fase VII - Celery & Redis)."""

from celery import Celery  # type: ignore[import-untyped]
from celery.schedules import crontab  # type: ignore[import-untyped]

from src.shared.config.settings import settings

celery_app = Celery(
    "sigmun",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=["src.shared.tasks", "src.shared.tasks.tasks"],
)
celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="America/Sao_Paulo",
    enable_utc=True,
    task_acks_late=True,
    worker_prefetch_multiplier=1,
    task_time_limit=settings.CELERY_TASK_TIME_LIMIT,
    task_soft_time_limit=settings.CELERY_TASK_SOFT_TIME_LIMIT,
    result_expires=settings.CELERY_RESULT_EXPIRES,
    task_default_queue="celery",
    task_routes={
        "sigmun.gdo.despachar_outbox": {"queue": "gdo.outbox"},
        "sigmun.gdo.expurgar_arquivos": {"queue": "gdo.expurgo"},
    },
    beat_schedule={
        "healthcheck-5min": {
            "task": "sigmun.healthcheck",
            "schedule": 300.0,
            "options": {"queue": "celery"},
        },
        "gdo-outbox-1min": {
            "task": "sigmun.gdo.despachar_outbox",
            "schedule": 60.0,
            "options": {"queue": "gdo.outbox"},
        },
        "gdo-expurgo-diario-02h": {
            "task": "sigmun.gdo.expurgar_arquivos",
            "schedule": crontab(hour=2, minute=0),
            "kwargs": {"dias_retencao": 30, "dry_run": False, "limite": 500},
            "options": {"queue": "gdo.expurgo"},
        },
    },
)
