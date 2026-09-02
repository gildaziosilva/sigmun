"""Exceções de domínio do módulo de Dados Corporativos."""


class DomainException(Exception):
    """Exceção base do domínio."""
    pass


class AtivoNaoEncontradoError(DomainException):
    """Ativo de dado não encontrado."""
    pass


class AtivoJaExisteError(DomainException):
    """Ativo de dado já cadastrado."""
    pass


class CatalogoNaoEncontradoError(DomainException):
    """Catálogo não encontrado."""
    pass


class CatalogoJaExisteError(DomainException):
    """Catálogo já cadastrado."""
    pass


class LinhagemNaoEncontradaError(DomainException):
    """Linhagem não encontrada."""
    pass


class LinhagemJaExisteError(DomainException):
    """Linhagem já cadastrada."""
    pass


class PoliticaNaoEncontradaError(DomainException):
    """Política não encontrada."""
    pass


class PoliticaJaExisteError(DomainException):
    """Política já cadastrada."""
    pass


class QualidadeNaoEncontradaError(DomainException):
    """Registro de qualidade não encontrado."""
    pass


class ClassificacaoInvalidaError(DomainException):
    """Classificação de dado inválida."""
    pass


class NomeAtivoInvalidoError(DomainException):
    """Nome de ativo inválido."""
    pass


__all__ = [
    "DomainException",
    "AtivoNaoEncontradoError",
    "AtivoJaExisteError",
    "CatalogoNaoEncontradoError",
    "CatalogoJaExisteError",
    "LinhagemNaoEncontradaError",
    "LinhagemJaExisteError",
    "PoliticaNaoEncontradaError",
    "PoliticaJaExisteError",
    "QualidadeNaoEncontradaError",
    "ClassificacaoInvalidaError",
    "NomeAtivoInvalidoError",
]
