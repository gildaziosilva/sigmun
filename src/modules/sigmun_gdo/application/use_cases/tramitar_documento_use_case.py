"""Use Case: Tramitar Documento."""

from dataclasses import dataclass
from datetime import datetime

from ...domain.entities import TipoTramitacao, TramitacaoDocumento
from ...domain.exceptions import DocumentoNaoEncontradoError
from ..interfaces import RepositorioDocumento, RepositorioTramitacao


@dataclass
class TramitarDocumentoInputDTO:
    documento_id: str
    unidade_origem_id: str
    unidade_destino_id: str
    tipo: TipoTramitacao
    motivo: str
    autor_id: str
    observacao: str = ""


class TramitarDocumentoUseCase:
    """Caso de uso para tramitar um documento entre unidades."""

    def __init__(
        self,
        repositorio_documento: RepositorioDocumento,
        repositorio_tramitacao: RepositorioTramitacao,
    ):
        self._repo_doc = repositorio_documento
        self._repo_tram = repositorio_tramitacao

    def execute(self, dto: TramitarDocumentoInputDTO) -> TramitacaoDocumento:
        documento = self._repo_doc.get_by_id(dto.documento_id)
        if not documento:
            raise DocumentoNaoEncontradoError(f"Documento {dto.documento_id} não encontrado")

        tramitacao = TramitacaoDocumento(
            documento_id=dto.documento_id,
            unidade_origem_id=dto.unidade_origem_id,
            unidade_destino_id=dto.unidade_destino_id,
            tipo=dto.tipo,
            data_envio=datetime.utcnow(),
            motivo=dto.motivo,
            observacao=dto.observacao,
            created_by=dto.autor_id,
        )
        return self._repo_tram.save(tramitacao)
