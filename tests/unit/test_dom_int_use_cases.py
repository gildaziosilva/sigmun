"""Testes unitários do módulo de Integração e Interoperabilidade (DOM-INT).

Cobrem:
  - Entidades: Webhook (inscrição em tópicos), EntregaWebhook (retry/DLQ/backoff),
    ApiExterna (eh_consumivel), ContratoIntegracao (eh_vigente), Conector (esta_ativo).
  - Casos de uso: APIs externas, contratos, conectores oficiais, webhooks,
    entregas e o barramento de eventos (consumo outbox + despacho).

Os casos de uso recebem repositórios injetados; estes testes usam repositórios
em memória (fake) para validar o comportamento de domínio sem persistência real.
"""

from __future__ import annotations

from datetime import datetime, timedelta

import pytest

from src.modules.sigmun_int.application.use_cases import (
    CancelarEntregaWebhookUseCase,
    ConsumirOutboxUseCase,
    DeletarApiExternaUseCase,
    DeletarConectorUseCase,
    DeletarContratoIntegracaoUseCase,
    DeletarWebhookUseCase,
    DespacharWebhooksUseCase,
    RetryEntregaWebhookUseCase,
    BuscarApiExternaUseCase,
    BuscarConectorUseCase,
    BuscarContratoIntegracaoUseCase,
    BuscarEntregaWebhookUseCase,
    BuscarWebhookUseCase,
    MudarEstadoApiUseCase,
    MudarEstadoConectorUseCase,
    MudarEstadoWebhookUseCase,
    CriarApiExternaUseCase,
    CriarConectorUseCase,
    CriarContratoIntegracaoUseCase,
    RegistrarWebhookUseCase,
)
from src.modules.sigmun_int.application.use_cases.contrato_use_cases import (
    AprovarContratoIntegracaoUseCase,
    AtualizarContratoIntegracaoUseCase,
    RetirarContratoIntegracaoUseCase,
)
from src.modules.sigmun_int.application.use_cases.conector_use_cases import (
    CONECTORES_OFICIAIS,
    CODIGOS_CONECTORES_OFICIAIS,
    AtualizarConectorUseCase,
)
from src.modules.sigmun_int.application.use_cases.api_use_cases import (
    AtualizarApiExternaUseCase,
)
from src.modules.sigmun_int.application.use_cases.webhook_use_cases import (
    AtualizarWebhookUseCase,
)
from src.modules.sigmun_int.application.use_cases.bus_use_cases import (
    FONTES_OUTBOX_VALIDAS,
)
from src.modules.sigmun_int.application.interfaces import (
    EventoOutbox,
    ResultadoEnvio,
    TransporteWebhook,
)
from src.modules.sigmun_int.domain.entities import (
    EstadoApi,
    EstadoContrato,
    EstadoConector,
    EstadoEntrega,
    EstadoInscricao,
    EntregaWebhook,
    EventoProcessado,
    Webhook,
)
from src.modules.sigmun_int.domain.exceptions import (
    ApiExternaJaExisteError,
    ApiExternaNaoEncontradaError,
    ConectorJaExisteError,
    ConectorNaoEncontradoError,
    ContratoIntegracaoJaExisteError,
    ContratoIntegracaoNaoEncontradoError,
    EntregaEstadoInvalidoError,
    EntregaNaoEncontradaError,
    FonteOutboxInvalidaError,
    OperacaoNaoPermitidaError,
    UrlWebhookInvalidaError,
    WebhookJaExisteError,
    WebhookNaoEncontradoError,
)


# ---------------------------------------------------------------------------
# Repositórios em memória (fakes)
# ---------------------------------------------------------------------------


class _RepoMixin:
    """Mixin base para repositórios em memória com delete lógico."""

    _db: dict

    def delete(self, _id: str) -> bool:
        obj = self._db.get(_id)
        if obj is None or getattr(obj, "is_deleted", False):
            return False
        obj.is_deleted = True
        obj.atualizado_em = datetime.utcnow()
        return True


class FakeApiRepo(_RepoMixin):
    """Repositório em memória de APIs externas."""

    def __init__(self):
        self._db: dict[str, object] = {}

    def save(self, api):
        self._db[api.id] = api
        return api

    def get_by_id(self, api_id):
        obj = self._db.get(api_id)
        return obj if obj and not getattr(obj, "is_deleted", False) else None

    def get_by_codigo(self, codigo):
        for a in self._db.values():
            if a.codigo == codigo and not a.is_deleted:
                return a
        return None

    def exists_by_codigo(self, codigo):
        return any(a.codigo == codigo and not a.is_deleted for a in self._db.values())

    def list_all(self, page=0, page_size=50, estado=None, tipo=None):
        items = [a for a in self._db.values() if not a.is_deleted]
        if estado:
            items = [a for a in items if a.estado.value == estado]
        if tipo:
            items = [a for a in items if a.tipo.value == tipo]
        return items, len(items)


class FakeConectorRepo(_RepoMixin):
    """Repositório em memória de conectores oficiais."""

    def __init__(self):
        self._db: dict[str, object] = {}

    def save(self, conector):
        self._db[conector.id] = conector
        return conector

    def get_by_id(self, conector_id):
        obj = self._db.get(conector_id)
        return obj if obj and not getattr(obj, "is_deleted", False) else None

    def get_by_codigo(self, codigo):
        for c in self._db.values():
            if c.codigo == codigo and not c.is_deleted:
                return c
        return None

    def exists_by_codigo(self, codigo):
        return any(c.codigo == codigo and not c.is_deleted for c in self._db.values())

    def list_all(self, page=0, page_size=50, estado=None):
        items = [c for c in self._db.values() if not c.is_deleted]
        if estado:
            items = [c for c in items if c.estado.value == estado]
        return items, len(items)


class FakeContratoRepo(_RepoMixin):
    """Repositório em memória de contratos de integração."""

    def __init__(self):
        self._db: dict[str, object] = {}

    def save(self, contrato):
        self._db[contrato.id] = contrato
        return contrato

    def get_by_id(self, contrato_id):
        obj = self._db.get(contrato_id)
        return obj if obj and not getattr(obj, "is_deleted", False) else None

    def get_by_codigo(self, codigo):
        for c in self._db.values():
            if c.codigo == codigo and not c.is_deleted:
                return c
        return None

    def exists_by_codigo(self, codigo):
        return any(c.codigo == codigo and not c.is_deleted for c in self._db.values())

    def list_all(self, page=0, page_size=50, estado=None, api_externa_id=None):
        items = [c for c in self._db.values() if not c.is_deleted]
        if estado:
            items = [c for c in items if c.estado.value == estado]
        if api_externa_id:
            items = [c for c in items if c.api_externa_id == api_externa_id]
        return items, len(items)


