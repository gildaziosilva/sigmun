"""Exceções de domínio do DOM-FRO — Gestão de Frota."""


class DomFroDomainError(Exception):
    """Base das exceções de negócio do domínio DOM-FRO."""

    pass


class RegraNegocioError(DomFroDomainError):
    """Erro de regra de negócio."""

    pass


class VeiculoNaoEncontradoError(DomFroDomainError):
    """Veículo não encontrado."""

    pass


class VeiculoJaExistenteError(DomFroDomainError):
    """Veículo já cadastrado (placa/renavam duplicado)."""

    pass


class ManutencaoNaoEncontradaError(DomFroDomainError):
    """Manutenção não encontrada."""

    pass


class AbastecimentoNaoEncontradoError(DomFroDomainError):
    """Abastecimento não encontrado."""

    pass


class RotaNaoEncontradaError(DomFroDomainError):
    """Rota não encontrada."""

    pass


DomainException = DomFroDomainError

__all__ = [
    "DomFroDomainError",
    "DomainException",
    "RegraNegocioError",
    "VeiculoNaoEncontradoError",
    "VeiculoJaExistenteError",
    "ManutencaoNaoEncontradaError",
    "AbastecimentoNaoEncontradoError",
    "RotaNaoEncontradaError",
]