"""Entidade Transferencia — movimentação interna de bens (DOM-PAT).

RN-PAT-010: uma transferência registra a movimentação entre localizações
    e/ou responsáveis, sem alterar a propriedade do ente.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from uuid import uuid4


class StatusTransferencia(Enum):
    """Situação da transferência."""

    PENDENTE = "pendente"
    CONCLUIDA = "concluida"
    CANCELADA = "cancelada"


@dataclass
class Transferencia:
    """Registro de movimentação de um bem."""

    id: str = field(default_factory=lambda: str(uuid4()))
    bem_id: str = ""
    de_localizacao: str = ""
    para_localizacao: str = ""
    de_responsavel_id: str = ""
    para_responsavel_id: str = ""
    data_transferencia: date | None = None
    motivo: str = ""
    status: StatusTransferencia = field(default=StatusTransferencia.PENDENTE)
    created_at: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""

    def validar(self) -> None:
        """Valida regras estruturais da transferência."""
        from ..exceptions import RegraNegocioError

        if not self.bem_id:
            raise RegraNegocioError("Transferência exige bem (RN-PAT-010)")
        if not self.para_localizacao:
            raise RegraNegocioError("Localização de destino é obrigatória")

    def concluir(self) -> None:
        """Consolida a transferência."""
        from ..exceptions import RegraNegocioError

        if self.status != StatusTransferencia.PENDENTE:
            raise RegraNegocioError("Apenas transferências pendentes podem ser concluídas")
        self.status = StatusTransferencia.CONCLUIDA

    def cancelar(self) -> None:
        """Cancela a transferência."""
        from ..exceptions import RegraNegocioError

        if self.status != StatusTransferencia.PENDENTE:
            raise RegraNegocioError("Apenas transferências pendentes podem ser canceladas")
        self.status = StatusTransferencia.CANCELADA


__all__ = ["StatusTransferencia", "Transferencia"]