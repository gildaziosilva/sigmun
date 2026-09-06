"""Use Case: Classificar Documento."""

from dataclasses import dataclass
from typing import Optional

from ..interfaces import (
    RepositorioDocumento,
    RepositorioClassificacaoDocumental,
)
from ...domain.entities import Documento
from ...domain.exceptions import (
    DocumentoNaoEncontradoError,
    ClassificacaoDocumentalNaoEncontradaError,
)
from ...domain.events import EventoDocumentoClassificado


@dataclass
class ClassificarDocumentoInputDTO:
    id: str
    classificacao_id: str
    autor_id: str


class ClassificarDocumentoUseCase:
    """Caso de uso para classificar um documento."""

    def __init__(
        self,
        repositorio_documento: RepositorioDocumento,
        repositorio_classificacao: RepositorioClassificacaoDocumental,
    ):
        self._repo_doc = repositorio_documento
        self._repo_class = repositorio_classificacao

    def execute(self, dto: ClassificarDocumentoInputDTO) -> bool:
        documento = self._repo_doc.get_by_id(dto.id)
        if not documento:
            raise DocumentoNaoEncontradoError(f"Documento {dto.id} não encontrado")

        classificacao = self._repo_class.get_by_id(dto.classificacao_id)
        if not classificacao:
            raise ClassificacaoDocumentalNaoEncontradaError(
                f"Classificação {dto.classificacao_id} não encontrada"
            )

        # Atualiza vinculo (simplificado — pode usar tabela associativa)
        documento.tipo_documental_id = dto.classificacao_id
        self._repo_doc.save(documento)

        # Evento de domínio
        evento = EventoDocumentoClassificado(
            documento_id=documento.id,
            usuario_id=dto.autor_id,
            payload={"classificacao_id": dto.classificacao_id},
        )
        return True
