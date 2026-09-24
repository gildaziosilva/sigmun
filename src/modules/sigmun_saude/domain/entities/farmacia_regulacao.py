"""Entidades Regulacao e Farmácia básica — fila de espera e dispensação (DOM-SAU).

RN-SAU-030: regulação nasce ``solicitada`` e transita para
    ``autorizada/negada/agendada``; autorizada pode virar ``agendada``.
RN-SAU-040: dispensação exige estoque suficiente; baixa é atômica no
    caso de uso (entidade só valida e calcula).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from uuid import uuid4


class PrioridadeRegulacao(Enum):
    """Criticidade clínica da solicitação."""

    ROTINA = "rotina"
    PRIORITARIA = "prioritaria"
    URGENCIA = "urgencia"


class StatusRegulacao(Enum):
    """Situação da solicitação na central de regulação."""

    SOLICITADA = "solicitada"
    AUTORIZADA = "autorizada"
    NEGADA = "negada"
    AGENDADA = "agendada"


@dataclass
class Regulacao:
    """Solicitação de procedimento/exame/consulta especializada."""

    id: str = field(default_factory=lambda: str(uuid4()))
    paciente_id: str = ""
    procedimento: str = ""
    prioridade: PrioridadeRegulacao = field(default=PrioridadeRegulacao.ROTINA)
    solicitante: str = ""
    data_solicitacao: date | None = None
    status: StatusRegulacao = field(default=StatusRegulacao.SOLICITADA)
    justificativa: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""

    def validar(self) -> None:
        """Valida regras estruturais da solicitação."""
        from ..exceptions import RegraNegocioError

        if not self.paciente_id:
            raise RegraNegocioError("Regulação exige paciente vinculado")
        if not self.procedimento:
            raise RegraNegocioError("Procedimento solicitado é obrigatório")

    def autorizar(self) -> None:
        """Autoriza a solicitação."""
        from ..exceptions import EstadoRegulacaoInvalidoError

        if self.status != StatusRegulacao.SOLICITADA:
            raise EstadoRegulacaoInvalidoError(
                f"Só é possível autorizar regulação solicitada (atual: {self.status.value})"
            )
        self.status = StatusRegulacao.AUTORIZADA
        self.updated_at = datetime.utcnow()

    def negar(self, justificativa: str = "") -> None:
        """Nega a solicitação com justificativa."""
        from ..exceptions import EstadoRegulacaoInvalidoError

        if self.status != StatusRegulacao.SOLICITADA:
            raise EstadoRegulacaoInvalidoError(
                "Só é possível negar regulação solicitada"
            )
        self.status = StatusRegulacao.NEGADA
        self.justificativa = justificativa
        self.updated_at = datetime.utcnow()

    def agendar(self) -> None:
        """Vincula a solicitação autorizada a uma vaga."""
        from ..exceptions import EstadoRegulacaoInvalidoError

        if self.status != StatusRegulacao.AUTORIZADA:
            raise EstadoRegulacaoInvalidoError(
                "Só é possível agendar regulação autorizada"
            )
        self.status = StatusRegulacao.AGENDADA
        self.updated_at = datetime.utcnow()


@dataclass
class Medicamento:
    """Item do elenco da farmácia básica municipal."""

    id: str = field(default_factory=lambda: str(uuid4()))
    nome: str = ""
    apresentacao: str = ""
    estoque: float = 0.0
    estoque_minimo: float = 0.0
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def abaixo_do_minimo(self) -> bool:
        """Indica necessidade de reposição."""
        return self.estoque < self.estoque_minimo

    def repor(self, quantidade: float) -> None:
        """Entrada de estoque."""
        from ..exceptions import RegraNegocioError

        if quantidade <= 0:
            raise RegraNegocioError("Reposição exige quantidade positiva")
        self.estoque = round(self.estoque + quantidade, 2)
        self.updated_at = datetime.utcnow()

    def dispensar(self, quantidade: float) -> None:
        """Baixa de estoque por dispensação (RN-SAU-040)."""
        from ..exceptions import EstoqueInsuficienteError, RegraNegocioError

        if quantidade <= 0:
            raise RegraNegocioError("Dispensação exige quantidade positiva")
        if quantidade > self.estoque:
            raise EstoqueInsuficienteError(
                f"Estoque insuficiente: solicitado {quantidade}, "
                f"disponível {self.estoque} (RN-SAU-040)"
            )
        self.estoque = round(self.estoque - quantidade, 2)
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida regras estruturais do medicamento."""
        from ..exceptions import RegraNegocioError

        if not self.nome:
            raise RegraNegocioError("Nome do medicamento é obrigatório")
        if self.estoque < 0:
            raise RegraNegocioError("Estoque não pode ser negativo")


@dataclass
class Dispensacao:
    """Registro de entrega de medicamento ao cidadão."""

    id: str = field(default_factory=lambda: str(uuid4()))
    paciente_id: str = ""
    medicamento_id: str = ""
    quantidade: float = 0.0
    data: date | None = None
    receita: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""

    def validar(self) -> None:
        """Valida regras estruturais da dispensação."""
        from ..exceptions import RegraNegocioError

        if not self.paciente_id or not self.medicamento_id:
            raise RegraNegocioError(
                "Dispensação exige paciente e medicamento (RN-SAU-040)"
            )
        if self.quantidade <= 0:
            raise RegraNegocioError("Quantidade dispensada deve ser positiva")


__all__ = [
    "PrioridadeRegulacao",
    "StatusRegulacao",
    "Regulacao",
    "Medicamento",
    "Dispensacao",
]