class FakeWebhookRepo(_RepoMixin):
    """Repositório em memória de webhooks."""

    def __init__(self):
        self._db: dict[str, object] = {}

    def save(self, webhook):
        self._db[webhook.id] = webhook
        return webhook

    def get_by_id(self, webhook_id):
        obj = self._db.get(webhook_id)
        return obj if obj and not getattr(obj, "is_deleted", False) else None

    def get_by_nome(self, nome):
        for w in self._db.values():
            if w.nome == nome and not w.is_deleted:
                return w
        return None

    def exists_by_nome(self, nome):
        return any(w.nome == nome and not w.is_deleted for w in self._db.values())

    def list_all(self, page=0, page_size=50, estado=None):
        items = [w for w in self._db.values() if not w.is_deleted]
        if estado:
            items = [w for w in items if w.estado.value == estado]
        return items, len(items)

    def find_ativos(self):
        return [
            w for w in self._db.values()
            if w.is_active and w.estado is EstadoInscricao.ATIVA
        ]


class FakeEntregaRepo(_RepoMixin):
    """Repositório em memória de entregas de mensagens."""

    def __init__(self):
        self._db: dict[str, object] = {}

    def save(self, entrega):
        self._db[entrega.id] = entrega
        return entrega

    def get_by_id(self, entrega_id):
        obj = self._db.get(entrega_id)
        return obj if obj and not getattr(obj, "is_deleted", False) else None

    def list_pendentes_para_retry(self, lote, agora):
        items = [
            e for e in self._db.values()
            if not e.is_deleted and e.pendente_para_retry(agora)
        ]
        return items[:lote]

    def list_by_webhook(self, webhook_id, page=0, page_size=50):
        items = [
            e for e in self._db.values()
            if not e.is_deleted and e.webhook_id == webhook_id
        ]
        total = len(items)
        return items[page * page_size:(page + 1) * page_size], total

    def list_all(self, page=0, page_size=50, estado=None):
        items = [e for e in self._db.values() if not e.is_deleted]
        if estado:
            items = [e for e in items if e.estado.value == estado]
        return items, len(items)


class FakeEventoProcessadoRepo(_RepoMixin):
    """Repositório em memória de eventos processados (inbox)."""

    def __init__(self):
        self._db: dict[str, object] = {}

    def save(self, evento):
        self._db[evento.id] = evento
        return evento

    def get_by_evento_outbox(self, fonte, evento_outbox_id):
        for e in self._db.values():
            if e.fonte == fonte and e.evento_outbox_id == evento_outbox_id:
                return e
        return None

    def exists(self, fonte, evento_outbox_id):
        return self.get_by_evento_outbox(fonte, evento_outbox_id) is not None

    def list_all(self, page=0, page_size=50, fonte=None):
        items = [e for e in self._db.values() if not e.is_deleted]
        if fonte:
            items = [e for e in items if e.fonte == fonte]
        return items, len(items)


class FakeOutboxSource:
    """Fonte em memória do Transactional Outbox para testes do barramento."""

    def __init__(self):
        self.eventos: list[EventoOutbox] = []
        self.publicados: list[str] = []

    def ler_pendentes(self, fonte, lote=100):
        return [e for e in self.eventos if not getattr(e, "_publicado", False)][:lote]

    def marcar_publicado(self, fonte, evento_outbox_id):
        self.publicados.append(evento_outbox_id)
        for e in self.eventos:
            if e.id == evento_outbox_id:
                e._publicado = True  # noqa: SLF001


class FakeTransporte(TransporteWebhook):
    """Transporte webhook em memória que controla o resultado do envio."""

    def __init__(self, ok=True, http_status=200, erro=""):
        self.ok = ok
        self.http_status = http_status
        self.erro = erro
        self.enviados: list[tuple[str, dict]] = []

    def enviar(self, url, payload, cabecalhos=None, timeout_seg=30):
        self.enviados.append((url, payload))
        return ResultadoEnvio(
            http_status=self.http_status,
            ok=self.ok,
            erro=self.erro,
            duracao_seg=0.1,
        )


# ---------------------------------------------------------------------------
# Testes de entidades
# ---------------------------------------------------------------------------


class TestWebhookEntity:
    """Suscrição a tópicos do barramento com comodín ``*``."""

    def test_inscrito_em_wildcard(self):
        w = Webhook(topicos=["*"])
        assert w.inscrito_em("gdo.doc.criado") is True

    def test_inscrito_em_topico_exacto(self):
        w = Webhook(topicos=["gdo.doc.criado"])
        assert w.inscrito_em("gdo.doc.criado") is True
        assert w.inscrito_em("gdo.otro") is False

    def test_inscrito_em_lista_multiple(self):
        w = Webhook(topicos=["gdo.doc.criado", "compras.compra.criada"])
        assert w.inscrito_em("compras.compra.criada") is True
        assert w.inscrito_em("gdo.doc.borrado") is False

    def test_inscrito_em_vacia(self):
        w = Webhook(topicos=[])
        assert w.inscrito_em("gdo.doc.criado") is False

    def test_esta_ativo(self):
        w = Webhook(estado=EstadoInscricao.ATIVA)
        assert w.is_active is True
        w.is_deleted = True
        assert w.is_active is False

    def test_is_active(self):
        w = Webhook()
        assert w.is_active is True
        w.is_deleted = True
        assert w.is_active is False


