"""Testes e2e: Fluxo completo de compras (fornecedor -> compra -> contrato).

Cobre: criar fornecedor -> criar compra -> avancar situacao ate
HOMOLOGADO -> formalizar contratacao (Compra -> Contrato) -> consultar.

Usa repositorios em memoria via dependency_overrides (mesmo padrao dos
testes de integracao de compras), sem depender de banco de dados.
"""
from uuid import UUID, uuid4

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.modules.sigmun_compras.application.services.servico_de_auditoria import (
    ServicoDeAuditoria,
)
from src.modules.sigmun_compras.presentation.api import (
    compras_router,
    contratos_router,
    fornecedores_router,
)
from src.shared.security.jwt import JWTUsuarioContexto, get_current_user_jwt
from tests.unit.test_compra_use_cases import InMemoryCompraRepository
from tests.unit.test_contrato_use_cases import InMemoryContratoRepository
from tests.unit.test_fornecedor_use_cases import InMemoryFornecedorRepository
from tests.unit.test_registro_auditoria import InMemoryTrilhaAuditoriaRepository

# Transicoes validas RN-COMPRAS-026: RASCUNHO -> ... -> HOMOLOGADO.
FLUXO_ATE_HOMOLOGADO = [
    "EM_INSTRUCAO",
    "EM_ANALISE",
    "EM_PROCEDIMENTO",
    "EM_JULGAMENTO",
    "HOMOLOGADO",
]


def _ctx_admin() -> JWTUsuarioContexto:
    return JWTUsuarioContexto(
        usuario_id=uuid4(), login="e2e.admin", roles=("admin",), unidades_ids=()
    )


@pytest.fixture()
def e2e_client():
    """Client e2e com repos em memoria compartilhados entre os routers."""
    processo_id = uuid4()
    unidade_id = uuid4()

    fornecedores = InMemoryFornecedorRepository()
    compras = InMemoryCompraRepository()
    contratos = InMemoryContratoRepository()
    trilha = InMemoryTrilhaAuditoriaRepository()

    # Vinculos de dominios core simulados (processo/unidade pre-existentes).
    compras.add_processo(processo_id)
    compras.add_unidade(unidade_id)
    contratos.add_processo_documental(processo_id)
    contratos.add_unidade(unidade_id)

    app.dependency_overrides[
        fornecedores_router.get_fornecedor_repository
    ] = lambda: fornecedores
    app.dependency_overrides[
        compras_router.get_compra_repository
    ] = lambda: compras
    # O router de contratos resolve o repo de compras pela SUA factory.
    app.dependency_overrides[
        contratos_router.get_compra_repository
    ] = lambda: compras
    app.dependency_overrides[
        contratos_router.get_contrato_repository
    ] = lambda: contratos
    app.dependency_overrides[
        contratos_router.get_servico_de_auditoria
    ] = lambda: ServicoDeAuditoria(trilha)
    app.dependency_overrides[get_current_user_jwt] = _ctx_admin
    try:
        with TestClient(app) as test_client:
            yield test_client, compras, contratos, processo_id, unidade_id
    finally:
        app.dependency_overrides.clear()

class TestComprasE2E:
    """Testes end-to-end do fluxo de compras."""

    def test_fluxo_completo_compras(self, e2e_client):
        """Fluxo: fornecedor -> compra -> homologar -> formalizar."""
        client, compras, contratos, processo_id, unidade_id = e2e_client

        # 1. Criar fornecedor
        fornecedor = client.post(
            "/api/v1/fornecedores",
            json={"pessoa_juridica_id": str(uuid4())},
        )
        assert fornecedor.status_code == 201, fornecedor.text
        forn_id = fornecedor.json()["id"]

        # Libera os vinculos cruzados entre os repos em memoria.
        compras.fornecedores_ativos.add(UUID(forn_id))
        contratos.fornecedores_ativos.add(UUID(forn_id))

        # 2. Criar compra
        compra = client.post(
            "/api/v1/compras",
            json={
                "processo_documental_id": str(processo_id),
                "fornecedor_id": forn_id,
                "unidade_id": str(unidade_id),
                "numero": "CMP-E2E-001",
                "valor_total": "10000.00",
            },
        )
        assert compra.status_code == 201, compra.text
        compra_id = compra.json()["id"]
        assert compra.json()["situacao"] == "RASCUNHO"

        # 3. Avancar a situacao ate HOMOLOGADO (RN-COMPRAS-026).
        for situacao in FLUXO_ATE_HOMOLOGADO:
            resp = client.patch(
                f"/api/v1/compras/{compra_id}/situacao",
                json={"situacao": situacao},
            )
            assert resp.status_code == 200, resp.text
        assert resp.json()["situacao"] == "HOMOLOGADO"

        # 4. Formalizar contratacao (Compra -> Contrato).
        formalizar = client.post(
            f"/api/v1/contratos/formalizar?compra_id={compra_id}",
            json={
                "numero": "CTR-E2E-001",
                "data_inicio": "2024-01-01",
                "data_fim": "2024-12-31",
                "valor": "9500.00",
                "objeto": "Compra E2E",
            },
        )
        assert formalizar.status_code == 201, formalizar.text
        contrato = formalizar.json()
        assert contrato["compra_id"] == compra_id
        assert contrato["numero"] == "CTR-E2E-001"

        # 5. Consultar o contrato criado.
        consulta = client.get(f"/api/v1/contratos/{contrato['id']}")
        assert consulta.status_code == 200, consulta.text
        assert consulta.json()["id"] == contrato["id"]

        # 6. A compra avancou para CONTRATADO (RN-COMPRAS-026).
        compra_final = client.get(f"/api/v1/compras/{compra_id}")
        assert compra_final.status_code == 200, compra_final.text
        assert compra_final.json()["situacao"] == "CONTRATADO"

    def test_fluxo_exige_autenticacao(self, e2e_client):
        """Sem JWT o fluxo e bloqueado com 401."""
        client, *_ = e2e_client
        app.dependency_overrides.pop(get_current_user_jwt, None)
        try:
            response = client.post(
                "/api/v1/fornecedores",
                json={"pessoa_juridica_id": str(uuid4())},
            )
        finally:
            app.dependency_overrides[get_current_user_jwt] = _ctx_admin
        assert response.status_code == 401
