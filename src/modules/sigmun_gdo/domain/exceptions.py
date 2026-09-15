"""Exceções de domínio do módulo de Gestão Documental."""


class DocumentalDomainError(Exception):
    """Base das exceções de negócio do domínio Documental (espelho DOM-COMPRAS-001)."""

    pass


class DocumentoNaoEncontradoError(DocumentalDomainError):
    """Documento não encontrado."""

    pass


class DocumentoJaCadastradoError(DocumentalDomainError):
    """Documento já existe."""

    pass


class VersaoDocumentoNaoEncontradaError(DocumentalDomainError):
    """Versão de documento não encontrada."""

    pass


class VersaoImutavelError(DocumentalDomainError):
    """Tentativa de modificar uma versão imutável."""

    pass


class CodigoDocumentalDuplicadoError(DocumentalDomainError):
    """Código documental já utilizado por outro tipo."""

    pass


class IntegridadeInvalidaError(DocumentalDomainError):
    """Hash de integridade inválido ou inconsistente."""

    pass


class ClassificacaoDocumentalNaoEncontradaError(DocumentalDomainError):
    """Classificação documental não encontrada."""

    pass


class ClassificacaoDocumentalDuplicadaError(DocumentalDomainError):
    """Classificação documental já cadastrada."""

    pass


class TramitacaoNaoEncontradaError(DocumentalDomainError):
    """Tramitação não encontrada."""

    pass


class ProcessoDocumentalNaoEncontradoError(DocumentalDomainError):
    """Processo documental não encontrado."""

    pass


class ProcessoDocumentalDuplicadoError(DocumentalDomainError):
    """Processo documental já existe."""

    pass


class PermissaoNegadaError(DocumentalDomainError):
    """Permissão negada para a operação solicitada."""

    pass


class DocumentoNaoAssinadoError(DocumentalDomainError):
    """Documento não possui assinatura válida."""

    pass


class TemporalidadeNaoEncontradaError(DocumentalDomainError):
    """Temporalidade não encontrada."""

    pass


class ArquivamentoInvalidoError(DocumentalDomainError):
    """Operação de arquivamento inválida (documento em fase de corrente)."""

    pass


class EliminacaoNaoAutorizadaError(DocumentalDomainError):
    """Eliminação não autorizada (falta de autoridade homologadora)."""

    pass


class TipoDocumentalInvalidoError(DocumentalDomainError):
    """Tipo documental não encontrado ou inativo."""

    pass


__all__ = [
    "DocumentalDomainError",
    "DomainException",
    "DocumentoNaoEncontradoError",
    "DocumentoJaCadastradoError",
    "DocumentoJaExisteError",
    "VersaoDocumentoNaoEncontradaError",
    "VersaoImutavelError",
    "CodigoDocumentalDuplicadoError",
    "IntegridadeInvalidaError",
    "ClassificacaoDocumentalNaoEncontradaError",
    "ClassificacaoDocumentalDuplicadaError",
    "ClassificacaoDocumentalJaExisteError",
    "TramitacaoNaoEncontradaError",
    "ProcessoDocumentalNaoEncontradoError",
    "ProcessoDocumentalDuplicadoError",
    "ProcessoDocumentalJaExisteError",
    "PermissaoNegadaError",
    "DocumentoNaoAssinadoError",
    "TemporalidadeNaoEncontradaError",
    "ArquivamentoInvalidoError",
    "EliminacaoNaoAutorizadaError",
    "TipoDocumentalInvalidoError",
]


# ---------------------------------------------------------------------------
# Aliases de compatibilidade.
# ---------------------------------------------------------------------------
DomainException = DocumentalDomainError
DocumentoJaExisteError = DocumentoJaCadastradoError
ClassificacaoDocumentalJaExisteError = ClassificacaoDocumentalDuplicadaError
ProcessoDocumentalJaExisteError = ProcessoDocumentalDuplicadoError