class TestEntregaWebhook:
    """Retry com backoff exponencial e fila de mensagens mortas (DLQ)."""

    def test_pendente_para_retry_sem_proximo(self):
        e = EntregaWebhook(estado=EstadoEntrega.PENDENTE)
        assert e.pendente_para_retry(datetime.utcnow()) is True

    def test_pendente_para_retry_com_fecha_futura(self):
        e = EntregaWebhook(
            estado=EstadoEntrega.PENDENTE,
            proximo_retry=datetime.utcnow() + timedelta(hours=1),
        )
        assert e.pendente_para_retry(datetime.utcnow()) is False

    def test_pendente_para_retry_estado_no_pendente(self):
        e = EntregaWebhook(estado=EstadoEntrega.SUCESSO)
        assert e.pendente_para_retry(datetime.utcnow()) is False

    def test_pendente_para_retry_estado_fallido(self):
        e = EntregaWebhook(estado=EstadoEntrega.FALHOU)
        assert e.pendente_para_retry(datetime.utcnow()) is False

    def test_registrar_sucesso(self):
        e = EntregaWebhook(max_tentativas=5, tentativas=2)
        e.registrar_sucesso(200, datetime.utcnow())
        assert e.estado is EstadoEntrega.SUCESSO
        assert e.tentativas == 3
        assert e.ultimo_erro == ""
        assert e.proximo_retry is None
        assert e.entregue_em is not None

    def test_registrar_falha_no_agoto_tentativas(self):
        e = EntregaWebhook(max_tentativas=5, tentativas=1, backoff_base_seg=60)
        antes = datetime.utcnow()
        e.registrar_falha(None, "timeout", antes)
        assert e.estado is EstadoEntrega.FALHOU
        assert e.tentativas == 2
        # backoff: 60 * 2^(2-1) = 120 segundos
        assert (e.proximo_retry - antes).total_seconds() == pytest.approx(120, abs=1)

    def test_registrar_falha_agota_tentativas_cola_muerta(self):
        e = EntregaWebhook(max_tentativas=3, tentativas=2, backoff_base_seg=60)
        antes = datetime.utcnow()
        e.registrar_falha(500, "server erro", antes)
        assert e.estado is EstadoEntrega.FILA_MORTA
        assert e.na_fila_morta is True
        assert e.proximo_retry is None

    def test_calcular_proximo_retry_backoff_exponencial(self):
        desde = datetime.utcnow()
        e = EntregaWebhook(backoff_base_seg=60, max_tentativas=5)
        e.tentativas = 1
        sig = e._calcular_proximo_retry(desde)  # noqa: SLF001
        assert (sig - desde).total_seconds() == pytest.approx(60, abs=1)
        e.tentativas = 2
        sig2 = e._calcular_proximo_retry(desde)  # noqa: SLF001
        assert (sig2 - desde).total_seconds() == pytest.approx(120, abs=1)
        e.tentativas = 3
        sig3 = e._calcular_proximo_retry(desde)  # noqa: SLF001
        assert (sig3 - desde).total_seconds() == pytest.approx(240, abs=1)

    def test_eh_sucesso(self):
        e = EntregaWebhook(estado=EstadoEntrega.SUCESSO)
        assert e.eh_sucesso is True
        e.estado = EstadoEntrega.FALHOU
        assert e.eh_sucesso is False

    def test_en_cola_muerta(self):
        e = EntregaWebhook(estado=EstadoEntrega.FILA_MORTA)
        assert e.na_fila_morta is True
        e.estado = EstadoEntrega.SUCESSO
        assert e.na_fila_morta is False


class TestEntidadesBasicas:
    """Testes rápidos de propriedades is_active / estado."""

    def test_api_eh_consumivel(self):
        from src.modules.sigmun_int.domain.entities import ApiExterna
        a = ApiExterna(estado=EstadoApi.ATIVA)
        assert a.eh_consumivel is True
        a.estado = EstadoApi.RASCUNHO
        assert a.eh_consumivel is False

    def test_contrato_eh_vigente(self):
        from src.modules.sigmun_int.domain.entities import ContratoIntegracao
        c = ContratoIntegracao(estado=EstadoContrato.VIGENTE)
        assert c.eh_vigente is True
        c.estado = EstadoContrato.RETIRADO
        assert c.eh_vigente is False

    def test_conector_esta_ativo(self):
        from src.modules.sigmun_int.domain.entities import Conector
        c = Conector(estado=EstadoConector.ATIVO, config={"k": "v"})
        assert c.esta_ativo is True
        c.estado = EstadoConector.INATIVO
        assert c.esta_ativo is False

    def test_evento_processado_is_active(self):
        e = EventoProcessado()
        assert e.is_active is True
        e.is_deleted = True
        assert e.is_active is False


# ---------------------------------------------------------------------------
# Testes de casos de uso: Conectores oficiais
# ---------------------------------------------------------------------------


class TestConectorUseCases:
    def test_conectores_oficiales_constante(self):
        assert len(CONECTORES_OFICIAIS) == 4
        assert set(CODIGOS_CONECTORES_OFICIAIS) == {"GOVBR", "ESOCIAL", "SIAFIC", "PNCP"}
        for c in CONECTORES_OFICIAIS:
            assert c["url_base"].startswith("https://")

    def test_criar_conector_oficial_completa_dados(self):
        repo = FakeConectorRepo()
        uc = CriarConectorUseCase(repo)
        conector = uc.execute(
            codigo="GOVBR",
            nome="",
            descricao="",
            provedor="",
            url_base="",
            autenticacao_tipo="oauth2",
            config={},
        )
        assert conector.codigo == "GOVBR"
        assert conector.nome == "Plataforma Digital GOV.BR"
        assert conector.url_base == "https://api.brasil.gov.br"
        assert conector.estado is EstadoConector.SEM_CONFIGURACAO

    def test_criar_conector_personalizado(self):
        repo = FakeConectorRepo()
        uc = CriarConectorUseCase(repo)
        conector = uc.execute(
            codigo="API-TEST",
            nome="API de prueba",
            url_base="https://api.test.gov.br",
            config={"key": "value"},
        )
        assert conector.codigo == "API-TEST"
        assert conector.nome == "API de prueba"
        assert conector.autenticacao_tipo == "oauth2"

    def test_criar_conector_codigo_invalido(self):
        repo = FakeConectorRepo()
        uc = CriarConectorUseCase(repo)
        with pytest.raises(ValueError, match="código"):
            uc.execute(codigo="invalid_code", nome="test")

    def test_criar_conector_duplicado(self):
        repo = FakeConectorRepo()
        uc = CriarConectorUseCase(repo)
        uc.execute(codigo="GOV-BR", nome="API 1", url_base="https://api.test.gov.br")
        with pytest.raises(ConectorJaExisteError):
            uc.execute(codigo="GOV-BR", nome="API 2", url_base="https://api.test.gov.br")

    def test_buscar_conector_por_id(self):
        repo = FakeConectorRepo()
        uc_criar = CriarConectorUseCase(repo)
        c = uc_criar.execute(codigo="GOVBR", nome="API 1", url_base="https://api.test.gov.br")
        uc_buscar = BuscarConectorUseCase(repo)
        assert uc_buscar.get_by_id(c.id).codigo == "GOVBR"

    def test_buscar_conector_nao_encontrado(self):
        repo = FakeConectorRepo()
        uc = BuscarConectorUseCase(repo)
        with pytest.raises(ConectorNaoEncontradoError):
            uc.get_by_id("nao-existe")

    def test_atualizar_conector(self):
        repo = FakeConectorRepo()
        uc_criar = CriarConectorUseCase(repo)
        c = uc_criar.execute(codigo="GOVBR", nome="API 1", url_base="https://api.test.gov.br")
        uc_act = AtualizarConectorUseCase(repo)
        actualizado = uc_act.execute(c.id, nome="API Atualizada", config={"entorno": "test"})
        assert actualizado.nome == "API Atualizada"
        assert actualizado.config["entorno"] == "test"

    def test_cambiar_estado_conector_sin_configuracion(self):
        """RN-INT-004: no se puede ativar um conector sin configuración."""
        repo = FakeConectorRepo()
        uc_criar = CriarConectorUseCase(repo)
        c = uc_criar.execute(codigo="API-TEST", nome="API 1", url_base="https://api.test.gov.br")
        uc_estado = MudarEstadoConectorUseCase(repo)
        with pytest.raises(OperacaoNaoPermitidaError, match="sem configuração"):
            uc_estado.execute(c.id, "ativo")

    def test_cambiar_estado_conector_con_configuracion(self):
        repo = FakeConectorRepo()
        uc_criar = CriarConectorUseCase(repo)
        c = uc_criar.execute(
            codigo="GOVBR",
            nome="API 1",
            url_base="https://api.test.gov.br",
            config={"entorno": "produccion"},
        )
        uc_estado = MudarEstadoConectorUseCase(repo)
        actualizado = uc_estado.execute(c.id, "ativo")
        assert actualizado.estado is EstadoConector.ATIVO

    def test_cambiar_estado_conector_nao_encontrado(self):
        repo = FakeConectorRepo()
        uc = MudarEstadoConectorUseCase(repo)
        with pytest.raises(ConectorNaoEncontradoError):
            uc.execute("nao-existe", "ativo")

    def test_eliminar_conector(self):
        repo = FakeConectorRepo()
        uc_criar = CriarConectorUseCase(repo)
        c = uc_criar.execute(codigo="GOVBR", nome="API 1", url_base="https://api.test.gov.br")
        uc_delete = DeletarConectorUseCase(repo)
        assert uc_delete.execute(c.id) is True
        assert repo.get_by_id(c.id) is None

    def test_eliminar_conector_nao_encontrado(self):
        repo = FakeConectorRepo()
        uc_delete = DeletarConectorUseCase(repo)
        with pytest.raises(ConectorNaoEncontradoError):
            uc_delete.execute("nao-existe")

    def test_listar_conectores(self):
        repo = FakeConectorRepo()
        uc = CriarConectorUseCase(repo)
        uc.execute(codigo="GOVBR", nome="API 1", url_base="https://api.test.gov.br")
        uc.execute(codigo="SIAFIC", nome="API 2", url_base="https://api.test.gov.br")
        uc_bus = BuscarConectorUseCase(repo)
        items, total = uc_bus.list_all(estado="sem_configuracao")
        assert total == 2


