"""Schemas de apresentação (Pydantic) para Identidade e Acesso (DOM-IDN)."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from src.modules.sigmun_idn.domain.entities import PermissaoEscopo, UsuarioStatus

# -- Payloads de criação -------------------------------------------------------


class UsuarioCreateRequest(BaseModel):
    """Payload de criação de usuário (POST)."""

    login: str = Field(..., min_length=3, max_length=50)
    email: str = Field(...)
    nome: str = Field(..., min_length=1)
    senha: str = Field(..., min_length=8)
    unidades_ids: list[str] = Field(default_factory=list)
    roles_ids: list[str] = Field(default_factory=list)


class RoleCreateRequest(BaseModel):
    """Payload de criação de role (POST)."""

    codigo: str = Field(..., min_length=1)
    nome: str = Field(..., min_length=1)
    descricao: str | None = None
    permissoes_ids: list[str] = Field(default_factory=list)


class PermissaoCreateRequest(BaseModel):
    """Payload de criação de permissão (POST)."""

    codigo: str = Field(..., min_length=1)
    nome: str = Field(..., min_length=1)
    descricao: str | None = None
    escopo: PermissaoEscopo = PermissaoEscopo.DOMINIO
    modulo: str = ""


class LoginRequest(BaseModel):
    """Payload de autenticação (POST)."""

    login: str = Field(...)
    senha: str = Field(...)


# -- Novos payloads para JWT (Fase 1) ------------------------------------------


class RefreshRequest(BaseModel):
    """Payload para renovação de access token via refresh token."""

    refresh_token: str = Field(..., description="Refresh token obtido no login")


# -- Schemas de resposta -------------------------------------------------------


class PermissaoResponse(BaseModel):
    """Representação de uma permissão."""

    model_config = ConfigDict(from_attributes=True)

    id: str
    codigo: str
    nome: str
    descricao: str | None = None
    escopo: str
    modulo: str
    created_at: datetime


class RoleResponse(BaseModel):
    """Representação de uma role."""

    model_config = ConfigDict(from_attributes=True)

    id: str
    codigo: str
    nome: str
    descricao: str | None = None
    permissoes: list[PermissaoResponse] = Field(default_factory=list)
    created_at: datetime


class UsuarioResponse(BaseModel):
    """Representação de um usuário."""

    model_config = ConfigDict(from_attributes=True)

    id: str
    login: str
    email: str
    nome: str
    status: str
    unidades_ids: list[str] = Field(default_factory=list)
    roles_ids: list[str] = Field(default_factory=list)
    last_login: datetime | None = None
    created_at: datetime
    updated_at: datetime | None = None


class UsuarioListResponse(BaseModel):
    """Envelope paginado de listagem de usuários."""

    total: int
    page: int
    page_size: int
    items: list[UsuarioResponse]


class LoginResponse(BaseModel):
    """Resposta de autenticação bem-sucedida (compatível com legacy).

    Campos legacy:
        token: str          # access token (JWT) ou session token (legacy)
        mensagem: str

    Campos novos (JWT):
        access_token: str   # JWT access token (stateless)
        refresh_token: str  # JWT refresh token (rotation)
        token_type: str     # "bearer"
        expires_in: int     # lifetime do access token em segundos
    """

    # Legacy (mantido para compatibilidade)
    token: str
    mensagem: str

    # JWT (novos campos opcionais para não quebrar clientes legacy)
    access_token: str | None = None
    refresh_token: str | None = None
    token_type: str | None = None
    expires_in: int | None = None


class TokenResponse(BaseModel):
    """Resposta padronizada OAuth2/OIDC para tokens JWT."""

    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int


class LogoutResponse(BaseModel):
    """Resposta de logout."""

    mensagem: str


class UsuarioStatusUpdateRequest(BaseModel):
    """Payload de atualização de status do usuário."""

    status: UsuarioStatus
    motivo: str | None = None


class ErrorResponse(BaseModel):
    """Erro padronizado da API."""

    detail: str


__all__ = [
    "UsuarioCreateRequest",
    "RoleCreateRequest",
    "PermissaoCreateRequest",
    "LoginRequest",
    "RefreshRequest",
    "PermissaoResponse",
    "RoleResponse",
    "UsuarioResponse",
    "UsuarioListResponse",
    "LoginResponse",
    "TokenResponse",
    "LogoutResponse",
    "UsuarioStatusUpdateRequest",
    "ErrorResponse",
]
