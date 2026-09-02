"""Repositórios SQLAlchemy do módulo sigmun_cadastro (DOM-CUM)."""

from src.modules.sigmun_cadastro.infrastructure.repositories.sqlalchemy_pessoa_repository import (
    SqlAlchemyPessoaRepository,
)
from src.modules.sigmun_cadastro.infrastructure.repositories.sqlalchemy_unidade_administrativa_repository import (
    SqlAlchemyUnidadeAdministrativaRepository,
)

__all__ = [
    "SqlAlchemyPessoaRepository",
    "SqlAlchemyUnidadeAdministrativaRepository",
]
