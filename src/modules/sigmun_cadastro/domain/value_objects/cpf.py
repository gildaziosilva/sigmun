"""Value Object: CPF.

Implementa a validação de Cadastro de Pessoa Física com dígitos
verificadores (RN-CUM-002). O número é armazenado apenas com dígitos;
a formatação é derivada.
"""

from __future__ import annotations

import re

_PADRAO = re.compile(r"^\d{11}$")


def _calcular_digito(digitos: str, peso_inicial: int) -> int:
    total = sum(int(d) * peso for d, peso in zip(digitos, range(peso_inicial, 1, -1)))
    resto = (total * 10) % 11
    return resto if resto < 10 else 0


class CPF:
    """Cadastro de Pessoa Física validado (imutável)."""

    __slots__ = ("_valor",)

    def __init__(self, valor: str) -> None:
        digitos = re.sub(r"\D", "", valor or "")
        if not _PADRAO.match(digitos):
            raise ValueError("CPF deve conter 11 dígitos (RN-CUM-002)")
        if digitos == digitos[0] * 11:
            raise ValueError("CPF inválido: dígitos repetidos (RN-CUM-002)")
        dv1 = _calcular_digito(digitos[:9], 10)
        dv2 = _calcular_digito(digitos[:9] + str(dv1), 11)
        if digitos[-2:] != f"{dv1}{dv2}":
            raise ValueError("CPF inválido: dígitos verificadores (RN-CUM-002)")
        self._valor = digitos

    @property
    def valor(self) -> str:
        """Número do CPF contendo apenas dígitos."""
        return self._valor

    def formatado(self) -> str:
        """Retorna no formato ``000.000.000-00``."""
        v = self._valor
        return f"{v[:3]}.{v[3:6]}.{v[6:9]}-{v[9:]}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, CPF) and other._valor == self._valor

    def __hash__(self) -> int:
        return hash(self._valor)

    def __str__(self) -> str:
        return self._valor

    def __repr__(self) -> str:  # pragma: no cover
        return f"CPF({self.formatado()!r})"


__all__ = ["CPF"]
