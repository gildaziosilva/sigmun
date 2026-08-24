"""Entidade Compra (processo de compras) do domínio Gestão de Compras.

Baseado em:
  - 013-Modelo-de-Dados (Processo de Contratação – ENT-COMPRAS-003;
    tabela consolidada compras.compras)
  - 026-Modelo-de-Dominio (Estados do Processo)
  - Modelo Físico / migration 20260820_01

Regras de negócio implementadas:
  - RN-COMPRAS-025: atos vinculados ao processo administrativo
    (processo_documental_id obrigatório e existente)
  - RN-COMPRAS-026: transições respeitam a sequência processual
  - RN-COMPRAS-027: pendências impeditivas bloqueiam avanço (transições)
  - RN-COMPRAS-028: responsável registrado em cada alteração
  - RN-COMPRAS-029: registro temporal das alterações

Nota: a entidade Requisição/Solicitação (ENT-COMPRAS-001 – Demanda) ainda
não possui modelo físico próprio; sua implementação dependerá de evolução
do modelo físico (nova migração).
"""

from __future__ import annotations

from datetime import UTC, date, datetime
from decimal import Decimal
from enum import Enum
from uuid import UUID, uuid4


class SituacaoCompra(str, Enum):
    """Estados do processo de compras (013-Modelo-de-Dados, seção 30)."""

    RASCUNHO = "RASCUNHO"
    EM_INSTRUCAO = "EM_INSTRUCAO"
    EM_ANALISE = "EM_ANALISE"
    EM_PROCEDIMENTO = "EM_PROCEDIMENTO"
    EM_JULGAMENTO = "EM_JULGAMENTO"
    HOMOLOGADO = "HOMOLOGADO"
    CONTRATADO = "CONTRATADO"
    ENCERRADO = "ENCERRADO"
    CANCELADO = "CANCELADO"
    ARQUIVADO = "ARQUIVADO"


#: Transições válidas (RN-COMPRAS-026/027). Estado ausente no mapa ou com
#: conjunto vazio é terminal.
TRANSICOES_VALIDAS: dict[SituacaoCompra, set[SituacaoCompra]] = {
    SituacaoCompra.RASCUNHO: {SituacaoCompra.EM_INSTRUCAO, SituacaoCompra.CANCELADO},
    SituacaoCompra.EM_INSTRUCAO: {SituacaoCompra.EM_ANALISE, SituacaoCompra.CANCELADO},
    SituacaoCompra.EM_ANALISE: {
        SituacaoCompra.EM_PROCEDIMENTO,
        SituacaoCompra.CANCELADO,
    },
    SituacaoCompra.EM_PROCEDIMENTO: {
        SituacaoCompra.EM_JULGAMENTO,
        SituacaoCompra.CANCELADO,
    },
    SituacaoCompra.EM_JULGAMENTO: {SituacaoCompra.HOMOLOGADO, SituacaoCompra.CANCELADO},
    SituacaoCompra.HOMOLOGADO: {SituacaoCompra.CONTRATADO, SituacaoCompra.CANCELADO},
    SituacaoCompra.CONTRATADO: {SituacaoCompra.ENCERRADO},
    SituacaoCompra.ENCERRADO: {SituacaoCompra.ARQUIVADO},
    SituacaoCompra.CANCELADO: {SituacaoCompra.ARQUIVADO},
    SituacaoCompra.ARQUIVADO: set(),
}


