"""Infraestrutura de conexão com o banco de dados.

Centraliza a criação do engine e das sessões SQLAlchemy compartilhadas
pelos módulos de domínio do SIGMUN.
"""

from __future__ import annotations

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.shared.config.settings import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    future=True,
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False)


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
