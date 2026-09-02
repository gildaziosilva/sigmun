"""Testes de API dos endpoints de Itens de Compra.

Sobrescrevem a dependência do repositório por um repositório em memória,
exercitando o ciclo completo requisição -> use case -> resposta sem banco.
"""

from decimal import Decimal
from uuid import UUID, uuid4

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.modules.sigmun_compras.presentation.api.itens_compras_router import (
    get_item_compra_repository,
)
from tests.unit.test_item_compra_use_cases import InMemoryItemCompraRepository


@pytest.fixture()
def repository() -> InMemoryItemCompraRepository:
    return InMemoryItemCompraRepository()


@pytest.fixture()
def client(repository: InMemoryItemCompraRepository) -> TestClient:
    app.dependency_overrides[get_item_compra_repository] = lambda: repository
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def _payload(
    descricao: str = "Notebook para secretaria", q: str = "3", vu: str = "4500.00"
) -> dict:
    return {"descricao": descricao, "quantidade": q, "valor_unitario": vu}


# -- POST /compras/{id}/itens ---------------------------------------------------


def test_post_cria_item(client: TestClient, repository):
    compra_id = uuid4()
    repository.add_compra(compra_id)

    response = client.post(f"/api/v1/compras/{compra_id}/itens", json=_payload())

    assert response.status_code == 201, response.text
    body = response.json()
    assert UUID(body["id"])
    assert Decimal(body["valor_total"]) == Decimal("13500.00")


def test_post_item_compra_inexistente_retorna_404(client: TestClient):
    response = client.post(f"/api/v1/compras/{uuid4()}/itens", json=_payload())

    assert response.status_code == 404


def test_post_item_quantidade_zero_retorna_422(client: TestClient, repository):
    compra_id = uuid4()
    repository.add_compra(compra_id)

    response = client.post(
        f"/api/v1/compras/{compra_id}/itens",
        json={"descricao": "Produto inválido", "quantidade": "0", "valor_unitario": "10.00"},
    )

    assert response.status_code == 422


# -- GET /compras/{id}/itens ------------------------------------------------------


def test_get_lista_itens_da_compra(client: TestClient, repository):
    compra_id = uuid4()
    repository.add_compra(compra_id)
    client.post(f"/api/v1/compras/{compra_id}/itens", json=_payload())
    client.post(
        f"/api/v1/compras/{compra_id}/itens",
        json=_payload(descricao="Serviço de instalação", q="1", vu="200.00"),
    )
    outra_compra = uuid4()
    repository.add_compra(outra_compra)
    client.post(
        f"/api/v1/compras/{outra_compra}/itens", json=_payload(descricao="Item de outra compra")
    )

    response = client.get(f"/api/v1/compras/{compra_id}/itens")

    assert response.status_code == 200
    body = response.json()
    assert body["total"] == 2
    assert all(item["compra_id"] == str(compra_id) for item in body["items"])


def test_get_lista_compra_inexistente_retorna_404(client: TestClient):
    response = client.get(f"/api/v1/compras/{uuid4()}/itens")

    assert response.status_code == 404


# -- GET /itens-compras/{id} -------------------------------------------------------


def test_get_item_por_id_sucesso_e_404(client: TestClient, repository):
    compra_id = uuid4()
    repository.add_compra(compra_id)
    criado = client.post(f"/api/v1/compras/{compra_id}/itens", json=_payload()).json()

    ok = client.get(f"/api/v1/itens-compras/{criado['id']}")
    not_found = client.get(f"/api/v1/itens-compras/{uuid4()}")

    assert ok.status_code == 200
    assert ok.json()["descricao"] == "Notebook para secretaria"
    assert not_found.status_code == 404


# -- PATCH /itens-compras/{id} ------------------------------------------------------


def test_patch_atualiza_e_recalcula_total(client: TestClient, repository):
    usuario = uuid4()
    compra_id = uuid4()
    repository.add_compra(compra_id)
    criado = client.post(f"/api/v1/compras/{compra_id}/itens", json=_payload()).json()

    response = client.patch(
        f"/api/v1/itens-compras/{criado['id']}",
        json={"quantidade": "5"},
        headers={"X-Usuario-Id": str(usuario)},
    )

    assert response.status_code == 200, response.text
    assert Decimal(response.json()["valor_total"]) == Decimal("22500.00")


def test_patch_sem_campos_retorna_400(client: TestClient, repository):
    compra_id = uuid4()
    repository.add_compra(compra_id)
    criado = client.post(f"/api/v1/compras/{compra_id}/itens", json=_payload()).json()

    response = client.patch(f"/api/v1/itens-compras/{criado['id']}", json={})

    assert response.status_code == 400


def test_patch_inexistente_retorna_404(client: TestClient):
    response = client.patch(f"/api/v1/itens-compras/{uuid4()}", json={"quantidade": "2"})

    assert response.status_code == 404


# -- DELETE /itens-compras/{id} ------------------------------------------------------


def test_delete_remove_item_logicamente(client: TestClient, repository):
    usuario = uuid4()
    compra_id = uuid4()
    repository.add_compra(compra_id)
    criado = client.post(f"/api/v1/compras/{compra_id}/itens", json=_payload()).json()

    delete = client.delete(
        f"/api/v1/itens-compras/{criado['id']}", headers={"X-Usuario-Id": str(usuario)}
    )
    consulta = client.get(f"/api/v1/itens-compras/{criado['id']}")

    assert delete.status_code == 200
    assert consulta.status_code == 404

    lista = client.get(f"/api/v1/compras/{compra_id}/itens")
    assert lista.json()["total"] == 0


def test_delete_sem_usuario_retorna_400(client: TestClient, repository):
    compra_id = uuid4()
    repository.add_compra(compra_id)
    criado = client.post(f"/api/v1/compras/{compra_id}/itens", json=_payload()).json()

    response = client.delete(f"/api/v1/itens-compras/{criado['id']}")

    assert response.status_code == 400