class Compra:
    """Entidade Compra — processo de compras vinculado a um processo documental."""

    def __init__(
        self,
        id: UUID | None = None,
        processo_documental_id: UUID | None = None,
        fornecedor_id: UUID | None = None,
        unidade_id: UUID | None = None,
        numero: str = "",
        data: date | None = None,
        valor_total: Decimal | None = None,
        situacao: SituacaoCompra = SituacaoCompra.RASCUNHO,
        created_at: datetime | None = None,
        created_by: UUID | None = None,
        updated_at: datetime | None = None,
        updated_by: UUID | None = None,
        deleted_at: datetime | None = None,
        deleted_by: UUID | None = None,
    ) -> None:
        if processo_documental_id is None:
            raise ValueError("processo_documental_id é obrigatório (RN-COMPRAS-025)")
        if fornecedor_id is None:
            raise ValueError("fornecedor_id é obrigatório")
        if unidade_id is None:
            raise ValueError("unidade_id é obrigatório")
        self.id: UUID = id or uuid4()
        self.processo_documental_id: UUID = processo_documental_id
        self.fornecedor_id: UUID = fornecedor_id
        self.unidade_id: UUID = unidade_id
        self.numero: str = self._validar_numero(numero)
        self.data: date = data if data is not None else datetime.now(UTC).date()
        self.valor_total: Decimal | None = self._validar_valor_total(valor_total)
        self.situacao: SituacaoCompra = self._validar_situacao(situacao)
        self.created_at: datetime = created_at or datetime.now(UTC)
        self.created_by: UUID | None = created_by
        self.updated_at: datetime = updated_at or datetime.now(UTC)
        self.updated_by: UUID | None = updated_by
        self.deleted_at: datetime | None = deleted_at
        self.deleted_by: UUID | None = deleted_by

    # -- Validações -----------------------------------------------------------

    @staticmethod
    def _validar_numero(numero: str) -> str:
        if numero is None or not numero.strip():
            raise ValueError("numero da compra é obrigatório")
        return numero.strip()

    @staticmethod
    def _validar_valor_total(valor: Decimal | None) -> Decimal | None:
        if valor is None:
            return None
        valor = Decimal(valor)
        if valor < 0:
            raise ValueError(f"valor_total não pode ser negativo: {valor}")
        return valor

    @staticmethod
    def _validar_situacao(situacao: SituacaoCompra) -> SituacaoCompra:
        if not isinstance(situacao, SituacaoCompra):
            raise ValueError(f"Situação inválida: {situacao}")
        return situacao

    # -- Comportamentos de domínio -------------------------------------------

    def pode_transicionar_para(self, nova_situacao: SituacaoCompra) -> bool:
        """Verifica se a transição é permitida pela sequência processual."""
        return nova_situacao in TRANSICOES_VALIDAS.get(self.situacao, set())

    def alterar_situacao(self, nova_situacao: SituacaoCompra, usuario_id: UUID) -> None:
        """Altera a situação respeitando a sequência processual (RN-026/027)."""
        nova_situacao = self._validar_situacao(nova_situacao)
        if nova_situacao == self.situacao:
            return
        if not self.pode_transicionar_para(nova_situacao):
            validas = sorted(t.value for t in TRANSICOES_VALIDAS[self.situacao])
            raise ValueError(
                f"Transição {self.situacao.value} -> {nova_situacao.value} não permitida "
                f"(RN-COMPRAS-026). Transições válidas a partir de "
                f"{self.situacao.value}: {validas}"
            )
        self.situacao = nova_situacao
        self.updated_at = datetime.now(UTC)
        self.updated_by = usuario_id

    def atualizar_dados(
        self,
        numero: str | None = None,
        data: date | None = None,
        valor_total: Decimal | None = None,
        usuario_id: UUID | None = None,
    ) -> None:
        """Atualiza campos cadastrais da compra (RN-COMPRAS-028/029)."""
        if numero is not None:
            self.numero = self._validar_numero(numero)
        if data is not None:
            self.data = data
        if valor_total is not None:
            self.valor_total = self._validar_valor_total(valor_total)
        self.updated_at = datetime.now(UTC)
        if usuario_id:
            self.updated_by = usuario_id

    def excluir(self, usuario_id: UUID) -> None:
        """Marca a compra como excluída (soft-delete, preserva histórico)."""
        self.deleted_at = datetime.now(UTC)
        self.deleted_by = usuario_id

    def foi_excluido(self) -> bool:
        """Retorna True se a compra foi logicamente excluída."""
        return self.deleted_at is not None

    def esta_cancelada(self) -> bool:
        return self.situacao in (SituacaoCompra.CANCELADO, SituacaoCompra.ARQUIVADO)


__all__ = ["Compra", "SituacaoCompra", "TRANSICOES_VALIDAS"]
