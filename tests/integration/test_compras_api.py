"""Testes de API dos endpoints de Compras (processos de compras).

Sobrescrevem a dependência do repositório por um repositório em memória,
exercitando o ciclo completo requisição -> use case -> resposta sem banco.
"""

from decimal import Decimal
from uuid import UUID, uuid4

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.modules.sigmun_compras.presentation.api.compras_router import (
    get_compra_repository,
)
from tests.unit.test_compra_use_cases import InMemoryCompraRepository


@pytest.fixture()
def repository() -> InMemoryCompraRepository:
    repo = InMemoryCompraRepository()
    repo.add_processo(uuid4())
    repo.add_fornecedor_ativo(uuid4())
    repo.add_unidade(uuid4())
    return repo


@pytest.fixture()
def client(repository: InMemoryCompraRepository) -> TestClient:
    app.dependency_overrides[get_compra_repository] = lambda: repository
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def _payload(repository: InMemoryCompraRepository, **overrides) -> dict:
    dados = {
        "processo_documental_id": str(next(iter(repository.processos))),
        "fornecedor_id": str(next(iter(repository.fornecedores_ativos))),
        "unidade_id": str(next(iter(repository.unidades))),
        "numero": "001/2026",
        "valor_total": "1000.00",
    }
    dados.update(overrides)
    return dados


# -- POST /api/v1/compras --------------------------------------------------------


def test_post_cria_compra(client: TestClient, repository):
    response = client.post("/api/v1/compras", json=_payload(repository))

    assert response.status_code == 201, response.text
    body = response.json()
    assert UUID(body["id"])
    assert body["situacao"] == "RASCUNHO"


def test_post_processo_inexistente_retorna_404(client: TestClient, repository):
    response = client.post(
        "/api/v1/compras", json=_payload(repository, processo_documental_id=str(uuid4()))
    )

    assert response.status_code == 404


def test_post_fornecedor_inexistente_retorna_404(client: TestClient, repository):
    response = client.post(
        "/api/v1/compras", json=_payload(repository, fornecedor_id=str(uuid4()))
    )

    assert response.status_code == 404


# -- GET /api/v1/compras -----------------------------------------------------------


def test_get_lista_vazia_e_com_itens(client: TestClient, repository):
    vazia = client.get("/api/v1/compras")
    assert vazia.status_code == 200
    assert vazia.json()["total"] == 0

    client.post("/api/v1/compras", json=_payload(repository))
    com_itens = client.get("/api/v1/compras")

    assert com_itens.status_code == 200
    assert com_itens.json()["total"] == 1


def test_get_lista_filtra_por_situacao(client: TestClient, repository):
    client.post("/api/v1/compras", json=_payload(repository))

    rascunhos = client.get("/api/v1/compras", params={"situacao": "RASCUNHO"})
    contratadas = client.get("/api/v1/compras", params={"situacao": "CONTRATADO"})
    invalida = client.get("/api/v1/compras", params={"situacao": "BANANA"})

    assert rascunhos.status_code == 200 and rascunhos.json()["total"] == 1
    assert contratadas.status_code == 200 and contratadas.json()["total"] == 0
    assert invalida.status_code == 400


# -- GET/PATCH /api/v1/compras/{id} --------------------------------------------------


def test_get_por_id_sucesso_e_404(client: TestClient, repository):
    criada = client.post("/api/v1/compras", json=_payload(repository)).json()

    ok = client.get(f"/api/v1/compras/{criada['id']}")
    not_found = client.get(f"/api/v1/compras/{uuid4()}")

    assert ok.status_code == 200
    assert ok.json()["numero"] == "001/2026"
    assert not_found.status_code == 404


def test_patch_atualiza_dados(client: TestClient, repository):
    usuario = uuid4()
    criada = client.post("/api/v1/compras", json=_payload(repository)).json()

    response = client.patch(
        f"/api/v1/compras/{criada['id']}",
        json={"valor_total": "2500.00"},
        headers={"X-Usuario-Id": str(usuario)},
    )

    assert response.status_code == 200, response.text
    assert Decimal(response.json()["valor_total"]) == Decimal("2500.00")


def test_patch_sem_campos_retorna_400(client: TestClient, repository):
    criada = client.post("/api/v1/compras", json=_payload(repository)).json()

    response = client.patch(f"/api/v1/compras/{criada['id']}", json={})

    assert response.status_code == 400


# -- PATCH /api/v1/compras/{id}/situacao -----------------------------------------------


def test_transicao_valida_avanca_situacao(client: TestClient, repository):
    usuario = uuid4()
    criada = client.post("/api/v1/compras", json=_payload(repository)).json()

    response = client.patch(
        f"/api/v1/compras/{criada['id']}/situacao",
        json={"situacao": "EM_INSTRUCAO"},
        headers={"X-Usuario-Id": str(usuario)},
    )

    assert response.status_code == 200, response.text
    assert response.json()["situacao"] == "EM_INSTRUCAO"


def test_transicao_invalida_retorna_400(client: TestClient, repository):
    criada = client.post("/api/v1/compras", json=_payload(repository)).json()

    response = client.patch(
        f"/api/v1/compras/{criada['id']}/situacao",
        json={"situacao": "CONTRATADO"},
    )

    assert response.status_code == 400
    assert "RN-COMPRAS-026" in response.json()["detail"]


def test_fluxo_completo_via_api_ate_contratado(client: TestClient, repository):
    criada = client.post("/api/v1/compras", json=_payload(repository)).json()
    url = f"/api/v1/compras/{criada['id']}/situacao"

    for situacao in (
        "EM_INSTRUCAO",
        "EM_ANALISE",
        "EM_PROCEDIMENTO",
        "EM_JULGAMENTO",
        "HOMOLOGADO",
        "CONTRATADO",
    ):
        resposta = client.patch(url, json={"situacao": situacao})
        assert resposta.status_code == 200, resposta.text

    assert resposta.json()["situacao"] == "CONTRATADO"


def test_transicao_em_compra_inexistente_retorna_404(client: TestClient):
    response = client.patch(
        f"/api/v1/compras/{uuid4()}/situacao", json={"situacao": "EM_INSTRUCAO"}
    )

    assert response.status_code == 404


# -- DELETE /api/v1/compras/{id} -------------------------------------------------------


def test_delete_exclui_logicamente(client: TestClient, repository):
    usuario = uuid4()
    criada = client.post("/api/v1/compras", json=_payload(repository)).json()

    delete = client.delete(
        f"/api/v1/compras/{criada['id']}", headers={"X-Usuario-Id": str(usuario)}
    )
    consulta = client.get(f"/api/v1/compras/{criada['id']}")

    assert delete.status_code == 200
    assert delete.json()["situacao"] == "RASCUNHO"
    assert consulta.status_code == 404


def test_delete_sem_usuario_retorna_400(client: TestClient, repository):
    criada = client.post("/api/v1/compras", json=_payload(repository)).json()

    response = client.delete(f"/api/v1/compras/{criada['id']}")

    assert response.status_code == 400


def test_delete_inexistente_retorna_404(client: TestClient):
    response = client.delete(
        f"/api/v1/compras/{uuid4()}", headers={"X-Usuario-Id": str(uuid4())}
    )

    assert response.status_code == 404
