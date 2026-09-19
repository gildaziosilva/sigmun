"""Exceções de domínio do DOM-PES - Gestão de Pessoas (RH e Folha)."""


class DomPesDomainError(Exception):
    """Base das exceções de negócio do domínio DOM-PES."""

    pass


class RegraNegocioError(DomPesDomainError):
    """Erro de regra de negócio."""

    pass


class ServidorNaoEncontradoError(DomPesDomainError):
    """Servidor não encontrado."""

    pass


class ServidorJaExistenteError(DomPesDomainError):
    """Servidor já existe (matrícula ou CPF duplicado)."""

    pass


class ServidorInativoError(DomPesDomainError):
    """Servidor está inativo e não pode sofrer a operação."""

    pass


class CargoNaoEncontradoError(DomPesDomainError):
    """Cargo não encontrado."""

    pass


class CargoJaExistenteError(DomPesDomainError):
    """Cargo já existe (código duplicado)."""

    pass


class LotacaoNaoEncontradaError(DomPesDomainError):
    """Lotação não encontrada."""

    pass


class LotacaoJaExistenteError(DomPesDomainError):
    """Lotação já existe para este servidor no período."""

    pass


class FolhaNaoEncontradaError(DomPesDomainError):
    """Folha de pagamento não encontrada."""

    pass


class FolhaJaExistenteError(DomPesDomainError):
    """Folha já existe para esta competência."""

    pass


class FolhaFechadaError(DomPesDomainError):
    """Folha já está fechada/homologada e não pode ser alterada."""

    pass


class FeriasNaoEncontradasError(DomPesDomainError):
    """Período de férias não encontrado."""

    pass


class FeriasEmEstadoInvalidoError(DomPesDomainError):
    """Férias em estado inválido para esta operação."""

    pass


class FrequenciaNaoEncontradaError(DomPesDomainError):
    """Registro de frequência não encontrado."""

    pass


class TransicaoInvalidaError(DomPesDomainError):
    """Transição de estado inválida."""

    pass


DomainException = DomPesDomainError


__all__ = [
    "DomPesDomainError",
    "DomainException",
    "RegraNegocioError",
    "ServidorNaoEncontradoError",
    "ServidorJaExistenteError",
    "ServidorInativoError",
    "CargoNaoEncontradoError",
    "CargoJaExistenteError",
    "LotacaoNaoEncontradaError",
    "LotacaoJaExistenteError",
    "FolhaNaoEncontradaError",
    "FolhaJaExistenteError",
    "FolhaFechadaError",
    "FeriasNaoEncontradasError",
    "FeriasEmEstadoInvalidoError",
    "FrequenciaNaoEncontradaError",
    "TransicaoInvalidaError",
]
