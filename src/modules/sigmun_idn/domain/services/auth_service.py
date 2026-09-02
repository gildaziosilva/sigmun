"""
Serviços de domínio do módulo de Identidade e Acesso.
"""

import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Optional

from src.modules.sigmun_idn.domain.entities import (
    Usuario,
    UsuarioStatus,
    Role,
    Permissao,
    Sessao,
    AuditoriaLogin,
)
from src.modules.sigmun_idn.domain.exceptions import (
    CredenciaisInvalidasError,
    UsuarioInativoError,
    UsuarioBloqueadoError,
    SessaoInvalidaError,
    PermissaoNegadaError,
)


class AutenticacaoService:
    """Serviço de autenticação."""

    @staticmethod
    def _hash_senha(senha: str) -> str:
        """Gera hash da senha."""
        salt = secrets.token_hex(16)
        hash_obj = hashlib.pbkdf2_hmac("sha256", senha.encode(), salt.encode(), 100000)
        return f"{salt}${hash_obj.hex()}"

    @staticmethod
    def _verificar_senha(senha: str, senha_hash: str) -> bool:
        """Verifica senha contra hash."""
        try:
            salt, hash_value = senha_hash.split("$")
            hash_obj = hashlib.pbkdf2_hmac("sha256", senha.encode(), salt.encode(), 100000)
            return hash_obj.hex() == hash_value
        except (ValueError, AttributeError):
            return False

    @classmethod
    def criar_hash_senha(cls, senha: str) -> str:
        """Cria hash de senha para armazenamento."""
        return cls._hash_senha(senha)

    @classmethod
    def autenticar(
        cls,
        usuario: Usuario,
        senha: str,
        ip_origem: str = "",
        user_agent: str = "",
    ) -> tuple[bool, Optional[str]]:
        """
        Autentica um usuário.

        Returns:
            Tuple de (sucesso, motivo_falha)
        """
        if usuario.is_deleted:
            return False, "Usuário não encontrado"

        if usuario.status == UsuarioStatus.BLOQUEADO:
            return False, "Usuário bloqueado"

        if usuario.status == UsuarioStatus.INATIVO:
            return False, "Usuário inativo"

        if usuario.status == UsuarioStatus.PENDENTE:
            return False, "Usuário pendente de ativação"

        if not cls._verificar_senha(senha, usuario.senha_hash):
            return False, "Credenciais inválidas"

        return True, ""

    @staticmethod
    def criar_sessao(
        usuario_id: str,
        duracao_horas: int = 24,
        ip_origem: str = "",
        user_agent: str = "",
    ) -> Sessao:
        """Cria nova sessão para o usuário."""
        token = secrets.token_urlsafe(64)
        expires_at = datetime.utcnow() + timedelta(hours=duracao_horas)

        return Sessao(
            usuario_id=usuario_id,
            token=token,
            ip_origem=ip_origem,
            user_agent=user_agent,
            expires_at=expires_at,
        )

    @staticmethod
    def validar_sessao(sessao: Optional[Sessao]) -> bool:
        """Valida se sessão é válida."""
        if sessao is None:
            return False
        if not sessao.is_active:
            return False
        if sessao.is_expired:
            return False
        return True


class AutorizacaoService:
    """Serviço de autorização."""

    @staticmethod
    def verificar_permissao(
        usuario: Usuario,
        codigo_permissao: str,
        roles: list[Role],
    ) -> bool:
        """
        Verifica se usuário possui permissão.

        Args:
            usuario: Usuário a verificar
            codigo_permissao: Código da permissão requerida
            roles: Lista de roles para busca

        Returns:
            True se usuário possui permissão
        """
        if usuario.is_deleted or not usuario.is_active:
            return False

        return usuario.has_permission(codigo_permissao, roles)

    @staticmethod
    def verificar_role(usuario: Usuario, codigo_role: str, roles: list[Role]) -> bool:
        """Verifica se usuário possui role específica."""
        if usuario.is_deleted or not usuario.is_active:
            return False

        for role in roles:
            if role.id in usuario.roles_ids and role.codigo == codigo_role:
                return not role.is_deleted
        return False

    @staticmethod
    def pode_acessar_unidade(usuario: Usuario, unidade_id: str) -> bool:
        """Verifica se usuário pode acessar unidade."""
        if usuario.is_deleted or not usuario.is_active:
            return False

        # Admin global tem acesso a todas as unidades
        if not usuario.unidades_ids:
            return True

        return unidade_id in usuario.unidades_ids


class AuditoriaService:
    """Serviço de auditoria de acesso."""

    @staticmethod
    def registrar_login(
        usuario_id: str,
        login: str,
        sucesso: bool,
        ip_origem: str = "",
        user_agent: str = "",
        motivo_falha: str = "",
    ) -> AuditoriaLogin:
        """Cria registro de auditoria de login."""
        return AuditoriaLogin(
            usuario_id=usuario_id,
            login=login,
            ip_origem=ip_origem,
            user_agent=user_agent,
            sucesso=sucesso,
            motivo_falha=motivo_falha,
        )


__all__ = [
    "AutenticacaoService",
    "AutorizacaoService",
    "AuditoriaService",
]
