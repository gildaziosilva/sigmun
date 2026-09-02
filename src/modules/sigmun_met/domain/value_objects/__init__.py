"""Value Objects do domínio de Metadados Corporativos."""

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class CodigoMetadado:
    """Value Object para código de metadado/classificação/taxonomia/termo."""
    valor: str

    def __post_init__(self):
        if not self.valor:
            raise ValueError("Código não pode ser vazio")
        if len(self.valor) < 2:
            raise ValueError("Código deve ter pelo menos 2 caracteres")
        if len(self.valor) > 50:
            raise ValueError("Código deve ter no máximo 50 caracteres")
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_]+$", self.valor):
            raise ValueError(
                "Código deve iniciar por letra e conter apenas letras, números e underlines"
            )

    @staticmethod
    def validar(valor: str) -> tuple[bool, str]:
        try:
            CodigoMetadado(valor)
            return True, ""
        except ValueError as e:
            return False, str(e)


@dataclass(frozen=True)
class NomeEntidade:
    """Value Object para nome de metadado/classificação/taxonomia."""
    valor: str

    def __post_init__(self):
        if not self.valor:
            raise ValueError("Nome não pode ser vazio")
        if len(self.valor) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres")
        if len(self.valor) > 200:
            raise ValueError("Nome deve ter no máximo 200 caracteres")

    @staticmethod
    def validar(nome: str) -> tuple[bool, str]:
        try:
            NomeEntidade(nome)
            return True, ""
        except ValueError as e:
            return False, str(e)


@dataclass(frozen=True)
class ValorAtributo:
    """Value Object para valor atribuído a uma entidade."""
    valor: str

    def __post_init__(self):
        if not self.valor:
            raise ValueError("Valor não pode ser vazio")
        if len(self.valor) > 1000:
            raise ValueError("Valor deve ter no máximo 1000 caracteres")

    @staticmethod
    def validar(valor: str) -> tuple[bool, str]:
        try:
            ValorAtributo(valor)
            return True, ""
        except ValueError as e:
            return False, str(e)


@dataclass(frozen=True)
class EntidadeAlvo:
    """Value Object para identificação da entidade alvo de um valor de metadado."""
    tipo: str
    id: str

    def __post_init__(self):
        if not self.tipo:
            raise ValueError("Tipo da entidade não pode ser vazio")
        if not re.match(r"^[a-z][a-z0-9_]+$", self.tipo):
            raise ValueError(
                "Tipo da entidade deve conter apenas letras minúsculas, números e underlines"
            )
        if not self.id:
            raise ValueError("ID da entidade não pode ser vazio")

    @staticmethod
    def validar(tipo: str, id_: str) -> tuple[bool, str]:
        try:
            EntidadeAlvo(tipo, id_)
            return True, ""
        except ValueError as e:
            return False, str(e)


__all__ = [
    "CodigoMetadado",
    "NomeEntidade",
    "ValorAtributo",
    "EntidadeAlvo",
]
