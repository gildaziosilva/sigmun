"""Value Objects do domínio de Dados Corporativos."""

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class NomeAtivo:
    """Value Object para nome de ativo de dado."""
    valor: str

    def __post_init__(self):
        if not self.valor:
            raise ValueError("Nome do ativo não pode ser vazio")
        if len(self.valor) < 3:
            raise ValueError("Nome do ativo deve ter pelo menos 3 caracteres")
        if len(self.valor) > 200:
            raise ValueError("Nome do ativo deve ter no máximo 200 caracteres")

    @staticmethod
    def validar(nome: str) -> tuple[bool, str]:
        try:
            NomeAtivo(nome)
            return True, ""
        except ValueError as e:
            return False, str(e)


@dataclass(frozen=True)
class ClassificacaoDado:
    """Value Object para classificação de dado."""
    valor: str

    VALORES_VALIDOS = ["PUBLICO", "INTERNO", "CONFIDENCIAL", "RESTRITO", "SENSIVEL"]

    def __post_init__(self):
        if not self.valor:
            raise ValueError("Classificação não pode ser vazia")
        if self.valor.upper() not in self.VALORES_VALIDOS:
            raise ValueError(f"Classificação inválida. Valores válidos: {self.VALORES_VALIDOS}")

    @staticmethod
    def validar(valor: str) -> tuple[bool, str]:
        try:
            ClassificacaoDado(valor)
            return True, ""
        except ValueError as e:
            return False, str(e)


@dataclass(frozen=True)
class Tag:
    """Value Object para tag."""
    valor: str

    def __post_init__(self):
        if not self.valor:
            raise ValueError("Tag não pode ser vazia")
        if len(self.valor) > 50:
            raise ValueError("Tag deve ter no máximo 50 caracteres")
        if not re.match(r"^[a-zA-Z0-9_-]+$", self.valor):
            raise ValueError("Tag pode conter apenas letras, números, hífens e underlines")

    @staticmethod
    def validar(valor: str) -> tuple[bool, str]:
        try:
            Tag(valor)
            return True, ""
        except ValueError as e:
            return False, str(e)


__all__ = ["NomeAtivo", "ClassificacaoDado", "Tag"]
