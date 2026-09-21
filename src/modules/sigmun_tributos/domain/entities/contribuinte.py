"""Entidade Contribuinte — sujeito passivo de tributos municipais (DOM-TRI).

RN-TRI-001: CPF/CNPJ do contribuinte é único e validado.
RN-TRI-002: inscrição municipal é um atributo do cadastro, mas não substitui
    a identificação pelo documento.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class TipoContribuinte(Enum):
    """Tipo de contribuinte (pessoa física ou jurídica)."""

    PESSOA_FISICA = "pf"
    PESSOA_JURIDICA = "pj"


class StatusContribuinte(Enum):
    """Situação cadastral do contribuinte."""

    ATIVO = "ativo"
    INATIVO = "inativo"


def _valida_cpf_cnpj(documento: str) -> None:
    """Valida a forma do documento (somente dígitos e comprimento)."""
    from ..exceptions import RegraNegocioError

    if not documento or not documento.isdigit() or len(documento) not in (11, 14):
        raise RegraNegocioError(
            "CPF/CNPJ inválido: informe somente dígitos (11 para CPF, 14 para CNPJ) "
            "(RN-TRI-001)"
        )


@dataclass
class Contribuinte:
    """Pessoa física ou jurídica sujeita a tributos municipais."""

    id: str = field(default_factory=lambda: str(uuid4()))
    tipo: TipoContribuinte = field(default=TipoContribuinte.PESSOA_FISICA)
    nome: str = ""
    cpf_cnpj: str = ""
    inscricao_municipal: str = ""
    email: str = ""
    telefone: str = ""
    endereco: str = ""
    status: StatusContribuinte = field(default=StatusContribuinte.ATIVO)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        """Indica se o contribuinte está ativo e não excluído."""
        return self.status == StatusContribuinte.ATIVO and not self.is_deleted

    def ativar(self) -> None:
        """Ativa o cadastro do contribuinte."""
        self.status = StatusContribuinte.ATIVO
        self.updated_at = datetime.utcnow()

    def inativar(self) -> None:
        """Inativa o cadastro do contribuinte."""
        self.status = StatusContribuinte.INATIVO
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca o contribuinte como excluído (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida regras estruturais da entidade."""
        from ..exceptions import RegraNegocioError

        if not self.nome:
            raise RegraNegocioError("Nome/Razão social do contribuinte é obrigatório")
        _valida_cpf_cnpj(self.cpf_cnpj)
        if self.tipo == TipoContribuinte.PESSOA_JURIDICA and len(self.cpf_cnpj) != 14:
            raise RegraNegocioError(
                "Pessoa jurídica exige CNPJ com 14 dígitos (RN-TRI-001)"
            )
        if self.tipo == TipoContribuinte.PESSOA_FISICA and len(self.cpf_cnpj) != 11:
            raise RegraNegocioError(
                "Pessoa física exige CPF com 11 dígitos (RN-TRI-001)"
            )


__all__ = ["TipoContribuinte", "StatusContribuinte", "Contribuinte"]