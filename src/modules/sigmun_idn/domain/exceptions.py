"""
Exceções de domínio do módulo de Identidade e Acesso.
"""


class DomainException(Exception):
    """Exceção base do domínio."""
    pass


class UsuarioNaoEncontradoError(DomainException):
    """Usuário não encontrado."""
    pass


class UsuarioJaExisteError(DomainException):
    """Usuário já cadastrado."""
    pass


class UsuarioInativoError(DomainException):
    """Usuário inativo."""
    pass


class UsuarioBloqueadoError(DomainException):
    """Usuário bloqueado."""
    pass


class CredenciaisInvalidasError(DomainException):
    """Credenciais inválidas."""
    pass


class RoleNaoEncontradaError(DomainException):
    """Role não encontrada."""
    pass


class RoleJaExisteError(DomainException):
    """Role já cadastrada."""
    pass


class PermissaoNaoEncontradaError(DomainException):
    """Permissão não encontrada."""
    pass


class PermissaoJaExisteError(DomainException):
    """Permissão já cadastrada."""
    pass


class SessaoInvalidaError(DomainException):
    """Sessão inválida ou expirada."""
    pass


class PermissaoNegadaError(DomainException):
    """Permissão negada."""
    pass


class TokenInvalidoError(DomainException):
    """Token inválido."""
    pass


class SenhaInvalidaError(DomainException):
    """Senha inválida."""
    pass


class EmailInvalidoError(DomainException):
    """Email inválido."""
    pass
