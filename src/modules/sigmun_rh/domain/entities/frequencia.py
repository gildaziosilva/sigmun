"""Entidade Frequencia — apontamento diário de presença (DOM-PES).

RN-PES-050: um registro por servidor/dia (unicidade servidor + data).
RN-PES-051: atraso superior a 60 minutos conta como meio período.
RN-PES-052: falta injustificada gera desconto em folha (integração DOM-PES→folha).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, time
from enum import Enum
from uuid import uuid4


class TipoFrequencia(Enum):
    """Tipo de apontamento de frequência."""

    PRESENCA = "presenca"
    FALTA = "falta"
    FALTA_JUSTIFICADA = "falta_justificada"
    LICENCA = "licenca"
    FERIAS = "ferias"
    AFASTAMENTO = "afastamento"


@dataclass
class Frequencia:
    """Registro diário de frequência do servidor."""

    id: str = field(default_factory=lambda: str(uuid4()))
    servidor_id: str = ""
    data: date | None = None
    tipo: TipoFrequencia = field(default=TipoFrequencia.PRESENCA)
    hora_entrada: time | None = None
    hora_saida: time | None = None
    minutos_atraso: int = 0
    justificativa: str = ""
    desconto_folha: bool = False
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        """Indica se o registro não foi excluído."""
        return not self.is_deleted

    @property
    def meio_periodo(self) -> bool:
        """Atraso > 60 min conta como meio período (RN-PES-051)."""
        return self.minutos_atraso > 60

    def justificar(self, justificativa: str) -> None:
        """Justifica uma falta (FALTA → FALTA_JUSTIFICADA)."""
        from ...domain.exceptions import RegraNegocioError

        if self.tipo != TipoFrequencia.FALTA:
            raise RegraNegocioError(
                f"Apenas faltas podem ser justificadas (atual: {self.tipo.value})"
            )
        if not justificativa:
            raise RegraNegocioError("Justificativa é obrigatória")
        self.tipo = TipoFrequencia.FALTA_JUSTIFICADA
        self.justificativa = justificativa
        self.desconto_folha = False
        self.updated_at = datetime.utcnow()

    def marcar_desconto(self) -> None:
        """Marca falta injustificada para desconto em folha."""
        self.desconto_folha = True
        self.updated_at = datetime.utcnow()


__all__ = ["TipoFrequencia", "Frequencia"]
