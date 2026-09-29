"""Exceções de domínio do DOM-ASS — Assistência Social."""


class DomAssDomainError(Exception):
    """Base das exceções de negócio do domínio DOM-ASS."""

    pass


class RegraNegocioError(DomAssDomainError):
    """Erro de regra de negócio."""

    pass


class FamiliaNaoEncontradaError(DomAssDomainError):
    """Família não encontrada no CadÚnico."""

    pass


class FamiliaJaExistenteError(DomAssDomainError):
    """Família já cadastrada (NIS duplicado)."""

    pass


class PessoaNaoEncontradaError(DomAssDomainError):
    """Pessoa não encontrada no CadÚnico."""

    pass


class PessoaJaExistenteError(DomAssDomainError):
    """Pessoa já cadastrada (CPF duplicado)."""

    pass


class BeneficioNaoEncontradoError(DomAssDomainError):
    """Benefício eventual não encontrado."""

    pass


class BeneficioJaExistenteError(DomAssDomainError):
    """Benefício já concedido para esta família no período."""

    pass


class UnidadeNaoEncontradaError(DomAssDomainError):
    """Unidade CRAS/CREAS não encontrada."""

    pass


class AtendimentoNaoEncontradoError(DomAssDomainError):
    """Atendimento social não encontrado."""

    pass


class EstoqueInsuficienteError(DomAssDomainError):
    """Estoque insuficiente para concessão do benefício."""

    pass


DomainException = DomAssDomainError

__all__ = [
    "DomAssDomainError",
    "DomainException",
    "RegraNegocioError",
    "FamiliaNaoEncontradaError",
    "FamiliaJaExistenteError",
    "PessoaNaoEncontradaError",
    "PessoaJaExistenteError",
    "BeneficioNaoEncontradoError",
    "BeneficioJaExistenteError",
    "UnidadeNaoEncontradaError",
    "AtendimentoNaoEncontradoError",
    "EstoqueInsuficienteError",
]