# ---------------------------------------------------------------------------
# Testes de casos de uso: APIs externas
# ---------------------------------------------------------------------------


class TestApiUseCases:
    def test_criar_api_valida(self):
        repo = FakeApiRepo()
        uc = CriarApiExternaUseCase(repo)
        api = uc.execute(
            codigo="API-TEST",
            nome="API de prueba",
            url_base="https://api.test.gov.br",
            tipo="rest",
            autenticacao="oauth2",
            estado="ativa",
        )
        assert api.codigo == "API-TEST"
        assert api.estado is EstadoApi.ATIVA

    def test_criar_api_codigo_invalido(self):
        repo = FakeApiRepo()
        uc = CriarApiExternaUseCase(repo)
        with pytest.raises(ValueError, match="código"):
            uc.execute(codigo="lowercase", nome="API")

    def test_criar_api_url_invalida(self):
        repo = FakeApiRepo()
        uc = CriarApiExternaUseCase(repo)
        with pytest.raises(ValueError, match="URL"):
            uc.execute(codigo="API-OK", nome="API", url_base="ftp://invalid")

    def test_criar_api_duplicada(self):
        repo = FakeApiRepo()
        uc = CriarApiExternaUseCase(repo)
        uc.execute(codigo="API-01", nome="API 1", url_base="https://api.test.gov.br")
        with pytest.raises(ApiExternaJaExisteError):
            uc.execute(codigo="API-01", nome="API 2", url_base="https://api.test.gov.br")

    def test_buscar_api_por_id(self):
        repo = FakeApiRepo()
        uc = CriarApiExternaUseCase(repo)
        api = uc.execute(codigo="API-01", nome="API", url_base="https://api.test.gov.br")
        uc_bus = BuscarApiExternaUseCase(repo)
        assert uc_bus.get_by_id(api.id).codigo == "API-01"

    def test_buscar_api_nao_encontrada(self):
        repo = FakeApiRepo()
        uc = BuscarApiExternaUseCase(repo)
        with pytest.raises(ApiExternaNaoEncontradaError):
            uc.get_by_id("nao-existe")

    def test_atualizar_api(self):
        repo = FakeApiRepo()
        uc = CriarApiExternaUseCase(repo)
        api = uc.execute(codigo="API-01", nome="API", url_base="https://api.test.gov.br")
        uc_act = AtualizarApiExternaUseCase(repo)
        actualizado = uc_act.execute(api.id, nome="API Atualizada", versao="2.0")
        assert actualizado.nome == "API Atualizada"
        assert actualizado.versao == "2.0"

    def test_mudar_estado_api(self):
        repo = FakeApiRepo()
        uc = CriarApiExternaUseCase(repo)
        api = uc.execute(codigo="API-01", nome="API", url_base="https://api.test.gov.br")
        uc_est = MudarEstadoApiUseCase(repo)
        actualizado = uc_est.execute(api.id, "ativa")
        assert actualizado.estado is EstadoApi.ATIVA

    def test_mudar_estado_api_nao_encontrada(self):
        repo = FakeApiRepo()
        uc = MudarEstadoApiUseCase(repo)
        with pytest.raises(ApiExternaNaoEncontradaError):
            uc.execute("nao-existe", "ativa")

    def test_deletar_api(self):
        repo = FakeApiRepo()
        uc = CriarApiExternaUseCase(repo)
        api = uc.execute(codigo="API-01", nome="API", url_base="https://api.test.gov.br")
        uc_del = DeletarApiExternaUseCase(repo)
        assert uc_del.execute(api.id) is True
        assert repo.get_by_id(api.id) is None

    def test_deletar_api_nao_encontrada(self):
        repo = FakeApiRepo()
        uc_del = DeletarApiExternaUseCase(repo)
        with pytest.raises(ApiExternaNaoEncontradaError):
            uc_del.execute("nao-existe")

    def test_listar_apis(self):
        repo = FakeApiRepo()
        uc = CriarApiExternaUseCase(repo)
        uc.execute(codigo="API-01", nome="API 1", url_base="https://api.test.gov.br")
        uc.execute(codigo="API-02", nome="API 2", url_base="https://api.test.gov.br", estado="ativa")
        uc_bus = BuscarApiExternaUseCase(repo)
        items, total = uc_bus.list_all(estado="ativa")
        assert total == 1


