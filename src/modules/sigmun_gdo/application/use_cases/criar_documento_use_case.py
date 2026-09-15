"""Use Case: Criar Documento Digital.

Baseado em ESP-GDO-001 — Especificação de Criação de Documento.
"""

from dataclasses import dataclass
from datetime import datetime

from ...domain.entities import Documento, StatusDocumento
from ...domain.exceptions import (
    CodigoDocumentalDuplicadoError,
    IntegridadeInvalidaError,
    TipoDocumentalInvalidoError,
)
from ..interfaces import RepositorioDocumento, RepositorioTipoDocumental


@dataclass
class CriarDocumentoInputDTO:
    """DTO de entrada para criação de documento."""

    codigo: str
    numero: str
    ano: int
    tipo_documental_id: str
    titulo: str
    descricao: str
    unidade_autor_id: str
    processo_id: str | None = None
    unidade_arquivo_id: str | None = None
    is_sigiloso: bool = False
    conteudo_ref: str = ""
    hash_integridade: str = ""
    created_by: str = ""


@dataclass
class CriarDocumentoOutputDTO:
    """DTO de saída para criação de documento."""

    id: str
    codigo: str
    numero: str
    titulo: str
    status: str
    is_sigiloso: bool
    created_at: datetime
    hash_integridade: str


class CriarDocumentoUseCase:
    """Caso de uso para criar um documento digital.

    Regra RN-GDO-001 (Unicidade de código): verifica se código já existe.
    Regra RN-GDO-002 (Integridade por hash): se hash informado, valida tamanho SHA-256.
    Regra RN-GDO-005 (Versão imutável): versão é criada separadamente.
    """

    def __init__(
        self,
        repositorio_documento: RepositorioDocumento,
        repositorio_tipo_documental: RepositorioTipoDocumental,
    ):
        self._repo = repositorio_documento
        self._repo_tipo = repositorio_tipo_documental

    def execute(self, dto: CriarDocumentoInputDTO) -> CriarDocumentoOutputDTO:
        """Executa o caso de uso."""
        # RF-GDO-004: Verificar unicidade do código (RN-GDO-001)
        documento_existente = self._repo.get_by_codigo(dto.codigo, dto.ano)
        if documento_existente:
            raise CodigoDocumentalDuplicadoError(
                f"Código '{dto.codigo}' já utilizado pelo documento {documento_existente.id}"
            )

        # Validação: tipo documental deve existir e estar ativo
        tipo_documental = self._repo_tipo.get_by_codigo(dto.tipo_documental_id)
        if not tipo_documental:
            raise TipoDocumentalInvalidoError(
                f"Tipo documental '{dto.tipo_documental_id}' não encontrado ou inativo"
            )

        # RF-GDO-005: Validar hash de integridade (RN-GDO-002)
        hash_final = dto.hash_integridade
        if hash_final and len(hash_final) != 64:
            raise IntegridadeInvalidaError(
                "Hash de integridade inválido. Deve ser SHA-256 (64 hex chars)"
            )

        # Criar entidade
        documento = Documento(
            codigo=dto.codigo,
            numero=dto.numero,
            ano=dto.ano,
            tipo_documental_id=dto.tipo_documental_id,
            titulo=dto.titulo,
            descricao=dto.descricao,
            unidade_autor_id=dto.unidade_autor_id,
            unidade_arquivo_id=dto.unidade_arquivo_id or "",
            processo_id=dto.processo_id or "",
            status=StatusDocumento.ATIVO,
            is_sigiloso=dto.is_sigiloso,
            conteudo_ref=dto.conteudo_ref,
            hash_integridade=hash_final,
            created_by=dto.created_by,
            created_at=datetime.utcnow(),
        )

        # Persistir
        documento_salvo = self._repo.save(documento)

        return CriarDocumentoOutputDTO(
            id=documento_salvo.id,
            codigo=documento_salvo.codigo,
            numero=documento_salvo.numero,
            titulo=documento_salvo.titulo,
            status=documento_salvo.status.value,
            is_sigiloso=documento_salvo.is_sigiloso,
            created_at=documento_salvo.created_at,
            hash_integridade=documento_salvo.hash_integridade,
        )
