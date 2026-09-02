"""Interface de repositório para Fornecedor.

Define o contrato que a camada de infraestrutura deverá implementar.
Baseado em:
  - 025-Estrutura-Tecnica (RepositorioDeFornecedores)
  - 013-Modelo-de-Dados (Tabela: core.fornecedores)
  - 005-Casos-de-Uso (UC-COMPRAS-019 a UC-COMPRAS-021)
"""

from __future__ import annotations

import builtins
from abc import ABC, abstractmethod
from uuid import UUID

from src.modules.sigmun_compras.domain.entities.fornecedor import (
    Fornecedor,
    SituacaoFornecedor,
)


class FornecedorRepository(ABC):
    """Abstração de repositório para a entidade Fornecedor."""

    @abstractmethod
    def save(self, fornecedor: Fornecedor) -> Fornecedor:
        """Persiste (cria ou atualiza) um fornecedor."""

    @abstractmethod
    def get_by_id(self, fornecedor_id: UUID) -> Fornecedor | None:
        """Retorna um fornecedor pelo ID ou None se não existir."""

    @abstractmethod
    def get_by_pessoa_juridica_id(
        self, pessoa_juridica_id: UUID
    ) -> Fornecedor | None:
        """Retorna um fornecedor pela pessoa jurídica referenciada."""

    @abstractmethod
    def list(
        self,
        situacao: SituacaoFornecedor | None = None,
        include_deleted: bool = False,
        limit: int | None = None,
        offset: int = 0,
    ) -> builtins.list[Fornecedor]:
        """Lista fornecedores, opcionalmente filtrando por situação."""

    @abstractmethod
    def update(self, fornecedor: Fornecedor) -> Fornecedor:
        """Atualiza os dados de um fornecedor existente."""

    @abstractmethod
    def delete(self, fornecedor_id: UUID, usuario_id: UUID) -> None:
        """Exclui logicamente (soft-delete) um fornecedor."""

    @abstractmethod
    def exists_pessoa_juridica(self, pessoa_juridica_id: UUID) -> bool:
        """Verifica se já existe um fornecedor para a pessoa jurídica informada.

        RN-COMPRAS-031: Unicidade Cadastral.
        """
