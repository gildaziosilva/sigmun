"""Testes e2e: Fluxo completo de compras (fornecedor -> compra -> contrato).

Cobre: criar fornecedor -> criar compra -> criar contrato -> formalizar.
"""
import pytest

from src.modules.sigmun_compras.infrastructure.database.seeds import (
    FORNECEDORES_DEMO,
    run as seed_compras,
)
from src.core.infrastructure.database.session import SessionLocal


class TestComprasE2E:
    """Testes end-to-end do fluxo de compras."""

    @pytest.fixture(autouse=True)
    def _setup(self):
        with SessionLocal() as session:
            from src.modules.sigmun_compras.infrastructure.database.seeds import run as seed_compras
            seed_compras(session)
            session.commit()
        yield

    def test_fluxo_completo_compras(self, client):
        """Fluxo: fornecedor -> compra -> contrato -> formalizar."""
        # 1. Criar fornecedor
        fornecedor = client.post(
            "/api/v1/fornecedores",
            json=FORNECEDORES_DEMO[0],
        )
        assert fornecedor.status_code == 201
        forn_id = fornecedor.json()["id"]

        # 2. Criar compra
        compra = client.post(
            "/api/v1/compras",
            json={
                "numero": "CMP-E2E-001",
                "ano": 2024,
                "objeto": "Compra E2E",
                "valor_estimado": 10000.0,
                "fornecedor_id": forn_id,
                "modalidade": "pregao_eletronico",
            },
        )
        assert compra.status_code == 201
        compra_id = compra.json()["id"]

        # 3. Criar contrato
        contrato = client.post(
            "/api/v1/contratos",
            json={
                "compra_id": compra_id,
                "numero": "CTR-E2E-001",
                "valor": 9500.0,
                "vigencia_inicio": "2024-01-01",
                "vigencia_fim": "2024-12-31",
            },
        )
        assert contrato.status_code == 201
        contrato_id = contrato.json()["id"]

        # 4. Formalizar contratação
        response = client.post(
            f"/api/v1/contratos/{contrato_id}/formalizar",
            json={"autor_id": "AUTOR-01"},
        )
        assert response.status_code == 200
        assert response.json()["status"] == "formalizado"