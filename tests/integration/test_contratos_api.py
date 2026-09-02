"""Testes de API dos endpoints de Contratos.

Sobrescrevem a dependência do repositório por um repositório em memória,
exercitando o ciclo completo requisição -> use case -> resposta sem banco.
"""

from uuid import UUID, uuid4

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.modules.sigmun_compras.application.services.servico_de_auditoria import (
    ServicoDeAuditoria,
)
from src.modules.sigmun_compras.presentation.api.contratos_router import (
    get_contrato_repository,
    get_servico_de_auditoria,
)
from tests.unit.test_contrato_use_cases import InMemoryContratoRepository
from tests.unit.test_registro_auditoria import InMemoryTrilhaAuditoriaRepository


@pytest.fixture()
def repository() -> InMemoryContratoRepository:
    repo = InMemoryContratoRepository()
    repo.add_processo_documental(uuid4())
    repo.add_fornecedor_ativo(uuid4())
    repo.add_unidade(uuid4())
    return repo


@pytest.fixture()
def trilha() -> InMemoryTrilhaAuditoriaRepository:
    return InMemoryTrilhaAuditoriaRepository()


@pytest.fixture()
def client(repository, trilha) -> TestClient:
    app.dependency_overrides[get_contrato_repository] = lambda: repository
    app.dependency_overrides[get_servico_de_auditoria] = lambda: ServicoDeAuditoria(trilha)
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def _payload(repository: InMemoryContratoRepository, **overrides) -> dict:
    dados = {
        "processo_documental_id": str(next(iter(repository.processos_documentais))),
        "fornecedor_id": str(next(iter(repository.fornecedores_ativos))),
        "unidade_id": str(next(iter(repository.unidades))),
        "numero": "001/2026",
        "data_inicio": "2026-01-01",
        "data_fim": "2026-12-31",
        "valor": "10000.00",
        "objeto": "Aquisição de serviços de limpeza",
    }
    dados.update(overrides)
    return dados



# -- POST /api/v1/contratos ------------------------------------------------------


def test_post_cria_contrato(client: TestClient, repository):
    response = client.post("/api/v1/contratos", json=_payload(repository))

    assert response.status_code == 201, response.text
    body = response.json()
    assert UUID(body["id"])
    assert body["numero"] == "001/2026"
    assert body["situacao"] == "EM_ELABORACAO"


def test_post_processo_inexistente_retorna_404(client: TestClient, repository):
    response = client.post(
        "/api/v1/contratos",
        json=_payload(repository, processo_documental_id=str(uuid4())),
    )

    assert response.status_code == 404


def test_post_fornecedor_inexistente_retorna_404(client: TestClient, repository):
    response = client.post(
        "/api/v1/contratos",
        json=_payload(repository, fornecedor_id=str(uuid4())),
    )

    assert response.status_code == 404


def test_post_unidade_inexistente_retorna_404(client: TestClient, repository):
    response = client.post(
        "/api/v1/contratos",
        json=_payload(repository, unidade_id=str(uuid4())),
    )

    assert response.status_code == 404


def test_post_duplicado_retorna_409(client: TestClient, repository):
    primeira = client.post("/api/v1/contratos", json=_payload(repository))
    duplicada = client.post(
        "/api/v1/contratos",
        json=_payload(repository, objeto="Outro objeto"),
    )

    assert primeira.status_code == 201
    assert duplicada.status_code == 409


def test_post_valor_negativo_retorna_422(client: TestClient, repository):
    response = client.post(
        "/api/v1/contratos",
        json=_payload(repository, valor="-100.00"),
    )

    assert response.status_code == 422


# -- GET /api/v1/contratos -------------------------------------------------------


def test_get_lista_vazia(client: TestClient):
    response = client.get("/api/v1/contratos")

    assert response.status_code == 200
    body = response.json()
    assert body["total"] == 0
    assert body["items"] == []


def test_get_lista_com_itens(client: TestClient, repository):
    client.post("/api/v1/contratos", json=_payload(repository))

    response = client.get("/api/v1/contratos")

    assert response.status_code == 200
    body = response.json()
    assert body["total"] == 1
    assert len(body["items"]) == 1
    assert body["items"][0]["numero"] == "001/2026"


def test_get_lista_filtra_por_situacao(client: TestClient, repository):
    client.post("/api/v1/contratos", json=_payload(repository, numero="001/2026"))

    response = client.get("/api/v1/contratos", params={"situacao": "EM_ELABORACAO"})
    invalido = client.get("/api/v1/contratos", params={"situacao": "BANANA"})

    assert response.status_code == 200
    assert response.json()["total"] == 1
    assert invalido.status_code == 400


