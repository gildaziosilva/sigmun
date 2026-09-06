"""Testes de integração dos endpoints de Gestão Documental (DOM-GDO).

Exercitam o ciclo completo requisição -> API -> use case -> repositório ->
PostgreSQL (schema gdo), conforme migração 20260901_02. Os dados criados são
limpos antes/depois de cada teste (TRUNCATE ... CASCADE), garantindo isolamento.
"""

from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import text

from src.core.infrastructure.database.session import SessionLocal
from src.main import app
from src.modules.sigmun_gdo.infrastructure.database.models import (
    ClassificacaoDocumentalModel,
    ProcessoDocumentoModel,
    TabelaTemporalidadeModel,
    TipoDocumentalModel,
)

# Ordem de limpeza respeitando FKs (filhas antes de pais)
TABELAS_GDO = (
    "gdo.metadados_documentos",
    "gdo.assinaturas_documentos",
    "gdo.arquivamentos_documentos",
    "gdo.tramitacoes_documentos",
    "gdo.versoes_documentos",
    "gdo.documentos",
    "gdo.tabelas_temporalidades",
    "gdo.classificacoes_documentais",
    "gdo.processos_documentos",
    "gdo.tipos_documentais",
)


def _limpar_gdo() -> None:
    """TRUNCATE de todas as tabelas do schema gdo (isolamento entre testes)."""
    with SessionLocal() as session:
        for tabela in TABELAS_GDO:
            session.execute(text(f"TRUNCATE TABLE {tabela} CASCADE"))
        session.commit()


@pytest.fixture(autouse=True)
def _isolamento_gdo():
    """Limpa o schema gdo antes e depois de cada teste."""
    _limpar_gdo()
    yield
    _limpar_gdo()


@pytest.fixture()
def client() -> TestClient:
    """Cliente HTTP contra a aplicação real (banco PostgreSQL)."""
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture()
def classificacao_id(db_session) -> str:
    """Cria uma classificação documental de apoio."""
    model = ClassificacaoDocumentalModel(
        codigo="1.01",
        nome="Administração Geral",
        descricao="Documentos de administração geral",
        nivel=1,
        prazo_retencao=180,
    )
    db_session.add(model)
    db_session.commit()
    return str(model.id)


@pytest.fixture()
def processo_id(db_session) -> str:
    """Cria um processo documental de apoio."""
    model = ProcessoDocumentoModel(
        numero="00001",
        ano=2026,
        tipo_processo_id="TP-ADMIN",
        titulo="Processo Administrativo de Teste",
        unidade_autor_id="UNIDADE-01",
    )
    db_session.add(model)
    db_session.commit()
    return str(model.id)


@pytest.fixture()
def temporalidade_codigo(db_session) -> str:
    """Cria uma tabela de temporalidade de apoio."""
    model = TabelaTemporalidadeModel(
        codigo="TEMP-001",
        nome="Documentos correntes",
        prazo_tempo=12,
        unidade_tempo="meses",
        evento_fim="encerramento",
        tipo_destinacao="eliminacao",
        is_ativo=True,
    )
    db_session.add(model)
    db_session.commit()
    return model.codigo


def _payload(**overrides) -> dict:
    """Payload padrão de criação de documento."""
    dados = {
        "codigo": f"DOC-{uuid4().hex[:10].upper()}",
        "numero": "0001",
        "ano": 2026,
        "tipo_documental_id": "TD-OFICIO",
        "titulo": "Ofício de teste de integração",
        "descricao": "Documento criado por teste de integração",
        "unidade_autor_id": "UNIDADE-01",
        "is_sigiloso": False,
    }
    dados.update(overrides)
    return dados


