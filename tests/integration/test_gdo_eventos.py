"""Testes de integração dos eventos de integração do DOM-GDO.

Validam o padrão Transactional Outbox (014-Modelo-de-Integracao, seção 6):
os endpoints de escrita gravam eventos em `gdo.eventos_outbox` na mesma
transação do negócio, e o `DespachadorRedisStreams` publica os eventos
pendentes em streams do Redis (testado contra o Redis local).
"""

import uuid

import pytest
import redis as redis_lib
from fastapi.testclient import TestClient
from sqlalchemy import select, text

from src.core.infrastructure.database.session import SessionLocal
from src.main import app
from src.modules.sigmun_gdo.infrastructure.database.models import EventoOutboxModel
from src.modules.sigmun_gdo.infrastructure.messaging import (
    TopicosGDO,
    despachar_eventos_pendentes,
)

TABELAS_EVENTOS = (
    "gdo.eventos_outbox",
    "gdo.assinaturas_documentos",
    "gdo.arquivamentos_documentos",
    "gdo.tramitacoes_documentos",
    "gdo.versoes_documentos",
    "gdo.documentos",
    "gdo.processos_documentos",
    "gdo.tipos_documentais",
)

TOPICOS = [t for attr, t in vars(TopicosGDO).items() if not attr.startswith("_")]


@pytest.fixture(autouse=True)
def _isolamento_eventos():
    """Limpa tabelas do schema gdo e os streams do Redis usados nos testes."""
    with SessionLocal() as session:
        session.execute(text(f"TRUNCATE TABLE {', '.join(TABELAS_EVENTOS)} CASCADE"))
        session.commit()
    redis = redis_lib.Redis.from_url(
        "redis://localhost:6379/0", decode_responses=True
    )
    redis.delete(*TOPICOS)
    yield
    redis.delete(*TOPICOS)
    with SessionLocal() as session:
        session.execute(text(f"TRUNCATE TABLE {', '.join(TABELAS_EVENTOS)} CASCADE"))
        session.commit()


@pytest.fixture()
def client() -> TestClient:
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def _tipo_documento_para_eventos():
    """Garante um tipo documental ativo para os testes de eventos."""
    from src.modules.sigmun_gdo.infrastructure.database.models import TipoDocumentalModel
    with SessionLocal() as session:
        tipo = session.query(TipoDocumentalModel).filter_by(codigo="TD-OFICIO").first()
        if not tipo:
            session.add(TipoDocumentalModel(
                codigo="TD-OFICIO", nome="Ofício", descricao="Documento de teste", is_ativo=True
            ))
            session.commit()
    yield


