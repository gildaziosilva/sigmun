"""Exceções de domínio do módulo de Dados Corporativos.

Base PT-BR espelhada no DOM-COM (ComprasDomainError).
Aliases dos nomes anteriores mantidos por compatibilidade.
"""


class DadosDomainError(Exception):
    """Base das exceções de negócio do domínio Dados."""


class AtivoNaoEncontradoError(DadosDomainError):
    """Ativo de dado não encontrado."""

    pass


class AtivoJaCadastradoError(DadosDomainError):
    """Ativo de dado já cadastrado."""

    pass


class CatalogoNaoEncontradoError(DadosDomainError):
    """Catálogo não encontrado."""

    pass


class CatalogoDuplicadoError(DadosDomainError):
    """Catálogo já cadastrado."""

    pass


class LinhagemNaoEncontradaError(DadosDomainError):
    """Linhagem não encontrada."""

    pass


class LinhagemDuplicadaError(DadosDomainError):
    """Linhagem já cadastrada."""

    pass


class PoliticaNaoEncontradaError(DadosDomainError):
    """Política não encontrada."""

    pass


class PoliticaDuplicadaError(DadosDomainError):
    """Política já cadastrada."""

    pass


class QualidadeNaoEncontradaError(DadosDomainError):
    """Registro de qualidade não encontrado."""

    pass


class ClassificacaoInvalidaError(DadosDomainError):
    """Classificação de dado inválida."""

    pass


class NomeAtivoInvalidoError(DadosDomainError):
    """Nome de ativo inválido."""

    pass


# ---------------------------------------------------------------------------
# Aliases de compatibilidade.
# ---------------------------------------------------------------------------
DomainException = DadosDomainError
AtivoJaExisteError = AtivoJaCadastradoError
CatalogoJaExisteError = CatalogoDuplicadoError
LinhagemJaExisteError = LinhagemDuplicadaError
PoliticaJaExisteError = PoliticaDuplicadaError


__all__ = [
    "DadosDomainError",
    "DomainException",
    "AtivoNaoEncontradoError",
    "AtivoJaCadastradoError",
    "AtivoJaExisteError",
    "CatalogoNaoEncontradoError",
    "CatalogoDuplicadoError",
    "CatalogoJaExisteError",
    "LinhagemNaoEncontradaError",
    "LinhagemDuplicadaError",
    "LinhagemJaExisteError",
    "PoliticaNaoEncontradaError",
    "PoliticaDuplicadaError",
    "PoliticaJaExisteError",
    "QualidadeNaoEncontradaError",
    "ClassificacaoInvalidaError",
    "NomeAtivoInvalidoError",
]
