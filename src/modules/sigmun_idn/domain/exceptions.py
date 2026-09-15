"""
Exceções de domínio do módulo de Identidade e Acesso.
"""


class IdentidadeDomainError(Exception):
    """Exceção base do domínio."""

    pass


class UsuarioNaoEncontradoError(IdentidadeDomainError):
    """Usuário não encontrado."""

    pass


class UsuarioJaCadastradoError(IdentidadeDomainError):
    """Usuário já cadastrado."""

    pass


class UsuarioInativoError(IdentidadeDomainError):
    """Usuário inativo."""

    pass


class UsuarioBloqueadoError(IdentidadeDomainError):
    """Usuário bloqueado."""

    pass


class CredenciaisInvalidasError(IdentidadeDomainError):
    """Credenciais inválidas."""

    pass


class RoleNaoEncontradaError(IdentidadeDomainError):
    """Role não encontrada."""

    pass


class RoleDuplicadaError(IdentidadeDomainError):
    """Role já cadastrada."""

    pass


class PermissaoNaoEncontradaError(IdentidadeDomainError):
    """Permissão não encontrada."""

    pass


class PermissaoDuplicadaError(IdentidadeDomainError):
    """Permissão já cadastrada."""

    pass


class SessaoInvalidaError(IdentidadeDomainError):
    """Sessão inválida ou expirada."""

    pass


class PermissaoNegadaError(IdentidadeDomainError):
    """Permissão negada."""

    pass


class TokenInvalidoError(IdentidadeDomainError):
    """Token inválido."""

    pass


class SenhaInvalidaError(IdentidadeDomainError):
    """Senha inválida."""

    pass


class EmailInvalidoError(IdentidadeDomainError):
    """Email inválido."""

    pass


# ---------------------------------------------------------------------------
# Aliases de compatibilidade.
# ---------------------------------------------------------------------------
DomainException = IdentidadeDomainError
UsuarioJaExisteError = UsuarioJaCadastradoError
RoleJaExisteError = RoleDuplicadaError
PermissaoJaExisteError = PermissaoDuplicadaError
