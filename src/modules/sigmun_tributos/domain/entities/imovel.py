"""Entidade Imóvel — cadastro imobiliário para IPTU (DOM-TRI).

RN-TRI-010: inscrição imobiliária é única no município.
RN-TRI-011: o IPTU é calculado sobre o valor venal aplicando a alíquota
    vigente do imóvel.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class StatusImovel(Enum):
    """Situação cadastral do imóvel."""

    ATIVO = "ativo"
    INATIVO = "inativo"
    DEMOLIDO = "demolido"


@dataclass
class Imovel:
    """Unidade imobiliária passível de incidência de IPTU."""

    id: str = field(default_factory=lambda: str(uuid4()))
    contribuinte_id: str = ""
    inscricao_imobiliaria: str = ""
    logradouro: str = ""
    numero: str = ""
    bairro: str = ""
    cidade: str = ""
    uf: str = ""
    cep: str = ""
    area_terreno: float = 0.0
    area_construida: float = 0.0
    valor_venal: float = 0.0
    aliquota: float = field(default=0.0)
    status: StatusImovel = field(default=StatusImovel.ATIVO)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    def validar(self) -> None:
        """Valida regras estruturais do imóvel."""
        from ..exceptions import RegraNegocioError

        if not self.contribuinte_id:
            raise RegraNegocioError("Imóvel exige contribuinte responsável (RN-TRI-010)")
        if not self.inscricao_imobiliaria:
            raise RegraNegocioError("Inscrição imobiliária é obrigatória (RN-TRI-010)")
        if self.valor_venal <= 0:
            raise RegraNegocioError("Valor venal deve ser maior que zero (RN-TRI-011)")
        if self.aliquota is not None and self.aliquota < 0:
            raise RegraNegocioError("Alíquota não pode ser negativa")

    def calcular_iptu(self) -> float:
        """Calcula o valor do IPTU (valor venal × alíquota)."""
        return round(self.valor_venal * self.aliquota, 2)

    def excluir(self) -> None:
        """Marca o imóvel como excluído (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()


__all__ = ["StatusImovel", "Imovel"]