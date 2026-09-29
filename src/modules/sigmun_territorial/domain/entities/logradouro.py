"""Logradouro público do DOM-TEL.

RN-TEL-002: o código do logradouro é único e todo logradouro pertence a um
    bairro cadastrado.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from .tipos import SituacaoLogradouro, TipoLogradouro


@dataclass
class Logradouro:
    """Logradouro público vinculado a um bairro (RN-TEL-002)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    tipo: TipoLogradouro = field(default=TipoLogradouro.RUA)
    bairro_id: str = ""
    cep: str = ""
    numero_inicial: int = 0
    numero_final: int = 0
    situacao: SituacaoLogradouro = field(default=SituacaoLogradouro.ATIVO)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        """Indica se o logradouro está ativo e não excluído."""
        return self.situacao == SituacaoLogradouro.ATIVO and not self.is_deleted

    def ativar(self) -> None:
        """Ativa o logradouro."""
        self.situacao = SituacaoLogradouro.ATIVO
        self.updated_at = datetime.utcnow()

    def inativar(self) -> None:
        """Inativa o logradouro."""
        self.situacao = SituacaoLogradouro.INATIVO
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca o logradouro como excluído (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida as regras estruturais do logradouro (RN-TEL-002)."""
        from ..exceptions import RegraNegocioError

        if not self.codigo or not self.nome:
            raise RegraNegocioError("Código e nome do logradouro são obrigatórios (RN-TEL-002)")
        if not self.bairro_id:
            raise RegraNegocioError("Logradouro deve estar vinculado a um bairro (RN-TEL-002)")
        if self.numero_inicial < 0 or self.numero_final < 0:
            raise RegraNegocioError("Numeração do logradouro não pode ser negativa")
        if self.numero_final and self.numero_final < self.numero_inicial:
            raise RegraNegocioError(
                "Número final do logradouro não pode ser menor que o número inicial"
            )


__all__ = ["Logradouro"]
