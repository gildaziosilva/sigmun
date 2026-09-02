"""Entidade Item de Compra do domínio Gestão de Compras e Contratações.

Baseado em:
  - 026-Modelo-de-Dominio (Entidade Item – material, serviço ou solução)
  - 013-Modelo-de-Dados (ENT-COMPRAS-004 – Item da Contratação)
  - Modelo Físico / migration 20260820_01 (Tabela: compras.itens_compras)

Regras de negócio implementadas:
  - RN-COMPRAS-011: descrição adequada e obrigatória do objeto
  - RN-COMPRAS-012: quantificação obrigatória (quantidade > 0)
  - Integridade aritmética: valor_total = quantidade × valor_unitario

Nota (RN-COMPRAS-013): unidade de medida ainda não compõe o modelo físico
de itens_compras; sua inclusão dependerá de evolução do modelo físico.

Um item representa um produto (material) ou serviço objeto de aquisição,
sempre vinculado a uma compra do domínio.
"""

from __future__ import annotations

from datetime import datetime
from decimal import ROUND_HALF_UP, Decimal
from uuid import UUID, uuid4

from src.shared.compat import UTC

_DOIS_DECIMAIS = Decimal("0.01")


class ItemCompra:
    """Entidade ItemCompra — bem ou serviço que compõe uma compra."""

    def __init__(
        self,
        id: UUID | None = None,
        compra_id: UUID | None = None,
        descricao: str = "",
        quantidade: Decimal = Decimal("0"),
        valor_unitario: Decimal = Decimal("0"),
        valor_total: Decimal | None = None,
        created_at: datetime | None = None,
        created_by: UUID | None = None,
        updated_at: datetime | None = None,
        updated_by: UUID | None = None,
        deleted_at: datetime | None = None,
        deleted_by: UUID | None = None,
    ) -> None:
        if compra_id is None:
            raise ValueError("compra_id é obrigatório para o item de compra")
        self.id: UUID = id or uuid4()
        self.compra_id: UUID = compra_id
        self.descricao: str = self._validar_descricao(descricao)
        self.quantidade: Decimal = self._validar_quantidade(quantidade)
        self.valor_unitario: Decimal = self._validar_valor(valor_unitario)
        self.valor_total: Decimal = (
            self.recalcular_valor_total() if valor_total is None else valor_total
        )
        self.created_at: datetime = created_at or datetime.now(UTC)
        self.created_by: UUID | None = created_by
        self.updated_at: datetime = updated_at or datetime.now(UTC)
        self.updated_by: UUID | None = updated_by
        self.deleted_at: datetime | None = deleted_at
        self.deleted_by: UUID | None = deleted_by

    # -- Validações (RN-COMPRAS-011/012) --------------------------------------

    @staticmethod
    def _validar_descricao(descricao: str) -> str:
        if descricao is None or not descricao.strip():
            raise ValueError(
                "descricao é obrigatória e deve ser adequada ao objeto "
                "(RN-COMPRAS-011)"
            )
        return descricao.strip()

    @staticmethod
    def _validar_quantidade(quantidade: Decimal) -> Decimal:
        quantidade = Decimal(quantidade)
        if quantidade <= 0:
            raise ValueError(f"quantidade deve ser maior que zero (RN-COMPRAS-012): {quantidade}")
        return quantidade

    @staticmethod
    def _validar_valor(valor: Decimal) -> Decimal:
        valor = Decimal(valor)
        if valor < 0:
            raise ValueError(f"valor não pode ser negativo: {valor}")
        return valor

    # -- Comportamentos de domínio -------------------------------------------

    def recalcular_valor_total(self) -> Decimal:
        """Recalcula o total do item (quantidade × valor_unitario)."""
        self.valor_total = (
            (self.quantidade * self.valor_unitario).quantize(_DOIS_DECIMAIS, rounding=ROUND_HALF_UP)
        )
        return self.valor_total

    def atualizar_dados(
        self,
        descricao: str | None = None,
        quantidade: Decimal | None = None,
        valor_unitario: Decimal | None = None,
        usuario_id: UUID | None = None,
    ) -> None:
        """Atualiza campos informados e recalcula o valor total."""
        # RN-COMPRAS-004: não operar sobre itens excluídos.
        if self.foi_excluido():
            raise ValueError("Item excluído não pode ser atualizado (RN-COMPRAS-004)")
        if descricao is not None:
            self.descricao = self._validar_descricao(descricao)
        if quantidade is not None:
            self.quantidade = self._validar_quantidade(quantidade)
        if valor_unitario is not None:
            self.valor_unitario = self._validar_valor(valor_unitario)
        self.recalcular_valor_total()
        self.updated_at = datetime.now(UTC)
        if usuario_id:
            self.updated_by = usuario_id

    def excluir(self, usuario_id: UUID) -> None:
        """Marca o item como excluído (soft-delete)."""
        self.deleted_at = datetime.now(UTC)
        self.deleted_by = usuario_id

    def foi_excluido(self) -> bool:
        """Retorna True se o item foi logicamente excluído."""
        return self.deleted_at is not None

    def pertence_a(self, compra_id: UUID) -> bool:
        """Verifica se o item pertence à compra informada."""
        return self.compra_id == compra_id


__all__ = ["ItemCompra"]
