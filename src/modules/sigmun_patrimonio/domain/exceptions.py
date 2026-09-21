"""Exceções de domínio do DOM-PAT — Gestão Patrimonial."""


class DomPatDomainError(Exception):
    """Base das exceções de negócio do domínio DOM-PAT."""

    pass


class RegraNegocioError(DomPatDomainError):
    """Erro de regra de negócio."""

    pass


class BemNaoEncontradoError(DomPatDomainError):
    """Bem não encontrado."""

    pass


class BemJaExistenteError(DomPatDomainError):
    """Bem já cadastrado (código/tombo duplicado)."""

    pass


class BemBaixadoError(DomPatDomainError):
    """Bem baixado não pode sofrer a operação."""

    pass


class TransferenciaNaoEncontradaError(DomPatDomainError):
    """Transferência não encontrada."""

    pass


DomainException = DomPatDomainError

__all__ = [
    "DomPatDomainError",
    "DomainException",
    "RegraNegocioError",
    "BemNaoEncontradoError",
    "BemJaExistenteError",
    "BemBaixadoError",
    "TransferenciaNaoEncontradaError",
]