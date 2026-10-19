"""Testes e2e: Fluxo completo CRUD de documento GDO.

Cobre: criação, listagem, busca, tramitação, arquivamento, assinatura.
"""
import pytest
from datetime import date

from src.modules.sigmun_gdo.infrastructure.database.seeds import popular_seed_gdo as seed_gdo
from src.modules.sigmun_gdo.infrastructure.database.models import TipoDocumentalModel
from src.core.infrastructure.database.session import SessionLocal


class TestDocumentoE2E:
    """Testes end-to-end do ciclo de vida de documento GDO."""

    @pytest.fixture(autouse=True)
    def _setup(self):
        """Popula dados de referência antes de cada teste."""
        with SessionLocal() as session:
            seed_gdo(session)
            session.commit()
        yield

    def test_criar_listar_buscar_documento(self, client):
        """Fluxo completo: criar -> listar -> buscar documento."""
        with SessionLocal() as session:
            tipo = session.query(TipoDocumentalModel).filter_by(codigo="TD-OFICIO").first()
            assert tipo is not None
            tipo_id = str(tipo.id)

        # Criar documento
        payload = {
            "codigo": f"DOC-E2E-{date.today().strftime('%Y%m%d')}",
            "numero": "001",
            "ano": 2024,
            "tipo_documental_id": tipo_id,
            "titulo": "Documento E2E",
            "descricao": "Teste e2e",
            "unidade_autor_id": "UNIDADE-01",
            "is_sigiloso": False,
        }
        response = client.post("/api/v1/gdo/documentos", json=payload)
        assert response.status_code == 201
        doc = response.json()
        doc_id = doc["id"]

        # Listar documentos
        response = client.get("/api/v1/gdo/documentos")
        assert response.status_code == 200
        data = response.json()
        assert data["total"] >= 1
        assert any(d["id"] == doc_id for d in data["items"])

        # Buscar documento específico
        response = client.get(f"/api/v1/gdo/documentos/{doc_id}")
        assert response.status_code == 200
        doc = response.json()
        assert doc["id"] == doc_id
        assert doc["titulo"] == "Documento E2E"

    def test_tramitar_arquivar_assinar_documento(self, client):
        """Fluxo: criar -> tramitar -> arquivar -> assinar documento."""
        with SessionLocal() as session:
            tipo = session.query(TipoDocumentalModel).filter_by(codigo="TD-OFICIO").first()
            tipo_id = str(tipo.id)

        payload = {
            "codigo": f"DOC-E2E-{date.today().strftime('%Y%m%d')}",
            "numero": "002",
            "ano": 2024,
            "tipo_documental_id": tipo_id,
            "titulo": "Doc Tramitacao",
            "unidade_autor_id": "UNIDADE-01",
        }
        response = client.post("/api/v1/gdo/documentos", json=payload)
        assert response.status_code == 201
        doc = response.json()
        doc_id = doc["id"]

        # Tramitar
        response = client.post(
            f"/api/v1/gdo/documentos/{doc_id}/tramitar",
            json={
                "unidade_origem_id": "UNIDADE-01",
                "unidade_destino_id": "UNIDADE-02",
                "tipo": "encaminhamento",
                "motivo": "Para analise",
            },
        )
        assert response.status_code == 201

        # Arquivar
        response = client.post(
            f"/api/v1/gdo/documentos/{doc_id}/arquivar",
            json={
                "unidade_arquivo_id": "ARQUIVO-01",
                "observacao": "Arquivado apos tramitacao",
            },
        )
        assert response.status_code == 201

        # Assinar
        response = client.post(
            f"/api/v1/gdo/documentos/{doc_id}/assinar",
            json={
                "conteudo": "conteudo do documento",
                "autor_id": "AUTOR-01",
            },
        )
        assert response.status_code == 201
        assert response.json()["is_valida"] is True