"""Testes unitarios Fase VII — Celery & Redis (mocks, sem broker/banco)."""

from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone

from src.modules.sigmun_gdo.infrastructure.database.models import EventoOutboxModel
from src.modules.sigmun_gdo.infrastructure.messaging.pubsub import (
    DespachadorPubSub,
    montar_envelope,
)
from src.shared.config.celery_app import celery_app


def _evento(status="pendente", tentativas=0, topico="gdo.documento.criado"):
    return EventoOutboxModel(
        id=uuid.uuid4(),
        topico=topico,
        evento_nome="DocumentoCriado",
        agregado_tipo="documento",
        agregado_id="doc-1",
        payload={"codigo": "DOC-001"},
        status=status,
        tentativas=tentativas,
        created_at=datetime.now(timezone.utc),
    )


class _FakeQuery:
    def __init__(self, itens):
        self._itens = itens

    def filter(self, *a, **k):
        return self

    def order_by(self, *a, **k):
        return self

    def limit(self, n):
        return _FakeQuery(self._itens[:n])

    def all(self):
        return list(self._itens)


class _FakeSession:
    def __init__(self, itens):
        self._q = _FakeQuery(itens)
        self.committed = False

    def query(self, *a, **k):
        return self._q

    def commit(self):
        self.committed = True


class _FakeRedis:
    def __init__(self, falhar=False):
        self.publicados = []
        self._falhar = falhar

    def publish(self, canal, mensagem):
        if self._falhar:
            raise ConnectionError("broker down")
        self.publicados.append((canal, mensagem))
        return 1


class TestHealthcheck:
    def test_retorno_ok(self):
        from src.shared.tasks.tasks import healthcheck

        resultado = healthcheck.apply().get()
        assert resultado["status"] == "ok"
        assert resultado["service"] == "SIGMUN"
        assert "timestamp" in resultado and "worker" in resultado

    def test_registrada_no_app(self):
        assert "sigmun.healthcheck" in celery_app.tasks
        assert "sigmun.gdo.despachar_outbox" in celery_app.tasks
        assert "sigmun.gdo.expurgar_arquivos" in celery_app.tasks


class TestDespachadorPubSub:
    def test_publica_envelope_no_canal(self):
        evento = _evento()
        sessao = _FakeSession([evento])
        redis = _FakeRedis()
        res = DespachadorPubSub(redis).despachar(sessao, lote=10)  # type: ignore[arg-type]
        assert res == {"processados": 1, "publicados": 1, "erros": 0}
        assert sessao.committed is True and evento.status == "publicado"
        assert evento.published_at is not None
        canal, mensagem = redis.publicados[0]
        assert canal == "gdo.documento.criado"
        env = json.loads(mensagem)
        assert env["evento_id"] == str(evento.id)
        assert env["payload"] == {"codigo": "DOC-001"}

    def test_montar_envelope(self):
        env = json.loads(montar_envelope(_evento()))
        assert env["topico"] == "gdo.documento.criado"
        assert env["evento_nome"] == "DocumentoCriado"

    def test_falha_incrementa_tentativa(self):
        evento = _evento()
        sessao = _FakeSession([evento])
        res = DespachadorPubSub(_FakeRedis(falhar=True)).despachar(sessao)  # type: ignore[arg-type]
        assert res["erros"] == 1 and res["publicados"] == 0
        assert evento.status == "pendente" and evento.tentativas == 1
        assert evento.ultimo_erro == "broker down"

    def test_esgota_tentativas_marca_erro(self):
        evento = _evento(tentativas=4)
        sessao = _FakeSession([evento])
        DespachadorPubSub(_FakeRedis(falhar=True)).despachar(sessao)  # type: ignore[arg-type]
        assert evento.status == "erro" and evento.tentativas == 5

    def test_lote_vazio(self):
        sessao = _FakeSession([])
        res = DespachadorPubSub(_FakeRedis()).despachar(sessao)  # type: ignore[arg-type]
        assert res == {"processados": 0, "publicados": 0, "erros": 0}


class TestConfigCelery:
    def test_filas_e_beat(self):
        rotas = celery_app.conf.task_routes
        assert rotas["sigmun.gdo.despachar_outbox"] == {"queue": "gdo.outbox"}
        assert rotas["sigmun.gdo.expurgar_arquivos"] == {"queue": "gdo.expurgo"}
        beat = celery_app.conf.beat_schedule
        assert set(beat) == {"healthcheck-5min", "gdo-outbox-1min", "gdo-expurgo-diario-02h"}
        assert beat["gdo-outbox-1min"]["task"] == "sigmun.gdo.despachar_outbox"
        assert celery_app.conf.task_acks_late is True
