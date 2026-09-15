"""Exceções de domínio do módulo de Metadados Corporativos."""


class MetadadosDomainError(Exception):
    """Base das exceções de negócio do domínio Metadados (espelho DOM-COMPRAS-001)."""


class MetadadoNaoEncontradoError(MetadadosDomainError):
    """Metadado não encontrado."""

    pass


class MetadadoJaCadastradoError(MetadadosDomainError):
    """Metadado já cadastrado."""

    pass


class ValorMetadadoNaoEncontradoError(MetadadosDomainError):
    """Valor de metadado não encontrado."""

    pass


class ValorMetadadoInvalidoError(MetadadosDomainError):
    """Valor inválido para o tipo de dado do metadado."""

    pass


class ClassificacaoNaoEncontradaError(MetadadosDomainError):
    """Classificação não encontrada."""

    pass


class ClassificacaoDuplicadaError(MetadadosDomainError):
    """Classificação já cadastrada."""

    pass


class TaxonomiaNaoEncontradaError(MetadadosDomainError):
    """Taxonomia não encontrada."""

    pass


class TaxonomiaDuplicadaError(MetadadosDomainError):
    """Taxonomia já cadastrada."""

    pass


class TermoNaoEncontradoError(MetadadosDomainError):
    """Termo de taxonomia não encontrado."""

    pass


class TermoDuplicadoError(MetadadosDomainError):
    """Termo de taxonomia já cadastrado."""

    pass


class CicloHierarquiaError(MetadadosDomainError):
    """Hierarquia de termos criaria um ciclo."""

    pass


class CodigoInvalidoError(MetadadosDomainError):
    """Código inválido."""

    pass


# ---------------------------------------------------------------------------
# Aliases de compatibilidade (nomes anteriores em inglês/híbridos).
# Mantidos para não quebrar importadores externos; remover em major futura.
# ---------------------------------------------------------------------------
DomainException = MetadadosDomainError
MetadadoJaExisteError = MetadadoJaCadastradoError
ClassificacaoJaExisteError = ClassificacaoDuplicadaError
TaxonomiaJaExisteError = TaxonomiaDuplicadaError
TermoJaExisteError = TermoDuplicadoError
HierarquiaCiclicaError = CicloHierarquiaError


__all__ = [
    "MetadadosDomainError",
    "DomainException",
    "MetadadoNaoEncontradoError",
    "MetadadoJaCadastradoError",
    "MetadadoJaExisteError",
    "ValorMetadadoNaoEncontradoError",
    "ValorMetadadoInvalidoError",
    "ClassificacaoNaoEncontradaError",
    "ClassificacaoDuplicadaError",
    "ClassificacaoJaExisteError",
    "TaxonomiaNaoEncontradaError",
    "TaxonomiaDuplicadaError",
    "TaxonomiaJaExisteError",
    "TermoNaoEncontradoError",
    "TermoDuplicadoError",
    "TermoJaExisteError",
    "CicloHierarquiaError",
    "HierarquiaCiclicaError",
    "CodigoInvalidoError",
]
