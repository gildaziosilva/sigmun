"""Testes de API dos endpoints de Processos Documentais.

Sobrescrevem a dependência do repositório por um repositório em memória,
exercitando o ciclo completo requisição -> use case -> resposta sem banco.
"""

from uuid import UUID, uuid4

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.modules.sigmun_compras.presentation.api.processo_documental_router import (
    get_processo_documental_repository,
)
from tests.unit.test_processo_documental_use_cases import InMemoryProcessoRepository


@pytest.fixture()
def repository() -> InMemoryProcessoRepository:
    repo = InMemoryProcessoRepository()
    repo.add_unidade(uuid4())
    return repo


@pytest.fixture()
def client(repository: InMemoryProcessoRepository) -> TestClient:
    app.dependency_overrides[get_processo_documental_repository] = lambda: repository
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def _payload(repository: InMemoryProcessoRepository, **overrides) -> dict:
    dados = {
        "unidade_id": str(next(iter(repository.unidades))),
        "numero": "001",
        "ano": 2026,
        "assunto": "Aquisição de material de escritório",
    }
    dados.update(overrides)
    return dados


# -- POST ------------------------------------------------------------------------


def test_post_abre_processo(client: TestClient, repository):
    response = client.post("/api/v1/processos-documentais", json=_payload(repository))

    assert response.status_code == 201, response.text
    body = response.json()
    assert UUID(body["id"])
    assert body["ano"] == 2026


def test_post_unidade_inexistente_retorna_404(client: TestClient, repository):
    response = client.post(
        "/api/v1/processos-documentais", json=_payload(repository, unidade_id=str(uuid4()))
    )

    assert response.status_code == 404


def test_post_duplicado_retorna_409(client: TestClient, repository):
    payload = _payload(repository)
    primeira = client.post("/api/v1/processos-documentais", json=payload)
    duplicada = client.post(
        "/api/v1/processos-documentais",
        json={**payload, "assunto": "Assunto diferente"},
    )

    assert primeira.status_code == 201
    assert duplicada.status_code == 409
    assert "Já existe" in duplicada.json()["detail"]


def test_post_ano_invalido_retorna_422(client: TestClient, repository):
    response = client.post(
        "/api/v1/processos-documentais", json=_payload(repository, ano=1800)
    )

    assert response.status_code == 422


# -- GET lista ----------------------------------------------------------------------


def test_get_lista_vazia_e_com_itens_e_filtro_ano(client: TestClient, repository):
    vazia = client.get("/api/v1/processos-documentais")
    assert vazia.status_code == 200 and vazia.json()["total"] == 0

    client.post("/api/v1/processos-documentais", json=_payload(repository))
    client.post(
        "/api/v1/processos-documentais", json=_payload(repository, numero="002", ano=2027)
    )

    todos = client.get("/api/v1/processos-documentais")
    de_2027 = client.get("/api/v1/processos-documentais", params={"ano": 2027})

    assert todos.status_code == 200 and todos.json()["total"] == 2
    assert de_2027.status_code == 200 and de_2027.json()["total"] == 1


# -- GET/PATCH/DELETE por id -----------------------------------------------------------


def test_get_por_id_sucesso_e_404(client: TestClient, repository):
    criado = client.post(
        "/api/v1/processos-documentais", json=_payload(repository)
    ).json()

    ok = client.get(f"/api/v1/processos-documentais/{criado['id']}")
    not_found = client.get(f"/api/v1/processos-documentais/{uuid4()}")

    assert ok.status_code == 200
    assert ok.json()["numero"] == "001"
    assert not_found.status_code == 404


def test_patch_atualiza_assunto(client: TestClient, repository):
    usuario = uuid4()
    criado = client.post(
        "/api/v1/processos-documentais", json=_payload(repository)
    ).json()

    response = client.patch(
        f"/api/v1/processos-documentais/{criado['id']}",
        json={"assunto": "Assunto atualizado"},
        headers={"X-Usuario-Id": str(usuario)},
    )

    assert response.status_code == 200, response.text
    assert response.json()["assunto"] == "Assunto atualizado"


def test_patch_para_par_duplicado_retorna_409(client: TestClient, repository):
    client.post("/api/v1/processos-documentais", json=_payload(repository))
    segundo = client.post(
        "/api/v1/processos-documentais",
        json=_payload(repository, numero="002", assunto="Outro"),
    ).json()

    response = client.patch(
        f"/api/v1/processos-documentais/{segundo['id']}",
        json={"numero": "001"},
    )

    assert response.status_code == 409


def test_patch_sem_campos_retorna_400(client: TestClient, repository):
    criado = client.post(
        "/api/v1/processos-documentais", json=_payload(repository)
    ).json()

    response = client.patch(f"/api/v1/processos-documentais/{criado['id']}", json={})

    assert response.status_code == 400


def test_patch_inexistente_retorna_404(client: TestClient):
    response = client.patch(
        f"/api/v1/processos-documentais/{uuid4()}", json={"assunto": "Assunto X"}
    )

    assert response.status_code == 404


def test_delete_exclui_logicamente(client: TestClient, repository):
    usuario = uuid4()
    criado = client.post(
        "/api/v1/processos-documentais", json=_payload(repository)
    ).json()

    delete = client.delete(
        f"/api/v1/processos-documentais/{criado['id']}",
        headers={"X-Usuario-Id": str(usuario)},
    )
    consulta = client.get(f"/api/v1/processos-documentais/{criado['id']}")

    assert delete.status_code == 200
    assert consulta.status_code == 404


def test_delete_sem_usuario_retorna_400(client: TestClient, repository):
    criado = client.post(
        "/api/v1/processos-documentais", json=_payload(repository)
    ).json()

    response = client.delete(f"/api/v1/processos-documentais/{criado['id']}")

    assert response.status_code == 400


def test_delete_inexistente_retorna_404(client: TestClient):
    response = client.delete(
        f"/api/v1/processos-documentais/{uuid4()}",
        headers={"X-Usuario-Id": str(uuid4())},
    )

    assert response.status_code == 404
