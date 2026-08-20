"""
Configuração do Celery para processamento assíncrono.
Baseado na Arquitetura de Software - Comunicação Assíncrona.
"""

from celery import Celery

from src.shared.config.settings import settings

celery_app = Celery(
    "sigmun",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=["src.shared.tasks"],
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="America/Sao_Paulo",
    enable_utc=True,
)
