"""Entidade Fornecedor do domínio Gestão de Compras e Contratações.

Baseado em:
  - 026-Modelo-de-Dominio-Gestao-de-Compras-e-Contratacoes.md (ENT-COMPRAS-007)
  - 013-Modelo-de-Dados-Gestao-de-Compras-e-Contratacoes.md (Tabela: core.fornecedores)
  - 007-Regras-de-Negocio-Gestao-de-Compras-e-Contratacoes.md (RN-COMPRAS-030 a 033)

Regras de negócio implementadas:
  - RN-COMPRAS-030: identificação suficiente (fornecedor deve referenciar pessoa jurídica)
  - RN-COMPRAS-031: unicidade cadastral (uma pessoa_juridica_id por fornecedor)
  - RN-COMPRAS-032: histórico rastreável (audit columns)
  - RN-COMPRAS-033: alterações preservam histórico de auditoria
"""

from __future__ import annotations

from datetime import UTC, datetime
from enum import Enum
from uuid import UUID, uuid4


class SituacaoFornecedor(str, Enum):
    """Situação cadastral do fornecedor (RN-COMPRAS-030)."""

    ATIVO = "ATIVO"
    INATIVO = "INATIVO"
    SUSPENSO = "SUSPENSO"


class Fornecedor:
    """Entidade Fornecedor (ENT-COMPRAS-007).

    Representa o fornecedor participante ou contratado.
    Preferencialmente referenciado a partir do Cadastro Único Municipal
    (pessoa jurídica corporativa).
    """

    def __init__(
        self,
        id: UUID | None = None,
        pessoa_juridica_id: UUID | None = None,
        situacao_cadastro: SituacaoFornecedor = SituacaoFornecedor.ATIVO,
        macro_categoria: str | None = None,
        created_at: datetime | None = None,
        created_by: UUID | None = None,
        updated_at: datetime | None = None,
        updated_by: UUID | None = None,
        deleted_at: datetime | None = None,
        deleted_by: UUID | None = None,
    ) -> None:
        self.id: UUID = id or uuid4()
        self.pessoa_juridica_id: UUID | None = pessoa_juridica_id
        self.situacao_cadastro: SituacaoFornecedor = situacao_cadastro
        self.macro_categoria: str | None = macro_categoria
        self.created_at: datetime = created_at or datetime.now(UTC)
        self.created_by: UUID | None = created_by
        self.updated_at: datetime = updated_at or datetime.now(UTC)
        self.updated_by: UUID | None = updated_by
        self.deleted_at: datetime | None = deleted_at
        self.deleted_by: UUID | None = deleted_by

    # -- Comportamentos de domínio -------------------------------------------

    def inativar(self, usuario_id: UUID) -> None:
        """Inativa o fornecedor (RN-COMPRAS-033)."""
        self.situacao_cadastro = SituacaoFornecedor.INATIVO
        self._registrar_alteracao(usuario_id)

    def ativar(self, usuario_id: UUID) -> None:
        """Reativa o fornecedor."""
        self.situacao_cadastro = SituacaoFornecedor.ATIVO
        self._registrar_alteracao(usuario_id)

    def suspender(self, usuario_id: UUID) -> None:
        """Suspende o fornecedor."""
        self.situacao_cadastro = SituacaoFornecedor.SUSPENSO
        self._registrar_alteracao(usuario_id)

    def atualizar_situacao(self, situacao: SituacaoFornecedor, usuario_id: UUID) -> None:
        """Atualiza a situação cadastral do fornecedor."""
        if not isinstance(situacao, SituacaoFornecedor):
            raise ValueError(f"Situação inválida: {situacao}")
        self.situacao_cadastro = situacao
        self._registrar_alteracao(usuario_id)

    def atualizar_categoria(self, macro_categoria: str | None) -> None:
        """Atualiza a macro categoria do fornecedor."""
        self.macro_categoria = macro_categoria
        self._registrar_alteracao(None)

    def excluir(self, usuario_id: UUID) -> None:
        """Marca o fornecedor como excluído (soft-delete, RN-COMPRAS-032)."""
        self.deleted_at = datetime.now(UTC)
        self.deleted_by = usuario_id

    def esta_ativo(self) -> bool:
        """Retorna True se o fornecedor está com situação ativa."""
        return self.situacao_cadastro == SituacaoFornecedor.ATIVO

    def foi_excluido(self) -> bool:
        """Retorna True se o fornecedor foi logicamente excluído."""
        return self.deleted_at is not None

    # -- Internals ----------------------------------------------------------

    def _registrar_alteracao(self, usuario_id: UUID | None) -> None:
        """Atualiza timestamps e auditoria de alteração."""
        self.updated_at = datetime.now(UTC)
        if usuario_id:
            self.updated_by = usuario_id