@pytest.fixture()
def db_session():
    """Sessão de banco para preparação de dados (arrange)."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


# =============================================================================
# POST /api/v1/gdo/documentos
# =============================================================================


def test_post_documentos_cria_201(client: TestClient):
    response = client.post("/api/v1/gdo/documentos", json=_payload())

    assert response.status_code == 201, response.text
    corpo = response.json()
    assert corpo["codigo"].startswith("DOC-")
    assert corpo["numero"] == "0001"
    assert corpo["ano"] == 2026
    assert corpo["status"] == "ativo"
    assert corpo["titulo"] == "Ofício de teste de integração"
    assert corpo["unidade_autor_id"] == "UNIDADE-01"
    assert corpo["created_at"] is not None


def test_post_documentos_hash_invalido_retorna_400(client: TestClient):
    """RN-GDO-002: hash informado deve ser SHA-256 (64 hex chars)."""
    response = client.post(
        "/api/v1/gdo/documentos", json=_payload(hash_integridade="hash-curto")
    )

    assert response.status_code == 400
    assert "SHA-256" in response.json()["detail"]


def test_post_documentos_codigo_duplicado_retorna_409(client: TestClient):
    """RN-GDO-001: unicidade de código documental por ano."""
    payload = _payload()
    primeira = client.post("/api/v1/gdo/documentos", json=payload)
    duplicada = client.post("/api/v1/gdo/documentos", json=payload)

    assert primeira.status_code == 201
    assert duplicada.status_code == 409


def test_post_documentos_payload_invalido_retorna_422(client: TestClient):
    response = client.post(
        "/api/v1/gdo/documentos", json=_payload(titulo="ab")  # < 3 chars
    )

    assert response.status_code == 422


@pytest.fixture(autouse=True)
def tipo_documental_ativo(db_session) -> str:
    """Cria um tipo documental ativo para testes (autouse: todos os testes têm pelo menos um tipo válido)."""
    model = TipoDocumentalModel(
        codigo="TD-OFICIO",
        nome="Ofício",
        descricao="Documento oficial de comunicação",
        is_ativo=True,
    )
    db_session.add(model)
    db_session.commit()
    return model.codigo


@pytest.fixture()
def tipo_documental_inativo(db_session) -> str:
    """Cria um tipo documental inativo para testes."""
    model = TipoDocumentalModel(
        codigo="TD-INATIVO",
        nome="Tipo Inativo",
        descricao="Tipo documental descontinuado",
        is_ativo=False,
    )
    db_session.add(model)
    db_session.commit()
    return model.codigo


def test_post_documentos_tipo_invalido_retorna_400(client: TestClient):
    """Validação: tipo documental não cadastrado deve retornar 400."""
    response = client.post(
        "/api/v1/gdo/documentos", json=_payload(tipo_documental_id="TD-INEXISTENTE")
    )

    assert response.status_code == 400
    assert "Tipo documental" in response.json()["detail"]


def test_post_documentos_tipo_inativo_retorna_400(
    client: TestClient, tipo_documental_inativo: str
):
    """Validação: tipo documental inativo deve retornar 400."""
    response = client.post(
        "/api/v1/gdo/documentos",
        json=_payload(tipo_documental_id=tipo_documental_inativo),
    )

    assert response.status_code == 400
    assert "Tipo documental" in response.json()["detail"]


def test_post_documentos_tipo_valido_retorna_201(
    client: TestClient, tipo_documental_ativo: str
):
    """Validação: tipo documental ativo deve permitir criação (201)."""
    response = client.post(
        "/api/v1/gdo/documentos",
        json=_payload(tipo_documental_id=tipo_documental_ativo),
    )

    assert response.status_code == 201
    assert response.json()["tipo_documental_id"] == tipo_documental_ativo


# =============================================================================
# Endpoints de Tipos Documentais
# =============================================================================


def test_criar_tipo_documento_201(client: TestClient):
    """Criação de tipo documental retorna 201."""
    response = client.post(
        "/api/v1/gdo/tipos-documentais",
        json={"codigo": "TD-MEMORANDO", "nome": "Memorando", "descricao": "Documento interno"},
    )

    assert response.status_code == 201
    corpo = response.json()
    assert corpo["codigo"] == "TD-MEMORANDO"
    assert corpo["nome"] == "Memorando"
    assert corpo["is_ativo"] is True


def test_criar_tipo_documento_codigo_duplicado_409(client: TestClient):
    """Código duplicado deve retornar 409."""
    payload = {"codigo": "TD-DUP", "nome": "Duplicado"}
    client.post("/api/v1/gdo/tipos-documentais", json=payload)
    response = client.post("/api/v1/gdo/tipos-documentais", json=payload)

    assert response.status_code == 409


def test_listar_tipos_documento(client: TestClient):
    """Lista tipos documentais ativos (inclui TD-OFICIO da fixture autouse)."""
    client.post(
        "/api/v1/gdo/tipos-documentais",
        json={"codigo": "TD-LIST-1", "nome": "Tipo 1"},
    )
    client.post(
        "/api/v1/gdo/tipos-documentais",
        json={"codigo": "TD-LIST-2", "nome": "Tipo 2"},
    )

    response = client.get("/api/v1/gdo/tipos-documentais")

    assert response.status_code == 200
    # 2 novos + TD-OFICIO da fixture autouse
    codigos = [t["codigo"] for t in response.json()]
    assert "TD-LIST-1" in codigos
    assert "TD-LIST-2" in codigos
    assert "TD-OFICIO" in codigos


def test_buscar_tipo_documento_200(client: TestClient):
    """Busca tipo documental por código retorna 200."""
    client.post(
        "/api/v1/gdo/tipos-documentais",
        json={"codigo": "TD-BUSCA", "nome": "Tipo Busca"},
    )

    response = client.get("/api/v1/gdo/tipos-documentais/TD-BUSCA")

    assert response.status_code == 200
    assert response.json()["codigo"] == "TD-BUSCA"


def test_buscar_tipo_documento_404(client: TestClient):
    """Busca tipo documental inexistente retorna 404."""
    response = client.get("/api/v1/gdo/tipos-documentais/TD-INEXISTENTE")

    assert response.status_code == 404


def test_inativar_e_ativar_tipo_documento(client: TestClient):
    """Inativar e ativar tipo documental."""
    client.post(
        "/api/v1/gdo/tipos-documentais",
        json={"codigo": "TD-ATIVAR", "nome": "Tipo Ativar"},
    )

    # Inativar
    inativar = client.patch("/api/v1/gdo/tipos-documentais/TD-ATIVAR/inativar")
    assert inativar.status_code == 200
    assert inativar.json()["is_ativo"] is False

    # Não deve aparecer na lista de ativos
    lista = client.get("/api/v1/gdo/tipos-documentais")
    assert all(t["codigo"] != "TD-ATIVAR" for t in lista.json())

    # Ativar
    ativar = client.patch("/api/v1/gdo/tipos-documentais/TD-ATIVAR/ativar")
    assert ativar.status_code == 200
    assert ativar.json()["is_ativo"] is True

    # Deve aparecer novamente na lista
    lista = client.get("/api/v1/gdo/tipos-documentais")
    assert any(t["codigo"] == "TD-ATIVAR" for t in lista.json())


def test_inativar_tipo_documento_inexistente_404(client: TestClient):
    """Inativar tipo documental inexistente retorna 404."""
    response = client.patch("/api/v1/gdo/tipos-documentais/TD-INEXISTENTE/inativar")

    assert response.status_code == 404


# =============================================================================
# GET /api/v1/gdo/documentos
# =============================================================================


def test_get_documentos_lista_vazia_e_com_itens(client: TestClient):
    vazia = client.get("/api/v1/gdo/documentos")
    assert vazia.status_code == 200
    assert vazia.json()["total"] == 0

    client.post("/api/v1/gdo/documentos", json=_payload())
    com_itens = client.get("/api/v1/gdo/documentos")

    assert com_itens.status_code == 200
    assert com_itens.json()["total"] == 1
    assert len(com_itens.json()["items"]) == 1


def test_get_documentos_paginacao(client: TestClient):
    for _ in range(3):
        client.post("/api/v1/gdo/documentos", json=_payload())

# =============================================================================
# GET /api/v1/gdo/documentos/{documento_id} e /processo/{processo_id}
# =============================================================================


def test_get_documento_por_id_200_e_404(client: TestClient):
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()

    ok = client.get(f"/api/v1/gdo/documentos/{criado['id']}")
    inexistente = client.get(f"/api/v1/gdo/documentos/{uuid4()}")

    assert ok.status_code == 200
    assert ok.json()["id"] == criado["id"]
    assert inexistente.status_code == 404


def test_get_documentos_do_processo(client: TestClient, processo_id: str):
    criado = client.post(
        "/api/v1/gdo/documentos", json=_payload(processo_id=processo_id)
    ).json()

    response = client.get(f"/api/v1/gdo/documentos/processo/{processo_id}")

    assert response.status_code == 200
    itens = response.json()
    assert len(itens) == 1
    assert itens[0]["id"] == criado["id"]


# =============================================================================
# POST /api/v1/gdo/documentos/{documento_id}/tramitar + tramitacoes
# =============================================================================


def test_post_tramitar_cria_201(client: TestClient):
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()

    response = client.post(
        f"/api/v1/gdo/documentos/{criado['id']}/tramitar",
        json={
            "unidade_origem_id": "UNIDADE-01",
            "unidade_destino_id": "UNIDADE-02",
            "tipo": "envio",
            "motivo": "Análise técnica",
        },
    )

    assert response.status_code == 201, response.text
    corpo = response.json()
    assert corpo["documento_id"] == criado["id"]
    assert corpo["unidade_origem_id"] == "UNIDADE-01"
    assert corpo["unidade_destino_id"] == "UNIDADE-02"
    assert corpo["tipo"] == "envio"
    assert corpo["data_envio"] is not None


def test_post_tramitar_documento_inexistente_retorna_404(client: TestClient):
    response = client.post(
        f"/api/v1/gdo/documentos/{uuid4()}/tramitar",
        json={
            "unidade_origem_id": "UNIDADE-01",
            "unidade_destino_id": "UNIDADE-02",
            "tipo": "envio",
        },
    )

    assert response.status_code == 404


def test_get_tramitacoes_do_documento(client: TestClient):
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()
    client.post(
        f"/api/v1/gdo/documentos/{criado['id']}/tramitar",
        json={
            "unidade_origem_id": "UNIDADE-01",
            "unidade_destino_id": "UNIDADE-02",
            "tipo": "envio",
            "motivo": "Primeira tramitação",
        },
    )

    response = client.get(f"/api/v1/gdo/documentos/{criado['id']}/tramitacoes")

    assert response.status_code == 200
    tramitacoes = response.json()
    assert len(tramitacoes) == 1
    assert tramitacoes[0]["motivo"] == "Primeira tramitação"


# =============================================================================
# GET /api/v1/gdo/classificacoes
# =============================================================================


def test_get_classificacoes_lista(client: TestClient, classificacao_id: str):
    response = client.get("/api/v1/gdo/classificacoes")

    assert response.status_code == 200
    corpo = response.json()
    assert corpo["total"] == 1
    assert corpo["items"][0]["codigo"] == "1.01"
    assert corpo["items"][0]["is_active"] is True


def test_get_classificacao_por_id_200_e_404(client: TestClient, classificacao_id: str):
    ok = client.get(f"/api/v1/gdo/classificacoes/{classificacao_id}")
    inexistente = client.get(f"/api/v1/gdo/classificacoes/{uuid4()}")

    assert ok.status_code == 200
    assert ok.json()["nome"] == "Administração Geral"
    assert inexistente.status_code == 404


# =============================================================================
# GET /api/v1/gdo/processos/{processo_id}
# =============================================================================


def test_get_processo_por_id_200_e_404(client: TestClient, processo_id: str):
    ok = client.get(f"/api/v1/gdo/processos/{processo_id}")
    inexistente = client.get(f"/api/v1/gdo/processos/{uuid4()}")

    assert ok.status_code == 200
    assert ok.json()["numero"] == "00001"
    assert ok.json()["status"] == "aberto"
    assert inexistente.status_code == 404


# =============================================================================
# GET /api/v1/gdo/temporalidades/{codigo}
# =============================================================================


def test_get_temporalidade_por_codigo_200_e_404(
    client: TestClient, temporalidade_codigo: str
):
    ok = client.get(f"/api/v1/gdo/temporalidades/{temporalidade_codigo}")
    inexistente = client.get("/api/v1/gdo/temporalidades/TEMP-INEXISTENTE")

    assert ok.status_code == 200
    corpo = ok.json()
    assert corpo["codigo"] == "TEMP-001"
    assert corpo["prazo_tempo"] == 12
    assert corpo["tipo_destinacao"] == "eliminacao"
    assert inexistente.status_code == 404


# =============================================================================
# POST /api/v1/gdo/documentos/{documento_id}/arquivar
# =============================================================================


def test_post_arquivar_cria_201(client: TestClient, db_session):
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()

    response = client.post(
        f"/api/v1/gdo/documentos/{criado['id']}/arquivar",
        json={
            "unidade_arquivo_id": "ARQUIVO-GERAL",
            "autor_id": "USUARIO-01",
            "observacao": "Arquivamento por teste",
        },
    )

    assert response.status_code == 201, response.text
    corpo = response.json()
    assert corpo["documento_id"] == criado["id"]
    assert corpo["data_arquivamento"] is not None
    assert corpo["is_restaurado"] is False
    assert corpo["observacao"] == "Arquivamento por teste"

    # Documento deve ficar com status arquivado e unidade de arquivo definida
    detalhe = client.get(f"/api/v1/gdo/documentos/{criado['id']}").json()
    assert detalhe["status"] == "arquivado"
    assert detalhe["unidade_arquivo_id"] == "ARQUIVO-GERAL"
    assert detalhe["data_arquivamento"] is not None


def test_post_arquivar_ja_arquivado_retorna_409(client: TestClient):
    """RN-GDO-008: documento arquivado não pode ser arquivado novamente."""
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()
    primeira = client.post(
        f"/api/v1/gdo/documentos/{criado['id']}/arquivar",
        json={"unidade_arquivo_id": "ARQUIVO-GERAL", "autor_id": "USUARIO-01"},
    )
    segunda = client.post(
        f"/api/v1/gdo/documentos/{criado['id']}/arquivar",
        json={"unidade_arquivo_id": "ARQUIVO-GERAL", "autor_id": "USUARIO-01"},
    )

    assert primeira.status_code == 201
    assert segunda.status_code == 409


def test_post_arquivar_documento_inexistente_retorna_404(client: TestClient):
    response = client.post(
        f"/api/v1/gdo/documentos/{uuid4()}/arquivar",
        json={"unidade_arquivo_id": "ARQUIVO-GERAL", "autor_id": "USUARIO-01"},
    )

    assert response.status_code == 404


# =============================================================================
# POST /api/v1/gdo/documentos/{documento_id}/assinar
# =============================================================================


def test_post_assinar_cria_201_e_fixa_integridade(client: TestClient):
    """RN-GDO-002: hash SHA-256 do conteúdo; RN-GDO-005: integridade fixada."""
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()

    response = client.post(
        f"/api/v1/gdo/documentos/{criado['id']}/assinar",
        json={
            "signatario_id": "SERVIDOR-77",
            "conteudo": "Conteúdo oficial do documento para assinatura",
            "autor_id": "USUARIO-01",
            "certificado_id": "CERT-ICP-001",
        },
    )

    assert response.status_code == 201, response.text
    corpo = response.json()
    assert corpo["documento_id"] == criado["id"]
    assert corpo["signatario_id"] == "SERVIDOR-77"
    assert len(corpo["hash_assinatura"]) == 64  # SHA-256 hex
    assert corpo["is_valida"] is True
    assert corpo["is_revogada"] is False

    detalhe = client.get(f"/api/v1/gdo/documentos/{criado['id']}").json()
    assert detalhe["hash_integridade"] == corpo["hash_assinatura"]


def test_post_assinar_ja_assinado_retorna_409(client: TestClient):
    """RN-GDO-005: novo conteúdo exige nova versão, não re-assinatura."""
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()
    payload = {
        "signatario_id": "SERVIDOR-77",
        "conteudo": "Conteúdo oficial do documento para assinatura",
        "autor_id": "USUARIO-01",
    }
    primeira = client.post(f"/api/v1/gdo/documentos/{criado['id']}/assinar", json=payload)
    segunda = client.post(f"/api/v1/gdo/documentos/{criado['id']}/assinar", json=payload)

    assert primeira.status_code == 201
    assert segunda.status_code == 409


def test_post_assinar_documento_inexistente_retorna_404(client: TestClient):
    response = client.post(
        f"/api/v1/gdo/documentos/{uuid4()}/assinar",
        json={"signatario_id": "S1", "conteudo": "texto", "autor_id": "U1"},
    )

    assert response.status_code == 404


# =============================================================================
# POST/GET /api/v1/gdo/documentos/{documento_id}/versoes
# =============================================================================


def test_post_versao_numera_incrementalmente(client: TestClient):
    """RN-GDO-005: versões imutáveis com numeração incremental."""
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()
    url = f"/api/v1/gdo/documentos/{criado['id']}/versoes"

    primeira = client.post(
        url,
        json={"conteudo_ref": "storage://doc/v1.pdf", "autor_id": "USUARIO-01"},
    )
    segunda = client.post(
        url,
        json={
            "conteudo_ref": "storage://doc/v2.pdf",
            "autor_id": "USUARIO-01",
            "hash_integridade": "a" * 64,
        },
    )

    assert primeira.status_code == 201, primeira.text
    assert segunda.status_code == 201, segunda.text
    assert primeira.json()["numero_versao"] == 1
    assert segunda.json()["numero_versao"] == 2
    assert segunda.json()["hash_integridade"] == "a" * 64


def test_post_versao_documento_inexistente_retorna_404(client: TestClient):
    response = client.post(
        f"/api/v1/gdo/documentos/{uuid4()}/versoes",
        json={"conteudo_ref": "storage://doc/x.pdf", "autor_id": "U1"},
    )

    assert response.status_code == 404


def test_get_versoes_lista_historico(client: TestClient):
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()
    url = f"/api/v1/gdo/documentos/{criado['id']}/versoes"
    client.post(url, json={"conteudo_ref": "storage://doc/v1.pdf", "autor_id": "U1"})
    client.post(url, json={"conteudo_ref": "storage://doc/v2.pdf", "autor_id": "U1"})

    response = client.get(url)
    inexistente = client.get(f"/api/v1/gdo/documentos/{uuid4()}/versoes")

    assert response.status_code == 200
    versoes = response.json()
    assert len(versoes) == 2
    # Mais recente primeiro
    assert versoes[0]["numero_versao"] == 2
    assert versoes[1]["numero_versao"] == 1
    assert inexistente.status_code == 404


# =============================================================================
# POST /api/v1/gdo/documentos/{documento_id}/destinacao
# =============================================================================


def test_post_destinacao_guarda_permanente_retorna_200(client: TestClient):
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()

    response = client.post(
        f"/api/v1/gdo/documentos/{criado['id']}/destinacao",
        json={
            "tipo_destinacao": "guarda_permanente",
            "autor_id": "USUARIO-01",
            "justificativa": "Valor histórico-probatório",
        },
    )

    assert response.status_code == 200, response.text
    corpo = response.json()
    assert corpo["id"] == criado["id"]


def test_post_destinacao_eliminacao_sem_autoridade_retorna_403(client: TestClient):
    """RN-GDO-011: eliminação exige autoridade homologadora."""
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()

    response = client.post(
        f"/api/v1/gdo/documentos/{criado['id']}/destinacao",
        json={
            "tipo_destinacao": "eliminacao",
            "autor_id": "USUARIO-01",
            "justificativa": "Sem valor administrativo",
        },
    )

    assert response.status_code == 403
    assert "RN-GDO-011" in response.json()["detail"]


def test_post_destinacao_eliminacao_com_autoridade_encerra(client: TestClient):
    criado = client.post("/api/v1/gdo/documentos", json=_payload()).json()

    response = client.post(
        f"/api/v1/gdo/documentos/{criado['id']}/destinacao",
        json={
            "tipo_destinacao": "eliminacao",
            "autor_id": "USUARIO-01",
            "autoridade_homologadora_id": "AUTORIDADE-01",
            "justificativa": "Sem valor administrativo",
        },
    )

    assert response.status_code == 200, response.text
    corpo = response.json()
    assert corpo["status"] == "encerrado"
    assert corpo["data_eliminacao"] is not None


def test_post_destinacao_rascunho_retorna_409(client: TestClient, db_session):
    """Documento em rascunho não possui destinação definida."""
    payload = _payload()
    response_criacao = client.post("/api/v1/gdo/documentos", json=payload)
    documento_id = response_criacao.json()["id"]

    # Rebaixa o documento para rascunho diretamente no banco (arrange)
    from sqlalchemy import text as sql_text

    db_session.execute(
        sql_text("UPDATE gdo.documentos SET status = 'rascunho' WHERE id = :id"),
        {"id": documento_id},
    )
    db_session.commit()

    response = client.post(
        f"/api/v1/gdo/documentos/{documento_id}/destinacao",
        json={"tipo_destinacao": "guarda_permanente", "autor_id": "USUARIO-01"},
    )

    assert response.status_code == 409


def test_post_destinacao_documento_inexistente_retorna_404(client: TestClient):
    response = client.post(
        f"/api/v1/gdo/documentos/{uuid4()}/destinacao",
        json={"tipo_destinacao": "guarda_permanente", "autor_id": "U1"},
    )

    assert response.status_code == 404




