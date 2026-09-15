"""Tarefas assíncronas compartilhadas do SIGMUN (Celery).

Pacote de scaffolding: as tarefas serão implementadas na Fase VII do
`TODO.md` (Processamento Assíncrono e Mensageria — Celery & Redis).
O pacote precisa existir porque `src.shared.config.celery_app` o declara
em `include`, e o Celery falha no startup caso o módulo não seja
importável.
"""
