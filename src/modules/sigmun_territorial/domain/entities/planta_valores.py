"""Planta genérica de valores do DOM-TEL.

RN-TEL-003: existe no máximo uma planta genérica de valores vigente por
    combinação de ano, bairro e tipo de ocupação.
RN-TEL-004: a planta obedece ao ciclo RASCUNHO -> VIGENTE -> REVOGADA, sem
    retorno a partir de REVOGADA.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from .tipos import SituacaoPlantaValores, TipoOcupacaoImovel


@dataclass
class PlantaGenericaValores:
    """Valores unitários de referência por ano, bairro e ocupação (RN-TEL-003/004)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    ano: int = 0
    bairro_id: str = ""
    ocupacao: TipoOcupacaoImovel = field(default=TipoOcupacaoImovel.RESIDENCIAL)
    valor_terreno_m2: float = 0.0
    valor_construcao_m2: float = 0.0
    aliquota_percent: float = 0.0
    situacao: SituacaoPlantaValores = field(default=SituacaoPlantaValores.RASCUNHO)
    legislacao: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def esta_vigente(self) -> bool:
        """Indica se a planta genérica de valores está vigente."""
        return self.situacao == SituacaoPlantaValores.VIGENTE and not self.is_deleted

    def ativar(self) -> None:
        """Ativa a planta genérica de valores (RN-TEL-004)."""
        from ..exceptions import RegraNegocioError

        if self.situacao != SituacaoPlantaValores.RASCUNHO:
            raise RegraNegocioError(
                "Somente planta em rascunho pode ser ativada (RN-TEL-004)"
            )
        self.validar()
        self.situacao = SituacaoPlantaValores.VIGENTE
        self.updated_at = datetime.utcnow()

    def revogar(self, motivo: str) -> None:
        """Revoga a planta genérica de valores (RN-TEL-004)."""
        from ..exceptions import RegraNegocioError

        if self.situacao != SituacaoPlantaValores.VIGENTE:
            raise RegraNegocioError("Somente planta vigente pode ser revogada (RN-TEL-004)")
        if not motivo:
            raise RegraNegocioError(
                "Justificativa é obrigatória para revogar a planta (RN-TEL-004)"
            )
        self.situacao = SituacaoPlantaValores.REVOGADA
        if motivo not in self.legislacao:
            self.legislacao = f"{self.legislacao} | revogada: {motivo}".strip(" |")
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida as regras estruturais da planta genérica de valores."""
        from ..exceptions import RegraNegocioError

        if not self.bairro_id:
            raise RegraNegocioError(
                "Planta genérica de valores exige bairro vinculado (RN-TEL-003)"
            )
        if not 1900 <= self.ano <= 2200:
            raise RegraNegocioError("Ano de vigência inválido para a planta de valores")
        if self.valor_terreno_m2 < 0:
            raise RegraNegocioError("Valor unitário do terreno não pode ser negativo")
        if self.valor_construcao_m2 < 0:
            raise RegraNegocioError("Valor unitário da construção não pode ser negativo")
        if not 0 <= self.aliquota_percent <= 100:
            raise RegraNegocioError("Alíquota deve estar entre 0 e 100")


__all__ = ["PlantaGenericaValores"]
