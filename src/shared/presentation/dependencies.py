"""
Dependências centralizadas de autenticação e autorização — T-2.1.

Contrato único para todos os módulos. Evita reimplementação de dependencies
em cada router e garante consistência do RBAC.

Uso nos routers:
    from src.shared.presentation.dependencies import (
        UsuarioObrigatorio,
        UsuarioOpcional,
        exigir_papeis,
    )

    @router.get("/protegido")
    def rota_protegida(usuario: UsuarioObrigatorio): ...

    @router.get("/publica")
    def rota_publica(usuario: UsuarioOpcional): ...

    @router.post("/escrita")
    def rota_escrita(usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor"))]): ...
"""

from typing import Annotated

from fastapi import Depends

from src.shared.security.jwt import (
    JWTUsuarioContexto,
    get_current_user_hybrid_optional,
    get_current_user_jwt,
    require_roles_hybrid,
)

# =============================================================================
# Dependências base — autenticação
# =============================================================================

# Usuário autenticado OBRIGATÓRIO (JWT estrito; sem fallback legacy).
# Retorna 401 se token ausente/inválido.
UsuarioObrigatorio = Annotated[JWTUsuarioContexto, Depends(get_current_user_jwt)]

# Usuário autenticado OPCIONAL (permite acesso anônimo).
# Retorna JWTUsuarioContexto se autenticado, None caso contrário.
# O fallback legacy só atua se ALLOW_LEGACY_HEADERS=True (T-0.2).
UsuarioOpcional = Annotated[
    JWTUsuarioContexto | None, Depends(get_current_user_hybrid_optional)
]

# =============================================================================
# Factories de autorização (RBAC)
# =============================================================================

# Reexport das factories do jwt.py para uso direto nos módulos
__all__ = [
    "JWTUsuarioContexto",
    "UsuarioObrigatorio",
    "UsuarioOpcional",
    "require_roles_hybrid",
    "exigir_papeis",
]

# Alias semântico para require_roles_hybrid (mesma função, nome em PT-BR)
exigir_papeis = require_roles_hybrid