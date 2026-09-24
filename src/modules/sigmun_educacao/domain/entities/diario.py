"""Entidade LancamentoDiário — diário de classe digital (DOM-EDU).

RN-EDU-020: o lançamento exige matrícula ativa vinculada; a nota, quando
informada, está na escala 0 a 10; ``presente`` registra a frequência do dia.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import uuid4


@dataclass
class LancamentoDiario:
    """Registro de frequência e/ou nota no diário de classe digital."""

    id: str = field(default_factory=lambda: str(uuid4()))
    matricula_id: str = ""
    data: date | None = None
    presente: bool = True
    nota: float | None = None
    observacao: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""

    def validar(self) -> None:
        """Valida regras estruturais do lançamento."""
        from ..exceptions import RegraNegocioError

        if not self.matricula_id:
            raise RegraNegocioError(
                "Lançamento no diário exige matrícula vinculada (RN-EDU-020)"
            )
        if self.nota is not None and not (0.0 <= self.nota <= 10.0):
            raise RegraNegocioError(
                f"Nota fora da escala 0-10: {self.nota} (RN-EDU-020)"
            )


__all__ = ["LancamentoDiario"]
