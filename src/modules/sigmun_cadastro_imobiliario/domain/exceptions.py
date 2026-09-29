"""Exceções de domínio do DOM-IMO — Cadastro Imobiliário."""


class DomImoDomainError(Exception):
    """Base das exceções de negócio do domínio DOM-IMO."""

    pass


class RegraNegocioError(DomImoDomainError):
    """Erro de regra de negócio."""

    pass


class ImovelNaoEncontradoError(DomImoDomainError):
    """Imóvel não encontrado no cadastro imobiliário."""

    pass


class ImovelJaExistenteError(DomImoDomainError):
    """Imóvel já cadastrado (inscrição imobiliária duplicada)."""

    pass


class ProprietarioNaoEncontradoError(DomImoDomainError):
    """Proprietário não encontrado."""

    pass


class ProprietarioJaExistenteError(DomImoDomainError):
    """Proprietário já vinculado ao imóvel."""

    pass


class ProprietarioPrincipalDuplicadoError(DomImoDomainError):
    """Imóvel já possui proprietário principal definido."""

    pass


class CaracteristicaNaoEncontradaError(DomImoDomainError):
    """Característica construtiva não encontrada."""

    pass


class CaracteristicaJaExistenteError(DomImoDomainError):
    """Característica construtiva já cadastrada para o imóvel."""

    pass


class GeometriaNaoEncontradaError(DomImoDomainError):
    """Geometria do lote não encontrada."""

    pass


class GeometriaJaExistenteError(DomImoDomainError):
    """Imóvel já possui geometria georreferenciada."""

    pass


class PlantaValoresIndisponivelError(DomImoDomainError):
    """Não há planta genérica de valores vigente para o ano e bairro informados."""

    pass


class AvaliacaoNaoEncontradaError(DomImoDomainError):
    """Avaliação do imóvel não encontrada."""

    pass


DomainException = DomImoDomainError

__all__ = [
    "DomImoDomainError",
    "DomainException",
    "RegraNegocioError",
    "ImovelNaoEncontradoError",
    "ImovelJaExistenteError",
    "ProprietarioNaoEncontradoError",
    "ProprietarioJaExistenteError",
    "ProprietarioPrincipalDuplicadoError",
    "CaracteristicaNaoEncontradaError",
    "CaracteristicaJaExistenteError",
    "GeometriaNaoEncontradaError",
    "GeometriaJaExistenteError",
    "PlantaValoresIndisponivelError",
    "AvaliacaoNaoEncontradaError",
]
