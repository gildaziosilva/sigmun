"""Infraestrutura de conexão com o banco de dados.

Centraliza a criação do engine e das sessões SQLAlchemy compartilhadas
pelos módulos de domínio do SIGMUN.
"""

from __future__ import annotations

from collections.abc import Generator
from threading import Lock

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.shared.config.settings import settings


class _SessionFactory:
    """Factory de sessões que pode ser reconfigurada em tempo de execução.
    
    Permite que o pytest-xdist crie bancos de dados dedicados por worker
    e atualize a fábrica de sessões globalmente.
    """
    
    def __init__(self):
        self._lock = Lock()
        self._sessionmaker = None
        self._engine = None
        self._initialize()
    
    def _initialize(self) -> None:
        """Inicializa o engine e sessionmaker com as configurações atuais."""
        engine = create_engine(
            settings.DATABASE_URL,
            pool_pre_ping=True,
            pool_size=5,
            max_overflow=10,
            future=True,
        )
        self._engine = engine
        self._sessionmaker = sessionmaker(
            bind=engine, autocommit=False, autoflush=False, expire_on_commit=False
        )
    
    def reconfigure(self) -> None:
        """Reconfigura a fábrica com as configurações atuais do settings."""
        with self._lock:
            if self._engine:
                self._engine.dispose()
            self._initialize()
    
    @property
    def engine(self):
        return self._engine
    
    def __call__(self) -> Session:
        """Cria uma nova sessão. Permite uso como `SessionLocal()`."""
        return self._sessionmaker()
    
    def __getattr__(self, name):
        """Delega atributos não encontrados ao sessionmaker subjacente."""
        return getattr(self._sessionmaker, name)


# Instância global da fábrica de sessões
SessionLocal = _SessionFactory()

# Para compatibilidade com código que acessa engine diretamente
engine = SessionLocal.engine


def get_db() -> Generator[Session, None, None]:
    """Fornece uma sessão de banco por requisição (dependency do FastAPI).

    A sessão é commitada ao final da requisição em caso de sucesso e
    revertida (rollback) em caso de erro.
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


__all__ = ["engine", "SessionLocal", "get_db"]
