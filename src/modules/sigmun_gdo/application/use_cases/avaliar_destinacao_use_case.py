"""Use Case: Avaliar Destinação de Documento.

RN-GDO-010/011 — eliminação exige autoridade homologadora;
RN-GDO-004 — a temporalidade orienta a destinação aplicada.
"""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from ..interfaces import RepositorioDocumento
from ...domain.entities import StatusDocumento
from ...domain.exceptions import (
    DocumentoNaoEncontradoError,
    EliminacaoNaoAutorizadaError,
    ArquivamentoInvalidoError,
)


class TipoDestinacaoAplicada(str, Enum):
    """Tipos de destinação que podem ser aplicadas ao documento."""

    ELIMINACAO = "eliminacao"
    GUARDA_PERMANENTE = "guarda_permanente"


@dataclass
class AvaliarDestinacaoInputDTO:
    documento_id: str
    tipo_destinacao: TipoDestinacaoAplicada
    autor_id: str
    autoridade_homologadora_id: str = ""
    justificativa: str = ""


class AvaliarDestinacaoUseCase:
    """Caso de uso para aplicar a destinação final ao documento."""

    def __init__(self, repositorio_documento: RepositorioDocumento):
        self._repo_doc = repositorio_documento

    def execute(self, dto: AvaliarDestinacaoInputDTO) -> None:
        documento = self._repo_doc.get_by_id(dto.documento_id)
        if not documento:
            raise DocumentoNaoEncontradoError(
                f"Documento {dto.documento_id} não encontrado"
            )

        if documento.status == StatusDocumento.RASCUNHO:
            raise ArquivamentoInvalidoError(
                "Documento em rascunho não possui destinação definida"
            )

        agora = datetime.utcnow()
        if dto.tipo_destinacao == TipoDestinacaoAplicada.ELIMINACAO:
            # RN-GDO-011: eliminação exige autoridade homologadora
            if not dto.autoridade_homologadora_id:
                raise EliminacaoNaoAutorizadaError(
                    "Eliminação requer autoridade homologadora (RN-GDO-011)"
                )
            documento.data_eliminacao = agora
            documento.status = StatusDocumento.ENCERRADO
        else:  # guarda permanente
            documento.unidade_arquivo_id = dto.autoridade_homologadora_id or (
                documento.unidade_arquivo_id
            )

        documento.updated_at = agora
        documento.updated_by = dto.autor_id
        self._repo_doc.save(documento)
