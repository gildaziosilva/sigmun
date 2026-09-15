"""
Módulo de Domínio do SIGMUN - Identidade e Acesso.

Este módulo contém as entidades, value objects, serviços e eventos
relacionados ao domínio de Identidade e Acesso.
"""

from src.modules.sigmun_idn.domain.entities import (
    AuditoriaLogin,
    Permissao,
    PermissaoEscopo,
    Role,
    Sessao,
    Usuario,
    UsuarioStatus,
)
from src.modules.sigmun_idn.domain.events import (
    DomainEvent,
    EventoIdentidade,
    LoginFalhouEvent,
    LoginRealizadoEvent,
    LogoutRealizadoEvent,
    PermissaoConcedidaEvent,
    PermissaoCriadaEvent,
    PermissaoRevogadaEvent,
    RoleAtualizadaEvent,
    RoleCriadaEvent,
    RoleRemovidaEvent,
    SenhaAlteradaEvent,
    SessaoCriadaEvent,
    SessaoInvalidadaEvent,
    UsuarioAtivadoEvent,
    UsuarioBloqueadoEvent,
    UsuarioCriadoEvent,
    UsuarioDesativadoEvent,
)
from src.modules.sigmun_idn.domain.exceptions import (
    CredenciaisInvalidasError,
    DomainException,
    EmailInvalidoError,
    IdentidadeDomainError,
    PermissaoDuplicadaError,
    PermissaoJaExisteError,
    PermissaoNaoEncontradaError,
    PermissaoNegadaError,
    RoleDuplicadaError,
    RoleJaExisteError,
    RoleNaoEncontradaError,
    SenhaInvalidaError,
    SessaoInvalidaError,
    TokenInvalidoError,
    UsuarioBloqueadoError,
    UsuarioInativoError,
    UsuarioJaCadastradoError,
    UsuarioJaExisteError,
    UsuarioNaoEncontradoError,
)
from src.modules.sigmun_idn.domain.services import (
    AuditoriaService,
    AutenticacaoService,
    AutorizacaoService,
)
from src.modules.sigmun_idn.domain.value_objects import Email, Login, Senha

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
    # Events
    "EventoIdentidade",
    "DomainEvent",
    "UsuarioCriadoEvent",
    "UsuarioAtivadoEvent",
    "UsuarioDesativadoEvent",
    "UsuarioBloqueadoEvent",
    "LoginRealizadoEvent",
    "LoginFalhouEvent",
    "LogoutRealizadoEvent",
    "PermissaoConcedidaEvent",
    "PermissaoRevogadaEvent",
    "RoleCriadaEvent",
    "RoleAtualizadaEvent",
    "RoleRemovidaEvent",
    "PermissaoCriadaEvent",
    "SenhaAlteradaEvent",
    "SessaoCriadaEvent",
    "SessaoInvalidadaEvent",
    # Exceptions
    "IdentidadeDomainError",
    "DomainException",
    "UsuarioNaoEncontradoError",
    "UsuarioJaCadastradoError",
    "UsuarioJaExisteError",
    "UsuarioInativoError",
    "UsuarioBloqueadoError",
    "CredenciaisInvalidasError",
    "RoleNaoEncontradaError",
    "RoleDuplicadaError",
    "RoleJaExisteError",
    "PermissaoNaoEncontradaError",
    "PermissaoDuplicadaError",
    "PermissaoJaExisteError",
    "SessaoInvalidaError",
    "PermissaoNegadaError",
    "TokenInvalidoError",
    "SenhaInvalidaError",
    "EmailInvalidoError",
]
