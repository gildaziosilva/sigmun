"""Entidade Depreciacao — registro periódico de depreciação (DOM-PAT)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import uuid4


@dataclass
class Depreciacao:
    """Parcela de depreciação aplicada a um bem."""

    id: str = field(default_factory=lambda: str(uuid4()))
    bem_id: str = ""
    data: date | None = None
    valor_depreciado: float = 0.0
    valor_acumulado: float = 0.0
    valor_liquido: float = 0.0
    created_at: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""

    def validar(self) -> None:
        """Valida regras estruturais da depreciação."""
        from ..exceptions import RegraNegocioError

        if not self.bem_id:
            raise RegraNegocioError("Depreciação exige bem de origem")
        if self.valor_depreciado <= 0:
            raise RegraNegocioError("Valor depreciado deve ser positivo")


__all__ = ["Depreciacao"]