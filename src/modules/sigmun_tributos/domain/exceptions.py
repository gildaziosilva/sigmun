"""Exceções de domínio do DOM-TRI — Administração Tributária."""


class DomTriDomainError(Exception):
    """Base das exceções de negócio do domínio DOM-TRI."""

    pass


class RegraNegocioError(DomTriDomainError):
    """Erro de regra de negócio."""

    pass


class ContribuinteNaoEncontradoError(DomTriDomainError):
    """Contribuinte não encontrado."""

    pass


class ContribuinteJaExistenteError(DomTriDomainError):
    """Contribuinte já cadastrado (CPF/CNPJ duplicado)."""

    pass


class ImovelNaoEncontradoError(DomTriDomainError):
    """Imóvel não encontrado."""

    pass


class ImovelJaExistenteError(DomTriDomainError):
    """Imóvel já cadastrado (inscrição imobiliária duplicada)."""

    pass


class LancamentoNaoEncontradoError(DomTriDomainError):
    """Lançamento (crédito tributário) não encontrado."""

    pass


class EstadoLancamentoInvalidoError(DomTriDomainError):
    """Transição de estado inválida para o lançamento."""

    pass


class DividaAtivaNaoEncontradaError(DomTriDomainError):
    """Inscrição de dívida ativa não encontrada."""

    pass


class CertidaoNaoEncontradaError(DomTriDomainError):
    """Certidão não encontrada."""

    pass


DomainException = DomTriDomainError

__all__ = [
    "DomTriDomainError",
    "DomainException",
    "RegraNegocioError",
    "ContribuinteNaoEncontradoError",
    "ContribuinteJaExistenteError",
    "ImovelNaoEncontradoError",
    "ImovelJaExistenteError",
    "LancamentoNaoEncontradoError",
    "EstadoLancamentoInvalidoError",
    "DividaAtivaNaoEncontradaError",
    "CertidaoNaoEncontradaError",
]