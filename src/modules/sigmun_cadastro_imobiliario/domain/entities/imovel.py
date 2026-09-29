"""Unidade imobiliária (lote) do DOM-IMO.

RN-IMO-001: a inscrição imobiliária é única no município.
RN-IMO-002: o imóvel exige logradouro e bairro vinculados (identificadores
    referenciados por contrato de integração, sem FK entre schemas).
RN-IMO-003: áreas não podem ser negativas e a área construída não pode
    ultrapassar o limite físico do terreno multiplicado pelos pavimentos.
RN-IMO-004: a situação do imóvel obedece à máquina de estados declarada em
    `tipos.transicao_permitida`.
RN-IMO-005: a avaliação de valor venal é calculada a partir dos valores
    unitários vigentes da planta genérica de valores.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from .tipos import SituacaoImovel, TipoImovel, TipoPropriedade, transicao_permitida


@dataclass
class Imovel:
    """Unidade imobiliária do município."""

    id: str = field(default_factory=lambda: str(uuid4()))
    inscricao_imobiliaria: str = ""
    logradouro_id: str = ""
    bairro_id: str = ""
    numero: str = ""
    complemento: str = ""
    tipo: TipoImovel = field(default=TipoImovel.LOTE)
    situacao: SituacaoImovel = field(default=SituacaoImovel.ATIVO)
    tipo_propriedade: TipoPropriedade = field(default=TipoPropriedade.PROPRIO)
    area_terreno_m2: float = 0.0
    area_construida_m2: float = 0.0
    ano_construcao: int | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        """Indica se o imóvel está ativo e não excluído."""
        return self.situacao == SituacaoImovel.ATIVO and not self.is_deleted

    def mudar_situacao(self, nova_situacao: SituacaoImovel) -> None:
        """Altera a situação do imóvel respeitando a máquina de estados (RN-IMO-004)."""
        from ..exceptions import RegraNegocioError

        if nova_situacao == self.situacao:
            self.updated_at = datetime.utcnow()
            return
        if not transicao_permitida(self.situacao, nova_situacao):
            raise RegraNegocioError(
                f"Transição de situação não permitida: {self.situacao.value} -> "
                f"{nova_situacao.value} (RN-IMO-004)"
            )
        self.situacao = nova_situacao
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca o imóvel como excluído (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida as regras estruturais do imóvel (RN-IMO-001/002/003)."""
        from ..exceptions import RegraNegocioError

        if not self.inscricao_imobiliaria:
            raise RegraNegocioError(
                "Inscrição imobiliária é obrigatória (RN-IMO-001)"
            )
        if not self.logradouro_id:
            raise RegraNegocioError("Imóvel exige logradouro vinculado (RN-IMO-002)")
        if not self.bairro_id:
            raise RegraNegocioError("Imóvel exige bairro vinculado (RN-IMO-002)")
        if self.area_terreno_m2 < 0:
            raise RegraNegocioError("Área do terreno não pode ser negativa (RN-IMO-003)")
        if self.area_construida_m2 < 0:
            raise RegraNegocioError("Área construída não pode ser negativa (RN-IMO-003)")
        if self.ano_construcao is not None and not 1800 <= self.ano_construcao <= 2200:
            raise RegraNegocioError("Ano de construção inválido")


__all__ = ["Imovel"]

