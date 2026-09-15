"""Use Case: Criar Versão de Documento (versionamento).

Numera incrementalmente as versões (RN-GDO-005 — versões imutáveis).
"""

from dataclasses import dataclass
from datetime import datetime

from ...domain.entities import VersaoDocumento
from ...domain.exceptions import DocumentoNaoEncontradoError
from ..interfaces import (
    RepositorioDocumento,
    RepositorioVersaoDocumento,
)


@dataclass
class CriarVersaoInputDTO:
    documento_id: str
    conteudo_ref: str
    autor_id: str
    hash_integridade: str = ""


class CriarVersaoDocumentoUseCase:
    """Caso de uso para registrar uma nova versão do documento."""

    def __init__(
        self,
        repositorio_documento: RepositorioDocumento,
        repositorio_versao: RepositorioVersaoDocumento,
    ):
        self._repo_doc = repositorio_documento
        self._repo_versao = repositorio_versao

    def execute(self, dto: CriarVersaoInputDTO) -> VersaoDocumento:
        documento = self._repo_doc.get_by_id(dto.documento_id)
        if not documento:
            raise DocumentoNaoEncontradoError(f"Documento {dto.documento_id} não encontrado")

        ultima = self._repo_versao.get_ultima_versao(dto.documento_id)
        numero = (ultima.numero_versao + 1) if ultima else 1

        versao = VersaoDocumento(
            documento_id=dto.documento_id,
            numero_versao=numero,
            conteudo_ref=dto.conteudo_ref,
            hash_integridade=dto.hash_integridade,
            data_versao=datetime.utcnow(),
            created_by=dto.autor_id,
        )
        return self._repo_versao.save(versao)
