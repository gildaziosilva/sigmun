"""Endpoints REST de Identidade e Acesso (DOM-IDN).

Fornece APIs para gerenciamento de usuários, roles, permissões,
autenticação e autorização.
"""

from __future__ import annotations

import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_idn.application.interfaces import (
    AuditoriaLoginRepositoryInterface,
    SessaoRepositoryInterface,
    UsuarioRepositoryInterface,
)
from src.modules.sigmun_idn.application.use_cases import (
    AtivarUsuarioUseCase,
    AutenticarUsuarioUseCase,
    BloquearUsuarioUseCase,
    BuscarUsuarioUseCase,
    CriarUsuarioUseCase,
    DesativarUsuarioUseCase,
    ListarUsuariosUseCase,
    LogoutUseCase,
)
from src.modules.sigmun_idn.application.use_cases.auth_use_cases import (
    AutenticarUsuarioJWTCommand,
    AutenticarUsuarioJWTUseCase,
    LogoutJWTCommand,
    LogoutJWTUseCase,
    RenovarTokenCommand,
    RenovarTokenUseCase,
)
from src.modules.sigmun_idn.domain.entities import Usuario
from src.modules.sigmun_idn.domain.exceptions import (
    UsuarioJaExisteError,
    UsuarioNaoEncontradoError,
)
from src.modules.sigmun_idn.infrastructure.repositories import (
    SqlAlchemyAuditoriaLoginRepository,
    SqlAlchemySessaoRepository,
    SqlAlchemyUsuarioRepository,
)
from src.modules.sigmun_idn.presentation.schemas import (
    LoginRequest,
    LoginResponse,
    LogoutResponse,
    RefreshRequest,
    TokenResponse,
    UsuarioCreateRequest,
    UsuarioListResponse,
    UsuarioResponse,
)
from src.shared.security.jwt import JWTUsuarioContexto, get_current_user_hybrid

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/idn", tags=["Identidade e Acesso"])


# -- Providers (composition root do módulo) ------------------------------------


def get_usuario_repository(
    session: Annotated[Session, Depends(get_db)],
) -> UsuarioRepositoryInterface:
    """Fornece o repositório de usuários concreto por requisição."""
    return SqlAlchemyUsuarioRepository(session)


def get_sessao_repository(
    session: Annotated[Session, Depends(get_db)],
) -> SessaoRepositoryInterface:
    """Fornece o repositório de sessões concreto por requisição."""
    return SqlAlchemySessaoRepository(session)


def get_auditoria_repository(
    session: Annotated[Session, Depends(get_db)],
) -> AuditoriaLoginRepositoryInterface:
    """Fornece o repositório de auditoria concreto por requisição."""
    return SqlAlchemyAuditoriaLoginRepository(session)


# -- Helper functions ----------------------------------------------------------


def _to_usuario_response(usuario: Usuario) -> UsuarioResponse:
    """Converte entidade Usuario para schema de resposta."""
    return UsuarioResponse(
        id=usuario.id,
        login=usuario.login,
        email=usuario.email,
        nome=usuario.nome,
        status=usuario.status.value,
        unidades_ids=usuario.unidades_ids,
        roles_ids=usuario.roles_ids,
        last_login=usuario.last_login,
        created_at=usuario.created_at,
        updated_at=usuario.updated_at,
    )


def _to_login_response(result: object) -> LoginResponse:
    """Converte resultado de autenticação para LoginResponse (compatível)."""
    # Se é resultado JWT novo, popula campos novos + legacy
    if hasattr(result, 'access_token') and result.access_token:
        return LoginResponse(
            token=result.access_token,  # legacy: token = access_token
            mensagem=result.mensagem,
            access_token=result.access_token,
            refresh_token=result.refresh_token,
            token_type=result.token_type,
            expires_in=result.expires_in,
        )
    # Legacy: token simples
    return LoginResponse(token=result[0], mensagem=result[1])


# -- Endpoints de Usuários -----------------------------------------------------


