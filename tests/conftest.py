"""
Configuração compartilhada para testes do SIGMUN.
"""

import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture(scope="session")
def client() -> TestClient:
    """Fixture do cliente HTTP para testes de API."""
    return TestClient(app)


@pytest.fixture(scope="session")
def app_instance():
    """Fixture da instância da aplicação FastAPI."""
    return app
