"""JWT Authentication for SIGMUN (Fase 1 - DOM-IDN JWT Migration).

Implements stateless JWT access tokens with refresh token rotation.
Compatible with existing header-based auth during transition period.
"""

from __future__ import annotations

import secrets
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Annotated
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
    decoded = jwt.decode(encoded, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
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
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
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


def _normaliza_papel(papel: str) -> str:
    """Reduz um papel à forma canônica de comparação.

    O banco grava códigos como ``ROLE_OUVIDOR`` (ver seeds de
    ``idn.roles``), enquanto as rotas declaram o papel sem prefixo e em
    minúsculas (``require_roles_hybrid("ouvidor")``). Comparar as duas
    strings literalmente nunca casa, e o efeito é um 403 para todo usuário
    legítimo. Normalizar em um único ponto evita que cada módulo precise
    conhecer a convenção do banco.
    """
    return str(papel or "").strip().upper().removeprefix("ROLE_")


@dataclass(frozen=True)
class JWTUsuarioContexto:
    """Contexto de autorização extraído do JWT validado."""

    usuario_id: UUID
    login: str
    roles: tuple[str, ...]
    unidades_ids: tuple[str, ...]

    def possui_papel(self, papel: str) -> bool:
        return _normaliza_papel(papel) in self._papeis_normalizados

    def possui_algum_papel(self, *papeis: str) -> bool:
        return bool({_normaliza_papel(p) for p in papeis} & self._papeis_normalizados)

    @property
    def _papeis_normalizados(self) -> set[str]:
        return {_normaliza_papel(r) for r in self.roles}


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
    """Factory: autenticação JWT estrita + papel (Fase 0 T-0.1).

    Usa ``get_current_user_jwt``: header legado NUNCA confere papel.
    Mantido o nome para compatibilidade reversa dos routers.
    """

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


# =============================================================================
# Compatibility: Legacy Header Support (Transition Period)
# =============================================================================


def _fallback_legacy_permitido() -> bool:
    """T-0.2: fallback só vale com ALLOW_LEGACY_HEADERS=True."""
    return bool(settings.ALLOW_LEGACY_HEADERS)


def _contexto_de_headers_legados(
    x_usuario_id: UUID | None, x_usuario_papel: str | None
) -> JWTUsuarioContexto | None:
    """Constroi contexto a partir dos headers (só chamado com flag ligada)."""
    if x_usuario_id is None:
        return None
    papeis: tuple[str, ...] = ()
    if x_usuario_papel:
        papeis = tuple(p.strip() for p in x_usuario_papel.split(",") if p.strip())
    return JWTUsuarioContexto(
        usuario_id=x_usuario_id,
        login="",
        roles=papeis,
        unidades_ids=(),
    )


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
) -> JWTUsuarioContexto | None:
    """Legacy header-based auth — SOMENTE com ALLOW_LEGACY_HEADERS=True (T-0.2).

    Com a flag desligada (default), retorna None: header legado nunca
    autentica ninguém. Fallback mantido só p/ leitura anônima opcional.
    """
    if not _fallback_legacy_permitido():
        return None
    return _contexto_de_headers_legados(x_usuario_id, x_usuario_papel)


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

    # Fallback legado: só com flag ligada (T-0.2); senão, anônimo (None).
    if _fallback_legacy_permitido():
        legado = _contexto_de_headers_legados(x_usuario_id, x_usuario_papel)
        if legado is not None:
            return legado

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

    # Fallback legado: só com flag ligada (T-0.2). Desligada => 401 mesmo
    # com X-Usuario-Id/Papel presentes (identidade forjável não entra).
    if _fallback_legacy_permitido():
        legado = _contexto_de_headers_legados(x_usuario_id, x_usuario_papel)
        if legado is not None:
            return legado

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Autenticação obrigatória. Use Authorization: Bearer <token>.",
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