@router.post(
    "/usuarios",
    response_model=UsuarioResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria um novo usuário",
    responses={
        400: {"description": "Dados inválidos"},
        409: {"description": "Usuário já existe"},
    },
)
def criar_usuario(
    payload: UsuarioCreateRequest,
    repository: Annotated[UsuarioRepositoryInterface, Depends(get_usuario_repository)],
) -> UsuarioResponse:
    use_case = CriarUsuarioUseCase(repository)
    try:
        usuario = use_case.execute(
            login=payload.login,
            email=payload.email,
            nome=payload.nome,
            senha=payload.senha,
            unidades_ids=payload.unidades_ids,
            roles_ids=payload.roles_ids,
        )
        return _to_usuario_response(usuario)
    except UsuarioJaExisteError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.get(
    "/usuarios",
    response_model=UsuarioListResponse,
    summary="Lista usuários com paginação",
)
def listar_usuarios(
    repository: Annotated[UsuarioRepositoryInterface, Depends(get_usuario_repository)],
    page: int = 1,
    page_size: int = 20,
) -> UsuarioListResponse:
    use_case = ListarUsuariosUseCase(repository)
    resultado = use_case.execute(page=page, page_size=page_size)
    return UsuarioListResponse(
        total=resultado.total,
        page=resultado.page,
        page_size=resultado.page_size,
        items=[_to_usuario_response(u) for u in resultado.items],
    )


@router.get(
    "/usuarios/{usuario_id}",
    response_model=UsuarioResponse,
    summary="Busca usuário por ID",
    responses={404: {"description": "Usuário não encontrado"}},
)
def buscar_usuario(
    usuario_id: str,
    repository: Annotated[UsuarioRepositoryInterface, Depends(get_usuario_repository)],
) -> UsuarioResponse:
    use_case = BuscarUsuarioUseCase(repository)
    try:
        usuario = use_case.execute(usuario_id)
        return _to_usuario_response(usuario)
    except UsuarioNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post(
    "/usuarios/{usuario_id}/ativar",
    response_model=UsuarioResponse,
    summary="Ativa um usuário",
    responses={404: {"description": "Usuário não encontrado"}},
)
def ativar_usuario(
    usuario_id: str,
    repository: Annotated[UsuarioRepositoryInterface, Depends(get_usuario_repository)],
) -> UsuarioResponse:
    use_case = AtivarUsuarioUseCase(repository)
    try:
        usuario = use_case.execute(usuario_id)
        return _to_usuario_response(usuario)
    except UsuarioNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post(
    "/usuarios/{usuario_id}/desativar",
    response_model=UsuarioResponse,
    summary="Desativa um usuário",
    responses={404: {"description": "Usuário não encontrado"}},
)
def desativar_usuario(
    usuario_id: str,
    repository: Annotated[UsuarioRepositoryInterface, Depends(get_usuario_repository)],
) -> UsuarioResponse:
    use_case = DesativarUsuarioUseCase(repository)
    try:
        usuario = use_case.execute(usuario_id)
        return _to_usuario_response(usuario)
    except UsuarioNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post(
    "/usuarios/{usuario_id}/bloquear",
    response_model=UsuarioResponse,
    summary="Bloqueia um usuário",
    responses={404: {"description": "Usuário não encontrado"}},
)
def bloquear_usuario(
    usuario_id: str,
    repository: Annotated[UsuarioRepositoryInterface, Depends(get_usuario_repository)],
) -> UsuarioResponse:
    use_case = BloquearUsuarioUseCase(repository)
    try:
        usuario = use_case.execute(usuario_id)
        return _to_usuario_response(usuario)
    except UsuarioNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


# -- Endpoints de Autenticação (Legacy - Compatibilidade) ----------------------


@router.post(
    "/auth/login",
    response_model=LoginResponse,
    summary="Autentica um usuário (Legacy - Session Token)",
    responses={401: {"description": "Credenciais inválidas"}},
    deprecated=True,
)
def login_legacy(
    payload: LoginRequest,
    usuario_repo: Annotated[UsuarioRepositoryInterface, Depends(get_usuario_repository)],
    sessao_repo: Annotated[SessaoRepositoryInterface, Depends(get_sessao_repository)],
    auditoria_repo: Annotated[AuditoriaLoginRepositoryInterface, Depends(get_auditoria_repository)],
) -> LoginResponse:
    """Autentica um usuário e retorna token de sessão (legacy, stateful).
    
    DEPRECADO: Use POST /auth/login/jwt para obter JWT tokens.
    """
    use_case = AutenticarUsuarioUseCase(
        usuario_repo=usuario_repo,
        sessao_repo=sessao_repo,
        auditoria_repo=auditoria_repo,
    )
    token, mensagem = use_case.execute(
        login=payload.login,
        senha=payload.senha,
    )
    if token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=mensagem)
    return LoginResponse(token=token, mensagem=mensagem)