@pytest.fixture()
def db():
    """Sessão independente para inspecionar a outbox e despachar eventos."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def _payload(**overrides) -> dict:
    dados = {
        "codigo": f"DOC-{uuid.uuid4().hex[:10].upper()}",
        "numero": "0001",
        "ano": 2026,
        "tipo_documental_id": "TD-OFICIO",
        "titulo": "Ofício para teste de eventos",
        "descricao": "Documento criado para validar a outbox",
        "unidade_autor_id": "UNIDADE-01",
    }
    dados.update(overrides)
    return dados


def _eventos_da_sessao(db, topico: str | None = None) -> list[EventoOutboxModel]:
    query = select(EventoOutboxModel).order_by(EventoOutboxModel.created_at)
    if topico:
        query = query.where(EventoOutboxModel.topico == topico)
    return list(db.scalars(query).all())


# =============================================================================
# Outbox — eventos gravados na mesma transação do negócio
# =============================================================================


def test_criar_documento_publica_evento_criado(client: TestClient, db):
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()

    eventos = _eventos_da_sessao(db, TopicosGDO.DOCUMENTO_CRIADO)

    assert len(eventos) == 1
    evento = eventos[0]
    assert evento.evento_nome == "DocumentoCriado"
    assert evento.agregado_tipo == "documento"
    assert evento.agregado_id == criado["id"]
    assert evento.status == "pendente"
    assert evento.published_at is None
    assert evento.payload["codigo"] == criado["codigo"]
    assert evento.payload["documento_id"] == criado["id"]
    assert evento.payload["status"] == criado["status"]


def test_criar_documento_com_processo_publica_dois_eventos(
    client: TestClient, db
):
    """Documento vinculado a processo publica `criado` e `vinculado_processo`."""
    from sqlalchemy import text as sql_text

    with SessionLocal() as session:
        row = session.execute(
            sql_text(
                "INSERT INTO gdo.processos_documentos "
                "(id, numero, ano, tipo_processo_id, titulo, unidade_autor_id, "
                "data_abertura, status, created_at, updated_at) "
                "VALUES (gen_random_uuid(), '00042', 2026, 'TP-TEST', "
                "'Processo de eventos', 'UNIDADE-01', now(), 'aberto', "
                "now(), now()) RETURNING id"
            )
        )
        processo_id = str(row.scalar_one())
        session.commit()

    client.post("/api/v1/gdo/documentos", json=_payload(processo_id=processo_id))

    topicos = [e.topico for e in _eventos_da_sessao(db)]

    assert topicos == [
        TopicosGDO.DOCUMENTO_CRIADO,
        TopicosGDO.DOCUMENTO_VINCULADO_PROCESSO,
    ]
    vinculado = _eventos_da_sessao(db, TopicosGDO.DOCUMENTO_VINCULADO_PROCESSO)[0]
    assert vinculado.evento_nome == "DocumentoVinculadoProcesso"
    assert vinculado.payload["processo_id"] == processo_id


def test_tramitar_publica_evento_tramitado(client: TestClient, db):
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()
    client.post(
        f"/api/v1/gdo/documentos/{criado['id']}/tramitar",
        json={
            "unidade_origem_id": "UNIDADE-01",
            "unidade_destino_id": "UNIDADE-02",
            "tipo": "envio",
            "motivo": "Encaminhado para análise",
        },
    )

    eventos = _eventos_da_sessao(db, TopicosGDO.DOCUMENTO_TRAMITADO)

    assert len(eventos) == 1
    assert eventos[0].evento_nome == "DocumentoTramitado"
    assert eventos[0].agregado_id == criado["id"]
    assert eventos[0].payload["unidade_destino_id"] == "UNIDADE-02"


def test_arquivar_publica_evento_arquivado(client: TestClient, db):
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()
    resposta = client.post(
        f"/api/v1/gdo/documentos/{criado['id']}/arquivar",
        json={
            "unidade_arquivo_id": "ARQ-01",
            "autor_id": "USER-10",
            "observacao": "Arquivamento inicial",
        },
    )

    assert resposta.status_code == 201, resposta.text
    eventos = _eventos_da_sessao(db, TopicosGDO.DOCUMENTO_ARQUIVADO)

    assert len(eventos) == 1
    assert eventos[0].evento_nome == "DocumentoArquivado"
    assert eventos[0].payload["status"] == "arquivado"


def test_assinar_publica_evento_assinado(client: TestClient, db):
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()
    resposta = client.post(
        f"/api/v1/gdo/documentos/{criado['id']}/assinar",
        json={
            "signatario_id": "USER-42",
            "conteudo": "a" * 64,
            "autor_id": "USER-42",
            "certificado_id": "CERT-ICP-01",
        },
    )

    assert resposta.status_code == 201, resposta.text
    eventos = _eventos_da_sessao(db, TopicosGDO.DOCUMENTO_ASSINADO)

    assert len(eventos) == 1
    assert eventos[0].evento_nome == "DocumentoAssinado"
    assert eventos[0].payload["signatario_id"] == "USER-42"


def test_destinacao_eliminacao_publica_evento_eliminado(client: TestClient, db):
    """RN-GDO-011: eliminação homologada publica `gdo.documento.eliminado`."""
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()
    resposta = client.post(
        f"/api/v1/gdo/documentos/{criado['id']}/destinacao",
        json={
            "tipo_destinacao": "eliminacao",
            "autor_id": "USER-10",
            "autoridade_homologadora_id": "AUTH-99",
            "justificativa": "Prazo de retenção expirado",
        },
    )

    assert resposta.status_code == 200, resposta.text
    eventos = _eventos_da_sessao(db, TopicosGDO.DOCUMENTO_ELIMINADO)

    assert len(eventos) == 1
    assert eventos[0].evento_nome == "DocumentoEliminado"
    assert eventos[0].payload["autoridade_homologadora_id"] == "AUTH-99"


# =============================================================================
# Dispatcher — despacho da outbox para Redis Streams
# =============================================================================


def test_despachar_publica_eventos_no_redis(client: TestClient, db):
    """Eventos pendentes são publicados no stream do tópico e marcados."""
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()

    resultado = despachar_eventos_pendentes(db)

    assert resultado["processados"] == 1
    assert resultado["publicados"] == 1
    assert resultado["erros"] == 0

    eventos = _eventos_da_sessao(db, TopicosGDO.DOCUMENTO_CRIADO)
    assert eventos[0].status == "publicado"
    assert eventos[0].published_at is not None

    redis = redis_lib.Redis.from_url("redis://localhost:6379/0", decode_responses=True)
    entradas = redis.xrange(TopicosGDO.DOCUMENTO_CRIADO, count=10)
    assert len(entradas) == 1
    campos = entradas[0][1]
    assert campos["evento_id"] == str(eventos[0].id)
    assert campos["evento_nome"] == "DocumentoCriado"
    assert criado["codigo"] in campos["payload"]


def test_despachar_sem_pendentes_retorna_zero(db):
    resultado = despachar_eventos_pendentes(db)

    assert resultado == {"processados": 0, "publicados": 0, "erros": 0}


def test_despachar_falha_incrementa_tentativas_e_marca_erro(db):
    """Falha de broker registra tentativa; ao esgotar, marca status `erro`."""
    with SessionLocal() as session:
        session.add(
            EventoOutboxModel(
                topico=TopicosGDO.DOCUMENTO_PUBLICADO,
                evento_nome="DocumentoPublicado",
                agregado_tipo="documento",
                agregado_id=str(uuid.uuid4()),
                payload={"codigo": "DOC-X"},
                status="pendente",
            )
        )
        session.commit()

    # Broker inacessível (porta fechada) — 2 tentativas esgotam o limite
    from src.modules.sigmun_gdo.infrastructure.messaging import (
        DespachadorRedisStreams,
    )

    despachador = DespachadorRedisStreams(
        "redis://localhost:59999/0", max_tentativas=2
    )

    primeira = despachador.despachar(db)
    segunda = despachador.despachar(db)

    assert primeira["erros"] == 1
    assert segunda["erros"] == 1
    eventos = _eventos_da_sessao(db, TopicosGDO.DOCUMENTO_PUBLICADO)
    assert eventos[0].tentativas == 2
    assert eventos[0].status == "erro"
    assert eventos[0].ultimo_erro  # mensagem de falha registrada
