"""Entidade ContaContabil — plano de contas PCASP (DOM-CON).

RN-CON-010: código da conta é único no plano vigente.
RN-CON-011: conta sintética não recebe lançamento (só analítica).
RN-CON-012: conta inativa não recebe lançamento.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class ContaContabil:
    """Conta do PCASP (classe até desdobramento analítico)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    classe: str = ""
    grupo: str = ""
    natureza_saldo: str = "devedora"
    tipo: str = "analitica"
    aceita_lancamento: bool = True
    ativa: bool = True
    conta_pai_id: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        """Indica se a conta está ativa e não excluída."""
        return self.ativa and not self.is_deleted

    def pode_receber_lancamento(self) -> bool:
        """Verifica se a conta aceita lançamento (RN-CON-011/012)."""
        return self.aceita_lancamento and self.tipo == "analitica" and self.is_active

    def desativar(self) -> None:
        """Desativa a conta (impede novos lançamentos)."""
        self.ativa = False
        self.updated_at = datetime.utcnow()

    def reativar(self) -> None:
        """Reativa a conta."""
        self.ativa = True
        self.updated_at = datetime.utcnow()


__all__ = ["ContaContabil"]