# ---------------------------------------------------------------------------
# Testes de casos de uso: Contratos de integração
# ---------------------------------------------------------------------------


class TestContratoUseCases:
    def test_criar_contrato_com_api(self):
        repo_c = FakeContratoRepo()
        repo_a = FakeApiRepo()
        uc_a = CriarApiExternaUseCase(repo_a)
        api = uc_a.execute(codigo="API-01", nome="API", url_base="https://api.test.gov.br")
        uc = CriarContratoIntegracaoUseCase(repo_c, repo_a)
        contrato = uc.execute(
            codigo="CONT-01",
            nome="Contrato",
            api_externa_id=api.id,
        )
        assert contrato.codigo == "CONT-01"
        assert contrato.estado is EstadoContrato.RASCUNHO

    def test_criar_contrato_api_inexistente(self):
        repo_c = FakeContratoRepo()
        repo_a = FakeApiRepo()
        uc = CriarContratoIntegracaoUseCase(repo_c, repo_a)
        with pytest.raises(ApiExternaNaoEncontradaError):
            uc.execute(codigo="CONT-01", nome="Contrato", api_externa_id="nao-existe")

    def test_criar_contrato_sin_api(self):
        repo_c = FakeContratoRepo()
        repo_a = FakeApiRepo()
        uc = CriarContratoIntegracaoUseCase(repo_c, repo_a)
        contrato = uc.execute(codigo="CONT-01", nome="Contrato")
        assert contrato.codigo == "CONT-01"
        assert contrato.api_externa_id == ""

    def test_criar_contrato_duplicado(self):
        repo_c = FakeContratoRepo()
        repo_a = FakeApiRepo()
        uc = CriarContratoIntegracaoUseCase(repo_c, repo_a)
        uc.execute(codigo="CONT-01", nome="C1")
        with pytest.raises(ContratoIntegracaoJaExisteError):
            uc.execute(codigo="CONT-01", nome="C2")

    def test_criar_contrato_codigo_invalido(self):
        repo_c = FakeContratoRepo()
        repo_a = FakeApiRepo()
        uc = CriarContratoIntegracaoUseCase(repo_c, repo_a)
        with pytest.raises(ValueError, match="código"):
            uc.execute(codigo="invalid", nome="C1")

    def test_approbar_contrato(self):
        repo_c = FakeContratoRepo()
        repo_a = FakeApiRepo()
        uc_c = CriarContratoIntegracaoUseCase(repo_c, repo_a)
        contrato = uc_c.execute(codigo="CONT-01", nome="C1")
        uc_apr = AprovarContratoIntegracaoUseCase(repo_c)
        actualizado = uc_apr.execute(contrato.id)
        assert actualizado.estado is EstadoContrato.VIGENTE

    def test_approbar_contrato_nao_encontrado(self):
        repo = FakeContratoRepo()
        uc = AprovarContratoIntegracaoUseCase(repo)
        with pytest.raises(ContratoIntegracaoNaoEncontradoError):
            uc.execute("nao-existe")

    def test_retirar_contrato(self):
        repo_c = FakeContratoRepo()
        repo_a = FakeApiRepo()
        uc_c = CriarContratoIntegracaoUseCase(repo_c, repo_a)
        uc_apr = AprovarContratoIntegracaoUseCase(repo_c)
        uc_ret = RetirarContratoIntegracaoUseCase(repo_c)
        contrato = uc_c.execute(codigo="CONT-01", nome="C1")
        contrato = uc_apr.execute(contrato.id)
        actualizado = uc_ret.execute(contrato.id)
        assert actualizado.estado is EstadoContrato.RETIRADO

    def test_retirar_contrato_nao_encontrado(self):
        repo = FakeContratoRepo()
        uc = RetirarContratoIntegracaoUseCase(repo)
        with pytest.raises(ContratoIntegracaoNaoEncontradoError):
            uc.execute("nao-existe")

    def test_atualizar_contrato(self):
        repo_c = FakeContratoRepo()
        repo_a = FakeApiRepo()
        uc_c = CriarContratoIntegracaoUseCase(repo_c, repo_a)
        contrato = uc_c.execute(codigo="CONT-01", nome="C1")
        uc_act = AtualizarContratoIntegracaoUseCase(repo_c)
        actualizado = uc_act.execute(contrato.id, nome="C Atualizado", versao_formato="2.0")
        assert actualizado.nome == "C Atualizado"
        assert actualizado.versao_formato == "2.0"

    def test_atualizar_contrato_nao_encontrado(self):
        repo = FakeContratoRepo()
        uc = AtualizarContratoIntegracaoUseCase(repo)
        with pytest.raises(ContratoIntegracaoNaoEncontradoError):
            uc.execute("nao-existe", nome="test")

    def test_buscar_contrato_nao_encontrado(self):
        repo = FakeContratoRepo()
        uc = BuscarContratoIntegracaoUseCase(repo)
        with pytest.raises(ContratoIntegracaoNaoEncontradoError):
            uc.get_by_id("nao-existe")

    def test_deletar_contrato(self):
        repo_c = FakeContratoRepo()
        repo_a = FakeApiRepo()
        uc = CriarContratoIntegracaoUseCase(repo_c, repo_a)
        contrato = uc.execute(codigo="CONT-01", nome="C1")
        uc_del = DeletarContratoIntegracaoUseCase(repo_c)
        assert uc_del.execute(contrato.id) is True

    def test_deletar_contrato_nao_encontrado(self):
        repo = FakeContratoRepo()
        uc = DeletarContratoIntegracaoUseCase(repo)
        with pytest.raises(ContratoIntegracaoNaoEncontradoError):
            uc.execute("nao-existe")


# ---------------------------------------------------------------------------
# Testes de casos de uso: Webhooks
# ---------------------------------------------------------------------------


