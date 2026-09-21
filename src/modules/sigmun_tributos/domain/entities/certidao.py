"""Entidade Certidao — certidões fiscais municipais (DOM-TRI).

RN-TRI-040: a certidão negativa é emitida somente quando o contribuinte não
    possui débitos vencidos (lançados ou inscritos em dívida ativa).
RN-TRI-041: a certidão positiva com efeitos de negativa cobre as demais
    situações mapeadas pela legislação municipal.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from uuid import uuid4


class TipoCertidao(Enum):
    """Classificação da certidão fiscal."""

    NEGATIVA = "negativa"
    POSITIVA = "positiva"
    POSITIVA_NEGATIVA = "positiva_negativa"


class StatusCertidao(Enum):
    """Situação do documento emitido."""

    EMITIDA = "emitida"
    CANCELADA = "cancelada"


@dataclass
class Certidao:
    """Documento de regularidade fiscal emitido ao contribuinte."""

    id: str = field(default_factory=lambda: str(uuid4()))
    contribuinte_id: str = ""
    tipo: TipoCertidao = field(default=TipoCertidao.NEGATIVA)
    numero: str = ""
    data_emissao: date | None = None
    valido_ate: date | None = None
    observacao: str = ""
    status: StatusCertidao = field(default=StatusCertidao.EMITIDA)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    def validar(self) -> None:
        """Valida regras estruturais da certidão."""
        from ..exceptions import RegraNegocioError

        if not self.contribuinte_id:
            raise RegraNegocioError("Certidão exige contribuinte (RN-TRI-040)")
        if not self.numero:
            raise RegraNegocioError("Número da certidão é obrigatório")

    def cancelar(self) -> None:
        """Cancela a certidão emitida."""
        from ..exceptions import RegraNegocioError

        if self.status != StatusCertidao.EMITIDA:
            raise RegraNegocioError("Apenas certidões emitidas podem ser canceladas")
        self.status = StatusCertidao.CANCELADA
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca a certidão como excluída (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()


__all__ = ["TipoCertidao", "StatusCertidao", "Certidao"]