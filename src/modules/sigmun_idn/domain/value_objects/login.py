"""
Value Object para Login.
"""

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Login:
    """Value Object que representa um login validado."""
    valor: str

    def __post_init__(self):
        self._validar(self.valor)

    @staticmethod
    def _validar(login: str):
        """Valida formato do login."""
        if not login:
            raise ValueError("Login não pode ser vazio")
        if len(login) < 3:
            raise ValueError("Login deve ter pelo menos 3 caracteres")
        if len(login) > 50:
            raise ValueError("Login deve ter no máximo 50 caracteres")
        if not re.match(r"^[a-zA-Z0-9_.-]+$", login):
            raise ValueError("Login pode conter apenas letras, números, pontos, hífens e underlines")
        if login.startswith(".") or login.startswith("-") or login.startswith("_"):
            raise ValueError("Login não pode começar com ponto, hífen ou underline")

    @staticmethod
    def validar_formato(login: str) -> tuple[bool, str]:
        """Valida formato do login sem lançar exceção."""
        try:
            Login._validar(login)
            return True, ""
        except ValueError as e:
            return False, str(e)
