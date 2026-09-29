"""Vistoria fiscalizadora da obra no DOM-OBR — Obras e Infraestrutura.

RN-OBR-008: a vistoria pertence a uma obra, exige fiscal e data, e registra o
    parecer sobre o avanço físico verificado em campo.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import uuid4

from .tipos import ParecerVistoria, TipoVistoria, validar_percentual


@dataclass
class VistoriaObra:
    """Vistoria técnica de avanço físico realizada na obra."""

    id: str = field(default_factory=lambda: str(uuid4()))
    obra_id: str = ""
    data: date = field(default_factory=date.today)
    tipo: TipoVistoria = field(default=TipoVistoria.PERIODICA)
    parecer: ParecerVistoria = field(default=ParecerVistoria.APROVADO)
    percentual_fisico_verificado: float = 0.0
    fiscal: str = ""
    observacao: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""
    is_deleted: bool = False

    @property
    def aprovada(self) -> bool:
        """Indica se a vistoria foi aprovada (total ou com ressalvas)."""
        return self.parecer in (ParecerVistoria.APROVADO, ParecerVistoria.APROVADO_COM_RESSALVAS)

    def excluir(self) -> None:
        """Marca a vistoria como excluída (soft-delete)."""
        self.is_deleted = True

    def validar(self) -> None:
        """Valida as regras estruturais da vistoria (RN-OBR-008)."""
        from ..exceptions import RegraNegocioError

        if not self.obra_id:
            raise RegraNegocioError("Obra é obrigatória na vistoria (RN-OBR-008)")
        if not self.fiscal:
            raise RegraNegocioError("Fiscal responsável é obrigatório na vistoria (RN-OBR-008)")
        validar_percentual(
            self.percentual_fisico_verificado, "Percentual físico verificado na vistoria"
        )


__all__ = ["VistoriaObra"]
