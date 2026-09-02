"""
Eventos de domínio do módulo de Identidade e Acesso.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import uuid4


@dataclass
class DomainEvent:
    """Base para eventos de domínio."""
    event_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)
    aggregate_id: str = ""


@dataclass
class UsuarioCriadoEvent(DomainEvent):
    """Evento disparado quando um usuário é criado."""
    login: str = ""
    email: str = ""
    nome: str = ""


@dataclass
class UsuarioAtivadoEvent(DomainEvent):
    """Evento disparado quando um usuário é ativado."""
    pass


@dataclass
class UsuarioDesativadoEvent(DomainEvent):
    """Evento disparado quando um usuário é desativado."""
    motivo: str = ""


@dataclass
class UsuarioBloqueadoEvent(DomainEvent):
    """Evento disparado quando um usuário é bloqueado."""
    motivo: str = ""


@dataclass
class LoginRealizadoEvent(DomainEvent):
    """Evento disparado quando um login é realizado com sucesso."""
    ip_origem: str = ""
    user_agent: str = ""


@dataclass
class LoginFalhouEvent(DomainEvent):
    """Evento disparado quando um login falha."""
    login: str = ""
    motivo: str = ""
    ip_origem: str = ""


@dataclass
class LogoutRealizadoEvent(DomainEvent):
    """Evento disparado quando um logout é realizado."""
    pass


@dataclass
class PermissaoConcedidaEvent(DomainEvent):
    """Evento disparado quando uma permissão é concedida."""
    role_id: str = ""
    permissao_codigo: str = ""


@dataclass
class PermissaoRevogadaEvent(DomainEvent):
    """Evento disparado quando uma permissão é revogada."""
    role_id: str = ""
    permissao_codigo: str = ""


@dataclass
class RoleCriadaEvent(DomainEvent):
    """Evento disparado quando uma role é criada."""
    codigo: str = ""
    nome: str = ""


@dataclass
class RoleAtualizadaEvent(DomainEvent):
    """Evento disparado quando uma role é atualizada."""
    pass


@dataclass
class RoleRemovidaEvent(DomainEvent):
    """Evento disparado quando uma role é removida."""
    pass


@dataclass
class PermissaoCriadaEvent(DomainEvent):
    """Evento disparado quando uma permissão é criada."""
    codigo: str = ""
    nome: str = ""
    modulo: str = ""


@dataclass
class SenhaAlteradaEvent(DomainEvent):
    """Evento disparado quando uma senha é alterada."""
    pass


@dataclass
class SessaoCriadaEvent(DomainEvent):
    """Evento disparado quando uma sessão é criada."""
    token: str = ""
    expires_at: Optional[datetime] = None


@dataclass
class SessaoInvalidadaEvent(DomainEvent):
    """Evento disparado quando uma sessão é invalidada."""
    motivo: str = ""


__all__ = [
    "DomainEvent",
    "UsuarioCriadoEvent",
    "UsuarioAtivadoEvent",
    "UsuarioDesativadoEvent",
    "UsuarioBloqueadoEvent",
    "LoginRealizadoEvent",
    "LoginFalhouEvent",
    "LogoutRealizadoEvent",
    "PermissaoConcedidaEvent",
    "PermissaoRevogadaEvent",
    "RoleCriadaEvent",
    "RoleAtualizadaEvent",
    "RoleRemovidaEvent",
    "PermissaoCriadaEvent",
    "SenhaAlteradaEvent",
    "SessaoCriadaEvent",
    "SessaoInvalidadaEvent",
]