def test_get_lista_paginada(client: TestClient, repository):
    client.post("/api/v1/contratos", json=_payload(repository, numero="001/2026"))
    client.post("/api/v1/contratos", json=_payload(repository, numero="002/2026"))

    pagina = client.get("/api/v1/contratos", params={"page": 0, "page_size": 1})

    assert pagina.status_code == 200
    body = pagina.json()
    assert body["total"] == 2
    assert len(body["items"]) == 1


# -- GET /api/v1/contratos/{id} --------------------------------------------------


def test_get_por_id_sucesso_e_404(client: TestClient, repository):
    criado = client.post("/api/v1/contratos", json=_payload(repository)).json()

    ok = client.get(f"/api/v1/contratos/{criado['id']}")
    not_found = client.get(f"/api/v1/contratos/{uuid4()}")

    assert ok.status_code == 200
    assert ok.json()["numero"] == "001/2026"
    assert not_found.status_code == 404


# -- PATCH /api/v1/contratos/{id} ------------------------------------------------


def test_patch_atualiza_dados(client: TestClient, repository):
    usuario = uuid4()
    criado = client.post("/api/v1/contratos", json=_payload(repository)).json()

    response = client.patch(
        f"/api/v1/contratos/{criado['id']}",
        json={"numero": "002/2026", "objeto": "Objeto atualizado"},
        headers={"X-Usuario-Id": str(usuario)},
    )

    assert response.status_code == 200, response.text
    assert response.json()["numero"] == "002/2026"
    assert response.json()["objeto"] == "Objeto atualizado"


def test_patch_sem_campos_retorna_400(client: TestClient, repository):
    criado = client.post("/api/v1/contratos", json=_payload(repository)).json()

    response = client.patch(f"/api/v1/contratos/{criado['id']}", json={})

    assert response.status_code == 400


def test_patch_inexistente_retorna_404(client: TestClient):
    response = client.patch(
        f"/api/v1/contratos/{uuid4()}", json={"numero": "001"}
    )

    assert response.status_code == 404


def test_patch_para_numero_duplicado_retorna_409(client: TestClient, repository):
    primeiro = client.post(
        "/api/v1/contratos", json=_payload(repository, numero="001/2026")
    ).json()
    segundo = client.post(
        "/api/v1/contratos", json=_payload(repository, numero="002/2026")
    ).json()

    response = client.patch(
        f"/api/v1/contratos/{segundo['id']}", json={"numero": "001/2026"}
    )

    assert response.status_code == 409


# -- PATCH /api/v1/contratos/{id}/situacao ----------------------------------------


def test_patch_situacao_transicao_valida(client: TestClient, repository):
    criado = client.post("/api/v1/contratos", json=_payload(repository)).json()

    response = client.patch(
        f"/api/v1/contratos/{criado['id']}/situacao",
        json={"situacao": "ASSINADO"},
    )

    assert response.status_code == 200, response.text
    assert response.json()["situacao"] == "ASSINADO"


def test_patch_situacao_transicao_invalida_retorna_400(client: TestClient, repository):
    criado = client.post("/api/v1/contratos", json=_payload(repository)).json()

    response = client.patch(
        f"/api/v1/contratos/{criado['id']}/situacao",
        json={"situacao": "VIGENTE"},
    )

    assert response.status_code == 400


def test_patch_situacao_inexistente_retorna_404(client: TestClient):
    response = client.patch(
        f"/api/v1/contratos/{uuid4()}/situacao", json={"situacao": "ASSINADO"}
    )

    assert response.status_code == 404


# -- DELETE /api/v1/contratos/{id} -----------------------------------------------


def test_delete_exclui_logicamente(client: TestClient, repository):
    usuario = uuid4()
    criado = client.post("/api/v1/contratos", json=_payload(repository)).json()

    delete = client.delete(
        f"/api/v1/contratos/{criado['id']}",
        headers={"X-Usuario-Id": str(usuario)},
    )
    consulta = client.get(f"/api/v1/contratos/{criado['id']}")

    assert delete.status_code == 200, delete.text
    assert consulta.status_code == 404


def test_delete_sem_usuario_retorna_400(client: TestClient, repository):
    criado = client.post("/api/v1/contratos", json=_payload(repository)).json()

    response = client.delete(f"/api/v1/contratos/{criado['id']}")

    assert response.status_code == 400


def test_delete_inexistente_retorna_404(client: TestClient):
    response = client.delete(
        f"/api/v1/contratos/{uuid4()}",
        headers={"X-Usuario-Id": str(uuid4())},
    )

    assert response.status_code == 404