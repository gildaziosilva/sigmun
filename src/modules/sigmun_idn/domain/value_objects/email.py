"""
Value Object para Email.
"""

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Email:
    """Value Object que representa um email validado."""
    valor: str

    def __post_init__(self):
        self._validar(self.valor)

    @staticmethod
    def _validar(email: str):
        """Valida formato do email."""
        if not email:
            raise ValueError("Email não pode ser vazio")
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            raise ValueError("Formato de email inválido")

    @staticmethod
    def validar_formato(email: str) -> tuple[bool, str]:
        """Valida formato do email sem lançar exceção."""
        try:
            Email._validar(email)
            return True, ""
        except ValueError as e:
            return False, str(e)