@router.post(
    "/auth/login/jwt",
    response_model=LoginResponse,
    summary="Autentica um usuário e retorna JWT token pair (access + refresh)",
    responses={401: {"description": "Credenciais inválidas"}},
)
def login_jwt(
    payload: LoginRequest,
    usuario_repo: Annotated[UsuarioRepositoryInterface, Depends(get_usuario_repository)],
    sessao_repo: Annotated[SessaoRepositoryInterface, Depends(get_sessao_repository)],
    auditoria_repo: Annotated[AuditoriaLoginRepositoryInterface, Depends(get_auditoria_repository)],
) -> LoginResponse:
    """Autentica um usuário e retorna JWT access token + refresh token.

    NOVO (Fase 1): Retorna tokens JWT stateless com refresh token rotation.
    Mantém compatibilidade populando campos legacy (token, mensagem).
    """
    use_case = AutenticarUsuarioJWTUseCase(
        usuario_repo=usuario_repo,
        sessao_repo=sessao_repo,
        auditoria_repo=auditoria_repo,
    )
    command = AutenticarUsuarioJWTCommand(
        login=payload.login,
        senha=payload.senha,
    )
    result = use_case.execute(command)
    return _to_login_response(result)


@router.post(
    "/auth/refresh",
    response_model=TokenResponse,
    summary="Renova access token usando refresh token (rotation)",
    responses={401: {"description": "Refresh token inválido ou expirado"}},
)
def refresh_token(
    payload: RefreshRequest,
    usuario_repo: Annotated[UsuarioRepositoryInterface, Depends(get_usuario_repository)],
    sessao_repo: Annotated[SessaoRepositoryInterface, Depends(get_sessao_repository)],
) -> TokenResponse:
    """Renova access token via refresh token com rotation.

    Invalida o refresh token usado e emite novo par (access + refresh).
    """
    use_case = RenovarTokenUseCase(
        usuario_repo=usuario_repo,
        sessao_repo=sessao_repo,
    )
    command = RenovarTokenCommand(refresh_token=payload.refresh_token)
    result = use_case.execute(command)
    return TokenResponse(
        access_token=result.access_token,
        refresh_token=result.refresh_token,
        token_type=result.token_type,
        expires_in=result.expires_in,
    )


@router.post(
    "/auth/logout",
    response_model=LogoutResponse,
    summary="Realiza logout (compatível: session token ou JWT)",
)
def logout(
    token: str,
    sessao_repo: Annotated[SessaoRepositoryInterface, Depends(get_sessao_repository)],
) -> LogoutResponse:
    """Invalida a sessão do usuário (logout legacy - session token).

    Para logout JWT, use POST /auth/logout/jwt com refresh_token.
    """
    use_case = LogoutUseCase(sessao_repo)
    sucesso = use_case.execute(token)
    if sucesso:
        return LogoutResponse(mensagem="Logout realizado com sucesso")
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Sessão inválida")


@router.post(
    "/auth/logout/jwt",
    response_model=LogoutResponse,
    summary="Realiza logout JWT (invalida refresh token)",
)
def logout_jwt(
    payload: RefreshRequest,
    sessao_repo: Annotated[SessaoRepositoryInterface, Depends(get_sessao_repository)],
) -> LogoutResponse:
    """Invalida refresh token (logout JWT).

    TODO: implementar blocklist de refresh tokens no Redis.
    Por enquanto apenas invalida sessão stateful legada se houver.
    """
    use_case = LogoutJWTUseCase(sessao_repo=sessao_repo)
    command = LogoutJWTCommand(refresh_token=payload.refresh_token)
    use_case.execute(command)
    return LogoutResponse(mensagem="Logout JWT realizado com sucesso")


# -- Endpoint de teste para validar JWT ----------------------------------------


@router.get(
    "/auth/me",
    response_model=UsuarioResponse,
    summary="Retorna dados do usuário autenticado (valida JWT ou legacy header)",
    responses={401: {"description": "Não autenticado"}},
)
def get_current_user(
    usuario_atual: Annotated[JWTUsuarioContexto, Depends(get_current_user_hybrid)],
    repository: Annotated[UsuarioRepositoryInterface, Depends(get_usuario_repository)],
) -> UsuarioResponse:
    """Endpoint de teste: retorna dados do usuário autenticado.

    Aceita tanto JWT (Authorization: Bearer) quanto legacy header (X-Usuario-Id).
    """
    # usuario_atual é JWTUsuarioContexto com usuario_id, login, roles, unidades_ids
    usuario = repository.get_by_id(str(usuario_atual.usuario_id))
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
    return _to_usuario_response(usuario)


__all__ = [
    "router",
    "get_usuario_repository",
    "get_sessao_repository",
    "get_auditoria_repository",
]
