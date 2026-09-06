"""Exceções de domínio do módulo de Gestão Documental."""


class DomainException(Exception):
    """Exceção base do domínio."""
    pass


class DocumentoNaoEncontradoError(DomainException):
    """Documento não encontrado."""
    pass


class DocumentoJaExisteError(DomainException):
    """Documento já existe."""
    pass


class VersaoDocumentoNaoEncontradaError(DomainException):
    """Versão de documento não encontrada."""
    pass


class VersaoImutavelError(DomainException):
    """Tentativa de modificar uma versão imutável."""
    pass


class CodigoDocumentalDuplicadoError(DomainException):
    """Código documental já utilizado por outro tipo."""
    pass


class IntegridadeInvalidaError(DomainException):
    """Hash de integridade inválido ou inconsistente."""
    pass


class ClassificacaoDocumentalNaoEncontradaError(DomainException):
    """Classificação documental não encontrada."""
    pass


class ClassificacaoDocumentalJaExisteError(DomainException):
    """Classificação documental já cadastrada."""
    pass


class TramitacaoNaoEncontradaError(DomainException):
    """Tramitação não encontrada."""
    pass


class ProcessoDocumentalNaoEncontradoError(DomainException):
    """Processo documental não encontrado."""
    pass


class ProcessoDocumentalJaExisteError(DomainException):
    """Processo documental já existe."""
    pass


class PermissaoNegadaError(DomainException):
    """Permissão negada para a operação solicitada."""
    pass


class DocumentoNaoAssinadoError(DomainException):
    """Documento não possui assinatura válida."""
    pass


class TemporalidadeNaoEncontradaError(DomainException):
    """Temporalidade não encontrada."""
    pass


class ArquivamentoInvalidoError(DomainException):
    """Operação de arquivamento inválida (documento em fase de corrente)."""
    pass


class EliminacaoNaoAutorizadaError(DomainException):
    """Eliminação não autorizada (falta de autoridade homologadora)."""
    pass


class TipoDocumentalInvalidoError(DomainException):
    """Tipo documental não encontrado ou inativo."""
    pass


__all__ = [
    "DomainException",
    "DocumentoNaoEncontradoError",
    "DocumentoJaExisteError",
    "VersaoDocumentoNaoEncontradaError",
    "VersaoImutavelError",
    "CodigoDocumentalDuplicadoError",
    "IntegridadeInvalidaError",
    "ClassificacaoDocumentalNaoEncontradaError",
    "ClassificacaoDocumentalJaExisteError",
    "TramitacaoNaoEncontradaError",
    "ProcessoDocumentalNaoEncontradoError",
    "ProcessoDocumentalJaExisteError",
    "PermissaoNegadaError",
    "DocumentoNaoAssinadoError",
    "TemporalidadeNaoEncontradaError",
    "ArquivamentoInvalidoError",
    "EliminacaoNaoAutorizadaError",
    "TipoDocumentalInvalidoError",
]