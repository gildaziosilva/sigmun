"""Entidade Bem — ativo patrimonial móvel ou imóvel (DOM-PAT).

RN-PAT-001: o tombo/código do bem é único no município.
RN-PAT-002: a depreciação é calculada pelo método linear
    (custo − residual) / vida útil.
RN-PAT-003: bens baixados não podem ser depreciados ou transferidos.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from uuid import uuid4


class TipoBem(Enum):
    """Classificação física do bem."""

    MOVEL = "movel"
    IMOVEL = "imovel"


class StatusBem(Enum):
    """Situação de uso do bem."""

    EM_USO = "em_uso"
    OCIOSO = "ocioso"
    EM_TRANSFERENCIA = "em_transferencia"
    BAIXADO = "baixado"


@dataclass
class Bem:
    """Ativo patrimonial do município."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    tipo: TipoBem = field(default=TipoBem.MOVEL)
    descricao: str = ""
    categoria: str = ""
    valor_aquisicao: float = 0.0
    data_aquisicao: date | None = None
    valor_residual: float = 0.0
    vida_util_anos: int = 0
    valor_contabil: float = 0.0
    status: StatusBem = field(default=StatusBem.EM_USO)
    localizacao: str = ""
    responsavel_id: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    def validar(self) -> None:
        """Valida regras estruturais do bem."""
        from ..exceptions import RegraNegocioError

        if not self.codigo:
            raise RegraNegocioError("Tombo/código do bem é obrigatório (RN-PAT-001)")
        if not self.descricao:
            raise RegraNegocioError("Descrição do bem é obrigatória")
        if self.valor_aquisicao <= 0:
            raise RegraNegocioError("Valor de aquisição deve ser maior que zero")

    def valor_depreciavel(self) -> float:
        """Montante sujeito à depreciação (custo − residual)."""
        return max(self.valor_aquisicao - self.valor_residual, 0.0)

    def depreciacao_anual(self) -> float:
        """Depreciação anual pelo método linear (RN-PAT-002)."""
        if self.vida_util_anos <= 0:
            return 0.0
        return round(self.valor_depreciavel() / self.vida_util_anos, 2)

    def depreciar(self, valor: float) -> None:
        """Aplica uma parcela de depreciação ao valor contábil."""
        from ..exceptions import BemBaixadoError, RegraNegocioError

        if self.status == StatusBem.BAIXADO:
            raise BemBaixadoError("Bem baixado não pode ser depreciado")
        if valor <= 0:
            raise RegraNegocioError("Valor de depreciação deve ser positivo")
        self.valor_contabil = round(max(self.valor_contabil - valor, 0.0), 2)
        self.updated_at = datetime.utcnow()

    def transferir(self, para_localizacao: str) -> None:
        """Inicia processo de transferência do bem."""
        from ..exceptions import BemBaixadoError, RegraNegocioError

        if self.status == StatusBem.BAIXADO:
            raise BemBaixadoError("Bem baixado não pode ser transferido")
        if not para_localizacao:
            raise RegraNegocioError("Localização de destino é obrigatória")
        self.status = StatusBem.EM_TRANSFERENCIA
        self.updated_at = datetime.utcnow()

    def confirmar_localizacao(self, localizacao: str) -> None:
        """Consolida a nova localização após transferência."""
        self.localizacao = localizacao
        self.status = StatusBem.EM_USO
        self.updated_at = datetime.utcnow()

    def baixar(self) -> None:
        """Baixa o bem (RN-PAT-003)."""
        from ..exceptions import BemBaixadoError

        if self.status == StatusBem.BAIXADO:
            raise BemBaixadoError("Bem já baixado")
        self.status = StatusBem.BAIXADO
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca o bem como excluído (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()


__all__ = ["TipoBem", "StatusBem", "Bem"]