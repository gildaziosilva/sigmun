"""Exceções de domínio do DOM-CON — Contabilidade Pública."""

from __future__ import annotations


class DomConDomainError(Exception):
    """Base das exceções de negócio do domínio DOM-CON."""

    pass


class RegraNegocioError(DomConDomainError):
    """Erro de regra de negócio."""

    pass


class EmpenhoNaoEncontradoError(DomConDomainError):
    """Empenho não encontrado."""

    pass


class EmpenhoJaExistenteError(DomConDomainError):
    """Empenho já existe (número duplicado no exercício)."""

    pass


class EmpenhoEmEstadoInvalidoError(DomConDomainError):
    """Empenho em estado inválido para esta operação."""

    pass


class LiquidacaoNaoEncontradaError(DomConDomainError):
    """Liquidação não encontrada."""

    pass


class PagamentoNaoEncontradoError(DomConDomainError):
    """Pagamento não encontrado."""

    pass


class ContaContabilNaoEncontradaError(DomConDomainError):
    """Conta contábil (PCASP) não encontrada."""

    pass


class ContaContabilJaExistenteError(DomConDomainError):
    """Conta contábil já existe (código duplicado)."""

    pass


class LancamentoNaoEncontradoError(DomConDomainError):
    """Lançamento contábil não encontrado."""

    pass


class LancamentoDesequilibradoError(DomConDomainError):
    """Partidas dobradas não balanceadas (débito ≠ crédito)."""

    pass


class ConciliacaoNaoEncontradaError(DomConDomainError):
    """Conciliação contábil não encontrada."""

    pass


class TransicaoInvalidaError(DomConDomainError):
    """Transição de estado inválida."""

    pass


DomainException = DomConDomainError


__all__ = [
    "DomConDomainError",
    "DomainException",
    "RegraNegocioError",
    "EmpenhoNaoEncontradoError",
    "EmpenhoJaExistenteError",
    "EmpenhoEmEstadoInvalidoError",
    "LiquidacaoNaoEncontradaError",
    "PagamentoNaoEncontradoError",
    "ContaContabilNaoEncontradaError",
    "ContaContabilJaExistenteError",
    "LancamentoNaoEncontradoError",
    "LancamentoDesequilibradoError",
    "ConciliacaoNaoEncontradaError",
    "TransicaoInvalidaError",
]
