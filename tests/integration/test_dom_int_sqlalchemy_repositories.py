"""Testes de integração dos repositórios SQLAlchemy do DOM-INT.

Validam os seis repositórios concretos contra o PostgreSQL configurado
pelo SIGMUN.

Isolamento:
    Cada teste utiliza uma transação externa que é revertida ao final.
    Nenhum dado criado pelos testes permanece no banco.

Escopo:
    - catálogo de APIs externas;
    - contratos de integração;
    - conectores;
    - webhooks;
    - entregas de webhook;
    - eventos processados/inbox;
    - soft-delete;
    - filtros e paginação;
    - FKs materializadas na migração DOM-INT;
    - unicidade da chave de idempotência.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from uuid import uuid4

import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import engine
from src.modules.sigmun_int.domain.entities import (
    ApiExterna,
    AutenticacaoApi,
    Conector,
    ContratoIntegracao,
    EntregaWebhook,
    EstadoApi,
    EstadoConector,
    EstadoContrato,
    EstadoEntrega,
    EstadoInscricao,
    EventoProcessado,
    TipoApi,
    Webhook,
)
from src.modules.sigmun_int.infrastructure.repositories.sqlalchemy_api_externa_repository import (
    SqlAlchemyApiExternaRepository,
)
from src.modules.sigmun_int.infrastructure.repositories.sqlalchemy_conector_repository import (
    SqlAlchemyConectorRepository,
)
from src.modules.sigmun_int.infrastructure.repositories.sqlalchemy_contrato_repository import (
    SqlAlchemyContratoIntegracaoRepository,
)
from src.modules.sigmun_int.infrastructure.repositories.sqlalchemy_entrega_repository import (
    SqlAlchemyEntregaWebhookRepository,
)
from src.modules.sigmun_int.infrastructure.repositories.sqlalchemy_evento_processado_repository import (
    SqlAlchemyEventoProcessadoRepository,
)
from src.modules.sigmun_int.infrastructure.repositories.sqlalchemy_webhook_repository import (
    SqlAlchemyWebhookRepository,
)


@pytest.fixture
def session() -> Session:
    """Sessão PostgreSQL isolada por rollback."""
    connection = engine.connect()
    transaction = connection.begin()

    session = Session(bind=connection, expire_on_commit=False)

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()


def _codigo(prefixo: str) -> str:
    return f"{prefixo}-{uuid4().hex[:10].upper()}"


def _api(codigo: str | None = None, **kwargs) -> ApiExterna:
    return ApiExterna(
        codigo=codigo or _codigo("API"),
        nome="API de Teste",
        descricao="API criada pelo teste de integração",
        provedor="SIGMUN Testes",
        url_base="https://example.test/api",
        **kwargs,
    )


def _contrato(api_id: str, codigo: str | None = None, **kwargs) -> ContratoIntegracao:
    return ContratoIntegracao(
        codigo=codigo or _codigo("CTR"),
        nome="Contrato de Integração de Teste",
        descricao="Contrato criado pelo teste de integração",
        versao_formato="1.0",
        esquema_ref="https://example.test/schema.json",
        api_externa_id=api_id,
        **kwargs,
    )


def _conector(codigo: str | None = None, **kwargs) -> Conector:
    return Conector(
        codigo=codigo or _codigo("CON"),
        nome="Conector de Teste",
        descricao="Conector criado pelo teste de integração",
        provedor="SIGMUN Testes",
        url_base="https://example.test",
        autenticacao_tipo="oauth2",
        config={"ambiente": "teste"},
        **kwargs,
    )


def _webhook(nome: str | None = None, **kwargs) -> Webhook:
    return Webhook(
        nome=nome or _codigo("WH"),
        url_destino="https://example.test/webhook",
        segredo_ref="secret:test",
        topicos=["compras.contrato.criado", "gdo.documento.criado"],
        cabecalhos={"X-SIGMUN-Test": "true"},
        **kwargs,
    )


def _entrega(webhook_id: str, **kwargs) -> EntregaWebhook:
    return EntregaWebhook(
        webhook_id=webhook_id,
        url_destino="https://example.test/webhook",
        cabecalhos={"Content-Type": "application/json"},
        topico="compras.contrato.criado",
        evento_nome="ContratoCriado",
        agregado_tipo="Contrato",
        agregado_id=str(uuid4()),
        payload={"teste": True},
        **kwargs,
    )


def _evento(
    fonte: str | None = None,
    evento_outbox_id: str | None = None,
    **kwargs,
) -> EventoProcessado:
    return EventoProcessado(
        fonte=fonte or "compras",
        evento_outbox_id=evento_outbox_id or str(uuid4()),
        topico="compras.contrato.criado",
        evento_nome="ContratoCriado",
        agregado_tipo="Contrato",
        agregado_id=str(uuid4()),
        payload={"teste": True},
        **kwargs,
    )


# ---------------------------------------------------------------------------
# API EXTERNA
# ---------------------------------------------------------------------------


class TestSqlAlchemyApiExternaRepository:
    def test_save_get_codigo_exists_e_list(self, session: Session) -> None:
        repo = SqlAlchemyApiExternaRepository(session)
        api = _api()

        salvo = repo.save(api)

        assert salvo.id == api.id
        assert repo.get_by_id(api.id).codigo == api.codigo
        assert repo.get_by_codigo(api.codigo).id == api.id
        assert repo.exists_by_codigo(api.codigo)

        itens, total = repo.list_all()
        assert total >= 1
        assert api.id in {item.id for item in itens}

    def test_update_persiste_alteracoes(self, session: Session) -> None:
        repo = SqlAlchemyApiExternaRepository(session)
        api = repo.save(_api())

        api.nome = "API Atualizada"
        api.estado = EstadoApi.ATIVA
        api.tipo = TipoApi.GRAPHQL
        api.autenticacao = AutenticacaoApi.API_KEY
        repo.save(api)

        obtida = repo.get_by_id(api.id)

        assert obtida is not None
        assert obtida.nome == "API Atualizada"
        assert obtida.estado is EstadoApi.ATIVA
        assert obtida.tipo is TipoApi.GRAPHQL
        assert obtida.autenticacao is AutenticacaoApi.API_KEY

    def test_filtros_estado_tipo_e_paginacao(self, session: Session) -> None:
        repo = SqlAlchemyApiExternaRepository(session)

        ativa = repo.save(
            _api(
                estado=EstadoApi.ATIVA,
                tipo=TipoApi.REST,
            )
        )
        repo.save(
            _api(
                estado=EstadoApi.RASCUNHO,
                tipo=TipoApi.SOAP,
            )
        )

        itens, total = repo.list_all(estado="ativa", tipo="rest")

        assert total == 1
        assert [item.id for item in itens] == [ativa.id]

    def test_delete_e_soft_delete(self, session: Session) -> None:
        repo = SqlAlchemyApiExternaRepository(session)
        api = repo.save(_api())

        assert repo.delete(api.id) is True
        assert repo.get_by_id(api.id) is None
        assert not repo.exists_by_codigo(api.codigo)

        itens, total = repo.list_all()
        assert api.id not in {item.id for item in itens}

    def test_delete_inexistente_retorna_false(self, session: Session) -> None:
        repo = SqlAlchemyApiExternaRepository(session)

        assert repo.delete(str(uuid4())) is False


# ---------------------------------------------------------------------------
# CONTRATO DE INTEGRAÇÃO
# ---------------------------------------------------------------------------


class TestSqlAlchemyContratoIntegracaoRepository:
    def test_save_get_codigo_exists_e_list_por_api(self, session: Session) -> None:
        api_repo = SqlAlchemyApiExternaRepository(session)
        contrato_repo = SqlAlchemyContratoIntegracaoRepository(session)

        api = api_repo.save(_api())
        contrato = contrato_repo.save(_contrato(api.id))

        obtido = contrato_repo.get_by_id(contrato.id)

        assert obtido is not None
        assert obtido.codigo == contrato.codigo
        assert obtido.api_externa_id == api.id
        assert contrato_repo.get_by_codigo(contrato.codigo).id == contrato.id
        assert contrato_repo.exists_by_codigo(contrato.codigo)

        itens, total = contrato_repo.list_all(api_externa_id=api.id)
        assert total == 1
        assert [item.id for item in itens] == [contrato.id]

    def test_update_e_filtro_por_estado(self, session: Session) -> None:
        api_repo = SqlAlchemyApiExternaRepository(session)
        contrato_repo = SqlAlchemyContratoIntegracaoRepository(session)

        api = api_repo.save(_api())
        contrato = contrato_repo.save(_contrato(api.id))

        contrato.nome = "Contrato Atualizado"
        contrato.estado = EstadoContrato.VIGENTE
        contrato_repo.save(contrato)

        obtido = contrato_repo.get_by_id(contrato.id)
        assert obtido is not None
        assert obtido.nome == "Contrato Atualizado"
        assert obtido.estado is EstadoContrato.VIGENTE

        itens, total = contrato_repo.list_all(estado="vigente")
        assert total == 1
        assert contrato.id in {item.id for item in itens}

    def test_delete_e_soft_delete(self, session: Session) -> None:
        api_repo = SqlAlchemyApiExternaRepository(session)
        contrato_repo = SqlAlchemyContratoIntegracaoRepository(session)

        api = api_repo.save(_api())
        contrato = contrato_repo.save(_contrato(api.id))

        assert contrato_repo.delete(contrato.id) is True
        assert contrato_repo.get_by_id(contrato.id) is None
        assert not contrato_repo.exists_by_codigo(contrato.codigo)

    def test_fk_api_externa_rejeita_id_inexistente(self, session: Session) -> None:
        repo = SqlAlchemyContratoIntegracaoRepository(session)

        contrato = _contrato(str(uuid4()))

        with pytest.raises(IntegrityError):
            with session.begin_nested():
                repo.save(contrato)


# ---------------------------------------------------------------------------
# CONECTOR
# ---------------------------------------------------------------------------


class TestSqlAlchemyConectorRepository:
    def test_save_get_codigo_exists_e_list(self, session: Session) -> None:
        repo = SqlAlchemyConectorRepository(session)
        conector = repo.save(_conector())

        obtido = repo.get_by_id(conector.id)

        assert obtido is not None
        assert obtido.codigo == conector.codigo
        assert obtido.config == {"ambiente": "teste"}
        assert repo.get_by_codigo(conector.codigo).id == conector.id
        assert repo.exists_by_codigo(conector.codigo)

        itens, total = repo.list_all()
        assert total >= 1
        assert conector.id in {item.id for item in itens}

    def test_filtro_estado_e_paginacao(self, session: Session) -> None:
        repo = SqlAlchemyConectorRepository(session)

        ativo = repo.save(_conector(estado=EstadoConector.ATIVO))
        repo.save(_conector(estado=EstadoConector.TESTES))

        itens, total = repo.list_all(
            page=0,
            page_size=10,
            estado="ativo",
        )

        assert total == 1
        assert [item.id for item in itens] == [ativo.id]

    def test_update_e_delete(self, session: Session) -> None:
        repo = SqlAlchemyConectorRepository(session)
        conector = repo.save(_conector())

        conector.nome = "Conector Atualizado"
        conector.config = {"ambiente": "producao"}
        repo.save(conector)

        obtido = repo.get_by_id(conector.id)
        assert obtido is not None
        assert obtido.nome == "Conector Atualizado"
        assert obtido.config == {"ambiente": "producao"}

        assert repo.delete(conector.id) is True
        assert repo.get_by_id(conector.id) is None
        assert not repo.exists_by_codigo(conector.codigo)


# ---------------------------------------------------------------------------
# WEBHOOK
# ---------------------------------------------------------------------------


class TestSqlAlchemyWebhookRepository:
    def test_save_get_nome_exists_list_e_ativos(self, session: Session) -> None:
        repo = SqlAlchemyWebhookRepository(session)

        ativo = repo.save(_webhook())
        desativado = repo.save(_webhook(estado=EstadoInscricao.DESATIVADA))

        obtido = repo.get_by_id(ativo.id)

        assert obtido is not None
        assert obtido.nome == ativo.nome
        assert obtido.topicos == ativo.topicos
        assert obtido.cabecalhos == ativo.cabecalhos
        assert repo.get_by_nome(ativo.nome).id == ativo.id
        assert repo.exists_by_nome(ativo.nome)

        ativos = repo.find_ativos()
        assert ativo.id in {item.id for item in ativos}
        assert desativado.id not in {item.id for item in ativos}

        itens, total = repo.list_all(estado="ativa")
        assert total == 1
        assert [item.id for item in itens] == [ativo.id]

    def test_update_e_delete(self, session: Session) -> None:
        repo = SqlAlchemyWebhookRepository(session)
        webhook = repo.save(_webhook())

        webhook.url_destino = "https://example.test/webhook-v2"
        webhook.topicos = ["novo.topico"]
        repo.save(webhook)

        obtido = repo.get_by_id(webhook.id)
        assert obtido is not None
        assert obtido.url_destino.endswith("/webhook-v2")
        assert obtido.topicos == ["novo.topico"]

        assert repo.delete(webhook.id) is True
        assert repo.get_by_id(webhook.id) is None
        assert not repo.exists_by_nome(webhook.nome)


# ---------------------------------------------------------------------------
# ENTREGA DE WEBHOOK
# ---------------------------------------------------------------------------


class TestSqlAlchemyEntregaWebhookRepository:
    def test_save_get_e_list_by_webhook(self, session: Session) -> None:
        webhook_repo = SqlAlchemyWebhookRepository(session)
        entrega_repo = SqlAlchemyEntregaWebhookRepository(session)

        webhook = webhook_repo.save(_webhook())
        entrega = entrega_repo.save(_entrega(webhook.id))

        obtida = entrega_repo.get_by_id(entrega.id)

        assert obtida is not None
        assert obtida.webhook_id == webhook.id
        assert obtida.payload == {"teste": True}
        assert obtida.estado is EstadoEntrega.PENDENTE

        itens, total = entrega_repo.list_by_webhook(webhook.id)
        assert total == 1
        assert [item.id for item in itens] == [entrega.id]

    def test_list_pendentes_para_retry_respeita_janela(self, session: Session) -> None:
        webhook_repo = SqlAlchemyWebhookRepository(session)
        entrega_repo = SqlAlchemyEntregaWebhookRepository(session)

        webhook = webhook_repo.save(_webhook())
        agora = datetime.now(timezone.utc)

        pronta = entrega_repo.save(
            _entrega(
                webhook.id,
                proximo_retry=None,
            )
        )
        futura = entrega_repo.save(
            _entrega(
                webhook.id,
                proximo_retry=agora + timedelta(minutes=10),
            )
        )

        vencida = entrega_repo.save(
            _entrega(
                webhook.id,
                proximo_retry=agora - timedelta(minutes=10),
            )
        )

        itens = entrega_repo.list_pendentes_para_retry(lote=10, agora=agora)
        ids = {item.id for item in itens}

        assert pronta.id in ids
        assert vencida.id in ids
        assert futura.id not in ids

    def test_list_pendentes_respeita_lote_e_estado(self, session: Session) -> None:
        webhook_repo = SqlAlchemyWebhookRepository(session)
        entrega_repo = SqlAlchemyEntregaWebhookRepository(session)

        webhook = webhook_repo.save(_webhook())
        agora = datetime.now(timezone.utc)

        primeiras = [
            entrega_repo.save(_entrega(webhook.id))
            for _ in range(3)
        ]

        sucesso = _entrega(webhook.id)
        sucesso.registrar_sucesso(200, agora)
        entrega_repo.save(sucesso)

        itens = entrega_repo.list_pendentes_para_retry(lote=2, agora=agora)

        assert len(itens) == 2
        assert all(item.estado is EstadoEntrega.PENDENTE for item in itens)
        assert {item.id for item in itens} <= {item.id for item in primeiras}

    def test_fk_webhook_rejeita_id_inexistente(self, session: Session) -> None:
        repo = SqlAlchemyEntregaWebhookRepository(session)

        with pytest.raises(IntegrityError):
            with session.begin_nested():
                repo.save(_entrega(str(uuid4())))

    def test_update_e_delete(self, session: Session) -> None:
        webhook_repo = SqlAlchemyWebhookRepository(session)
        entrega_repo = SqlAlchemyEntregaWebhookRepository(session)

        webhook = webhook_repo.save(_webhook())
        entrega = entrega_repo.save(_entrega(webhook.id))

        agora = datetime.now(timezone.utc)
        entrega.registrar_falha(500, "erro de teste", agora)
        entrega_repo.save(entrega)

        obtida = entrega_repo.get_by_id(entrega.id)
        assert obtida is not None
        assert obtida.tentativas == 1
        assert obtida.estado is EstadoEntrega.FALHOU
        assert obtida.ultimo_http_status == 500
        assert obtida.proximo_retry is not None

        assert entrega_repo.delete(entrega.id) is True
        assert entrega_repo.get_by_id(entrega.id) is None


# ---------------------------------------------------------------------------
# EVENTO PROCESSADO / IDEMPOTÊNCIA
# ---------------------------------------------------------------------------


class TestSqlAlchemyEventoProcessadoRepository:
    def test_save_get_exists_e_list(self, session: Session) -> None:
        repo = SqlAlchemyEventoProcessadoRepository(session)
        evento = repo.save(_evento())

        obtido = repo.get_by_evento_outbox(
            evento.fonte,
            evento.evento_outbox_id,
        )

        assert obtido is not None
        assert obtido.id == evento.id
        assert obtido.payload == {"teste": True}
        assert repo.exists(evento.fonte, evento.evento_outbox_id)

        itens, total = repo.list_all(fonte=evento.fonte)
        assert total == 1
        assert [item.id for item in itens] == [evento.id]

    def test_delete_remove_evento_da_consulta_logica(self, session: Session) -> None:
        repo = SqlAlchemyEventoProcessadoRepository(session)
        evento = repo.save(_evento())

        assert repo.delete(evento.id) is True
        assert repo.get_by_evento_outbox(
            evento.fonte,
            evento.evento_outbox_id,
        ) is None
        assert not repo.exists(evento.fonte, evento.evento_outbox_id)

    def test_constraint_idempotencia_fonte_evento(self, session: Session) -> None:
        repo = SqlAlchemyEventoProcessadoRepository(session)

        fonte = "compras"
        evento_outbox_id = str(uuid4())

        primeiro = repo.save(
            _evento(
                fonte=fonte,
                evento_outbox_id=evento_outbox_id,
            )
        )

        with session.begin_nested():
            with pytest.raises(IntegrityError):
                repo.save(
                    _evento(
                        fonte=fonte,
                        evento_outbox_id=evento_outbox_id,
                    )
                )

        assert repo.exists(fonte, evento_outbox_id)
        assert repo.get_by_evento_outbox(fonte, evento_outbox_id).id == primeiro.id

    def test_mesmo_id_em_fontes_diferentes_e_permitido(self, session: Session) -> None:
        repo = SqlAlchemyEventoProcessadoRepository(session)

        evento_id = str(uuid4())

        gdo = repo.save(
            _evento(
                fonte="gdo",
                evento_outbox_id=evento_id,
            )
        )
        compras = repo.save(
            _evento(
                fonte="compras",
                evento_outbox_id=evento_id,
            )
        )

        assert gdo.id != compras.id
        assert repo.exists("gdo", evento_id)
        assert repo.exists("compras", evento_id)

    def test_paginacao_e_filtro_por_fonte(self, session: Session) -> None:
        repo = SqlAlchemyEventoProcessadoRepository(session)

        eventos = [
            repo.save(_evento(fonte="gdo"))
            for _ in range(3)
        ]
        repo.save(_evento(fonte="compras"))

        itens, total = repo.list_all(
            page=0,
            page_size=2,
            fonte="gdo",
        )

        assert total == 3
        assert len(itens) == 2
        assert {item.id for item in itens} <= {item.id for item in eventos}

    def test_delete_inexistente_retorna_false(self, session: Session) -> None:
        repo = SqlAlchemyEventoProcessadoRepository(session)

        assert repo.delete(str(uuid4())) is False