class TestWebhookUseCases:
    def test_registrar_webhook_valido(self):
        repo = FakeWebhookRepo()
        uc = RegistrarWebhookUseCase(repo)
        w = uc.execute(
            nome="Webhook de prueba",
            url_destino="https://webhook.test.gov.br/endpoint",
            topicos=["gdo.doc.criado", "gdo.doc.borrado"],
        )
        assert w.nome == "Webhook de prueba"
        assert w.estado is EstadoInscricao.ATIVA
        assert w.topicos == ["gdo.doc.criado", "gdo.doc.borrado"]

    def test_registrar_webhook_url_invalida(self):
        repo = FakeWebhookRepo()
        uc = RegistrarWebhookUseCase(repo)
        with pytest.raises(UrlWebhookInvalidaError):
            uc.execute(
                nome="Webhook test",
                url_destino="ftp://webhook.test.gov.br",
                topicos=["*"],
            )

    def test_registrar_webhook_url_vacia(self):
        repo = FakeWebhookRepo()
        uc = RegistrarWebhookUseCase(repo)
        with pytest.raises(UrlWebhookInvalidaError):
            uc.execute(
                nome="Webhook test",
                url_destino="",
                topicos=["*"],
            )

    def test_registrar_webhook_nome_corto(self):
        repo = FakeWebhookRepo()
        uc = RegistrarWebhookUseCase(repo)
        with pytest.raises(ValueError, match="3 caracteres"):
            uc.execute(
                nome="ab",
                url_destino="https://webhook.test.gov.br",
                topicos=["*"],
            )

    def test_registrar_webhook_topicos_vacios(self):
        repo = FakeWebhookRepo()
        uc = RegistrarWebhookUseCase(repo)
        with pytest.raises(ValueError, match="tópico"):
            uc.execute(
                nome="Webhook test",
                url_destino="https://webhook.test.gov.br",
                topicos=[],
            )

    def test_registrar_webhook_duplicado(self):
        repo = FakeWebhookRepo()
        uc = RegistrarWebhookUseCase(repo)
        uc.execute(
            nome="Webhook test",
            url_destino="https://webhook.test.gov.br",
            topicos=["*"],
        )
        with pytest.raises(WebhookJaExisteError):
            uc.execute(
                nome="Webhook test",
                url_destino="https://otro.test.gov.br",
                topicos=["gdo.doc.criado"],
            )

    def test_registrar_webhook_max_tentativas_invalido(self):
        repo = FakeWebhookRepo()
        uc = RegistrarWebhookUseCase(repo)
        with pytest.raises(ValueError, match="max_tentativas"):
            uc.execute(
                nome="Webhook test",
                url_destino="https://webhook.test.gov.br",
                topicos=["*"],
                max_tentativas=0,
            )

    def test_registrar_webhook_backoff_negativo(self):
        repo = FakeWebhookRepo()
        uc = RegistrarWebhookUseCase(repo)
        with pytest.raises(ValueError, match="backoff_base_seg"):
            uc.execute(
                nome="Webhook test",
                url_destino="https://webhook.test.gov.br",
                topicos=["*"],
                backoff_base_seg=-1,
            )

    def test_buscar_webhook(self):
        repo = FakeWebhookRepo()
        uc_reg = RegistrarWebhookUseCase(repo)
        w = uc_reg.execute(
            nome="Webhook test",
            url_destino="https://webhook.test.gov.br",
            topicos=["gdo.doc.criado"],
        )
        uc_bus = BuscarWebhookUseCase(repo)
        assert uc_bus.get_by_id(w.id).nome == "Webhook test"

    def test_buscar_webhook_nao_encontrado(self):
        repo = FakeWebhookRepo()
        uc = BuscarWebhookUseCase(repo)
        with pytest.raises(WebhookNaoEncontradoError):
            uc.get_by_id("nao-existe")

    def test_atualizar_webhook(self):
        repo = FakeWebhookRepo()
        uc_reg = RegistrarWebhookUseCase(repo)
        w = uc_reg.execute(
            nome="Webhook test",
            url_destino="https://webhook.test.gov.br",
            topicos=["gdo.doc.criado"],
        )
        uc_act = AtualizarWebhookUseCase(repo)
        actualizado = uc_act.execute(
            w.id,
            url_destino="https://novo.test.gov.br",
            topicos=["gdo.doc.borrado"],
            max_tentativas=10,
        )
        assert actualizado.url_destino == "https://novo.test.gov.br"
        assert actualizado.topicos == ["gdo.doc.borrado"]
        assert actualizado.max_tentativas == 10

    def test_atualizar_webhook_nao_encontrado(self):
        repo = FakeWebhookRepo()
        uc = AtualizarWebhookUseCase(repo)
        with pytest.raises(WebhookNaoEncontradoError):
            uc.execute("nao-existe", url_destino="https://test.gov.br")

    def test_mudar_estado_webhook(self):
        repo = FakeWebhookRepo()
        uc_reg = RegistrarWebhookUseCase(repo)
        w = uc_reg.execute(
            nome="Webhook test",
            url_destino="https://webhook.test.gov.br",
            topicos=["*"],
        )
        uc_est = MudarEstadoWebhookUseCase(repo)
        actualizado = uc_est.execute(w.id, "desativada")
        assert actualizado.estado is EstadoInscricao.DESATIVADA

    def test_mudar_estado_webhook_nao_encontrado(self):
        repo = FakeWebhookRepo()
        uc = MudarEstadoWebhookUseCase(repo)
        with pytest.raises(WebhookNaoEncontradoError):
            uc.execute("nao-existe", "desativada")

    def test_deletar_webhook(self):
        repo = FakeWebhookRepo()
        uc_reg = RegistrarWebhookUseCase(repo)
        w = uc_reg.execute(
            nome="Webhook test",
            url_destino="https://webhook.test.gov.br",
            topicos=["*"],
        )
        uc_del = DeletarWebhookUseCase(repo)
        assert uc_del.execute(w.id) is True
        assert repo.get_by_id(w.id) is None

    def test_deletar_webhook_nao_encontrado(self):
        repo = FakeWebhookRepo()
        uc_del = DeletarWebhookUseCase(repo)
        with pytest.raises(WebhookNaoEncontradoError):
            uc_del.execute("nao-existe")

    def test_listar_webhooks(self):
        repo = FakeWebhookRepo()
        uc_reg = RegistrarWebhookUseCase(repo)
        uc_reg.execute(nome="Webhook A", url_destino="https://a.test.gov.br", topicos=["*"])
        uc_reg.execute(nome="Webhook B", url_destino="https://b.test.gov.br", topicos=["*"])
        uc_bus = BuscarWebhookUseCase(repo)
        items, total = uc_bus.list_all()
        assert total == 2


# ---------------------------------------------------------------------------
# Testes de casos de uso: Entregas
# ---------------------------------------------------------------------------


