"""Divisão territorial (bairro, distrito, setor, zona rural) do DOM-TEL.

RN-TEL-001: o código do bairro é único no cadastro territorial municipal.
RN-TEL-006: bairro com logradouros ativos não pode ser excluído.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from .tipos import SituacaoBairro, TipoBairro


@dataclass
class Bairro:
    """Divisão territorial de referência da planta genérica de valores."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    tipo: TipoBairro = field(default=TipoBairro.BAIRRO)
    populacao_estimada: int = 0
    area_km2: float = 0.0
    situacao: SituacaoBairro = field(default=SituacaoBairro.ATIVO)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        """Indica se o bairro está ativo e não excluído."""
        return self.situacao == SituacaoBairro.ATIVO and not self.is_deleted

    def ativar(self) -> None:
        """Ativa o bairro."""
        self.situacao = SituacaoBairro.ATIVO
        self.updated_at = datetime.utcnow()

    def inativar(self) -> None:
        """Inativa o bairro."""
        self.situacao = SituacaoBairro.INATIVO
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca o bairro como excluído (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida as regras estruturais do bairro (RN-TEL-001)."""
        from ..exceptions import RegraNegocioError

        if not self.codigo or not self.nome:
            raise RegraNegocioError("Código e nome do bairro são obrigatórios (RN-TEL-001)")
        if self.populacao_estimada < 0:
            raise RegraNegocioError("População estimada não pode ser negativa")
        if self.area_km2 < 0:
            raise RegraNegocioError("Área do bairro não pode ser negativa")


__all__ = ["Bairro"]
