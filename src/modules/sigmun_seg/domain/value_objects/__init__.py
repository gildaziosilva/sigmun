"""Value Objects do domínio de Segurança da Informação."""

import re


class CodigoControle:
    """Valida código de controle (ex: A.5.1.1)."""

    @staticmethod
    def validar(codigo: str) -> tuple[bool, str]:
        if not codigo:
            return False, "Código não pode ser vazio"
        if len(codigo) > 20:
            return False, "Código muito longo"
        return True, ""


class NivelRisco:
    """Valida nível de risco (baixo, medio, alto, critico)."""

    NIVEIS = ("baixo", "medio", "alto", "critico")

    @staticmethod
    def validar(nivel: str) -> tuple[bool, str]:
        if nivel.lower() not in NivelRisco.NIVEIS:
            return False, f"Nível inválido: {nivel}"
        return True, ""


class ProtocoloSeguro:
    """Valida nome/identificador seguro."""

    @staticmethod
    def validar(valor: str, campo: str = "campo") -> tuple[bool, str]:
        if not valor:
            return False, f"{campo} não pode ser vazio"
        if len(valor) < 3:
            return False, f"{campo} precisa ter pelo menos 3 caracteres"
        if not re.match(r"^[a-zA-Z0-9_\-\.]+$", valor):
            return False, f"{campo} contém caracteres inválidos"
        return True, ""


__all__ = ["CodigoControle", "NivelRisco", "ProtocoloSeguro"]
