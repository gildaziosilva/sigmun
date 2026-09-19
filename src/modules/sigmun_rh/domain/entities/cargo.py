"""Entidade Cargo — plano de cargos do município (DOM-PES).

RN-PES-001: código do cargo é único no município.
RN-PES-002: salário-base deve ser maior que zero.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class Cargo:
    """Cargo efetivo, comissionado ou temporário."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    nivel: str = "basico"
    salario_base: float = 0.0
    carga_horaria_semanal: int = 40
    ativo: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        """Indica se o cargo está ativo e não excluído."""
        return self.ativo and not self.is_deleted

    def desativar(self) -> None:
        """Desativa o cargo (impede novas admissões)."""
        self.ativo = False
        self.updated_at = datetime.utcnow()

    def reativar(self) -> None:
        """Reativa o cargo."""
        self.ativo = True
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca o cargo como excluído (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()


__all__ = ["Cargo"]
