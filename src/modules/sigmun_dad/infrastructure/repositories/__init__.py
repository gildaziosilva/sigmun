"""Repositórios SQLAlchemy do módulo sigmun_dad (DOM-DAD)."""

from src.modules.sigmun_dad.infrastructure.repositories.sqlalchemy_ativo_repository import (
    SqlAlchemyAtivoRepository,
)
from src.modules.sigmun_dad.infrastructure.repositories.sqlalchemy_catalogo_repository import (
    SqlAlchemyCatalogoRepository,
)
from src.modules.sigmun_dad.infrastructure.repositories.sqlalchemy_linhagem_repository import (
    SqlAlchemyLinhagemRepository,
)
from src.modules.sigmun_dad.infrastructure.repositories.sqlalchemy_politica_repository import (
    SqlAlchemyPoliticaRepository,
)
from src.modules.sigmun_dad.infrastructure.repositories.sqlalchemy_qualidade_repository import (
    SqlAlchemyQualidadeRepository,
)

__all__ = [
    "SqlAlchemyAtivoRepository",
    "SqlAlchemyCatalogoRepository",
    "SqlAlchemyLinhagemRepository",
    "SqlAlchemyPoliticaRepository",
    "SqlAlchemyQualidadeRepository",
]

