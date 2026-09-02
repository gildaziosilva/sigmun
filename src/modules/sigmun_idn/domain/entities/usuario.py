"""
Entidades do domínio de Identidade e Acesso.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import uuid4


class UsuarioStatus(Enum):
    """Status do usuário."""
    ATIVO = "ativo"
    INATIVO = "inativo"
    BLOQUEADO = "bloqueado"
    PENDENTE = "pendente"


class PermissaoEscopo(Enum):
    """Escopo da permissão."""
    GLOBAL = "global"
    DOMINIO = "dominio"
    UNIDADE = "unidade"
    PROPRIO = "proprio"


@dataclass
class Usuario:
    """Entidade de Usuário."""
    id: str = field(default_factory=lambda: str(uuid4()))
    login: str = ""
    email: str = ""
    nome: str = ""
    status: UsuarioStatus = UsuarioStatus.PENDENTE
    senha_hash: str = ""
    unidades_ids: list[str] = field(default_factory=list)
    roles_ids: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    last_login: Optional[datetime] = None
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return self.status == UsuarioStatus.ATIVO

    @property
    def is_blocked(self) -> bool:
        return self.status == UsuarioStatus.BLOQUEADO

    def activate(self):
        """Ativa o usuário."""
        self.status = UsuarioStatus.ATIVO
        self.updated_at = datetime.utcnow()

    def deactivate(self):
        """Desativa o usuário."""
        self.status = UsuarioStatus.INATIVO
        self.updated_at = datetime.utcnow()

    def block(self):
        """Bloqueia o usuário."""
        self.status = UsuarioStatus.BLOQUEADO
        self.updated_at = datetime.utcnow()

    def update_last_login(self):
        """Atualiza timestamp do último login."""
        self.last_login = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def has_role(self, role_id: str) -> bool:
        """Verifica se usuário possui role."""
        return role_id in self.roles_ids

    def has_permission(self, permission_code: str, roles: list["Role"]) -> bool:
        """Verifica se usuário possui permissão através de suas roles."""
        user_roles = [r for r in roles if r.id in self.roles_ids and not r.is_deleted]
        for role in user_roles:
            if any(p.codigo == permission_code for p in role.permissoes):
                return True
        return False


@dataclass
class Role:
    """Entidade de Role (Papel)."""
    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    permissoes: list["Permissao"] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return not self.is_deleted

    def add_permission(self, permissao: "Permissao"):
        """Adiciona permissão à role."""
        if permissao.id not in [p.id for p in self.permissoes]:
            self.permissoes.append(permissao)
            self.updated_at = datetime.utcnow()

    def remove_permission(self, permissao_id: str):
        """Remove permissão da role."""
        self.permissoes = [p for p in self.permissoes if p.id != permissao_id]
        self.updated_at = datetime.utcnow()

    def has_permission(self, permission_code: str) -> bool:
        """Verifica se role possui permissão."""
        return any(p.codigo == permission_code for p in self.permissoes)


@dataclass
class Permissao:
    """Entidade de Permissão."""
    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    escopo: PermissaoEscopo = PermissaoEscopo.DOMINIO
    modulo: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return not self.is_deleted


@dataclass
class Sessao:
    """Entidade de Sessão."""
    id: str = field(default_factory=lambda: str(uuid4()))
    usuario_id: str = ""
    token: str = ""
    ip_origem: str = ""
    user_agent: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    expires_at: Optional[datetime] = None
    is_active: bool = True

    @property
    def is_expired(self) -> bool:
        if self.expires_at is None:
            return False
        return datetime.utcnow() > self.expires_at

    def invalidate(self):
        """Invalida a sessão."""
        self.is_active = False


@dataclass
class AuditoriaLogin:
    """Entidade de auditoria de login."""
    id: str = field(default_factory=lambda: str(uuid4()))
    usuario_id: str = ""
    login: str = ""
    ip_origem: str = ""
    user_agent: str = ""
    sucesso: bool = False
    motivo_falha: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)


__all__ = [
    "Usuario",
    "UsuarioStatus",
    "Role",
    "Permissao",
    "PermissaoEscopo",
    "Sessao",
    "AuditoriaLogin",
]
