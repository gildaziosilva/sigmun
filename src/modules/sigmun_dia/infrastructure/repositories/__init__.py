"""Repositórios SQLAlchemy do domínio Gestão de Diárias.

Importante: os repositórios aqui exportados implementam as interfaces
definidas em ``application.interfaces`` e são injetados via *dependency
injection* nas rotas FastAPI.
"""

from .sqlalchemy_viagem_repository import SQLAlchemyViagemRepository
from .sqlalchemy_diaria_repository import SQLAlchemyDiariaRepository
from .sqlalchemy_prestacao_repository import SQLAlchemyPrestacaoContasRepository

__all__ = [
    "SQLAlchemyViagemRepository",
    "SQLAlchemyDiariaRepository",
    "SQLAlchemyPrestacaoContasRepository",
]
