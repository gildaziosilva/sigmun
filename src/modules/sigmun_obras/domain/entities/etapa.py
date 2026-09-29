"""Etapa física da obra no DOM-OBR — Obras e Infraestrutura.

RN-OBR-007: a etapa pertence a uma obra, exige responsável, e obedece ao ciclo
    PENDENTE -> EM_EXECUCAO -> CONCLUIDA, com ATRASADA e CANCELADA disponíveis.

`percentual_previsto` e o peso da etapa no conjunto da obra (as etapas de uma
obra somam 100%); `percentual_realizado` e a conclusao da propria etapa. Sao
escalas distintas: uma etapa de peso 40% pode estar 100% concluida. Ambas sao
validadas na faixa 0..100.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import uuid4

from .tipos import SituacaoEtapa, TipoEtapa, validar_percentual


@dataclass
class EtapaObra:
    """Etapa de execução fisicamente verificável de uma obra."""

    id: str = field(default_factory=lambda: str(uuid4()))
    obra_id: str = ""
    numero: str = ""
    descricao: str = ""
    tipo: TipoEtapa = field(default=TipoEtapa.ESTRUTURA)
    situacao: SituacaoEtapa = field(default=SituacaoEtapa.PENDENTE)
    percentual_previsto: float = 0.0
    percentual_realizado: float = 0.0
    data_inicio_prevista: date | None = None
    data_fim_prevista: date | None = None
    data_conclusao: date | None = None
    responsavel: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    def iniciar(self) -> None:
        """Inicia a execução da etapa (RN-OBR-007)."""
        from ..exceptions import RegraNegocioError

        if self.situacao == SituacaoEtapa.CONCLUIDA:
            raise RegraNegocioError("Etapa concluída não pode ser reiniciada (RN-OBR-007)")
        if self.situacao == SituacaoEtapa.CANCELADA:
            raise RegraNegocioError("Etapa cancelada não pode ser iniciada (RN-OBR-007)")
        self.situacao = SituacaoEtapa.EM_EXECUCAO
        self.updated_at = datetime.utcnow()

    def concluir(self, data: date | None = None) -> None:
        """Conclui a etapa, exigindo 100% do previsto (RN-OBR-007)."""
        from ..exceptions import RegraNegocioError

        if self.situacao == SituacaoEtapa.CONCLUIDA:
            raise RegraNegocioError("Etapa já está concluída (RN-OBR-007)")
        if self.percentual_realizado < 100.0:
            raise RegraNegocioError(
                "Etapa só pode ser concluída com 100% do percentual previsto "
                "realizado (RN-OBR-007)"
            )
        self.situacao = SituacaoEtapa.CONCLUIDA
        self.data_conclusao = data or date.today()
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca a etapa como excluída (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida as regras estruturais da etapa (RN-OBR-007)."""
        from ..exceptions import RegraNegocioError

        if not self.obra_id:
            raise RegraNegocioError("Obra é obrigatória na etapa (RN-OBR-007)")
        if not self.descricao:
            raise RegraNegocioError("Descrição da etapa é obrigatória (RN-OBR-007)")
        if not self.responsavel:
            raise RegraNegocioError("Responsável pela etapa é obrigatório (RN-OBR-007)")
        validar_percentual(self.percentual_previsto, "Percentual previsto da etapa")
        validar_percentual(self.percentual_realizado, "Percentual realizado da etapa")
        # `percentual_previsto` (peso da etapa na obra) e `percentual_realizado`
        # (conclusao da etapa) sao escalas distintas: uma etapa de peso 40% pode
        # estar 100% concluida. Ambas sao validadas apenas na faixa 0..100.


__all__ = ["EtapaObra"]
