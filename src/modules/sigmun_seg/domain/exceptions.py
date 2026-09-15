"""Exceções do domínio de Segurança da Informação."""


class SegurancaError(Exception):
    """Exceção base do domínio de segurança."""


class ControleJaExisteError(SegurancaError):
    """Controle já cadastrado."""


class ControleNaoEncontradoError(SegurancaError):
    """Controle não encontrado."""


class PoliticaJaExisteError(SegurancaError):
    """Política já cadastrada."""


class PoliticaNaoEncontradaError(SegurancaError):
    """Política não encontrada."""


class IncidenteNaoEncontradoError(SegurancaError):
    """Incidente não encontrado."""


class IncidenteJaResolvidoError(SegurancaError):
    """Incidente já resolve/encerrado."""


class ChaveNaoEncontradaError(SegurancaError):
    """Chave criptográfica não encontrada."""


class ChaveJaRevogadaError(SegurancaError):
    """Chave já revogada."""


class CredencialNaoEncontradaError(SegurancaError):
    """Credencial não encontrada."""


class CredencialJaRevogadaError(SegurancaError):
    """Credencial já revogada."""


class CodigoInvalidoError(SegurancaError):
    """Código inválido."""


class NivelRiscoInvalidoError(SegurancaError):
    """Nível de risco inválido."""


class OperacaoNaoPermitidaError(SegurancaError):
    """Operação não permitida no estado atual."""


__all__ = [
    "SegurancaError",
    "ControleJaExisteError",
    "ControleNaoEncontradoError",
    "PoliticaJaExisteError",
    "PoliticaNaoEncontradaError",
    "IncidenteNaoEncontradoError",
    "IncidenteJaResolvidoError",
    "ChaveNaoEncontradaError",
    "ChaveJaRevogadaError",
    "CredencialNaoEncontradaError",
    "CredencialJaRevogadaError",
    "CodigoInvalidoError",
    "NivelRiscoInvalidoError",
    "OperacaoNaoPermitidaError",
]
