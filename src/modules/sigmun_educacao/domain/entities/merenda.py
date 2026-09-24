"""Entidades ItemMerenda e DistribuicaoMerenda — merenda escolar (DOM-EDU).

RN-EDU-040: distribuição exige estoque suficiente; a baixa é atômica no
caso de uso (a entidade valida e calcula); quantidade sempre positiva.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import uuid4


@dataclass
class ItemMerenda:
    """Item do elenco de merenda da rede (estoque + mínimo)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    nome: str = ""
    tipo: str = "refeicao"
    estoque: float = 0.0
    estoque_minimo: float = 0.0
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def abaixo_do_minimo(self) -> bool:
        """Indica necessidade de reposição."""
        return self.estoque < self.estoque_minimo

    def repor(self, quantidade: float) -> None:
        """Entrada de estoque."""
        from ..exceptions import RegraNegocioError

        if quantidade <= 0:
            raise RegraNegocioError("Reposição exige quantidade positiva (RN-EDU-040)")
        self.estoque = round(self.estoque + quantidade, 2)
        self.updated_at = datetime.utcnow()

    def distribuir(self, quantidade: float) -> None:
        """Baixa de estoque por distribuição (RN-EDU-040)."""
        from ..exceptions import EstoqueInsuficienteError, RegraNegocioError

        if quantidade <= 0:
            raise RegraNegocioError(
                f"Distribuição exige quantidade positiva (RN-EDU-040)"
            )
        if quantidade > self.estoque:
            raise EstoqueInsuficienteError(
                f"Estoque insuficiente: solicitado {quantidade}, "
                f"disponível {self.estoque} (RN-EDU-040)"
            )
        self.estoque = round(self.estoque - quantidade, 2)
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida regras estruturais do item."""
        from ..exceptions import RegraNegocioError

        if not self.nome:
            raise RegraNegocioError("Nome do item de merenda é obrigatório")
        if self.estoque < 0 or self.estoque_minimo < 0:
            raise RegraNegocioError("Estoque não pode ser negativo")


@dataclass
class DistribuicaoMerenda:
    """Entrega de refeição/porção a um aluno matriculado."""

    id: str = field(default_factory=lambda: str(uuid4()))
    matricula_id: str = ""
    item_id: str = ""
    quantidade: float = 0.0
    data: date | None = None
    refeicao: str = "almoco"
    created_at: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""

    def validar(self) -> None:
        """Valida regras estruturais da distribuição."""
        from ..exceptions import RegraNegocioError

        if not self.matricula_id or not self.item_id:
            raise RegraNegocioError(
                "Distribuição exige matrícula e item (RN-EDU-040)"
            )
        if self.quantidade <= 0:
            raise RegraNegocioError("Quantidade distribuída deve ser positiva")


__all__ = ["ItemMerenda", "DistribuicaoMerenda"]
