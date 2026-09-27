"""JWT Authentication for SIGMUN (Fase 1 - DOM-IDN JWT Migration).

Implements stateless JWT access tokens with refresh token rotation.
Compatible with existing header-based auth during transition period.
"""

from __future__ import annotations

import secrets
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Annotated, Optional
from uuid import UUID

from fastapi import Depends, Header, HTTPException, status
from jose import JWTError, jwt
from pydantic import BaseModel

from src.shared.config.settings import settings


# =============================================================================
# Token Models
# =============================================================================


class TokenPayload(BaseModel):
    """JWT payload structure."""

    sub: str  # usuario_id
    login: str
    roles: list[str] = []
    unidades_ids: list[str] = []
    exp: int
    iat: int
    type: str = "access"  # "access" or "refresh"
    jti: str  # unique token identifier for revocation


class TokenPair(BaseModel):
    """Access + Refresh token pair."""

    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int  # access token lifetime in seconds


# =============================================================================
# Token Creation / Validation
# =============================================================================


def create_access_token(
    *,
    usuario_id: UUID | str,
    login: str,
    roles: list[str] | None = None,
    unidades_ids: list[str] | None = None,
    expires_delta: timedelta | None = None,
) -> str:
    """Create a short-lived JWT access token."""
    usuario_id_str = str(usuario_id)
    now = datetime.now(timezone.utc)
    expire = now + (expires_delta or timedelta(hours=settings.JWT_EXPIRATION_HOURS))

    payload = TokenPayload(
        sub=usuario_id_str,
        login=login,
        roles=roles or [],
        unidades_ids=unidades_ids or [],
        exp=int(expire.timestamp()),
        iat=int(now.timestamp()),
        type="access",
        jti="",  # will be set after encoding
    )

    # Add jti (JWT ID) for potential revocation tracking
    encoded = jwt.encode(
        payload.model_dump(exclude={"jti"}),
        settings.SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )

    # Decode to add jti, then re-encode
    decoded = jwt.decode(
        encoded, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
    )
    decoded["jti"] = secrets.token_urlsafe(16)

    return jwt.encode(decoded, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def create_refresh_token(
    *,
    usuario_id: UUID | str,
    login: str,
    expires_delta: timedelta | None = None,
) -> str:
    """Create a long-lived JWT refresh token."""
    usuario_id_str = str(usuario_id)
    now = datetime.now(timezone.utc)
    expire = now + (expires_delta or timedelta(days=settings.JWT_REFRESH_EXPIRATION_DAYS))

    payload = TokenPayload(
        sub=usuario_id_str,
        login=login,
        roles=[],  # refresh token doesn't need roles
        unidades_ids=[],
        exp=int(expire.timestamp()),
        iat=int(now.timestamp()),
        type="refresh",
        jti=secrets.token_urlsafe(16),
    )

    return jwt.encode(
        payload.model_dump(),
        settings.SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )


def create_token_pair(
    *,
    usuario_id: UUID | str,
    login: str,
    roles: list[str] | None = None,
    unidades_ids: list[str] | None = None,
) -> TokenPair:
    """Create both access and refresh tokens."""
    access_token = create_access_token(
        usuario_id=usuario_id,
        login=login,
        roles=roles,
        unidades_ids=unidades_ids,
    )
    refresh_token = create_refresh_token(usuario_id=usuario_id, login=login)

    return TokenPair(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=settings.JWT_EXPIRATION_HOURS * 3600,
    )


def decode_token(token: str) -> TokenPayload:
    """Decode and validate a JWT token."""
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        return TokenPayload(**payload)
    except JWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc


def verify_token_type(token: str, expected_type: str) -> TokenPayload:
    """Decode token and verify it's the expected type."""
    payload = decode_token(token)
    if payload.type != expected_type:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token inválido: esperado tipo '{expected_type}', recebido '{payload.type}'",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload

# =============================================================================
# FastAPI Dependencies
# =============================================================================


@dataclass(frozen=True)
class JWTUsuarioContexto:
    """Contexto de autorização extraído do JWT validado."""

    usuario_id: UUID
    login: str
    roles: tuple[str, ...]
    unidades_ids: tuple[str, ...]

    def possui_papel(self, papel: str) -> bool:
        return papel in self.roles

    def possui_algum_papel(self, *papeis: str) -> bool:
        return bool(set(papeis) & set(self.roles))


def get_current_user_jwt(
    authorization: Annotated[
        str | None,
        Header(
            alias="Authorization",
            description="Bearer token (JWT access token)",
        ),
    ] = None,
) -> JWTUsuarioContexto:
    """FastAPI dependency: valida JWT access token e retorna contexto do usuário."""
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticação obrigatória. Informe o header Authorization: Bearer <token>.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = authorization[7:]  # Remove "Bearer "
    payload = verify_token_type(token, "access")

    return JWTUsuarioContexto(
        usuario_id=UUID(payload.sub),
        login=payload.login,
        roles=tuple(payload.roles),
        unidades_ids=tuple(payload.unidades_ids),
    )


def require_roles_jwt(*required_roles: str):
    """Factory: dependency que exige autenticação JWT + um dos papéis."""

    def dependency(
        user: Annotated[JWTUsuarioContexto, Depends(get_current_user_jwt)],
    ) -> JWTUsuarioContexto:
        if not user.possui_algum_papel(*required_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Acesso negado. Requer um dos papéis: {', '.join(required_roles)}",
            )
        return user

    return dependency


def require_roles_hybrid(*required_roles: str):
    """Factory: dependency que exige autenticação (JWT ou legacy) + um dos papéis.

    Usa get_current_user_hybrid para compatibilidade durante transição.
    """
    def dependency(
        user: Annotated[JWTUsuarioContexto, Depends(get_current_user_hybrid)],
    ) -> JWTUsuarioContexto:
        if not user.possui_algum_papel(*required_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Acesso negado. Requer um dos papéis: {', '.join(required_roles)}",
            )
        return user

    return dependency


# =============================================================================
# Compatibility: Legacy Header Support (Transition Period)
# =============================================================================


def get_current_user_legacy(
    x_usuario_id: Annotated[
        UUID | None,
        Header(
            alias="X-Usuario-Id",
            description="[DEPRECADO] Use Authorization: Bearer <token>",
        ),
    ] = None,
    x_usuario_papel: Annotated[
        str | None,
        Header(
            alias="X-Usuario-Papel",
            description="[DEPRECADO] Use JWT com roles no token",
        ),
    ] = None,
) -> Optional[JWTUsuarioContexto]:
    """Legacy header-based auth (compatibilidade durante transição)."""
    if x_usuario_id is None:
        return None

    papeis: tuple[str, ...] = ()
    if x_usuario_papel:
        papeis = tuple(p.strip() for p in x_usuario_papel.split(",") if p.strip())

    return JWTUsuarioContexto(
        usuario_id=x_usuario_id,
        login="",  # não disponível no legacy
        roles=papeis,
        unidades_ids=(),
    )


def get_current_user_hybrid_optional(
    authorization: Annotated[
        str | None,
        Header(
            alias="Authorization",
            description="Bearer token (JWT access token)",
        ),
    ] = None,
    x_usuario_id: Annotated[
        UUID | None,
        Header(
            alias="X-Usuario-Id",
            description="[DEPRECADO] Use Authorization: Bearer <token>",
        ),
    ] = None,
    x_usuario_papel: Annotated[
        str | None,
        Header(
            alias="X-Usuario-Papel",
            description="[DEPRECADO] Use JWT com roles no token",
        ),
    ] = None,
) -> JWTUsuarioContexto | None:
    """Dependency híbrida opcional: tenta JWT, cai para legacy header, retorna None se nenhum.

    Para endpoints que permitem acesso anônimo (compatibilidade durante transição).
    """
    # Tenta JWT primeiro
    if authorization and authorization.startswith("Bearer "):
        token = authorization[7:]  # Remove "Bearer "
        try:
            payload = verify_token_type(token, "access")
            return JWTUsuarioContexto(
                usuario_id=UUID(payload.sub),
                login=payload.login,
                roles=tuple(payload.roles),
                unidades_ids=tuple(payload.unidades_ids),
            )
        except HTTPException:
            pass  # Cai para legacy se JWT inválido

    # Fallback para legacy headers
    if x_usuario_id is not None:
        papeis: tuple[str, ...] = ()
        if x_usuario_papel:
            papeis = tuple(p.strip() for p in x_usuario_papel.split(",") if p.strip())
        return JWTUsuarioContexto(
            usuario_id=x_usuario_id,
            login="",
            roles=papeis,
            unidades_ids=(),
        )

    return None


def get_current_user_hybrid(
    authorization: Annotated[
        str | None,
        Header(
            alias="Authorization",
            description="Bearer token (JWT access token)",
        ),
    ] = None,
    x_usuario_id: Annotated[
        UUID | None,
        Header(
            alias="X-Usuario-Id",
            description="[DEPRECADO] Use Authorization: Bearer <token>",
        ),
    ] = None,
    x_usuario_papel: Annotated[
        str | None,
        Header(
            alias="X-Usuario-Papel",
            description="[DEPRECADO] Use JWT com roles no token",
        ),
    ] = None,
) -> JWTUsuarioContexto:
    """Dependency híbrida: tenta JWT primeiro, cai para legacy header.

    Permite migração gradual sem quebrar clientes existentes.
    """
    # Tenta JWT primeiro
    if authorization and authorization.startswith("Bearer "):
        token = authorization[7:]  # Remove "Bearer "
        try:
            payload = verify_token_type(token, "access")
            return JWTUsuarioContexto(
                usuario_id=UUID(payload.sub),
                login=payload.login,
                roles=tuple(payload.roles),
                unidades_ids=tuple(payload.unidades_ids),
            )
        except HTTPException:
            pass  # Cai para legacy se JWT inválido

    # Fallback para legacy headers
    if x_usuario_id is not None:
        papeis: tuple[str, ...] = ()
        if x_usuario_papel:
            papeis = tuple(p.strip() for p in x_usuario_papel.split(",") if p.strip())
        return JWTUsuarioContexto(
            usuario_id=x_usuario_id,
            login="",
            roles=papeis,
            unidades_ids=(),
        )

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Autenticação obrigatória. Use Authorization: Bearer <token> ou header legado X-Usuario-Id.",
        headers={"WWW-Authenticate": "Bearer"},
    )


__all__ = [
    "TokenPayload",
    "TokenPair",
    "JWTUsuarioContexto",
    "create_access_token",
    "create_refresh_token",
    "create_token_pair",
    "decode_token",
    "verify_token_type",
    "get_current_user_jwt",
    "require_roles_jwt",
    "require_roles_hybrid",
    "get_current_user_legacy",
    "get_current_user_hybrid",
    "get_current_user_hybrid_optional",
]
