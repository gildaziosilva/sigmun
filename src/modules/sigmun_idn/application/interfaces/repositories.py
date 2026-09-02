"""
Interfaces para repositórios do módulo de Identidade e Acesso.
"""

from abc import ABC, abstractmethod
from typing import Optional

from src.modules.sigmun_idn.domain.entities import (
    Usuario,
    Role,
    Permissao,
    Sessao,
    AuditoriaLogin,
)


class UsuarioRepositoryInterface(ABC):
    """Interface para repositório de usuários."""

    @abstractmethod
    def get_by_id(self, usuario_id: str) -> Optional[Usuario]:
        """Busca usuário por ID."""
        pass

    @abstractmethod
    def get_by_login(self, login: str) -> Optional[Usuario]:
        """Busca usuário por login."""
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[Usuario]:
        """Busca usuário por email."""
        pass

    @abstractmethod
    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        status: Optional[str] = None,
    ) -> tuple[list[Usuario], int]:
        """Lista usuários com paginação."""
        pass

    @abstractmethod
    def save(self, usuario: Usuario) -> Usuario:
        """Salva usuário."""
        pass

    @abstractmethod
    def delete(self, usuario_id: str) -> bool:
        """Remove usuário (soft delete)."""
        pass

    @abstractmethod
    def exists_by_login(self, login: str) -> bool:
        """Verifica se login já existe."""
        pass

    @abstractmethod
    def exists_by_email(self, email: str) -> bool:
        """Verifica se email já existe."""
        pass


class RoleRepositoryInterface(ABC):
    """Interface para repositório de roles."""

    @abstractmethod
    def get_by_id(self, role_id: str) -> Optional[Role]:
        """Busca role por ID."""
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str) -> Optional[Role]:
        """Busca role por código."""
        pass

    @abstractmethod
    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
    ) -> tuple[list[Role], int]:
        """Lista roles com paginação."""
        pass

    @abstractmethod
    def save(self, role: Role) -> Role:
        """Salva role."""
        pass

    @abstractmethod
    def delete(self, role_id: str) -> bool:
        """Remove role (soft delete)."""
        pass

    @abstractmethod
    def exists_by_codigo(self, codigo: str) -> bool:
        """Verifica se código já existe."""
        pass


class PermissaoRepositoryInterface(ABC):
    """Interface para repositório de permissões."""

    @abstractmethod
    def get_by_id(self, permissao_id: str) -> Optional[Permissao]:
        """Busca permissão por ID."""
        pass

    @abstractmethod
    def get_by_codigo(self, codigo: str) -> Optional[Permissao]:
        """Busca permissão por código."""
        pass

    @abstractmethod
    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        modulo: Optional[str] = None,
    ) -> tuple[list[Permissao], int]:
        """Lista permissões com paginação."""
        pass

    @abstractmethod
    def save(self, permissao: Permissao) -> Permissao:
        """Salva permissão."""
        pass

    @abstractmethod
    def delete(self, permissao_id: str) -> bool:
        """Remove permissão (soft delete)."""
        pass

    @abstractmethod
    def exists_by_codigo(self, codigo: str) -> bool:
        """Verifica se código já existe."""
        pass


class SessaoRepositoryInterface(ABC):
    """Interface para repositório de sessões."""

    @abstractmethod
    def get_by_token(self, token: str) -> Optional[Sessao]:
        """Busca sessão por token."""
        pass

    @abstractmethod
    def get_by_usuario(self, usuario_id: str) -> list[Sessao]:
        """Busca sessões ativas do usuário."""
        pass

    @abstractmethod
    def save(self, sessao: Sessao) -> Sessao:
        """Salva sessão."""
        pass

    @abstractmethod
    def invalidate(self, token: str) -> bool:
        """Invalida sessão."""
        pass

    @abstractmethod
    def invalidate_all_for_usuario(self, usuario_id: str) -> int:
        """Invalida todas as sessões do usuário."""
        pass


class AuditoriaLoginRepositoryInterface(ABC):
    """Interface para repositório de auditoria de login."""

    @abstractmethod
    def save(self, auditoria: AuditoriaLogin) -> AuditoriaLogin:
        """Salva registro de auditoria."""
        pass

    @abstractmethod
    def get_by_usuario(
        self,
        usuario_id: str,
        page: int = 0,
        page_size: int = 50,
    ) -> tuple[list[AuditoriaLogin], int]:
        """Busca histórico de logins do usuário."""
        pass

    @abstractmethod
    def count_failed_recent(self, login: str, minutes: int = 30) -> int:
        """Conta falhas recentes de login."""
        pass


__all__ = [
    "UsuarioRepositoryInterface",
    "RoleRepositoryInterface",
    "PermissaoRepositoryInterface",
    "SessaoRepositoryInterface",
    "AuditoriaLoginRepositoryInterface",
]
