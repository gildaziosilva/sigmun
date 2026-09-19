"""Exceções de domínio do DOM-DIA - Gestão de Diárias, Viagens e Deslocamentos."""


class DomDiaDomainError(Exception):
    """Base das exceções de negócio do domínio DOM-DIA."""
    pass


class RegraNegocioError(DomDiaDomainError):
    """Erro de regra de negócio."""
    pass


class ViagemNaoEncontradaError(DomDiaDomainError):
    """Viagem não encontrada."""
    pass


class ViagemSemDiariasError(DomDiaDomainError):
    """Viagem sem diárias associadas."""
    pass


class ViagemCategoriaInvalidaError(DomDiaDomainError):
    """Categoria de diária inválida para esta viagem."""
    pass


class DiariaNaoEncontradaError(DomDiaDomainError):
    """Diária não encontrada."""
    pass


class DiariaJaExistenteError(DomDiaDomainError):
    """Diária já existe para esta viagem."""
    pass


class DiariaJaTerminadaError(DomDiaDomainError):
    """Diária já está em estado terminal (não pode mais ser alterada)."""
    pass


class ValidacaoDiariaError(DomDiaDomainError):
    """Erro de validação de diária."""
    pass


class DiariaEmEstadoInvalidoError(DomDiaDomainError):
    """Diária está em estado inválido para esta operação."""
    pass


class DiariaPendenteAutorizacaoError(DomDiaDomainError):
    """Diária está pendente de autorização."""
    pass


class PrestacaoContasNaoEncontradaError(DomDiaDomainError):
    """Prestação de contas não encontrada."""
    pass


class PrestacaoContasJaExistenteError(DomDiaDomainError):
    """Prestação de contas já existe para esta diária."""
    pass


class TransicaoInvalidaError(DomDiaDomainError):
    """Transição de estado inválida."""
    pass


DomainException = DomDiaDomainError


__all__ = [
    'DomDiaDomainError',
    'DomainException',
    'RegraNegocioError',
    'ViagemNaoEncontradaError',
    'ViagemSemDiariasError',
    'ViagemCategoriaInvalidaError',
    'DiariaNaoEncontradaError',
    'DiariaJaExistenteError',
    'DiariaJaTerminadaError',
    'ValidacaoDiariaError',
    'DiariaEmEstadoInvalidoError',
    'DiariaPendenteAutorizacaoError',
    'PrestacaoContasNaoEncontradaError',
    'PrestacaoContasJaExistenteError',
    'TransicaoInvalidaError',
]
