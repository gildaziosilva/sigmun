"""
Módulo de Domínio do SIGMUN - Identidade e Acesso.

Este módulo contém as entidades, value objects, serviços e eventos
relacionados ao domínio de Identidade e Acesso.
"""

from src.modules.sigmun_idn.domain.entities import (
    Usuario,
    UsuarioStatus,
    Role,
    Permissao,
    PermissaoEscopo,
    Sessao,
    AuditoriaLogin,
)
from src.modules.sigmun_idn.domain.value_objects import Senha, Email, Login
from src.modules.sigmun_idn.domain.events import *
from src.modules.sigmun_idn.domain.services import (
    AutenticacaoService,
    AutorizacaoService,
    AuditoriaService,
)
from src.modules.sigmun_idn.domain.exceptions import *

__all__ = [
    # Entities
    "Usuario",
    "UsuarioStatus",
    "Role",
    "Permissao",
    "PermissaoEscopo",
    "Sessao",
    "AuditoriaLogin",
    # Value Objects
    "Senha",
    "Email",
    "Login",
    # Services
    "AutenticacaoService",
    "AutorizacaoService",
    "AuditoriaService",
]

