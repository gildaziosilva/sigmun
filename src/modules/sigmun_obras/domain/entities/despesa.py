"""Despesa financeira da obra no DOM-OBR — Obras e Infraestrutura.

RN-OBR-006: a despesa pertence a uma obra, exige valor positivo e não pode
    superar o valor já medido da obra: não se paga o que não foi medido.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import uuid4

from .tipos import TipoDespesa, validar_valor


@dataclass
class DespesaObra:
    """Desembolso financeiro vinculado a uma obra pública."""

    id: str = field(default_factory=lambda: str(uuid4()))
    obra_id: str = ""
    medicao_id: str = ""
    descricao: str = ""
    tipo: TipoDespesa = field(default=TipoDespesa.MEDICAO)
    valor: float = 0.0
    data: date = field(default_factory=date.today)
    documento: str = ""
    credor: str = ""
    observacao: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""
    is_deleted: bool = False

    def excluir(self) -> None:
        """Marca a despesa como excluída (soft-delete)."""
        self.is_deleted = True

    def validar(self) -> None:
        """Valida as regras estruturais da despesa (RN-OBR-006)."""
        from ..exceptions import RegraNegocioError

        if not self.obra_id:
            raise RegraNegocioError("Obra é obrigatória na despesa (RN-OBR-006)")
        if not self.descricao:
            raise RegraNegocioError("Descrição da despesa é obrigatória (RN-OBR-006)")
        validar_valor(self.valor, "Valor da despesa")
        if self.valor <= 0:
            raise RegraNegocioError("Valor da despesa deve ser maior que zero (RN-OBR-006)")


__all__ = ["DespesaObra"]
