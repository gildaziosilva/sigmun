"""Entidades do domínio de Gestão de Diárias, Viagens e Deslocamentos.

Responsável pelo núcleo administrativo e econômico-financeiro:
- Diárias com máquina de estados completa
- Viagens oficiais e deslocamentos
- Prestação de contas e aprovação/glosa/restituição
"""

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from uuid import uuid4


class StatusDiaria(Enum):
    """Máquina de estados da diária oficial.

    Ciclo de vida completo conforme RN-DIA-003:
    SOLICITADA → AUTORIZADA → CALCULADA → CONCEDIDA →
    EM_PRESTACAO → PAGA → APROVADA / GLOSA → RESTITUIDA
    """

    SOLICITADA = "solicitada"
    AUTORIZADA = "autorizada"
    CALCULADA = "calculada"
    CONCEDIDA = "concedida"
    EM_PRESTACAO = "em_prestacao"
    PAGA = "paga"
    APROVADA = "aprovada"
    GLOSA = "glosa"
    RESTITUIDA = "restituida"
    CANCELADA = "cancelada"


class CategoriaDiaria(Enum):
    """Categoria da diária conforme legislação (Lei 8.666/93, art. 23)."""

    EVENTO = "evento"
    REUNIAO = "reuniao"
    TREINAMENTO = "treinamento"
    VIAGEM_OFICIAL = "viagem_oficial"
    SERVICO_CONSULTIVO = "servico_consultivo"


class TipoDeslocamento(Enum):
    """Tipo de deslocamento da viagem."""

    TERRESTRE = "terrestre"
    AEREO = "aereo"
    FLUVIAL = "fluvial"
    MARITIMO = "maritimo"


# =============================================================================
# Máquina de estados
# =============================================================================

TRANSICOES_VALIDAS: dict[str, set[str]] = {
    StatusDiaria.SOLICITADA.value: {
        StatusDiaria.AUTORIZADA.value,
        StatusDiaria.CANCELADA.value,
    },
    StatusDiaria.AUTORIZADA.value: {
        StatusDiaria.CALCULADA.value,
        StatusDiaria.CANCELADA.value,
    },
    StatusDiaria.CALCULADA.value: {
        StatusDiaria.CONCEDIDA.value,
        StatusDiaria.CANCELADA.value,
    },
    StatusDiaria.CONCEDIDA.value: {
        StatusDiaria.EM_PRESTACAO.value,
        StatusDiaria.CANCELADA.value,
    },
    StatusDiaria.EM_PRESTACAO.value: {
        StatusDiaria.PAGA.value,
        StatusDiaria.CANCELADA.value,
    },
    StatusDiaria.PAGA.value: {
        StatusDiaria.APROVADA.value,
        StatusDiaria.GLOSA.value,
        StatusDiaria.RESTITUIDA.value,
    },
    StatusDiaria.GLOSA.value: {
        StatusDiaria.PAGA.value,
        StatusDiaria.RESTITUIDA.value,
    },
    StatusDiaria.RESTITUIDA.value: set(),
    StatusDiaria.APROVADA.value: set(),
    StatusDiaria.CANCELADA.value: set(),
}

ESTADOS_TERMINAIS: set[str] = {
    StatusDiaria.APROVADA.value,
    StatusDiaria.RESTITUIDA.value,
    StatusDiaria.CANCELADA.value,
}


# =============================================================================
# Entidade Viagem
# =============================================================================


