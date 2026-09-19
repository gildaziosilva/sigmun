"""Entidade Lotacao — vínculo servidor × unidade administrativa (DOM-PES).

RN-PES-020: servidor só pode ter uma lotação vigente por período
    (sem sobreposição de datas).
RN-PES-021: lotação exige unidade de destino e data de início.
RN-PES-022: remoção encerra a lotação vigente (data_fim = data da remoção).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import uuid4


@dataclass
class Lotacao:
    """Lotação de um servidor em uma unidade administrativa."""

    id: str = field(default_factory=lambda: str(uuid4()))
    servidor_id: str = ""
    unidade_id: str = ""
    cargo_id: str = ""
    data_inicio: date | None = None
    data_fim: date | None = None
    vigente: bool = True
    motivo: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        """Indica se a lotação está vigente e não excluída."""
        return self.vigente and not self.is_deleted

    def encerrar(self, data_fim: date | None = None, motivo: str = "") -> None:
        """Encerra a lotação vigente (remoção/transferência)."""
        from ...domain.exceptions import RegraNegocioError

        if not self.vigente:
            raise RegraNegocioError("Lotação já encerrada")
        fim = data_fim or date.today()
        if self.data_inicio and fim < self.data_inicio:
            raise RegraNegocioError(
                "Data de encerramento anterior ao início (RN-PES-020)"
            )
        self.data_fim = fim
        self.vigente = False
        if motivo:
            self.motivo = motivo
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca a lotação como excluída (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()


__all__ = ["Lotacao"]
