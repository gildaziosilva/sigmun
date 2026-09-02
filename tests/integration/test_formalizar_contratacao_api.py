"""Testes de API da Formalização da Contratação (Compra -> Contrato).

Exercita o endpoint POST /api/v1/contratos/formalizar com repositórios
em memória para os dois domínios (compras e contratos), validando a
integração, a autorização obrigatória (401) e os códigos de status.
"""

from datetime import date
from decimal import Decimal
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.modules.sigmun_compras.application.services.servico_de_auditoria import (
    ServicoDeAuditoria,
)
from src.modules.sigmun_compras.domain.entities.compra import Compra, SituacaoCompra
from src.modules.sigmun_compras.presentation.api.contratos_router import (
    get_compra_repository,
    get_contrato_repository,
    get_servico_de_auditoria,
)
from tests.unit.test_compra_use_cases import InMemoryCompraRepository
from tests.unit.test_contrato_use_cases import InMemoryContratoRepository
from tests.unit.test_registro_auditoria import InMemoryTrilhaAuditoriaRepository


@pytest.fixture()
def trilha() -> InMemoryTrilhaAuditoriaRepository:
    return InMemoryTrilhaAuditoriaRepository()


@pytest.fixture()
def repositorios():
    processo = uuid4()
    fornecedor = uuid4()
    unidade = uuid4()

    compras = InMemoryCompraRepository()
    contratos = InMemoryContratoRepository()

    compras.add_processo(processo)
    compras.add_fornecedor_ativo(fornecedor)
    compras.add_unidade(unidade)

    contratos.add_processo_documental(processo)
    contratos.add_fornecedor_ativo(fornecedor)
    contratos.add_unidade(unidade)

    compra = Compra(
        processo_documental_id=processo,
        fornecedor_id=fornecedor,
        unidade_id=unidade,
        numero="001/2026",
        data=date(2026, 1, 1),
        valor_total=Decimal("10000.00"),
        situacao=SituacaoCompra.HOMOLOGADO,
    )
    compras.save(compra)

    return {"compras": compras, "contratos": contratos, "compra": compra}


@pytest.fixture()
def client(repositorios, trilha) -> TestClient:
    app.dependency_overrides[get_contrato_repository] = lambda: repositorios["contratos"]
    app.dependency_overrides[get_compra_repository] = lambda: repositorios["compras"]
    app.dependency_overrides[get_servico_de_auditoria] = lambda: ServicoDeAuditoria(trilha)
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def _payload(**overrides) -> dict:
    dados = {
        "numero": "CT-001/2026",
        "data_inicio": "2026-02-01",
        "data_fim": "2026-12-31",
        "valor": "10000.00",
        "objeto": "Serviços de limpeza",
    }
    dados.update(overrides)
    return dados


def _form_url(compra_id) -> str:
    return f"/api/v1/contratos/formalizar?compra_id={compra_id}"


def test_formalizar_com_autenticacao_cria_contrato(client, repositorios):
    compra = repositorios["compra"]

    response = client.post(
        _form_url(compra.id),
        json=_payload(),
        headers={"X-Usuario-Id": str(uuid4())},
    )

    assert response.status_code == 201, response.text
    body = response.json()
    assert body["compra_id"] == str(compra.id)
    assert body["numero"] == "CT-001/2026"


def test_formalizar_requer_autenticacao(client, repositorios):
    response = client.post(
        _form_url(repositorios["compra"].id), json=_payload()
    )

    assert response.status_code == 401


def test_formalizar_compra_inexistente_retorna_404(client):
    response = client.post(
        _form_url(uuid4()),
        json=_payload(),
        headers={"X-Usuario-Id": str(uuid4())},
    )

    assert response.status_code == 404


def test_formalizar_avanca_compra_para_contratado(client, repositorios):
    compra = repositorios["compra"]
    response = client.post(
        _form_url(compra.id),
        json=_payload(),
        headers={"X-Usuario-Id": str(uuid4())},
    )

    assert response.status_code == 201
    compra_salva = repositorios["compras"].get_by_id(compra.id)
    assert compra_salva is not None
    assert compra_salva.situacao == SituacaoCompra.CONTRATADO


def test_formalizar_com_assinatura_avanca_contrato(client, repositorios):
    compra = repositorios["compra"]
    response = client.post(
        _form_url(compra.id),
        json=_payload(data_assinatura="2026-02-02"),
        headers={"X-Usuario-Id": str(uuid4())},
    )

    assert response.status_code == 201, response.text
    assert response.json()["situacao"] == "ASSINADO"
