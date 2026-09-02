"""Testes de API da Trilha de Auditoria.

Validam o controle de acesso por perfil (017, seção 40), os filtros de
consulta (seção 42) e a auditoria do próprio acesso (seção 41).
"""

from datetime import datetime

from src.shared.compat import UTC
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.modules.sigmun_compras.domain.entities.registro_auditoria import (
    CategoriaEventoAuditoria,
    RegistroAuditoria,
)
from src.modules.sigmun_compras.presentation.api.auditoria_router import (
    get_trilha_auditoria_repository,
)
from tests.unit.test_registro_auditoria import InMemoryTrilhaAuditoriaRepository


@pytest.fixture()
def trilha() -> InMemoryTrilhaAuditoriaRepository:
    repo = InMemoryTrilhaAuditoriaRepository()
    usuario = uuid4()
    contrato_id = uuid4()

    repo.registrar(
        RegistroAuditoria(
            ocorrido_em=datetime(2026, 8, 22, 8, 0, tzinfo=UTC),
            categoria=CategoriaEventoAuditoria.CRIACAO,
            tipo_evento="ContratoCriado",
            operacao="criarContrato",
            recurso_tipo="Contrato",
            recurso_id=contrato_id,
            chave_negocio="CT-001/2026",
            ator_id=usuario,
        )
    )
    repo.registrar(
        RegistroAuditoria(
            ocorrido_em=datetime(2026, 8, 22, 9, 0, tzinfo=UTC),
            categoria=CategoriaEventoAuditoria.ASSINATURA,
            tipo_evento="ContratoAssinado",
            operacao="alterarSituacaoContrato",
            recurso_tipo="Contrato",
            recurso_id=contrato_id,
            chave_negocio="CT-001/2026",
            ator_id=usuario,
        )
    )
    return repo


@pytest.fixture()
def client(trilha: InMemoryTrilhaAuditoriaRepository) -> TestClient:
    app.dependency_overrides[get_trilha_auditoria_repository] = lambda: trilha
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


_HEADERS_AUDITOR = {"X-Usuario-Id": str(uuid4()), "X-Usuario-Papel": "auditor"}


def test_consulta_sem_autenticacao_retorna_401(client: TestClient):
    response = client.get("/api/v1/auditoria")

    assert response.status_code == 401


def test_consulta_sem_papel_retorna_403(client: TestClient):
    response = client.get(
        "/api/v1/auditoria",
        headers={"X-Usuario-Id": str(uuid4()), "X-Usuario-Papel": "compras"},
    )

    assert response.status_code == 403


def test_consulta_com_perfil_auditor_retorna_200(client: TestClient, trilha):
    response = client.get("/api/v1/auditoria", headers=_HEADERS_AUDITOR)

    assert response.status_code == 200, response.text
    body = response.json()
    # 2 eventos semeados na resposta; o evento de ACESSO desta consulta
    # é gravado na trilha mas não entra na mesma resposta (seção 41).
    assert body["total"] == 2
    assert len(body["items"]) == 2


def test_consulta_filtra_por_categoria(client: TestClient, trilha):
    response = client.get(
        "/api/v1/auditoria",
        params={"categoria": "ASSINATURA"},
        headers=_HEADERS_AUDITOR,
    )

    assert response.status_code == 200
    body = response.json()
    assert all(i["categoria"] == "ASSINATURA" for i in body["items"])
    assert any(i["tipo_evento"] == "ContratoAssinado" for i in body["items"])


def test_consulta_filtra_por_recurso(client: TestClient, trilha):
    recurso = next(iter(trilha.eventos)).recurso_id
    response = client.get(
        "/api/v1/auditoria",
        params={"recurso_tipo": "Contrato", "recurso_id": str(recurso)},
        headers=_HEADERS_AUDITOR,
    )

    assert response.status_code == 200
    assert response.json()["total"] >= 2


def test_acesso_a_trilha_eh_auditado(client: TestClient, trilha):
    total_antes = len(trilha.eventos)

    client.get("/api/v1/auditoria", headers=_HEADERS_AUDITOR)

    acessos = [
        e
        for e in trilha.eventos
        if e.categoria == CategoriaEventoAuditoria.ACESSO
        and e.tipo_evento == "TrilhaConsultada"
    ]
    assert len(acessos) == total_antes - 2 + 1  # 2 semeados; novo acesso registrado
