"""Exceções de domínio do módulo de Metadados Corporativos."""


class DomainException(Exception):
    """Exceção base do domínio."""
    pass


class MetadadoNaoEncontradoError(DomainException):
    """Metadado não encontrado."""
    pass


class MetadadoJaExisteError(DomainException):
    """Metadado já cadastrado."""
    pass


class ValorMetadadoNaoEncontradoError(DomainException):
    """Valor de metadado não encontrado."""
    pass


class ValorMetadadoInvalidoError(DomainException):
    """Valor inválido para o tipo de dado do metadado."""
    pass


class ClassificacaoNaoEncontradaError(DomainException):
    """Classificação não encontrada."""
    pass


class ClassificacaoJaExisteError(DomainException):
    """Classificação já cadastrada."""
    pass


class TaxonomiaNaoEncontradaError(DomainException):
    """Taxonomia não encontrada."""
    pass


class TaxonomiaJaExisteError(DomainException):
    """Taxonomia já cadastrada."""
    pass


class TermoNaoEncontradoError(DomainException):
    """Termo de taxonomia não encontrado."""
    pass


class TermoJaExisteError(DomainException):
    """Termo de taxonomia já cadastrado."""
    pass


class HierarquiaCiclicaError(DomainException):
    """Hierarquia de termos criaria um ciclo."""
    pass


class CodigoInvalidoError(DomainException):
    """Código inválido."""
    pass


__all__ = [
    "DomainException",
    "MetadadoNaoEncontradoError",
    "MetadadoJaExisteError",
    "ValorMetadadoNaoEncontradoError",
    "ValorMetadadoInvalidoError",
    "ClassificacaoNaoEncontradaError",
    "ClassificacaoJaExisteError",
    "TaxonomiaNaoEncontradaError",
    "TaxonomiaJaExisteError",
    "TermoNaoEncontradoError",
    "TermoJaExisteError",
    "HierarquiaCiclicaError",
    "CodigoInvalidoError",
]
