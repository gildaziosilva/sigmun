"""
Testes unitários do endpoint de health check.
"""

from fastapi.testclient import TestClient


def test_health_check(client: TestClient):
    """Verifica se o endpoint de health check retorna status saudável."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "SIGMUN"


def test_root(client: TestClient):
    """Verifica se o endpoint raiz retorna informações do serviço."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "SIGMUN"
    assert "documentation" in data
