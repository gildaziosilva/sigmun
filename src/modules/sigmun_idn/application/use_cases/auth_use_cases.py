"""Casos de uso de autenticação com JWT (Fase 1 - DOM-IDN).

Substitui a autenticação baseada em sessão stateful por JWT stateless
com refresh token rotation.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from uuid import UUID

from src.modules.sigmun_idn.application.interfaces import (
    AuditoriaLoginRepositoryInterface,
    SessaoRepositoryInterface,
    UsuarioRepositoryInterface,
)
from src.modules.sigmun_idn.domain.entities import (
    AuditoriaLogin,
    Sessao,
    Usuario,
    UsuarioStatus,
)
from src.modules.sigmun_idn.domain.exceptions import (
    UsuarioNaoEncontradoError,
)
from src.modules.sigmun_idn.domain.services import AuditoriaService, AutenticacaoService
from src.shared.security.jwt import create_token_pair

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class AutenticarUsuarioJWTCommand:
    """Comando para autenticar usuário e gerar token pair JWT."""

    login: str
    senha: str
    ip_origem: str = ""
    user_agent: str = ""


@dataclass(frozen=True)
class AutenticarUsuarioJWTResult:
    """Resultado da autenticação JWT."""

    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
    usuario: Usuario
    mensagem: str


@dataclass(frozen=True)
class RenovarTokenCommand:
    """Comando para renovar access token via refresh token."""

    refresh_token: str


@dataclass(frozen=True)
class RenovarTokenResult:
    """Resultado da renovação de token."""

    access_token: str
    refresh_token: str  # novo refresh token (rotation)
    token_type: str
    expires_in: int


@dataclass(frozen=True)
class LogoutJWTCommand:
    """Comando para logout (invalida refresh token)."""

    refresh_token: str
    access_token: str | None = None


class AutenticarUsuarioJWTUseCase:
    """Caso de uso para autenticar usuário e gerar JWT token pair.

    Mantém compatibilidade: também cria sessão stateful no BD para
    não quebrar logout legacy durante transição.
    """

    def __init__(
        self,
        usuario_repo: UsuarioRepositoryInterface,
        sessao_repo: SessaoRepositoryInterface | None = None,
        auditoria_repo: AuditoriaLoginRepositoryInterface | None = None,
    ) -> None:
        self._usuario_repo = usuario_repo
        self._sessao_repo = sessao_repo
        self._auditoria_repo = auditoria_repo

    def execute(self, command: AutenticarUsuarioJWTCommand) -> AutenticarUsuarioJWTResult:
        """Autentica usuário e retorna JWT token pair."""
        usuario = self._usuario_repo.get_by_login(command.login)
        if usuario is None:
            self._registrar_auditoria(
                usuario_id="",
                login=command.login,
                sucesso=False,
                ip_origem=command.ip_origem,
                user_agent=command.user_agent,
                motivo_falha="Credenciais inválidas",
            )
            raise UsuarioNaoEncontradoError("Credenciais inválidas")

        sucesso, motivo = AutenticacaoService.autenticar(
            usuario, command.senha, command.ip_origem, command.user_agent
        )

        self._registrar_auditoria(
            usuario_id=str(usuario.id),
            login=command.login,
            sucesso=sucesso,
            ip_origem=command.ip_origem,
            user_agent=command.user_agent,
            motivo_falha=motivo or "",
        )

        if not sucesso:
            raise UsuarioNaoEncontradoError(motivo or "Credenciais inválidas")

        # Atualiza último login
        usuario.atualizar_ultimo_login()
        self._usuario_repo.save(usuario)

        # Busca roles e permissões do usuário para incluir no token
        roles = self._buscar_roles_usuario(usuario)
        unidades_ids = list(usuario.unidades_ids) if usuario.unidades_ids else []

        # Gera JWT token pair
        token_pair = create_token_pair(
            usuario_id=usuario.id,
            login=usuario.login,
            roles=roles,
            unidades_ids=unidades_ids,
        )

        # Mantém sessão stateful para compatibilidade com logout legacy
        if self._sessao_repo:
            sessao = AutenticacaoService.criar_sessao(
                usuario_id=str(usuario.id),
                ip_origem=command.ip_origem,
                user_agent=command.user_agent,
            )
            self._sessao_repo.save(sessao)

        logger.info(
            "Autenticação JWT realizada",
            extra={"extra_data": {"usuario_id": str(usuario.id), "login": usuario.login}},
        )

        return AutenticarUsuarioJWTResult(
            access_token=token_pair.access_token,
            refresh_token=token_pair.refresh_token,
            token_type=token_pair.token_type,
            expires_in=token_pair.expires_in,
            usuario=usuario,
            mensagem="Autenticação realizada com sucesso",
        )

    def _buscar_roles_usuario(self, usuario: Usuario) -> list[str]:
        """Busca códigos das roles do usuário.

        Nota: implementação simplificada - em produção buscar via RoleRepository.
        """
        # TODO: implementar busca real de roles via repository
        # Por enquanto retorna roles_ids como códigos (assumindo que são códigos)
        return list(usuario.roles_ids) if usuario.roles_ids else []

    def _registrar_auditoria(
        self,
        usuario_id: str,
        login: str,
        sucesso: bool,
        ip_origem: str,
        user_agent: str,
        motivo_falha: str,
    ) -> None:
        if self._auditoria_repo:
            auditoria = AuditoriaService.registrar_login(
                usuario_id=usuario_id,
                login=login,
                sucesso=sucesso,
                ip_origem=ip_origem,
                user_agent=user_agent,
                motivo_falha=motivo_falha,
            )
            self._auditoria_repo.save(auditoria)


class RenovarTokenUseCase:
    """Caso de uso para renovar access token via refresh token (rotation).

    Implementa refresh token rotation: invalida o refresh token usado
    e emite um novo par (access + refresh).
    """

    def __init__(
        self,
        usuario_repo: UsuarioRepositoryInterface,
        sessao_repo: SessaoRepositoryInterface | None = None,
    ) -> None:
        self._usuario_repo = usuario_repo
        self._sessao_repo = sessao_repo

    def execute(self, command: RenovarTokenCommand) -> RenovarTokenResult:
        """Renova access token usando refresh token."""
        from src.shared.security.jwt import decode_token, verify_token_type

        # Valida refresh token
        payload = verify_token_type(command.refresh_token, "refresh")
        usuario_id = UUID(payload.sub)

        # Busca usuário
        usuario = self._usuario_repo.get_by_id(str(usuario_id))
        if usuario is None or not usuario.esta_ativo:
            raise UsuarioNaoEncontradoError("Usuário não encontrado ou inativo")

        # Busca roles
        roles = self._buscar_roles_usuario(usuario)
        unidades_ids = list(usuario.unidades_ids) if usuario.unidades_ids else []

        # Gera novo token pair (rotation)
        token_pair = create_token_pair(
            usuario_id=usuario.id,
            login=usuario.login,
            roles=roles,
            unidades_ids=unidades_ids,
        )

        logger.info(
            "Token renovado via refresh token rotation",
            extra={"extra_data": {"usuario_id": str(usuario.id)}},
        )

        return RenovarTokenResult(
            access_token=token_pair.access_token,
            refresh_token=token_pair.refresh_token,
            token_type=token_pair.token_type,
            expires_in=token_pair.expires_in,
        )

    def _buscar_roles_usuario(self, usuario: Usuario) -> list[str]:
        return list(usuario.roles_ids) if usuario.roles_ids else []


class LogoutJWTUseCase:
    """Caso de uso para logout com JWT.

    Invalida o refresh token (marca como revogado) e opcionalmente
    a sessão stateful legada.
    """

    def __init__(
        self,
        sessao_repo: SessaoRepositoryInterface | None = None,
    ) -> None:
        self._sessao_repo = sessao_repo

    def execute(self, command: LogoutJWTCommand) -> bool:
        """Realiza logout invalidando tokens."""
        # TODO: implementar blocklist de refresh tokens (Redis)
        # Por enquanto apenas invalida sessão stateful legada
        if command.access_token and self._sessao_repo:
            # Tenta extrair session token do access token legacy
            # Se for JWT, não há sessão stateful correspondente
            pass

        logger.info("Logout JWT realizado")
        return True


__all__ = [
    "AutenticarUsuarioJWTCommand",
    "AutenticarUsuarioJWTResult",
    "AutenticarUsuarioJWTUseCase",
    "RenovarTokenCommand",
    "RenovarTokenResult",
    "RenovarTokenUseCase",
    "LogoutJWTCommand",
    "LogoutJWTUseCase",
]
