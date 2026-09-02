"""Entidade Contrato do domínio Gestão de Compras.

Baseado em:
  - 013-Modelo-de-Dados (ENT-COMPRAS-009 – Contrato)
  - 026-Modelo-de-Dominio (Estados do Contrato)
  - Modelo Físico / migration 20260820_01 (Tabela: compras.contratos)

Regras de negócio implementadas:
  - RN-COMPRAS-036: identificação única (numero não duplicado)
  - RN-COMPRAS-037: vigência coerente (data_fim >= data_inicio)
  - RN-COMPRAS-038: vínculo ao objeto/processo contratado
  - RN-COMPRAS-039: valor contratual não negativo
  - RN-COMPRAS-046: controle de vigência (entrada em vigor e termo final)
  - RN-COMPRAS-004: integridade do histórico (não operar sobre excluídos)

Estados (013-Modelo-de-Dados, seção 30): EM_ELABORACAO, ASSINADO,
VIGENTE, SUSPENSO, ENCERRADO, RESCINDIDO, EXTINTO.
"""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from src.shared.compat import UTC


class SituacaoContrato(str, Enum):
    """Estados do contrato (013-Modelo-de-Dados, seção 30)."""

    EM_ELABORACAO = "EM_ELABORACAO"
    ASSINADO = "ASSINADO"
    VIGENTE = "VIGENTE"
    SUSPENSO = "SUSPENSO"
    ENCERRADO = "ENCERRADO"
    RESCINDIDO = "RESCINDIDO"
    EXTINTO = "EXTINTO"


#: Transições válidas. Estados com conjunto vazio são terminais.
TRANSICOES_VALIDAS: dict[SituacaoContrato, set[SituacaoContrato]] = {
    SituacaoContrato.EM_ELABORACAO: {SituacaoContrato.ASSINADO},
    SituacaoContrato.ASSINADO: {SituacaoContrato.VIGENTE},
    SituacaoContrato.VIGENTE: {
        SituacaoContrato.SUSPENSO,
        SituacaoContrato.ENCERRADO,
        SituacaoContrato.RESCINDIDO,
    },
    SituacaoContrato.SUSPENSO: {
        SituacaoContrato.VIGENTE,
        SituacaoContrato.ENCERRADO,
        SituacaoContrato.RESCINDIDO,
        SituacaoContrato.EXTINTO,
    },
    SituacaoContrato.ENCERRADO: set(),
    SituacaoContrato.RESCINDIDO: set(),
    SituacaoContrato.EXTINTO: set(),
}

#: Estados terminais do contrato (não admitem novas transições nem
#: alteração cadastral). Baseado em 013-Modelo-de-Dados, seção 30.
ESTADOS_TERMINAIS: frozenset[SituacaoContrato] = frozenset(
    {
        SituacaoContrato.ENCERRADO,
        SituacaoContrato.RESCINDIDO,
        SituacaoContrato.EXTINTO,
    }
)


