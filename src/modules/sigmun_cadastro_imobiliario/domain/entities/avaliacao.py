"""Avaliação de valor venal do imóvel do DOM-IMO.

RN-IMO-005: o valor venal é apurado a partir dos valores unitários vigentes da
    planta genérica de valores:
        valor_terreno   = area_terreno_m2   * valor_terreno_m2_unitario
        valor_construcao= area_construida_m2* valor_construcao_m2_unitario
        valor_venal     = valor_terreno + valor_construcao
A avaliação segue o ciclo RASCUNHO -> CONCLUIDA, com CANCELADA disponível
enquanto não concluída.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import uuid4

from .tipos import SituacaoAvaliacao


def _arredonda(valor: float) -> float:
    """Arredonda o valor monetário para duas casas decimais."""
    return round(valor + 0.0, 2)


@dataclass
class AvaliacaoImovel:
    """Avaliação do valor venal de um imóvel para um exercício."""

    id: str = field(default_factory=lambda: str(uuid4()))
    imovel_id: str = ""
    ano: int = 0
    valor_terreno_m2_unitario: float = 0.0
    valor_construcao_m2_unitario: float = 0.0
    aliquota_percent: float = 0.0
    area_terreno_m2: float = 0.0
    area_construida_m2: float = 0.0
    situacao: SituacaoAvaliacao = field(default=SituacaoAvaliacao.RASCUNHO)
    data_avaliacao: date = field(default_factory=date.today)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def valor_terreno(self) -> float:
        """Valor venal da parcela do terreno."""
        return _arredonda(self.area_terreno_m2 * self.valor_terreno_m2_unitario)

    @property
    def valor_construcao(self) -> float:
        """Valor venal da parcela construída."""
        return _arredonda(self.area_construida_m2 * self.valor_construcao_m2_unitario)

    @property
    def valor_venal(self) -> float:
        """Valor venal total do imóvel (RN-IMO-005)."""
        return _arredonda(self.valor_terreno + self.valor_construcao)

    @property
    def valor_lancamento(self) -> float:
        """Valor estimado de lançamento do tributo, pela alíquota da planta."""
        return _arredonda(self.valor_venal * self.aliquota_percent / 100.0)

    def concluir(self) -> None:
        """Conclui a avaliação."""
        from ..exceptions import RegraNegocioError

        if self.situacao != SituacaoAvaliacao.RASCUNHO:
            raise RegraNegocioError(
                "Somente avaliação em rascunho pode ser concluída (RN-IMO-005)"
            )
        self.situacao = SituacaoAvaliacao.CONCLUIDA
        self.updated_at = datetime.utcnow()

    def cancelar(self, motivo: str) -> None:
        """Cancela a avaliação ainda não concluída."""
        from ..exceptions import RegraNegocioError

        if self.situacao == SituacaoAvaliacao.CONCLUIDA:
            raise RegraNegocioError(
                "Avaliação já concluída não pode ser cancelada (RN-IMO-005)"
            )
        self.situacao = SituacaoAvaliacao.CANCELADA
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida as regras estruturais da avaliação (RN-IMO-005)."""
        from ..exceptions import RegraNegocioError

        if not self.imovel_id:
            raise RegraNegocioError("Avaliação exige imóvel vinculado (RN-IMO-005)")
        if not 1900 <= self.ano <= 2200:
            raise RegraNegocioError("Ano da avaliação inválido")
        if self.valor_terreno_m2_unitario < 0 or self.valor_construcao_m2_unitario < 0:
            raise RegraNegocioError("Valores unitários não podem ser negativos")
        if not 0 <= self.aliquota_percent <= 100:
            raise RegraNegocioError("Alíquota deve estar entre 0 e 100")
        if self.area_terreno_m2 < 0 or self.area_construida_m2 < 0:
            raise RegraNegocioError("Áreas do imóvel não podem ser negativas")


__all__ = ["AvaliacaoImovel"]
