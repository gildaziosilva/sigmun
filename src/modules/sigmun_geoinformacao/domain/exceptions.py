"""Exceções de domínio do DOM-GEO — Geoinformação Municipal."""


class DomGeoDomainError(Exception):
    """Base das exceções de negócio do domínio DOM-GEO."""

    pass


class RegraNegocioError(DomGeoDomainError):
    """Erro de regra de negócio."""

    pass


class CamadaMapaNaoEncontradaError(DomGeoDomainError):
    """Camada de mapa não encontrada."""

    pass


class CamadaMapaJaExistenteError(DomGeoDomainError):
    """Camada de mapa já cadastrada (código duplicado)."""

    pass


class MapaSigNaoEncontradoError(DomGeoDomainError):
    """Mapa SIG não encontrado."""

    pass


class MapaSigJaExistenteError(DomGeoDomainError):
    """Mapa SIG já cadastrado (código duplicado)."""

    pass


class MapaComCamadasError(DomGeoDomainError):
    """Mapa possui camadas vinculadas e não pode ser excluído."""

    pass


class MapaSemCamadasError(DomGeoDomainError):
    """Mapa não possui camadas para a operação solicitada (RN-GEO-004)."""

    pass


class MapaNaoEditavelError(DomGeoDomainError):
    """Mapa publicado não aceita alterações de composição (RN-GEO-004)."""

    pass


class FeatureGeoNaoEncontradaError(DomGeoDomainError):
    """Elemento geoespacial não encontrado."""

    pass


class FeatureGeoJaExistenteError(DomGeoDomainError):
    """Já existe elemento geoespacial com o mesmo código na camada."""

    pass


class ServicoGeoNaoEncontradoError(DomGeoDomainError):
    """Serviço geoespacial não encontrado."""

    pass


class ServicoGeoJaExistenteError(DomGeoDomainError):
    """Serviço geoespacial já cadastrado (código duplicado)."""

    pass


DomainException = DomGeoDomainError

__all__ = [
    "DomGeoDomainError",
    "DomainException",
    "RegraNegocioError",
    "CamadaMapaNaoEncontradaError",
    "CamadaMapaJaExistenteError",
    "MapaSigNaoEncontradoError",
    "MapaSigJaExistenteError",
    "MapaComCamadasError",
    "MapaSemCamadasError",
    "MapaNaoEditavelError",
    "FeatureGeoNaoEncontradaError",
    "FeatureGeoJaExistenteError",
    "ServicoGeoNaoEncontradoError",
    "ServicoGeoJaExistenteError",
]
