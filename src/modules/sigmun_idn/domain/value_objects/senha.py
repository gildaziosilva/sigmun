"""
Value Object para Senha.
"""

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Senha:
    """Value Object que representa uma senha validada."""
    valor: str

    def __post_init__(self):
        self._validar(self.valor)

    @staticmethod
    def _validar(senha: str):
        """Valida requisitos mínimos de senha."""
        if not senha:
            raise ValueError("Senha não pode ser vazia")
        if len(senha) < 8:
            raise ValueError("Senha deve ter pelo menos 8 caracteres")
        if not re.search(r"[A-Z]", senha):
            raise ValueError("Senha deve conter pelo menos uma letra maiúscula")
        if not re.search(r"[a-z]", senha):
            raise ValueError("Senha deve conter pelo menos uma letra minúscula")
        if not re.search(r"[0-9]", senha):
            raise ValueError("Senha deve conter pelo menos um número")

    @staticmethod
    def validar_formato(senha: str) -> tuple[bool, str]:
        """Valida formato da senha sem lançar exceção."""
        try:
            Senha._validar(senha)
            return True, ""
        except ValueError as e:
            return False, str(e)