class Contrato:
    """Entidade Contrato — instrumento formal da contratação."""

    def __init__(
        self,
        id: Optional[UUID] = None,
        processo_documental_id: Optional[UUID] = None,
        fornecedor_id: Optional[UUID] = None,
        unidade_id: Optional[UUID] = None,
        licitacao_master_id: Optional[UUID] = None,
        compra_id: Optional[UUID] = None,
        numero: str = "",
        data_inicio: Optional[date] = None,
        data_fim: Optional[date] = None,
        valor: Optional[Decimal] = None,
        objeto: Optional[str] = None,
        situacao: SituacaoContrato = SituacaoContrato.EM_ELABORACAO,
        created_at: Optional[datetime] = None,
        created_by: Optional[UUID] = None,
        updated_at: Optional[datetime] = None,
        updated_by: Optional[UUID] = None,
        deleted_at: Optional[datetime] = None,
        deleted_by: Optional[UUID] = None,
    ) -> None:
        if processo_documental_id is None:
            raise ValueError("processo_documental_id é obrigatório (RN-COMPRAS-038)")
        if fornecedor_id is None:
            raise ValueError("fornecedor_id é obrigatório")
        if unidade_id is None:
            raise ValueError("unidade_id é obrigatório")
        self.id: UUID = id or uuid4()
        self.processo_documental_id: UUID = processo_documental_id
        self.fornecedor_id: UUID = fornecedor_id
        self.unidade_id: UUID = unidade_id
        self.licitacao_master_id: Optional[UUID] = licitacao_master_id
        self.compra_id: Optional[UUID] = compra_id
        self.numero: str = self._validar_numero(numero)
        self.data_inicio: date = (
            data_inicio if data_inicio is not None else datetime.now(UTC).date()
        )
        self.data_fim: Optional[date] = data_fim
        self._validar_vigencia(self.data_inicio, self.data_fim)
        self.valor: Optional[Decimal] = self._validar_valor(valor)
        self.objeto: Optional[str] = objeto.strip() if objeto else None
        self.situacao: SituacaoContrato = self._validar_situacao(situacao)
        self.created_at: datetime = created_at or datetime.now(UTC)
        self.created_by: Optional[UUID] = created_by
        self.updated_at: datetime = updated_at or datetime.now(UTC)
        self.updated_by: Optional[UUID] = updated_by
        self.deleted_at: Optional[datetime] = deleted_at
        self.deleted_by: Optional[UUID] = deleted_by

    # -- Validações -----------------------------------------------------------

    @staticmethod
    def _validar_numero(numero: str) -> str:
        if numero is None or not numero.strip():
            raise ValueError("numero do contrato é obrigatório (RN-COMPRAS-036)")
        return numero.strip()

    @staticmethod
    def _validar_valor(valor: Optional[Decimal]) -> Optional[Decimal]:
        if valor is None:
            return None
        valor = Decimal(valor)
        if valor < 0:
            raise ValueError(f"valor não pode ser negativo (RN-COMPRAS-039): {valor}")
        return valor

    @staticmethod
    def _validar_situacao(situacao: SituacaoContrato) -> SituacaoContrato:
        if not isinstance(situacao, SituacaoContrato):
            raise ValueError(f"Situação inválida: {situacao}")
        return situacao

    @staticmethod
    def _validar_vigencia(
        data_inicio: date, data_fim: Optional[date]
    ) -> None:
        if data_fim is not None and data_fim < data_inicio:
            raise ValueError(
                f"data_fim ({data_fim}) não pode ser anterior à data_inicio "
                f"({data_inicio}) (RN-COMPRAS-037)"
            )

    # -- Comportamentos de domínio -------------------------------------------

    def pode_transicionar_para(self, nova_situacao: SituacaoContrato) -> bool:
        """Verifica se a transição é permitida."""
        return nova_situacao in TRANSICOES_VALIDAS.get(self.situacao, set())

    def alterar_situacao(self, nova_situacao: SituacaoContrato, usuario_id: UUID) -> None:
        """Altera a situação respeitando as transições válidas."""
        # RN-COMPRAS-004: não operar sobre contratos excluídos.
        if self.foi_excluido():
            raise ValueError(
                "Contrato excluído não pode ter sua situação alterada "
                "(RN-COMPRAS-004)"
            )
        nova_situacao = self._validar_situacao(nova_situacao)
        if nova_situacao == self.situacao:
            return
        if not self.pode_transicionar_para(nova_situacao):
            validas = sorted(t.value for t in TRANSICOES_VALIDAS[self.situacao])
            raise ValueError(
                f"Transição {self.situacao.value} -> {nova_situacao.value} não permitida. "
                f"Transições válidas a partir de {self.situacao.value}: {validas}"
            )

        # RN-COMPRAS-046: não se vigenta contrato antes do início da vigência.
        hoje = date.today()
        if nova_situacao == SituacaoContrato.VIGENTE and self.data_inicio > hoje:
            raise ValueError(
                "Contrato não pode entrar em vigor antes da data_inicio "
                f"({self.data_inicio}) (RN-COMPRAS-046)"
            )

        self.situacao = nova_situacao
        # Encerramento sem termo definido registra o fim na data do ato.
        if nova_situacao == SituacaoContrato.ENCERRADO and self.data_fim is None:
            self.data_fim = hoje
        self.updated_at = datetime.now(UTC)
        self.updated_by = usuario_id

    def atualizar_dados(
        self,
        numero: Optional[str] = None,
        data_inicio: Optional[date] = None,
        data_fim: Optional[date] = None,
        valor: Optional[Decimal] = None,
        objeto: Optional[str] = None,
        usuario_id: Optional[UUID] = None,
    ) -> None:
        """Atualiza campos informados (RN-COMPRAS-036 a 039)."""
        # RN-COMPRAS-004: não operar sobre contratos excluídos.
        if self.foi_excluido():
            raise ValueError(
                "Contrato excluído não pode ser atualizado (RN-COMPRAS-004)"
            )
        # RN-COMPRAS-106: contratos em estado terminal não podem ser alterados.
        if self.situacao in ESTADOS_TERMINAIS:
            raise ValueError(
                f"Contrato em situação {self.situacao.value} não pode ser "
                f"atualizado (RN-COMPRAS-106)"
            )
        if numero is not None:
            self.numero = self._validar_numero(numero)
        novo_inicio = data_inicio if data_inicio is not None else self.data_inicio
        novo_fim = data_fim if data_fim is not None else self.data_fim
        self._validar_vigencia(novo_inicio, novo_fim)
        if data_inicio is not None:
            self.data_inicio = data_inicio
        if data_fim is not None:
            self.data_fim = data_fim
        if valor is not None:
            self.valor = self._validar_valor(valor)
        if objeto is not None:
            self.objeto = objeto.strip() or None
        self.updated_at = datetime.now(UTC)
        if usuario_id:
            self.updated_by = usuario_id

    # -- Acompanhamento da vigência (RN-COMPRAS-046) --------------------------

    def esta_vencido(self, hoje: Optional[date] = None) -> bool:
        """True se o contrato VIGENTE ultrapassou a data_fim."""
        hoje = hoje or date.today()
        return (
            self.situacao == SituacaoContrato.VIGENTE
            and self.data_fim is not None
            and self.data_fim < hoje
        )

    def dias_para_vencimento(self, hoje: Optional[date] = None) -> Optional[int]:
        """Dias restantes de vigência; None quando não aplicável."""
        if self.situacao != SituacaoContrato.VIGENTE or self.data_fim is None:
            return None
        return (self.data_fim - (hoje or date.today())).days

    def vigencia_contem(self, data: date) -> bool:
        """True se a data está dentro do intervalo de vigência informado."""
        if data < self.data_inicio:
            return False
        return self.data_fim is None or data <= self.data_fim

    def excluir(self, usuario_id: UUID) -> None:
        """Marca o contrato como excluído (soft-delete)."""
        self.deleted_at = datetime.now(UTC)
        self.deleted_by = usuario_id

    def foi_excluido(self) -> bool:
        """Retorna True se o contrato foi logicamente excluído."""
        return self.deleted_at is not None

    def esta_vigente(self) -> bool:
        return self.situacao == SituacaoContrato.VIGENTE


__all__ = [
    "Contrato",
    "SituacaoContrato",
    "TRANSICOES_VALIDAS",
    "ESTADOS_TERMINAIS",
]
