"""
Eventos de domínio do módulo de Identidade e Acesso.
"""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class EventoIdentidade:
    """Base para eventos de domínio."""

    event_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)
    aggregate_id: str = ""


@dataclass
class UsuarioCriadoEvent(EventoIdentidade):
    """Evento disparado quando um usuário é criado."""

    login: str = ""
    email: str = ""
    nome: str = ""


@dataclass
class UsuarioAtivadoEvent(EventoIdentidade):
    """Evento disparado quando um usuário é ativado."""

    pass


@dataclass
class UsuarioDesativadoEvent(EventoIdentidade):
    """Evento disparado quando um usuário é desativado."""

    motivo: str = ""


@dataclass
class UsuarioBloqueadoEvent(EventoIdentidade):
    """Evento disparado quando um usuário é bloqueado."""

    motivo: str = ""


@dataclass
class LoginRealizadoEvent(EventoIdentidade):
    """Evento disparado quando um login é realizado com sucesso."""

    ip_origem: str = ""
    user_agent: str = ""


@dataclass
class LoginFalhouEvent(EventoIdentidade):
    """Evento disparado quando um login falha."""

    login: str = ""
    motivo: str = ""
    ip_origem: str = ""


@dataclass
class LogoutRealizadoEvent(EventoIdentidade):
    """Evento disparado quando um logout é realizado."""

    pass


@dataclass
class PermissaoConcedidaEvent(EventoIdentidade):
    """Evento disparado quando uma permissão é concedida."""

    role_id: str = ""
    permissao_codigo: str = ""


@dataclass
class PermissaoRevogadaEvent(EventoIdentidade):
    """Evento disparado quando uma permissão é revogada."""

    role_id: str = ""
    permissao_codigo: str = ""


@dataclass
class RoleCriadaEvent(EventoIdentidade):
    """Evento disparado quando uma role é criada."""

    codigo: str = ""
    nome: str = ""


@dataclass
class RoleAtualizadaEvent(EventoIdentidade):
    """Evento disparado quando uma role é atualizada."""

    pass


@dataclass
class RoleRemovidaEvent(EventoIdentidade):
    """Evento disparado quando uma role é removida."""

    pass


@dataclass
class PermissaoCriadaEvent(EventoIdentidade):
    """Evento disparado quando uma permissão é criada."""

    codigo: str = ""
    nome: str = ""
    modulo: str = ""


@dataclass
class SenhaAlteradaEvent(EventoIdentidade):
    """Evento disparado quando uma senha é alterada."""

    pass


@dataclass
class SessaoCriadaEvent(EventoIdentidade):
    """Evento disparado quando uma sessão é criada."""

    token: str = ""
    expires_at: datetime | None = None


@dataclass
class SessaoInvalidadaEvent(EventoIdentidade):
    """Evento disparado quando uma sessão é invalidada."""

    motivo: str = ""


# Alias de compatibilidade.
DomainEvent = EventoIdentidade

__all__ = [
    "EventoIdentidade",
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