class TestEntregaUseCases:
    def test_get_by_id(self):
        repo = FakeEntregaRepo()
        uc = BuscarEntregaWebhookUseCase(repo)
        e = EntregaWebhook(
            webhook_id="wh-1",
            url_destino="https://webhook.test.gov.br",
            topico="gdo.doc.criado",
            evento_nome="DocumentoCriado",
            agregado_tipo="Documento",
            agregado_id="doc-1",
            payload={"id": "doc-1"},
        )
        repo.save(e)
        result = uc.get_by_id(e.id)
        assert result.id == e.id

    def test_get_by_id_nao_encontrado(self):
        repo = FakeEntregaRepo()
        uc = BuscarEntregaWebhookUseCase(repo)
        with pytest.raises(EntregaNaoEncontradaError):
            uc.get_by_id("nao-existe")

    def test_reenfileirar_entrega_bem_sucedida(self):
        repo = FakeEntregaRepo()
        uc = RetryEntregaWebhookUseCase(repo)
        e = EntregaWebhook(
            estado=EstadoEntrega.FALHOU,
            max_tentativas=5,
            tentativas=3,
        )
        repo.save(e)
        result = uc.execute(e.id)
        assert result.estado is EstadoEntrega.PENDENTE
        assert result.tentativas == 0
        assert result.proximo_retry is None
        assert result.ultimo_erro == ""

    def test_reenfileirar_entrega_nao_encontrada(self):
        repo = FakeEntregaRepo()
        uc = RetryEntregaWebhookUseCase(repo)
        with pytest.raises(EntregaNaoEncontradaError):
            uc.execute("nao-existe")

    def test_reenfileirar_entrega_ja_bem_sucedida(self):
        repo = FakeEntregaRepo()
        uc = RetryEntregaWebhookUseCase(repo)
        e = EntregaWebhook(estado=EstadoEntrega.SUCESSO)
        repo.save(e)
        with pytest.raises(EntregaEstadoInvalidoError):
            uc.execute(e.id)

    def test_reenfileirar_entrega_ja_pendente(self):
        repo = FakeEntregaRepo()
        uc = RetryEntregaWebhookUseCase(repo)
        e = EntregaWebhook(estado=EstadoEntrega.PENDENTE)
        repo.save(e)
        with pytest.raises(EntregaEstadoInvalidoError):
            uc.execute(e.id)

    def test_cancelar_entrega(self):
        repo = FakeEntregaRepo()
        uc = CancelarEntregaWebhookUseCase(repo)
        e = EntregaWebhook(estado=EstadoEntrega.PENDENTE)
        repo.save(e)
        result = uc.execute(e.id)
        assert result.estado is EstadoEntrega.CANCELADO

    def test_cancelar_entrega_ya_sucessosa(self):
        repo = FakeEntregaRepo()
        uc = CancelarEntregaWebhookUseCase(repo)
        e = EntregaWebhook(estado=EstadoEntrega.SUCESSO)
        repo.save(e)
        with pytest.raises(EntregaEstadoInvalidoError):
            uc.execute(e.id)

    def test_listar_entregas(self):
        repo = FakeEntregaRepo()
        e1 = EntregaWebhook(estado=EstadoEntrega.SUCESSO)
        e2 = EntregaWebhook(estado=EstadoEntrega.FALHOU)
        repo.save(e1)
        repo.save(e2)
        uc = BuscarEntregaWebhookUseCase(repo)
        items, total = uc.list_all()
        assert total == 2
        items, total = uc.list_all(estado="sucesso")
        assert total == 1
        assert items[0].estado is EstadoEntrega.SUCESSO


# ---------------------------------------------------------------------------
# Testes de casos de uso: Barramento de eventos (ConsomirOutbox + Despachar)
# ---------------------------------------------------------------------------


