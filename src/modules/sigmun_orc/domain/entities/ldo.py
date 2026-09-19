"""Entidade LDO — Lei de Diretrizes Orçamentárias (DOM-ORC).

RN-ORC-010: exercício é único no município.
RN-ORC-011: LDO exige PPA vigente que cubra o exercício.
RN-ORC-012: LDO sancionada é terminal (imutável).

Máquina de estados:
    ELABORACAO → APROVADA → SANCIONADA (+ CANCELADA a partir de ELABORACAO)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4

TRANSICOES_LDO: dict[str, set[str]] = {
    "elaboracao": {"aprovada", "cancelada"},
    "aprovada": {"sancionada"},
    "sancionada": set(),
    "cancelada": set(),
}

ESTADOS_TERMINAIS_LDO: set[str] = {"sancionada", "cancelada"}


class StatusLDO(Enum):
    """Estado da LDO no exercício."""

    ELABORACAO = "elaboracao"
    APROVADA = "aprovada"
    SANCIONADA = "sancionada"
    CANCELADA = "cancelada"


@dataclass
class LDO:
    """Lei de Diretrizes Orçamentárias de um exercício."""

    id: str = field(default_factory=lambda: str(uuid4()))
    exercicio: int = 0
    ppa_id: str = ""
    descricao: str = ""
    status: StatusLDO = field(default=StatusLDO.ELABORACAO)
    meta_fiscal_receita: float = 0.0
    meta_fiscal_despesa: float = 0.0
    data_aprovacao: datetime | None = None
    data_sancao: datetime | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    updated_by: str = ""
    is_deleted: bool = False

    @property
    def is_terminal(self) -> bool:
        """Indica se a LDO está em estado terminal."""
        return self.status.value in ESTADOS_TERMINAIS_LDO

    @property
    def is_active(self) -> bool:
        """Indica se a LDO não foi excluída."""
        return not self.is_deleted

    def _transicao_valida(self, novo: StatusLDO) -> None:
        from ...domain.exceptions import RegraNegocioError

        atual = self.status.value
        if novo.value not in TRANSICOES_LDO.get(atual, set()):
            raise RegraNegocioError(f"Transição inválida de LDO: {atual} → {novo.value}")

    def aprovar(self) -> None:
        """Aprova a LDO (ELABORACAO → APROVADA)."""
        self._transicao_valida(StatusLDO.APROVADA)
        self.status = StatusLDO.APROVADA
        self.data_aprovacao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def sancionar(self) -> None:
        """Sanciona a LDO aprovada (RN-ORC-012)."""
        self._transicao_valida(StatusLDO.SANCIONADA)
        self.status = StatusLDO.SANCIONADA
        self.data_sancao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def cancelar(self) -> None:
        """Cancela a LDO ainda em elaboração."""
        self._transicao_valida(StatusLDO.CANCELADA)
        self.status = StatusLDO.CANCELADA
        self.updated_at = datetime.utcnow()


__all__ = ["StatusLDO", "LDO", "TRANSICOES_LDO", "ESTADOS_TERMINAIS_LDO"]
