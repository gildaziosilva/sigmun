"""Entidade Endereço do Cadastro Único Municipal.

Baseado em:
  - Modelo-Fisico.md §4.1 (Tabela: core.enderecos)
  - 026-Modelo-de-Dominio-Cadastro-Unico-Municipal.md

Regras de negócio implementadas:
  - RN-CUM-005: unicidade de endereço principal vigente por pessoa
  - Histórico de vigência: alterações encerram a vigência anterior
    (``vigencia_fim`` NULL = endereço vigente)
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

from src.shared.compat import UTC


class TipoEndereco(str, Enum):
    """Tipos de endereço aceitos no cadastro."""

    RESIDENCIAL = "RESIDENCIAL"
    COMERCIAL = "COMERCIAL"
    COBRANCA = "COBRANCA"
    ENTREGA = "ENTREGA"
    OUTRO = "OUTRO"


class Endereco:
    """Endereço de uma pessoa, com histórico de vigência (1:N)."""

    def __init__(
        self,
        pessoa_id: UUID,
        tipo: TipoEndereco,
        logradouro: str,
        numero: str,
        id: UUID | None = None,
        complemento: str | None = None,
        bairro: str | None = None,
        cep: str | None = None,
        cidade: str | None = None,
        estado: str | None = None,
        pais: str | None = None,
        principal: bool = False,
        vigencia_inicio: datetime | None = None,
        vigencia_fim: datetime | None = None,
        motivo_alteracao: str | None = None,
        created_at: datetime | None = None,
        created_by: UUID | None = None,
        updated_at: datetime | None = None,
        updated_by: UUID | None = None,
        deleted_at: datetime | None = None,
        deleted_by: UUID | None = None,
    ) -> None:
        if not logradouro or not logradouro.strip():
            raise ValueError("Logradouro é obrigatório")
        if not numero or not numero.strip():
            raise ValueError("Número do endereço é obrigatório")
        self.id: UUID = id or uuid4()
        self.pessoa_id: UUID = pessoa_id
        self.tipo: TipoEndereco = tipo
        self.logradouro: str = logradouro.strip()
        self.numero: str = numero.strip()
        self.complemento: str | None = complemento
        self.bairro: str | None = bairro
        self.cep: str | None = cep
        self.cidade: str | None = cidade
        self.estado: str | None = estado
        self.pais: str | None = pais
        self.principal: bool = principal
        self.vigencia_inicio: datetime = vigencia_inicio or datetime.now(UTC)
        self.vigencia_fim: datetime | None = vigencia_fim
        self.motivo_alteracao: str | None = motivo_alteracao
        self.created_at: datetime = created_at or datetime.now(UTC)
        self.created_by: UUID | None = created_by
        self.updated_at: datetime = updated_at or datetime.now(UTC)
        self.updated_by: UUID | None = updated_by
        self.deleted_at: datetime | None = deleted_at
        self.deleted_by: UUID | None = deleted_by

    def esta_vigente(self) -> bool:
        """Retorna True se o endereço está vigente (não excluído, sem fim)."""
        return self.deleted_at is None and self.vigencia_fim is None

    def encerrar_vigencia(self, motivo: str | None = None) -> None:
        """Encerra a vigência do endereço preservando o histórico."""
        if self.vigencia_fim is None:
            self.vigencia_fim = datetime.now(UTC)
            self.motivo_alteracao = motivo
            self.updated_at = datetime.now(UTC)

    def excluir(self, usuario_id: UUID | None) -> None:
        """Soft-delete do endereço (RN-CUM-007)."""
        self.deleted_at = datetime.now(UTC)
        self.deleted_by = usuario_id

    def foi_excluido(self) -> bool:
        """Retorna True se o endereço foi logicamente excluído."""
        return self.deleted_at is not None


__all__ = ["Endereco", "TipoEndereco"]
