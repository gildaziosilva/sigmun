"""Use Case: Arquivar Documento.

RN-GDO-008 — Arquivamento somente após conclusão (documento ativo).
"""

from dataclasses import dataclass
from datetime import datetime

from ..interfaces import RepositorioDocumento, RepositorioArquivamento
from ...domain.entities import ArquivamentoDocumento, StatusDocumento
from ...domain.exceptions import (
    DocumentoNaoEncontradoError,
    ArquivamentoInvalidoError,
)


@dataclass
class ArquivarDocumentoInputDTO:
    documento_id: str
    unidade_arquivo_id: str
    autor_id: str
    observacao: str = ""


class ArquivarDocumentoUseCase:
    """Caso de uso para arquivar um documento corrente."""

    def __init__(
        self,
        repositorio_documento: RepositorioDocumento,
        repositorio_arquivamento: RepositorioArquivamento,
    ):
        self._repo_doc = repositorio_documento
        self._repo_arq = repositorio_arquivamento

    def execute(self, dto: ArquivarDocumentoInputDTO) -> ArquivamentoDocumento:
        documento = self._repo_doc.get_by_id(dto.documento_id)
        if not documento:
            raise DocumentoNaoEncontradoError(
                f"Documento {dto.documento_id} não encontrado"
            )

        # RN-GDO-008: apenas documentos ativos podem ser arquivados
        if documento.status == StatusDocumento.ARQUIVADO:
            raise ArquivamentoInvalidoError("Documento já se encontra arquivado")
        if documento.status in (StatusDocumento.ENCERRADO, StatusDocumento.REJEITADO):
            raise ArquivamentoInvalidoError(
                "Documento encerrado/rejeitado não pode ser arquivado"
            )

        agora = datetime.utcnow()
        arquivamento = ArquivamentoDocumento(
            documento_id=dto.documento_id,
            data_arquivamento=agora,
            created_by=dto.autor_id,
            observacao=dto.observacao,
        )
        self._repo_arq.save(arquivamento)

        documento.status = StatusDocumento.ARQUIVADO
        documento.data_arquivamento = agora
        documento.unidade_arquivo_id = dto.unidade_arquivo_id
        documento.updated_at = agora
        documento.updated_by = dto.autor_id
        self._repo_doc.save(documento)

        return arquivamento
