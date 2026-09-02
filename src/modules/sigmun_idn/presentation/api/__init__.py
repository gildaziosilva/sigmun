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
    CriarUsuarioUseCase,
    DesativarUsuarioUseCase,
    LogoutUseCase,
)
from src.modules.sigmun_idn.domain.entities import UsuarioStatus
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
    UsuarioCreateRequest,
    UsuarioListResponse,
    UsuarioResponse,
)

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


def _to_usuario_response(usuario) -> UsuarioResponse:
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
    """Cria um novo usuário no sistema."""
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
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get(
    "/usuarios/{usuario_id}",
    response_model=UsuarioResponse,
    summary="Busca usuário por ID",
    responses={
        404: {"description": "Usuário não encontrado"},
    },
)
def buscar_usuario(
    usuario_id: str,
    repository: Annotated[UsuarioRepositoryInterface, Depends(get_usuario_repository)],
) -> UsuarioResponse:
    """Busca um usuário pelo ID."""
    from src.modules.sigmun_idn.application.use_cases.usuario_use_cases import (
        BuscarUsuarioUseCase,
    )
    use_case = BuscarUsuarioUseCase(repository)
    try:
        usuario = use_case.get_by_id(usuario_id)
        return _to_usuario_response(usuario)
    except UsuarioNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get(
    "/usuarios",
    response_model=UsuarioListResponse,
    summary="Lista usuários",
)
def listar_usuarios(
    repository: Annotated[UsuarioRepositoryInterface, Depends(get_usuario_repository)],
    page: int = 0,
    page_size: int = 50,
    status_filter: str | None = None,
) -> UsuarioListResponse:
    """Lista usuários com paginação e filtro opcional por status."""
    usuarios, total = repository.list_all(page=page, page_size=page_size, status=status_filter)
    return UsuarioListResponse(
        total=total,
        page=page,
        page_size=page_size,
        items=[_to_usuario_response(u) for u in usuarios],
    )


@router.post(
    "/usuarios/{usuario_id}/ativar",
    response_model=UsuarioResponse,
    summary="Ativa um usuário",
    responses={
        404: {"description": "Usuário não encontrado"},
    },
)
def ativar_usuario(
    usuario_id: str,
    repository: Annotated[UsuarioRepositoryInterface, Depends(get_usuario_repository)],
) -> UsuarioResponse:
    """Ativa um usuário pendente ou inativo."""
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
    responses={
        404: {"description": "Usuário não encontrado"},
    },
)
def desativar_usuario(
    usuario_id: str,
    repository: Annotated[UsuarioRepositoryInterface, Depends(get_usuario_repository)],
) -> UsuarioResponse:
    """Desativa um usuário ativo."""
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
    responses={
        404: {"description": "Usuário não encontrado"},
    },
)
def bloquear_usuario(
    usuario_id: str,
    repository: Annotated[UsuarioRepositoryInterface, Depends(get_usuario_repository)],
) -> UsuarioResponse:
    """Bloqueia um usuário."""
    use_case = BloquearUsuarioUseCase(repository)
    try:
        usuario = use_case.execute(usuario_id)
        return _to_usuario_response(usuario)
    except UsuarioNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


# -- Endpoints de Autenticação -------------------------------------------------


@router.post(
    "/auth/login",
    response_model=LoginResponse,
    summary="Autentica um usuário",
    responses={
        401: {"description": "Credenciais inválidas"},
    },
)
def login(
    payload: LoginRequest,
    usuario_repo: Annotated[UsuarioRepositoryInterface, Depends(get_usuario_repository)],
    sessao_repo: Annotated[SessaoRepositoryInterface, Depends(get_sessao_repository)],
    auditoria_repo: Annotated[AuditoriaLoginRepositoryInterface, Depends(get_auditoria_repository)],
) -> LoginResponse:
    """Autentica um usuário e retorna token de sessão."""
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
    "/auth/logout",
    response_model=LogoutResponse,
    summary="Realiza logout",
)
def logout(
    token: str,
    sessao_repo: Annotated[SessaoRepositoryInterface, Depends(get_sessao_repository)],
) -> LogoutResponse:
    """Invalida a sessão do usuário (logout)."""
    use_case = LogoutUseCase(sessao_repo)
    sucesso = use_case.execute(token)
    if sucesso:
        return LogoutResponse(mensagem="Logout realizado com sucesso")
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Sessão inválida")


__all__ = [
    "router",
    "get_usuario_repository",
    "get_sessao_repository",
    "get_auditoria_repository",
]
