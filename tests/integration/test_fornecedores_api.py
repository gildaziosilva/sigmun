"""Testes de API dos endpoints de Fornecedores.

Sobrescrevem a dependência do repositório por um repositório em memória,
exercitando o ciclo completo requisição -> use case -> resposta sem banco.
"""

from uuid import UUID, uuid4

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.modules.sigmun_compras.domain.entities.fornecedor import Fornecedor
from src.modules.sigmun_compras.presentation.api.fornecedores_router import (
    get_fornecedor_repository,
)
from tests.unit.test_fornecedor_use_cases import InMemoryFornecedorRepository


@pytest.fixture()
def repository() -> InMemoryFornecedorRepository:
    return InMemoryFornecedorRepository()


@pytest.fixture()
def client(repository: InMemoryFornecedorRepository) -> TestClient:
    app.dependency_overrides[get_fornecedor_repository] = lambda: repository
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def _criar_payload() -> dict:
    return {"pessoa_juridica_id": str(uuid4())}


def _semente(repository: InMemoryFornecedorRepository) -> Fornecedor:
    fornecedor = Fornecedor(pessoa_juridica_id=uuid4())
    return repository.save(fornecedor)


# -- POST /api/v1/fornecedores -------------------------------------------------


def test_post_cria_fornecedor(client: TestClient):
    response = client.post("/api/v1/fornecedores", json=_criar_payload())

    assert response.status_code == 201, response.text
    body = response.json()
    assert UUID(body["id"])
    assert body["situacao_cadastro"] == "ATIVO"


def test_post_fornecedor_duplicado_retorna_409(client: TestClient, repository):
    pessoa_juridica_id = str(uuid4())
    primeira = client.post(
        "/api/v1/fornecedores", json={"pessoa_juridica_id": pessoa_juridica_id}
    )
    assert primeira.status_code == 201

    duplicada = client.post(
        "/api/v1/fornecedores", json={"pessoa_juridica_id": pessoa_juridica_id}
    )

    assert duplicada.status_code == 409
    assert "RN-COMPRAS-031" in duplicada.json()["detail"]


# -- GET /api/v1/fornecedores ----------------------------------------------------


def test_get_lista_vazia(client: TestClient):
    response = client.get("/api/v1/fornecedores")

    assert response.status_code == 200
    body = response.json()
    assert body["total"] == 0
    assert body["items"] == []


def test_get_lista_com_itens(client: TestClient, repository):
    criado = _semente(repository)

    response = client.get("/api/v1/fornecedores")

    assert response.status_code == 200
    body = response.json()
    assert body["total"] == 1
    assert body["items"][0]["id"] == str(criado.id)


def test_get_lista_filtra_por_situacao(client: TestClient, repository):
    semente = Fornecedor(pessoa_juridica_id=uuid4())
    repository.save(semente)

    ativos = client.get("/api/v1/fornecedores", params={"situacao": "ATIVO"})
    suspensos = client.get("/api/v1/fornecedores", params={"situacao": "SUSPENSO"})
    invalidos = client.get("/api/v1/fornecedores", params={"situacao": "BANANA"})

    assert ativos.status_code == 200 and ativos.json()["total"] == 1
    assert suspensos.status_code == 200 and suspensos.json()["total"] == 0
    assert invalidos.status_code == 400


# -- GET /api/v1/fornecedores/{id} -------------------------------------------------


def test_get_por_id_sucesso(client: TestClient, repository):
    criado = _semente(repository)

    response = client.get(f"/api/v1/fornecedores/{criado.id}")

    assert response.status_code == 200
    assert response.json()["pessoa_juridica_id"] == str(criado.pessoa_juridica_id)


def test_get_por_id_inexistente_retorna_404(client: TestClient):
    response = client.get(f"/api/v1/fornecedores/{uuid4()}")

    assert response.status_code == 404


# -- PATCH /api/v1/fornecedores/{id} -------------------------------------------------


def test_patch_atualiza_situacao(client: TestClient, repository):
    usuario = uuid4()
    criado = _semente(repository)

    response = client.patch(
        f"/api/v1/fornecedores/{criado.id}",
        json={"situacao_cadastro": "SUSPENSO"},
        headers={"X-Usuario-Id": str(usuario)},
    )

    assert response.status_code == 200, response.text
    assert response.json()["situacao_cadastro"] == "SUSPENSO"
    assert repository._data[criado.id].updated_by == usuario  # noqa: SLF001


def test_patch_sem_campos_retorna_400(client: TestClient, repository):
    criado = _semente(repository)

    response = client.patch(f"/api/v1/fornecedores/{criado.id}", json={})

    assert response.status_code == 400


def test_patch_inexistente_retorna_404(client: TestClient):
    response = client.patch(
        f"/api/v1/fornecedores/{uuid4()}",
        json={"situacao_cadastro": "INATIVO"},
    )

    assert response.status_code == 404


# -- DELETE /api/v1/fornecedores/{id} -------------------------------------------------


def test_delete_inativa_fornecedor(client: TestClient, repository):
    usuario = uuid4()
    criado = _semente(repository)

    response = client.delete(
        f"/api/v1/fornecedores/{criado.id}", headers={"X-Usuario-Id": str(usuario)}
    )
    assert response.status_code == 200, response.text
    assert response.json()["situacao_cadastro"] == "INATIVO"

    consulta = client.get(f"/api/v1/fornecedores/{criado.id}")
    assert consulta.status_code == 404


def test_delete_sem_usuario_retorna_400(client: TestClient, repository):
    criado = _semente(repository)

    response = client.delete(f"/api/v1/fornecedores/{criado.id}")

    assert response.status_code == 400


def test_delete_inexistente_retorna_404(client: TestClient):
    response = client.delete(
        f"/api/v1/fornecedores/{uuid4()}", headers={"X-Usuario-Id": str(uuid4())}
    )

    assert response.status_code == 404
