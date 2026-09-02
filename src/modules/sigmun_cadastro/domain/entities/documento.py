"""Entidade Documento do Cadastro Único Municipal.

Baseado em:
  - Modelo-Fisico.md §4.1 (Tabela: core.documentos)
  - 026-Modelo-de-Dominio-Cadastro-Unico-Municipal.md

Regras de negócio implementadas:
  - RN-CUM-006: unicidade de documento principal por tipo por pessoa
  - LGPD: o número é dado pessoal — criptografia em repouso na fase de
    segurança (modelo físico: 'LGPD: criptografado (AES-256)')
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from uuid import UUID, uuid4

from src.shared.compat import UTC


class TipoDocumento(str, Enum):
    """Tipos de documento aceitos no cadastro."""

    CPF = "CPF"
    CNPJ = "CNPJ"
    RG = "RG"
    INSCRICAO_ESTADUAL = "INSCRICAO_ESTADUAL"
    INSCRICAO_MUNICIPAL = "INSCRICAO_MUNICIPAL"
    CNH = "CNH"
    OUTRO = "OUTRO"


class Documento:
    """Documento de identificação vinculado a uma pessoa (1:N)."""

    def __init__(
        self,
        pessoa_id: UUID,
        tipo: TipoDocumento,
        numero: str,
        id: UUID | None = None,
        orgao_emissor: str | None = None,
        data_emissao: date | None = None,
        data_validade: date | None = None,
        principal: bool = False,
        created_at: datetime | None = None,
        created_by: UUID | None = None,
        updated_at: datetime | None = None,
        updated_by: UUID | None = None,
        deleted_at: datetime | None = None,
        deleted_by: UUID | None = None,
    ) -> None:
        if not numero or not numero.strip():
            raise ValueError("Número do documento é obrigatório")
        self.id: UUID = id or uuid4()
        self.pessoa_id: UUID = pessoa_id
        self.tipo: TipoDocumento = tipo
        self.numero: str = numero.strip()
        self.orgao_emissor: str | None = orgao_emissor
        self.data_emissao: date | None = data_emissao
        self.data_validade: date | None = data_validade
        self.principal: bool = principal
        self.created_at: datetime = created_at or datetime.now(UTC)
        self.created_by: UUID | None = created_by
        self.updated_at: datetime = updated_at or datetime.now(UTC)
        self.updated_by: UUID | None = updated_by
        self.deleted_at: datetime | None = deleted_at
        self.deleted_by: UUID | None = deleted_by

    def excluir(self, usuario_id: UUID | None) -> None:
        """Soft-delete do documento (RN-CUM-007)."""
        self.deleted_at = datetime.now(UTC)
        self.deleted_by = usuario_id

    def esta_vigente(self, referencia: date | None = None) -> bool:
        """Retorna True se o documento não está excluído nem vencido."""
        if self.deleted_at is not None:
            return False
        if self.data_validade is None:
            return True
        return referencia is None or self.data_validade >= referencia

    def foi_excluido(self) -> bool:
        """Retorna True se o documento foi logicamente excluído."""
        return self.deleted_at is not None


__all__ = ["Documento", "TipoDocumento"]
