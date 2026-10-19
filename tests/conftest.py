"""
Configuração compartilhada para testes do SIGMUN.
"""

import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker

from src.main import app
from src.core.infrastructure.database.session import engine, SessionLocal
from src.shared.config.settings import settings


@pytest.fixture(scope="session", autouse=True)
def _habilitar_headers_legados_nos_testes():
    """Transicao Fase 0 T-0.2: testes legados pendentes de migracao JWT.

    O default de producao (False) e preservado; a flag e ligada apenas
    no processo de teste. A regressao test_fase0_seguranca.py prova o
    comportamento seguro com ela OFF.
    """
    anterior = settings.ALLOW_LEGACY_HEADERS
    settings.ALLOW_LEGACY_HEADERS = True
    try:
        yield
    finally:
        settings.ALLOW_LEGACY_HEADERS = anterior


@pytest.fixture(scope="session")
def client() -> TestClient:
    """Fixture do cliente HTTP para testes de API."""
    return TestClient(app)


@pytest.fixture(scope="session")
def app_instance():
    """Fixture da instância da aplicação FastAPI."""
    return app


# =============================================================================
# Worker isolation: each pytest-xdist worker gets its own database cloned from
# the template database (sigmun_template). This prevents TRUNCATE conflicts.
# =============================================================================

def _get_worker_id() -> str:
    """Get the pytest-xdist worker ID (e.g., 'gw0', 'gw1') or 'master'."""
    return os.environ.get("PYTEST_XDIST_WORKER", "master")


def _create_worker_database(worker_id: str) -> str:
    """Create a database for the worker from the template."""
    db_name = f"sigmun_test_{worker_id}"
    
    # Connect to postgres database to create/drop databases
    admin_engine = create_engine(
        f"postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASSWORD}"
        f"@{settings.DB_HOST}:{settings.DB_PORT}/postgres",
        isolation_level="AUTOCOMMIT",
    )
    
    with admin_engine.connect() as conn:
        # Terminate any existing connections to the worker database
        conn.execute(text(f"""
            SELECT pg_terminate_backend(pid)
            FROM pg_stat_activity
            WHERE datname = '{db_name}' AND pid <> pg_backend_pid()
        """))
        # Drop if exists
        conn.execute(text(f"DROP DATABASE IF EXISTS {db_name}"))
        # Create from template
        conn.execute(text(f"CREATE DATABASE {db_name} TEMPLATE sigmun_template"))
    
    admin_engine.dispose()
    return db_name


def _drop_worker_database(worker_id: str) -> None:
    """Drop the worker's database."""
    db_name = f"sigmun_test_{worker_id}"
    
    admin_engine = create_engine(
        f"postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASSWORD}"
        f"@{settings.DB_HOST}:{settings.DB_PORT}/postgres",
        isolation_level="AUTOCOMMIT",
    )
    
    with admin_engine.connect() as conn:
        # Terminate any existing connections
        conn.execute(text(f"""
            SELECT pg_terminate_backend(pid)
            FROM pg_stat_activity
            WHERE datname = '{db_name}' AND pid <> pg_backend_pid()
        """))
        conn.execute(text(f"DROP DATABASE IF EXISTS {db_name}"))
    
    admin_engine.dispose()


@pytest.fixture(scope="session", autouse=True)
def _worker_database_isolation():
    """
    Create a dedicated database for each pytest-xdist worker.
    
    This fixture runs once per worker (session scope) and creates a database
    cloned from sigmun_template. All tests in this worker will use this database.
    """
    worker_id = _get_worker_id()
    
    # Only create separate databases when running with pytest-xdist
    if worker_id == "master":
        # Running without xdist, use the main database
        yield
        return
    
    # Create worker database
    db_name = _create_worker_database(worker_id)
    
    # Update settings to use the worker database
    original_db_name = settings.DB_NAME
    settings.DB_NAME = db_name
    
    # Reconfigure the session factory to use the new database
    from src.core.infrastructure.database.session import SessionLocal
    SessionLocal.reconfigure()
    
    try:
        yield
    finally:
        # Restore original settings
        settings.DB_NAME = original_db_name
        # Reconfigure back to original database
        SessionLocal.reconfigure()
        # Drop worker database
        _drop_worker_database(worker_id)