class TestBusUseCases:
    def test_fontes_validas(self):
        assert FONTES_OUTBOX_VALIDAS == ("gdo", "compras")

    def test_consumir_outbox_fonte_invalida(self):
        outbox = FakeOutboxSource()
        repo_w = FakeWebhookRepo()
        repo_e = FakeEntregaRepo()
        repo_ep = FakeEventoProcessadoRepo()
        uc = ConsumirOutboxUseCase(outbox, repo_w, repo_e, repo_ep)
        with pytest.raises(FonteOutboxInvalidaError):
            uc.execute(fonte="invalida", lote=10)

    def test_consumir_outbox_cria_entregas_para_webhooks_inscritos(self):
        outbox = FakeOutboxSource()
        repo_w = FakeWebhookRepo()
        repo_e = FakeEntregaRepo()
        repo_ep = FakeEventoProcessadoRepo()

        # Webhook inscrito a gdo.doc.criado
        wh = Webhook(
            nome="Webhook GDO",
            url_destino="https://webhook.test.gov.br",
            topicos=["gdo.doc.criado"],
            estado=EstadoInscricao.ATIVA,
        )
        repo_w.save(wh)

        evento = EventoOutbox(
            id="evt-1",
            topico="gdo.doc.criado",
            evento_nome="DocumentoCriado",
            agregado_tipo="Documento",
            agregado_id="doc-1",
            payload={"id": "doc-1"},
        )
        outbox.eventos.append(evento)

        uc = ConsumirOutboxUseCase(outbox, repo_w, repo_e, repo_ep)
        resumo = uc.execute(fonte="gdo", lote=10)

        assert resumo["lidos"] == 1
        assert resumo["novos"] == 1
        assert resumo["duplicados"] == 0
        assert resumo["entregas_criadas"] == 1

        entregas = repo_e.list_all()[0]
        assert len(entregas) == 1
        assert entregas[0].topico == "gdo.doc.criado"
        assert entregas[0].webhook_id == wh.id

        # Verificar idempotência: reapresenta o mesmo evento já processado.
        evento._publicado = False
        resumo2 = uc.execute(fonte="gdo", lote=10)
        assert resumo2["duplicados"] == 1
        assert resumo2["novos"] == 0
        assert resumo2["entregas_criadas"] == 0

    def test_consumir_outbox_sin_webhooks_inscritos(self):
        outbox = FakeOutboxSource()
        repo_w = FakeWebhookRepo()
        repo_e = FakeEntregaRepo()
        repo_ep = FakeEventoProcessadoRepo()

        evento = EventoOutbox(
            id="evt-1",
            topico="gdo.doc.criado",
            evento_nome="DocumentoCriado",
            agregado_tipo="Documento",
            agregado_id="doc-1",
        )
        outbox.eventos.append(evento)

        uc = ConsumirOutboxUseCase(outbox, repo_w, repo_e, repo_ep)
        resumo = uc.execute(fonte="gdo", lote=10)

        assert resumo["lidos"] == 1
        assert resumo["entregas_criadas"] == 0
        assert resumo["novos"] == 1

    def test_consumir_outbox_webhook_wildcard(self):
        outbox = FakeOutboxSource()
        repo_w = FakeWebhookRepo()
        repo_e = FakeEntregaRepo()
        repo_ep = FakeEventoProcessadoRepo()

        wh = Webhook(
            nome="Webhook Wildcard",
            url_destino="https://webhook.test.gov.br",
            topicos=["*"],
            estado=EstadoInscricao.ATIVA,
        )
        repo_w.save(wh)

        evento = EventoOutbox(
            id="evt-1",
            topico="gdo.doc.criado",
            evento_nome="DocumentoCriado",
            agregado_tipo="Documento",
            agregado_id="doc-1",
        )
        outbox.eventos.append(evento)

        uc = ConsumirOutboxUseCase(outbox, repo_w, repo_e, repo_ep)
        resumo = uc.execute(fonte="gdo", lote=10)

        assert resumo["entregas_criadas"] == 1

    def test_consumir_outbox_webhook_desativado_no_recebe(self):
        outbox = FakeOutboxSource()
        repo_w = FakeWebhookRepo()
        repo_e = FakeEntregaRepo()
        repo_ep = FakeEventoProcessadoRepo()

        wh = Webhook(
            nome="Webhook Desativado",
            url_destino="https://webhook.test.gov.br",
            topicos=["gdo.doc.criado"],
            estado=EstadoInscricao.DESATIVADA,
        )
        repo_w.save(wh)

        evento = EventoOutbox(
            id="evt-1",
            topico="gdo.doc.criado",
            evento_nome="DocumentoCriado",
        )
        outbox.eventos.append(evento)

        uc = ConsumirOutboxUseCase(outbox, repo_w, repo_e, repo_ep)
        resumo = uc.execute(fonte="gdo", lote=10)

        assert resumo["entregas_criadas"] == 0

    def test_consumir_outbox_multiple_webhooks(self):
        outbox = FakeOutboxSource()
        repo_w = FakeWebhookRepo()
        repo_e = FakeEntregaRepo()
        repo_ep = FakeEventoProcessadoRepo()

        wh1 = Webhook(
            nome="Webhook 1",
            url_destino="https://w1.test.gov.br",
            topicos=["gdo.doc.criado"],
            estado=EstadoInscricao.ATIVA,
        )
        wh2 = Webhook(
            nome="Webhook 2",
            url_destino="https://w2.test.gov.br",
            topicos=["gdo.doc.criado"],
            estado=EstadoInscricao.ATIVA,
        )
        wh3 = Webhook(
            nome="Webhook 3",
            url_destino="https://w3.test.gov.br",
            topicos=["compras.compra.criada"],
            estado=EstadoInscricao.ATIVA,
        )
        repo_w.save(wh1)
        repo_w.save(wh2)
        repo_w.save(wh3)

        evento = EventoOutbox(
            id="evt-1",
            topico="gdo.doc.criado",
            evento_nome="DocumentoCriado",
        )
        outbox.eventos.append(evento)

        uc = ConsumirOutboxUseCase(outbox, repo_w, repo_e, repo_ep)
        resumo = uc.execute(fonte="gdo", lote=10)

        assert resumo["entregas_criadas"] == 2  # wh1 e wh2, não wh3

    def test_despachar_webhooks_sucesso(self):
        repo_e = FakeEntregaRepo()
        transporte = FakeTransporte(ok=True, http_status=200)

        e = EntregaWebhook(
            url_destino="https://webhook.test.gov.br",
            topico="gdo.doc.criado",
            evento_nome="DocumentoCriado",
            agregado_tipo="Documento",
            agregado_id="doc-1",
            payload={"id": "doc-1"},
            estado=EstadoEntrega.PENDENTE,
            max_tentativas=5,
        )
        repo_e.save(e)

        uc = DespacharWebhooksUseCase(repo_e, transporte)
        resumo = uc.execute(lote=10)

        assert resumo["processadas"] == 1
        assert resumo["sucessos"] == 1
        assert resumo["falhas"] == 0
        assert resumo["fila_morta"] == 0
        assert e.estado is EstadoEntrega.SUCESSO
        assert e.tentativas == 1
        assert e.entregue_em is not None
        assert len(transporte.enviados) == 1

    def test_despachar_webhooks_falha_sem_esgotar(self):
        repo_e = FakeEntregaRepo()
        transporte = FakeTransporte(ok=False, http_status=500, erro="Server Error")

        e = EntregaWebhook(
            estado=EstadoEntrega.PENDENTE,
            max_tentativas=5,
            tentativas=0,
            backoff_base_seg=60,
        )
        repo_e.save(e)

        uc = DespacharWebhooksUseCase(repo_e, transporte)
        resumo = uc.execute(lote=10)

        assert resumo["processadas"] == 1
        assert resumo["sucessos"] == 0
        assert resumo["falhas"] == 1
        assert resumo["fila_morta"] == 0
        assert e.estado is EstadoEntrega.FALHOU
        assert e.tentativas == 1
        assert e.ultimo_http_status == 500

    def test_despachar_webhooks_falha_esgota_fila_morta(self):
        repo_e = FakeEntregaRepo()
        transporte = FakeTransporte(ok=False, http_status=500, erro="Server Error")

        e = EntregaWebhook(
            estado=EstadoEntrega.PENDENTE,
            max_tentativas=1,
            tentativas=0,
            backoff_base_seg=60,
        )
        repo_e.save(e)

        uc = DespacharWebhooksUseCase(repo_e, transporte)
        resumo = uc.execute(lote=10)

        assert resumo["processadas"] == 1
        assert resumo["sucessos"] == 0
        assert resumo["falhas"] == 0
        assert resumo["fila_morta"] == 1
        assert e.estado is EstadoEntrega.FILA_MORTA

    def test_despachar_webhooks_sem_pendentes(self):
        repo_e = FakeEntregaRepo()
        transporte = FakeTransporte(ok=True)

        e_sucesso = EntregaWebhook(estado=EstadoEntrega.SUCESSO)
        repo_e.save(e_sucesso)

        uc = DespacharWebhooksUseCase(repo_e, transporte)
        resumo = uc.execute(lote=10)

        assert resumo["processadas"] == 0
        assert resumo["sucessos"] == 0

    def test_despachar_webhooks_payload_envelope(self):
        """Verifica que o envio inclui o envelope correto do barramento."""
        repo_e = FakeEntregaRepo()
        transporte = FakeTransporte(ok=True)

        e = EntregaWebhook(
            url_destino="https://webhook.test.gov.br",
            topico="gdo.doc.criado",
            evento_nome="DocumentoCriado",
            agregado_tipo="Documento",
            agregado_id="doc-1",
            payload={"id": "doc-1"},
            estado=EstadoEntrega.PENDENTE,
        )
        repo_e.save(e)

        uc = DespacharWebhooksUseCase(repo_e, transporte)
        uc.execute(lote=10)

        _, payload = transporte.enviados[0]
        assert payload["topico"] == "gdo.doc.criado"
        assert payload["evento_nome"] == "DocumentoCriado"
        assert payload["agregado_tipo"] == "Documento"
        assert payload["agregado_id"] == "doc-1"
        assert payload["tentativa"] == 0
        assert payload["payload"] == {"id": "doc-1"}
