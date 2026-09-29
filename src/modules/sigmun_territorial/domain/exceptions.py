"""Exceções de domínio do DOM-TEL — Gestão Territorial."""


class DomTelDomainError(Exception):
    """Base das exceções de negócio do domínio DOM-TEL."""

    pass


class RegraNegocioError(DomTelDomainError):
    """Erro de regra de negócio."""

    pass


class BairroNaoEncontradoError(DomTelDomainError):
    """Bairro não encontrado no cadastro territorial."""

    pass


class BairroJaExistenteError(DomTelDomainError):
    """Bairro já cadastrado (código duplicado)."""

    pass


class BairroComDependenciasError(DomTelDomainError):
    """Bairro possui logradouros vinculados e não pode ser excluído."""

    pass


class LogradouroNaoEncontradoError(DomTelDomainError):
    """Logradouro não encontrado no cadastro territorial."""

    pass


class LogradouroJaExistenteError(DomTelDomainError):
    """Logradouro já cadastrado (código duplicado)."""

    pass


class PlantaValoresNaoEncontradaError(DomTelDomainError):
    """Planta genérica de valores não encontrada."""

    pass


class PlantaValoresJaExistenteError(DomTelDomainError):
    """Já existe planta genérica de valores vigente para o mesmo ano, bairro e tipo."""

    pass


class GeorreferenciaNaoEncontradaError(DomTelDomainError):
    """Georreferência não encontrada."""

    pass


DomainException = DomTelDomainError

__all__ = [
    "DomTelDomainError",
    "DomainException",
    "RegraNegocioError",
    "BairroNaoEncontradoError",
    "BairroJaExistenteError",
    "BairroComDependenciasError",
    "LogradouroNaoEncontradoError",
    "LogradouroJaExistenteError",
    "PlantaValoresNaoEncontradaError",
    "PlantaValoresJaExistenteError",
    "GeorreferenciaNaoEncontradaError",
]
