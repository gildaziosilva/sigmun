"""Testes de integração: operações de contratos geram eventos de auditoria.

Valida a instrumentação do router de contratos (017-Modelo-de-Auditoria,
seção 44 – auditoria reforçada de contratos) com repositórios em memória.
"""

from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.modules.sigmun_compras.application.services.servico_de_auditoria import (
    ServicoDeAuditoria,
)
from src.modules.sigmun_compras.domain.entities.registro_auditoria import (
    CategoriaEventoAuditoria,
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


def _payload(repository, **overrides) -> dict:
    dados = {
        "processo_documental_id": str(next(iter(repository.processos_documentais))),
        "fornecedor_id": str(next(iter(repository.fornecedores_ativos))),
        "unidade_id": str(next(iter(repository.unidades))),
        "numero": "CT-001/2026",
    }
    dados.update(overrides)
    return dados


def _eventos(trilha, categoria):
    return [e for e in trilha.eventos if e.categoria == categoria]


def test_criar_contrato_registra_evento_criacao(client, repository, trilha):
    response = client.post("/api/v1/contratos", json=_payload(repository))

    assert response.status_code == 201
    criacoes = _eventos(trilha, CategoriaEventoAuditoria.CRIACAO)
    assert len(criacoes) == 1
    evento = criacoes[0]
    assert evento.tipo_evento == "ContratoCriado"
    assert evento.recurso_tipo == "Contrato"
    assert str(evento.recurso_id) == response.json()["id"]
    assert evento.chave_negocio == "CT-001/2026"


def test_atualizar_contrato_registra_evento_alteracao(client, repository, trilha):
    criado = client.post(
        "/api/v1/contratos", json=_payload(repository), headers={"X-Usuario-Id": str(uuid4())}
    ).json()

    client.patch(
        f"/api/v1/contratos/{criado['id']}",
        json={"objeto": "Objeto alterado"},
        headers={"X-Usuario-Id": str(uuid4())},
    )

    alteracoes = _eventos(trilha, CategoriaEventoAuditoria.ALTERACAO)
    assert len(alteracoes) == 1
    assert alteracoes[0].tipo_evento == "ContratoAlterado"
    assert alteracoes[0].detalhes == {"campos": ["objeto"]}


def test_assinatura_registra_evento_assinatura(client, repository, trilha):
    usuario = uuid4()
    criado = client.post(
        "/api/v1/contratos", json=_payload(repository), headers={"X-Usuario-Id": str(usuario)}
    ).json()

    client.patch(
        f"/api/v1/contratos/{criado['id']}/situacao",
        json={"situacao": "ASSINADO"},
        headers={"X-Usuario-Id": str(usuario)},
    )

    assinaturas = _eventos(trilha, CategoriaEventoAuditoria.ASSINATURA)
    assert len(assinaturas) == 1
    assert assinaturas[0].tipo_evento == "ContratoAssinado"
    assert assinaturas[0].detalhes == {"situacao_nova": "ASSINADO"}


def test_excluir_contrato_registra_evento_exclusao(client, repository, trilha):
    usuario = uuid4()
    criado = client.post(
        "/api/v1/contratos", json=_payload(repository), headers={"X-Usuario-Id": str(usuario)}
    ).json()

    client.delete(
        f"/api/v1/contratos/{criado['id']}",
        headers={"X-Usuario-Id": str(usuario)},
    )

    exclusoes = _eventos(trilha, CategoriaEventoAuditoria.EXCLUSAO)
    assert len(exclusoes) == 1
    assert exclusoes[0].tipo_evento == "ContratoExcluido"


def test_operacao_com_erro_nao_registra_evento(client, repository, trilha):
    # duplicado -> 409; nenhuma mutação ocorreu
    payload = _payload(repository)
    client.post("/api/v1/contratos", json=payload)
    total_apos_primeira = len(trilha.eventos)

    resposta_duplicada = client.post("/api/v1/contratos", json=payload)

    assert resposta_duplicada.status_code == 409
    assert len(trilha.eventos) == total_apos_primeira
