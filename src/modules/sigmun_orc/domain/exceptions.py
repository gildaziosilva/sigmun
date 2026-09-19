"""Exceções de domínio do DOM-ORC — Orçamento Público."""

from __future__ import annotations


class DomOrcDomainError(Exception):
    """Base das exceções de negócio do domínio DOM-ORC."""

    pass


class RegraNegocioError(DomOrcDomainError):
    """Erro de regra de negócio."""

    pass


class PPANaoEncontradoError(DomOrcDomainError):
    """PPA não encontrado."""

    pass


class PPAJaExistenteError(DomOrcDomainError):
    """PPA já existe para este quadriênio."""

    pass


class LDONaoEncontradaError(DomOrcDomainError):
    """LDO não encontrada."""

    pass


class LDOJaExistenteError(DomOrcDomainError):
    """LDO já existe para este exercício."""

    pass


class LOANaoEncontradaError(DomOrcDomainError):
    """LOA não encontrada."""

    pass


class LOAJaExistenteError(DomOrcDomainError):
    """LOA já existe para este exercício."""

    pass


class DotacaoNaoEncontradaError(DomOrcDomainError):
    """Dotação orçamentária não encontrada."""

    pass


class DotacaoSemSaldoError(DomOrcDomainError):
    """Dotação sem saldo disponível para reserva/empenho."""

    pass


class ReservaNaoEncontradaError(DomOrcDomainError):
    """Reserva de saldo não encontrada."""

    pass


class ReservaEmEstadoInvalidoError(DomOrcDomainError):
    """Reserva em estado inválido para esta operação."""

    pass


class TransicaoInvalidaError(DomOrcDomainError):
    """Transição de estado inválida."""

    pass


DomainException = DomOrcDomainError


__all__ = [
    "DomOrcDomainError",
    "DomainException",
    "RegraNegocioError",
    "PPANaoEncontradoError",
    "PPAJaExistenteError",
    "LDONaoEncontradaError",
    "LDOJaExistenteError",
    "LOANaoEncontradaError",
    "LOAJaExistenteError",
    "DotacaoNaoEncontradaError",
    "DotacaoSemSaldoError",
    "ReservaNaoEncontradaError",
    "ReservaEmEstadoInvalidoError",
    "TransicaoInvalidaError",
]
