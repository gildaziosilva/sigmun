"""Entidade PPA — Plano Plurianual (DOM-ORC).

RN-ORC-001: quadriênio (ano_inicial/ano_final) é único por município.
RN-ORC-002: PPA nasce em elaboração; só PPA publicado pode fundamentar LDO/LOA.
RN-ORC-003: PPA encerrado é terminal (imutável).

Máquina de estados:
    ELABORACAO → VIGENTE → ENCERRADO (+ CANCELADO a partir de ELABORACAO)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4

TRANSICOES_PPA: dict[str, set[str]] = {
    "elaboracao": {"vigente", "cancelado"},
    "vigente": {"encerrado"},
    "encerrado": set(),
    "cancelado": set(),
}

ESTADOS_TERMINAIS_PPA: set[str] = {"encerrado", "cancelado"}


class StatusPPA(Enum):
    """Estado do PPA no quadriênio."""

    ELABORACAO = "elaboracao"
    VIGENTE = "vigente"
    ENCERRADO = "encerrado"
    CANCELADO = "cancelado"


@dataclass
class PPA:
    """Plano Plurianual do município (diretrizes quadrienais)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    ano_inicial: int = 0
    ano_final: int = 0
    descricao: str = ""
    status: StatusPPA = field(default=StatusPPA.ELABORACAO)
    data_publicacao: datetime | None = None
    data_encerramento: datetime | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    updated_by: str = ""
    is_deleted: bool = False

    @property
    def quadrienio(self) -> str:
        """Quadriênio formatado como ``AAAA-AAAA``."""
        return f"{self.ano_inicial:04d}-{self.ano_final:04d}"

    @property
    def is_terminal(self) -> bool:
        """Indica se o PPA está em estado terminal."""
        return self.status.value in ESTADOS_TERMINAIS_PPA

    @property
    def is_active(self) -> bool:
        """Indica se o PPA não foi excluído."""
        return not self.is_deleted

    def _transicao_valida(self, novo: StatusPPA) -> None:
        from ...domain.exceptions import RegraNegocioError

        atual = self.status.value
        if novo.value not in TRANSICOES_PPA.get(atual, set()):
            raise RegraNegocioError(f"Transição inválida de PPA: {atual} → {novo.value}")

    def publicar(self) -> None:
        """Publica o PPA (ELABORACAO → VIGENTE)."""
        from ...domain.exceptions import RegraNegocioError

        if self.ano_final - self.ano_inicial != 3:
            raise RegraNegocioError("PPA deve cobrir um quadriênio (RN-ORC-001)")
        self._transicao_valida(StatusPPA.VIGENTE)
        self.status = StatusPPA.VIGENTE
        self.data_publicacao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def encerrar(self) -> None:
        """Encerra o PPA vigente."""
        self._transicao_valida(StatusPPA.ENCERRADO)
        self.status = StatusPPA.ENCERRADO
        self.data_encerramento = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def cancelar(self) -> None:
        """Cancela o PPA ainda em elaboração."""
        self._transicao_valida(StatusPPA.CANCELADO)
        self.status = StatusPPA.CANCELADO
        self.updated_at = datetime.utcnow()


__all__ = ["StatusPPA", "PPA", "TRANSICOES_PPA", "ESTADOS_TERMINAIS_PPA"]
