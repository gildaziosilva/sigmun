"""Use Case: Assinar Documento Digitalmente.

Calcula o hash SHA-256 do conteúdo (ServicoHashIntegridade), registra a
assinatura e fixa a integridade no documento (RN-GDO-002).
"""

from dataclasses import dataclass
from datetime import datetime

from ..interfaces import RepositorioDocumento, RepositorioAssinatura
from ...domain.entities import AssinaturaDocumento, StatusDocumento
from ...domain.exceptions import (
    DocumentoNaoEncontradoError,
    DocumentoJaExisteError,
    ArquivamentoInvalidoError,
)
from ...domain.services import ServicoHashIntegridade


@dataclass
class AssinarDocumentoInputDTO:
    documento_id: str
    signatario_id: str
    conteudo: str
    autor_id: str
    certificado_id: str = ""


class AssinarDocumentoUseCase:
    """Caso de uso para assinar digitalmente um documento."""

    def __init__(
        self,
        repositorio_documento: RepositorioDocumento,
        repositorio_assinatura: RepositorioAssinatura,
    ):
        self._repo_doc = repositorio_documento
        self._repo_ass = repositorio_assinatura

    def execute(self, dto: AssinarDocumentoInputDTO) -> AssinaturaDocumento:
        documento = self._repo_doc.get_by_id(dto.documento_id)
        if not documento:
            raise DocumentoNaoEncontradoError(
                f"Documento {dto.documento_id} não encontrado"
            )

        if documento.status in (StatusDocumento.ARQUIVADO, StatusDocumento.ENCERRADO):
            raise ArquivamentoInvalidoError(
                "Documento arquivado/encerrado não pode ser assinado"
            )
        # Integridade já fixada: novo conteúdo exige nova versão (RN-GDO-005)
        if documento.hash_integridade:
            raise DocumentoJaExisteError("Documento já possui assinatura registrada")

        hash_conteudo = ServicoHashIntegridade.calcular_hash(
            dto.conteudo.encode("utf-8")
        )
        assinatura = AssinaturaDocumento(
            documento_id=dto.documento_id,
            signatario_id=dto.signatario_id,
            data_assinatura=datetime.utcnow(),
            hash_assinatura=hash_conteudo,
            certificado_id=dto.certificado_id,
            is_valida=True,
            is_revogada=False,
        )
        self._repo_ass.save(assinatura)

        agora = datetime.utcnow()
        documento.hash_integridade = hash_conteudo
        documento.updated_at = agora
        documento.updated_by = dto.autor_id
        self._repo_doc.save(documento)

        return assinatura
