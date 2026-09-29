"""Vínculo de pessoa (proprietário) com a unidade imobiliária do DOM-IMO.

RN-IMO-006: cada imóvel possui no máximo um proprietário titular principal e
    o CPF do titular deve ser válido.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from .tipos import TipoVinculo


@dataclass
class ProprietarioImovel:
    """Vínculo entre uma pessoa e um imóvel."""

    id: str = field(default_factory=lambda: str(uuid4()))
    imovel_id: str = ""
    pessoa_id: str = ""
    nome: str = ""
    cpf: str = ""
    vinculo: TipoVinculo = field(default=TipoVinculo.TITULAR)
    principal: bool = False
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def e_titular_principal(self) -> bool:
        """Indica se o vínculo é de titularidade principal."""
        return self.principal and self.vinculo == TipoVinculo.TITULAR

    def remover(self) -> None:
        """Marca o vínculo como removido (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida as regras estruturais do vínculo (RN-IMO-006).

        O documento do titular é o CPF (11 dígitos) para pessoa física ou o
        CNPJ (14 dígitos) para pessoa jurídica.
        """
        from ..exceptions import RegraNegocioError

        if not self.imovel_id:
            raise RegraNegocioError("Vínculo exige imóvel vinculado (RN-IMO-006)")
        if not self.nome:
            raise RegraNegocioError("Nome do proprietário é obrigatório (RN-IMO-006)")
        documento = self.cpf
        if not documento or not documento.isdigit() or len(documento) not in (11, 14):
            raise RegraNegocioError(
                "CPF (11 dígitos) ou CNPJ (14 dígitos) do proprietário é obrigatório "
                "(RN-IMO-006)"
            )


__all__ = ["ProprietarioImovel"]
