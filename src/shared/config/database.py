"""
Configuração do banco de dados SQLAlchemy (compatibilidade).

DEPRECATED: o engine e a fábrica de sessão canônicos ficam em
``src/core/infrastructure/database/session.py``. Este módulo é mantido
apenas para compatibilidade com importações legadas (ex.: ``Base``) e
não deve receber novos usos — prefira importar ``engine``,
``SessionLocal`` e ``get_db`` do módulo do core.
"""

from sqlalchemy.orm import declarative_base

from src.core.infrastructure.database.session import SessionLocal, engine, get_db

Base = declarative_base()

__all__ = ["engine", "SessionLocal", "get_db", "Base"]
