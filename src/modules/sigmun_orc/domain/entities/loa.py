"""Entidade LOA — Lei Orçamentária Anual (DOM-ORC).

RN-ORC-020: exercício é único no município.
RN-ORC-021: LOA exige LDO sancionada do mesmo exercício.
RN-ORC-022: LOA publicada é terminal para edição (apenas suplementação via dotação).

Máquina de estados:
    ELABORACAO → APROVADA → PUBLICADA (+ CANCELADA a partir de ELABORACAO)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4

TRANSICOES_LOA: dict[str, set[str]] = {
    "elaboracao": {"aprovada", "cancelada"},
    "aprovada": {"publicada"},
    "publicada": set(),
    "cancelada": set(),
}

ESTADOS_TERMINAIS_LOA: set[str] = {"publicada", "cancelada"}


class StatusLOA(Enum):
    """Estado da LOA no exercício."""

    ELABORACAO = "elaboracao"
    APROVADA = "aprovada"
    PUBLICADA = "publicada"
    CANCELADA = "cancelada"


@dataclass
class LOA:
    """Lei Orçamentária Anual de um exercício."""

    id: str = field(default_factory=lambda: str(uuid4()))
    exercicio: int = 0
    ldo_id: str = ""
    descricao: str = ""
    status: StatusLOA = field(default=StatusLOA.ELABORACAO)
    valor_receita_prevista: float = 0.0
    valor_despesa_fixada: float = 0.0
    data_aprovacao: datetime | None = None
    data_publicacao: datetime | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    updated_by: str = ""
    is_deleted: bool = False

    @property
    def is_terminal(self) -> bool:
        """Indica se a LOA está em estado terminal."""
        return self.status.value in ESTADOS_TERMINAIS_LOA

    @property
    def is_active(self) -> bool:
        """Indica se a LOA não foi excluída."""
        return not self.is_deleted

    def _transicao_valida(self, novo: StatusLOA) -> None:
        from ...domain.exceptions import RegraNegocioError

        atual = self.status.value
        if novo.value not in TRANSICOES_LOA.get(atual, set()):
            raise RegraNegocioError(f"Transição inválida de LOA: {atual} → {novo.value}")

    def aprovar(self) -> None:
        """Aprova a LOA (ELABORACAO → APROVADA)."""
        from ...domain.exceptions import RegraNegocioError

        if self.valor_despesa_fixada > self.valor_receita_prevista:
            raise RegraNegocioError(
                "Despesa fixada não pode exceder receita prevista (RN-ORC-022)"
            )
        self._transicao_valida(StatusLOA.APROVADA)
        self.status = StatusLOA.APROVADA
        self.data_aprovacao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def publicar(self) -> None:
        """Publica a LOA aprovada."""
        self._transicao_valida(StatusLOA.PUBLICADA)
        self.status = StatusLOA.PUBLICADA
        self.data_publicacao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def cancelar(self) -> None:
        """Cancela a LOA ainda em elaboração."""
        self._transicao_valida(StatusLOA.CANCELADA)
        self.status = StatusLOA.CANCELADA
        self.updated_at = datetime.utcnow()


__all__ = ["StatusLOA", "LOA", "TRANSICOES_LOA", "ESTADOS_TERMINAIS_LOA"]
