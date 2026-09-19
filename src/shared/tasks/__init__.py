"""Tarefas assíncronas compartilhadas do SIGMUN (Celery — Fase VII).

Reexporta as tasks registradas em `src.shared.tasks.tasks` para que
`celery -A src.shared.config.celery_app worker` as descubra via `include`.
"""

from .expurgo import (
    ResultadoExpurgo,
    coletar_candidatos_expurgo,
    expurgar_arquivos,
    resolver_caminho_seguro,
)
from .tasks import despachar_outbox_gdo, expurgar_arquivos_gdo, healthcheck

__all__ = [
    "healthcheck",
    "despachar_outbox_gdo",
    "expurgar_arquivos_gdo",
    "ResultadoExpurgo",
    "coletar_candidatos_expurgo",
    "expurgar_arquivos",
    "resolver_caminho_seguro",
]