@dataclass
class Viagem:
    """Entidade Viagem — solicitação de viagem oficial.

    Referenciada por DOM-PES (servidor) e DOM-ORC (dotação orçamentária).
    Uma viagem pode ter muitas diárias associadas.
    """

    id: str = field(default_factory=lambda: str(uuid4()))
    servidor_id: str = ""
    dota_id: str = ""
    motivo: str = ""
    cargo_ocupado: str = ""
    unidade_origem_id: str = ""
    unidade_destino_id: str = ""
    unidade_atual_id: str = ""
    data_inicio: date | None = None
    data_fim: date | None = None
    destino: str = ""
    is_antecipacao: bool = False
    data_visita: datetime | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return not self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo

    @property
    def foi_excluido(self) -> bool:
        return self.is_deleted

    def excluir(self) -> None:
        """Marca a viagem como excluída (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def tramitar_para(self, unidade_destino_id: str, autor_id: str = "") -> None:
        """Tramita a viagem entre unidades.

        Atualiza a unidade atual (origem passa a ser a atual) e aponta
        para a nova unidade de destino informada.
        """
        self.unidade_origem_id = self.unidade_atual_id or self.unidade_origem_id
        self.unidade_atual_id = self.unidade_destino_id or self.unidade_atual_id
        self.unidade_destino_id = unidade_destino_id
        self.updated_at = datetime.utcnow()

    def visitar(
        self,
        data_visita: datetime | None = None,
        visitante_id: str = "",
        autor_id: str = "",
    ) -> None:
        """Registra uma visita/chegada à unidade de destino da viagem."""
        self.data_visita = data_visita or datetime.utcnow()
        self.updated_at = datetime.utcnow()


# =============================================================================
# Entidade Diária
# =============================================================================


@dataclass
class Diaria:
    """Entidade Diária — núcleo do DOM-DIA.

    Representa uma diária oficial com máquina de estados completa (RN-DIA-003).
    Ciclo: SOLICITADA → AUTORIZADA → CALCULADA → CONCEDIDA →
    EM_PRESTACAO → PAGA → APROVADA / GLOSA → RESTITUIDA / CANCELADA.
    """

    id: str = field(default_factory=lambda: str(uuid4()))
    viagem_id: str = ""
    servidor_id: str = ""
    dota_id: str = ""
    categoria: CategoriaDiaria = field(default=CategoriaDiaria.EVENTO)
    descricao: str = ""
    data_inicio: date | None = None
    data_fim: date | None = None
    valor_diaria: float = 0.0
    valor_total: float = 0.0
    status: StatusDiaria = field(default=StatusDiaria.SOLICITADA)
    data_solicitacao: datetime = field(default_factory=datetime.utcnow)
    data_autorizacao: datetime | None = None
    data_calculo: datetime | None = None
    data_concessao: datetime | None = None
    data_inicio_prestacao: datetime | None = None
    data_fim_prestacao: datetime | None = None
    data_pagamento: datetime | None = None
    data_aprovacao: datetime | None = None
    data_glosa: datetime | None = None
    data_restituicao: datetime | None = None
    data_cancelamento: datetime | None = None
    motivo_cancelamento: str = ""
    motivo_glosa: str = ""
    valor_glosado: float = 0.0
    documento_prestacao_id: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    updated_by: str = ""
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        return not self.is_deleted

    @property
    def is_active(self) -> bool:
        return self.esta_ativo

    @property
    def foi_excluido(self) -> bool:
        return self.is_deleted

    @property
    def is_terminal(self) -> bool:
        return self.status.value in ESTADOS_TERMINAIS

    # -------------------------------------------------------------------------
    # Máquina de estados
    # -------------------------------------------------------------------------

    def _transicao_valida(self, novo_status: StatusDiaria) -> None:
        """Valida se a transição de estado é permitida."""
        from ...domain.exceptions import RegraNegocioError

        novo_valor = novo_status.value
        atual_valor = self.status.value

        if atual_valor not in TRANSICOES_VALIDAS:
            raise RegraNegocioError(
                f"Estado atual '{atual_valor}' não possui transições definidas"
            )

        if novo_valor not in TRANSICOES_VALIDAS[atual_valor]:
            raise RegraNegocioError(
                f"Transição inválida: {atual_valor} → {novo_valor}"
            )

    def solicitar(self) -> None:
        """RN-DIA-001: Solicitação inicial da diária."""
        self._transicao_valida(StatusDiaria.SOLICITADA)
        self.status = StatusDiaria.SOLICITADA
        self.data_solicitacao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def autorizar(self, valor_diaria: float = 0.0) -> None:
        """RN-DIA-002: Autoriza a diária com valor."""
        from ...domain.exceptions import RegraNegocioError

        if valor_diaria <= 0:
            raise RegraNegocioError("Valor da diária deve ser maior que zero (RN-DIA-002)")
        self._transicao_valida(StatusDiaria.AUTORIZADA)
        self.status = StatusDiaria.AUTORIZADA
        self.valor_diaria = valor_diaria
        self.data_autorizacao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def calcular(self, valor_total: float) -> None:
        """RN-DIA-003: Calcula o valor total da diária."""
        from ...domain.exceptions import RegraNegocioError

        if valor_total < self.valor_diaria:
            raise RegraNegocioError("Valor total deve ser maior ou igual à diária (RN-DIA-003)")
        self._transicao_valida(StatusDiaria.CALCULADA)
        self.status = StatusDiaria.CALCULADA
        self.valor_total = valor_total
        self.data_calculo = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def conceder(self) -> None:
        """RN-DIA-004: Concede a diária (autorização final)."""
        self._transicao_valida(StatusDiaria.CONCEDIDA)
        self.status = StatusDiaria.CONCEDIDA
        self.data_concessao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def iniciar_prestacao(self) -> None:
        """RN-DIA-005: Inicia o período de prestação de contas."""
        self._transicao_valida(StatusDiaria.EM_PRESTACAO)
        self.status = StatusDiaria.EM_PRESTACAO
        self.data_inicio_prestacao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def finalizar_prestacao(self) -> None:
        """RN-DIA-006: Finaliza o período de prestação de contas."""
        from ...domain.exceptions import RegraNegocioError

        if not self.data_inicio_prestacao:
            raise RegraNegocioError("Não é possível finalizar sem início de prestação")
        self._transicao_valida(StatusDiaria.PAGA)
        self.status = StatusDiaria.PAGA
        self.data_fim_prestacao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def pagar(self) -> None:
        """RN-DIA-007: Registra o pagamento da diária."""
        self._transicao_valida(StatusDiaria.PAGA)
        self.status = StatusDiaria.PAGA
        self.data_pagamento = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def prestar_conta(self, documento_prestacao_id: str) -> None:
        """RN-DIA-009: Presta contas (requer documento GDO anexado)."""
        from ...domain.exceptions import RegraNegocioError

        if not documento_prestacao_id:
            raise RegraNegocioError("Prestação de contas requer documento anexo (RN-DIA-009)")
        self._transicao_valida(StatusDiaria.PAGA)
        self.documento_prestacao_id = documento_prestacao_id
        self.updated_at = datetime.utcnow()

    def cancelar(self, motivo: str) -> None:
        """Cancela a diária (permitido em estados não terminais)."""
        from ...domain.exceptions import RegraNegocioError

        if not motivo:
            raise RegraNegocioError("Cancelamento requer motivo")
        self._transicao_valida(StatusDiaria.CANCELADA)
        self.status = StatusDiaria.CANCELADA
        self.motivo_cancelamento = motivo
        self.data_cancelamento = datetime.utcnow()
        self.updated_at = datetime.utcnow()


# =============================================================================
# Entidade PrestacaoContas
# =============================================================================


@dataclass
class PrestacaoContas:
    """Entidade PrestacaoContas — registro contábil de prestação de diária."""

    id: str = field(default_factory=lambda: str(uuid4()))
    diaria_id: str = ""
    servidor_id: str = ""
    dota_id: str = ""
    data_emissao: datetime = field(default_factory=datetime.utcnow)
    data_vencimento: datetime | None = None
    documento_id: str = ""
    valor_previsto: float = 0.0
    valor_apresentado: float = 0.0
    valor_glosado: float = 0.0
    valor_liquido: float = 0.0
    status: str = "aberta"
    motivo_glosa: str = ""
    data_aprovacao: datetime | None = None
    data_glosa: datetime | None = None
    data_restituicao: datetime | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return not self.is_deleted

    def aprovar(self, autor_id: str = "") -> None:
        """Aprova a prestação de contas (status 'aberta' → 'aprovada')."""
        from ...domain.exceptions import RegraNegocioError

        if self.status != "aberta":
            raise RegraNegocioError(
                f"Apenas prestações abertas podem ser aprovadas (status atual: {self.status})"
            )
        self.status = "aprovada"
        self.valor_liquido = self.valor_apresentado - self.valor_glosado
        self.data_aprovacao = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if autor_id:
            self.updated_by = autor_id

    def glosar(self, motivo: str, valor_glosado: float = 0.0, autor_id: str = "") -> None:
        """Glosa a prestação de contas (requer motivo, RN-DIA-016)."""
        from ...domain.exceptions import RegraNegocioError

        if self.status != "aberta":
            raise RegraNegocioError(
                f"Apenas prestações abertas podem ser glosadas (status atual: {self.status})"
            )
        if not motivo:
            raise RegraNegocioError("Glosa requer motivo (RN-DIA-016)")
        if valor_glosado < 0 or valor_glosado > self.valor_apresentado:
            raise RegraNegocioError("Valor glosado inválido")
        self.status = "glosa"
        self.motivo_glosa = motivo
        self.valor_glosado = valor_glosado
        self.valor_liquido = self.valor_apresentado - valor_glosado
        self.data_glosa = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if autor_id:
            self.updated_by = autor_id

    def restituir(self, autor_id: str = "") -> None:
        """Restitui o valor glosado (status 'glosa' → 'restituida')."""
        from ...domain.exceptions import RegraNegocioError

        if self.status != "glosa":
            raise RegraNegocioError(
                f"Apenas prestações em glosa podem ser restituídas (status atual: {self.status})"
            )
        if self.valor_glosado <= 0:
            raise RegraNegocioError("Não há valor glosado para restituir")
        self.status = "restituida"
        self.data_restituicao = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if autor_id:
            self.updated_by = autor_id


# =============================================================================
# Entidade EventoDiaria
# =============================================================================


@dataclass
class EventoDiaria:
    """Entidade EventoDiaria — log de auditoria de transições de estado."""

    id: str = field(default_factory=lambda: str(uuid4()))
    diaria_id: str = ""
    status_anterior: str = ""
    status_posterior: str = ""
    usuario_id: str = ""
    motivo: str = ""
    data_evento: datetime = field(default_factory=datetime.utcnow)
    detalhes: str = ""


# =============================================================================
# Exportação pública
# =============================================================================

__all__ = [
    "StatusDiaria",
    "CategoriaDiaria",
    "TipoDeslocamento",
    "Viagem",
    "Diaria",
    "PrestacaoContas",
    "EventoDiaria",
    "TRANSICOES_VALIDAS",
    "ESTADOS_TERMINAIS",
]
