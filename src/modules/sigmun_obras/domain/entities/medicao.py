"""Medição físico-financeira da obra no DOM-OBR — Obras e Infraestrutura.

RN-OBR-005: a medição exige percentual físico entre 0 e 100, valor medido não
    negativo e obedec ao ciclo
    REGISTRADA -> CONFERIDA -> APROVADA, com GLOSADA e CANCELADA disponíveis;
    apenas medição APROVADA compõe o avanço da obra.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import uuid4

from .tipos import (
    SituacaoMedicao,
    TipoMedicao,
    validar_percentual,
    validar_valor,
)


@dataclass
class MedicaoObra:
    """Medição de avanço físico-financeiro de uma obra pública."""

    id: str = field(default_factory=lambda: str(uuid4()))
    obra_id: str = ""
    numero: str = ""
    tipo: TipoMedicao = field(default=TipoMedicao.AVANCO)
    situacao: SituacaoMedicao = field(default=SituacaoMedicao.REGISTRADA)
    data: date = field(default_factory=date.today)
    percentual_fisico: float = 0.0
    valor_medido: float = 0.0
    responsavel_tecnico: str = ""
    observacao: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def aprovada(self) -> bool:
        """Indica se a medição compõe o avanço da obra (RN-OBR-005)."""
        return self.situacao == SituacaoMedicao.APROVADA

    def conferir(self, autor_id: str = "") -> None:
        """Conferir a medição pelo fiscal responsável (RN-OBR-005)."""
        from ..exceptions import RegraNegocioError

        if self.situacao != SituacaoMedicao.REGISTRADA:
            raise RegraNegocioError("Somente medição registrada pode ser conferida (RN-OBR-005)")
        self.situacao = SituacaoMedicao.CONFERIDA
        self.updated_at = datetime.utcnow()

    def aprovar(self, autor_id: str = "") -> None:
        """Aprova a medição, permitindo compor o avanço (RN-OBR-005)."""
        from ..exceptions import RegraNegocioError

        if self.situacao != SituacaoMedicao.CONFERIDA:
            raise RegraNegocioError(
                "Somente medição conferida pode ser aprovada (RN-OBR-005)"
            )
        self.situacao = SituacaoMedicao.APROVADA
        self.updated_at = datetime.utcnow()

    def glosar(self, motivo: str) -> None:
        """Glosa (recusa parcial/total) a medição conferida (RN-OBR-005)."""
        from ..exceptions import RegraNegocioError

        if self.situacao != SituacaoMedicao.CONFERIDA:
            raise RegraNegocioError("Somente medição conferida pode ser glosada (RN-OBR-005)")
        self.situacao = SituacaoMedicao.GLOSADA
        if motivo:
            self.observacao = motivo
        self.updated_at = datetime.utcnow()

    def cancelar(self, motivo: str = "") -> None:
        """Cancela a medição (RN-OBR-005)."""
        from ..exceptions import RegraNegocioError

        if self.situacao == SituacaoMedicao.APROVADA:
            raise RegraNegocioError(
                "Medição aprovada não pode ser cancelada; registre a glosa (RN-OBR-005)"
            )
        if self.situacao == SituacaoMedicao.CANCELADA:
            raise RegraNegocioError("Medição já está cancelada (RN-OBR-005)")
        self.situacao = SituacaoMedicao.CANCELADA
        if motivo:
            self.observacao = motivo
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca a medição como excluída (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida as regras estruturais da medição (RN-OBR-005)."""
        from ..exceptions import RegraNegocioError

        if not self.obra_id:
            raise RegraNegocioError("Obra é obrigatória na medição (RN-OBR-005)")
        if not self.numero:
            raise RegraNegocioError("Número da medição é obrigatório (RN-OBR-005)")
        if not self.responsavel_tecnico:
            raise RegraNegocioError(
                "Responsável técnico é obrigatório na medição (RN-OBR-005)"
            )
        validar_percentual(self.percentual_fisico, "Percentual físico da medição")
        validar_valor(self.valor_medido, "Valor medido")


__all__ = ["MedicaoObra"]
