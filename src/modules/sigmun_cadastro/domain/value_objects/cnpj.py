"""Value Object: CNPJ.

Implementa a validação de Cadastro Nacional da Pessoa Jurídica com
dígitos verificadores (RN-CUM-003). O número é armazenado apenas com
dígitos; a formatação é derivada.
"""

from __future__ import annotations

import re

_PADRAO = re.compile(r"^\d{14}$")


def _calcular_digito(digitos: str, pesos: tuple[int, ...]) -> int:
    total = sum(int(d) * p for d, p in zip(digitos, pesos))
    resto = total % 11
    return 0 if resto < 2 else 11 - resto


class CNPJ:
    """Cadastro Nacional da Pessoa Jurídica validado (imutável)."""

    __slots__ = ("_valor",)

    def __init__(self, valor: str) -> None:
        digitos = re.sub(r"\D", "", valor or "")
        if not _PADRAO.match(digitos):
            raise ValueError("CNPJ deve conter 14 dígitos (RN-CUM-003)")
        if digitos == digitos[0] * 14:
            raise ValueError("CNPJ inválido: dígitos repetidos (RN-CUM-003)")
        dv1 = _calcular_digito(digitos[:12], (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2))
        dv2 = _calcular_digito(digitos[:12] + str(dv1), (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2))
        if digitos[-2:] != f"{dv1}{dv2}":
            raise ValueError("CNPJ inválido: dígitos verificadores (RN-CUM-003)")
        self._valor = digitos

    @property
    def valor(self) -> str:
        """Número do CNPJ contendo apenas dígitos."""
        return self._valor

    def formatado(self) -> str:
        """Retorna no formato ``00.000.000/0000-00``."""
        v = self._valor
        return f"{v[:2]}.{v[2:5]}.{v[5:8]}/{v[8:12]}-{v[12:]}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, CNPJ) and other._valor == self._valor

    def __hash__(self) -> int:
        return hash(self._valor)

    def __str__(self) -> str:
        return self._valor

    def __repr__(self) -> str:  # pragma: no cover
        return f"CNPJ({self.formatado()!r})"


__all__ = ["CNPJ"]
