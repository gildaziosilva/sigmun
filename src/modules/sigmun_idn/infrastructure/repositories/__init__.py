"""Repositórios SQLAlchemy do módulo sigmun_cadastro (DOM-IDN)."""

from src.modules.sigmun_idn.infrastructure.repositories.sqlalchemy_usuario_repository import (
    SqlAlchemyUsuarioRepository,
)
from src.modules.sigmun_idn.infrastructure.repositories.sqlalchemy_role_repository import (
    SqlAlchemyRoleRepository,
)
from src.modules.sigmun_idn.infrastructure.repositories.sqlalchemy_permissao_repository import (
    SqlAlchemyPermissaoRepository,
)
from src.modules.sigmun_idn.infrastructure.repositories.sqlalchemy_sessao_repository import (
    SqlAlchemySessaoRepository,
)
from src.modules.sigmun_idn.infrastructure.repositories.sqlalchemy_auditoria_repository import (
    SqlAlchemyAuditoriaLoginRepository,
)

__all__ = [
    "SqlAlchemyUsuarioRepository",
    "SqlAlchemyRoleRepository",
    "SqlAlchemyPermissaoRepository",
    "SqlAlchemySessaoRepository",
    "SqlAlchemyAuditoriaLoginRepository",
]
