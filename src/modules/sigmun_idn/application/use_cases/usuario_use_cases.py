"""
Casos de uso para gerenciamento de usuários.
"""

import logging

from src.modules.sigmun_idn.application.interfaces import (
    AuditoriaLoginRepositoryInterface,
    SessaoRepositoryInterface,
    UsuarioRepositoryInterface,
)
from src.modules.sigmun_idn.domain.entities import (
    Usuario,
    UsuarioStatus,
)
from src.modules.sigmun_idn.domain.exceptions import (
    EmailInvalidoError,
    SenhaInvalidaError,
    UsuarioJaCadastradoError,
    UsuarioNaoEncontradoError,
)
from src.modules.sigmun_idn.domain.services import AutenticacaoService
from src.modules.sigmun_idn.domain.value_objects import Email, Login, Senha

logger = logging.getLogger(__name__)


class CriarUsuarioUseCase:
    """Caso de uso para criar um novo usuário."""

    def __init__(self, usuario_repo: UsuarioRepositoryInterface) -> None:
        self._repo = usuario_repo

    def execute(
        self,
        login: str,
        email: str,
        nome: str,
        senha: str,
        unidades_ids: list[str] | None = None,
        roles_ids: list[str] | None = None,
    ) -> Usuario:
        """Cria um novo usuário."""
        valido, msg = Login.validar_formato(login)
        if not valido:
            raise ValueError(f"Login inválido: {msg}")

        valido, msg = Email.validar_formato(email)
        if not valido:
            raise EmailInvalidoError(f"Email inválido: {msg}")

        valido, msg = Senha.validar_formato(senha)
        if not valido:
            raise SenhaInvalidaError(f"Senha inválida: {msg}")

        if self._repo.exists_by_login(login):
            raise UsuarioJaCadastradoError(f"Login '{login}' já está em uso")

        if self._repo.exists_by_email(email):
            raise UsuarioJaCadastradoError(f"Email '{email}' já está em uso")

        senha_hash = AutenticacaoService.criar_hash_senha(senha)

        usuario = Usuario(
            login=login,
            email=email,
            nome=nome,
            senha_hash=senha_hash,
            status=UsuarioStatus.ATIVO,
            unidades_ids=unidades_ids or [],
            roles_ids=roles_ids or [],
        )

        return self._repo.save(usuario)


class AtivarUsuarioUseCase:
    """Caso de uso para ativar um usuário."""

    def __init__(self, usuario_repo: UsuarioRepositoryInterface) -> None:
        self._repo = usuario_repo

    def execute(self, usuario_id: str) -> Usuario:
        """Ativa um usuário."""
        usuario = self._repo.get_by_id(usuario_id)
        if usuario is None:
            raise UsuarioNaoEncontradoError(f"Usuário '{usuario_id}' não encontrado")
        usuario.ativar()
        return self._repo.save(usuario)


class DesativarUsuarioUseCase:
    """Caso de uso para desativar um usuário."""

    def __init__(self, usuario_repo: UsuarioRepositoryInterface) -> None:
        self._repo = usuario_repo

    def execute(self, usuario_id: str) -> Usuario:
        """Desativa um usuário."""
        usuario = self._repo.get_by_id(usuario_id)
        if usuario is None:
            raise UsuarioNaoEncontradoError(f"Usuário '{usuario_id}' não encontrado")
        usuario.desativar()
        return self._repo.save(usuario)


class BloquearUsuarioUseCase:
    """Caso de uso para bloquear um usuário."""

    def __init__(self, usuario_repo: UsuarioRepositoryInterface) -> None:
        self._repo = usuario_repo

    def execute(self, usuario_id: str, motivo: str = "") -> Usuario:
        """Bloqueia um usuário."""
        usuario = self._repo.get_by_id(usuario_id)
        if usuario is None:
            raise UsuarioNaoEncontradoError(f"Usuário '{usuario_id}' não encontrado")
        usuario.bloquear()
        return self._repo.save(usuario)


class BuscarUsuarioUseCase:
    """Caso de uso para buscar usuários."""

    def __init__(self, usuario_repo: UsuarioRepositoryInterface) -> None:
        self._repo = usuario_repo

    def get_by_id(self, usuario_id: str) -> Usuario:
        """Busca usuário por ID."""
        usuario = self._repo.get_by_id(usuario_id)
        if usuario is None:
            raise UsuarioNaoEncontradoError(f"Usuário '{usuario_id}' não encontrado")
        return usuario

    def get_by_login(self, login: str) -> Usuario:
        """Busca usuário por login."""
        usuario = self._repo.get_by_login(login)
        if usuario is None:
            raise UsuarioNaoEncontradoError(f"Usuário '{login}' não encontrado")
        return usuario


class AutenticarUsuarioUseCase:
    """Caso de uso para autenticar um usuário."""

    def __init__(
        self,
        usuario_repo: UsuarioRepositoryInterface,
        sessao_repo: SessaoRepositoryInterface | None = None,
        auditoria_repo: AuditoriaLoginRepositoryInterface | None = None,
    ) -> None:
        self._usuario_repo = usuario_repo
        self._sessao_repo = sessao_repo
        self._auditoria_repo = auditoria_repo

    def execute(
        self, login: str, senha: str, ip_origem: str = "", user_agent: str = ""
    ) -> tuple[str | None, str]:
        """Autentica usuário e retorna token de sessão."""
        from src.modules.sigmun_idn.domain.services import AuditoriaService, AutenticacaoService

        usuario = self._usuario_repo.get_by_login(login)
        if usuario is None:
            return None, "Credenciais inválidas"

        sucesso, motivo = AutenticacaoService.autenticar(usuario, senha, ip_origem, user_agent)

        if self._auditoria_repo:
            auditoria = AuditoriaService.registrar_login(
                usuario_id=usuario.id,
                login=login,
                sucesso=sucesso,
                ip_origem=ip_origem,
                user_agent=user_agent,
                motivo_falha=motivo or "",
            )
            self._auditoria_repo.save(auditoria)

        if not sucesso:
            return None, motivo or "Erro desconhecido"

        usuario.atualizar_ultimo_login()
        self._usuario_repo.save(usuario)

        if self._sessao_repo:
            sessao = AutenticacaoService.criar_sessao(
                usuario_id=usuario.id,
                ip_origem=ip_origem,
                user_agent=user_agent,
            )
            self._sessao_repo.save(sessao)
            return sessao.token, "Autenticação realizada com sucesso"

        return "", "Autenticação realizada com sucesso"


class LogoutUseCase:
    """Caso de uso para realizar logout."""

    def __init__(self, sessao_repo: SessaoRepositoryInterface) -> None:
        self._sessao_repo = sessao_repo

    def execute(self, token: str) -> bool:
        """Invalida sessão (logout)."""
        return self._sessao_repo.invalidate(token)


# ---------------------------------------------------------------------------
# Aliases PT-BR espelhados no DOM-COMPRAS-001 (Registrar/Consultar/Listar).
# ---------------------------------------------------------------------------
RegistrarUsuarioUseCase = CriarUsuarioUseCase
ConsultarUsuarioUseCase = BuscarUsuarioUseCase
ListarUsuariosUseCase = BuscarUsuarioUseCase


__all__ = [
    "CriarUsuarioUseCase",
    "RegistrarUsuarioUseCase",
    "AtivarUsuarioUseCase",
    "DesativarUsuarioUseCase",
    "BloquearUsuarioUseCase",
    "BuscarUsuarioUseCase",
    "ConsultarUsuarioUseCase",
    "ListarUsuariosUseCase",
    "AutenticarUsuarioUseCase",
    "LogoutUseCase",
]
