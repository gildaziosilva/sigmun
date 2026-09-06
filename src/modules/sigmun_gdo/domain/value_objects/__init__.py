"""Value objects do domínio de Gestão Documental."""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class HashIntegridade:
    """Value Object para hash de integridade (SHA-256)."""

    def __init__(self, valor: str):
        if not valor or len(valor) != 64:
            raise ValueError("Hash de integridade deve ser um SHA-256 válido (64 hex chars)")
        self._valor = valor.lower()

    @property
    def valor(self) -> str:
        return self._valor

    def __eq__(self, other):
        return isinstance(other, HashIntegridade) and self._valor == other._valor

    def __str__(self) -> str:
        return self._valor


@dataclass(frozen=True)
class CodigoDocumental:
    """Value Object para código documental único."""
    valor: str

    def __post_init__(self):
        if not self.valor or len(self.valor) < 3:
            raise ValueError("Código documental inválido")


@dataclass(frozen=True)
class NumeroDocumento:
    """Value Object para número de documento."""
    numero: str
    ano: int


__all__ = [
    "HashIntegridade",
    "CodigoDocumental",
    "NumeroDocumento",
]
