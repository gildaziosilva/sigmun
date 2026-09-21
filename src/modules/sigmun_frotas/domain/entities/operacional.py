"""Entidades Abastecimento, Manutencao e Rota do DOM-FRO."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from uuid import uuid4

from .veiculo import Combustivel


@dataclass
class Abastecimento:
    """Registro de abastecimento de um veículo."""

    id: str = field(default_factory=lambda: str(uuid4()))
    veiculo_id: str = ""
    data: date | None = None
    quantidade_litros: float = 0.0
    valor_unitario: float = 0.0
    valor_total: float = 0.0
    odometro: float = 0.0
    posto: str = ""
    tipo_combustivel: Combustivel = field(default=Combustivel.FLEX)
    created_at: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""

    def recalcular_total(self) -> None:
        """Recompõe o valor total a partir da quantidade e preço unitário."""
        self.valor_total = round(self.quantidade_litros * self.valor_unitario, 2)

    def validar(self) -> None:
        """Valida regras estruturais do abastecimento."""
        from ..exceptions import RegraNegocioError

        if not self.veiculo_id:
            raise RegraNegocioError("Abastecimento exige veículo")
        if self.quantidade_litros <= 0:
            raise RegraNegocioError("Quantidade de combustível deve ser positiva")


class TipoManutencao(Enum):
    """Classificação da manutenção."""

    PREVENTIVA = "preventiva"
    CORRETIVA = "corretiva"


class StatusManutencao(Enum):
    """Situação da manutenção."""

    ABERTA = "aberta"
    EM_ANDAMENTO = "em_andamento"
    CONCLUIDA = "concluida"


@dataclass
class Manutencao:
    """Ordem de manutenção de um veículo."""

    id: str = field(default_factory=lambda: str(uuid4()))
    veiculo_id: str = ""
    data_entrada: date | None = None
    data_saida: date | None = None
    tipo: TipoManutencao = field(default=TipoManutencao.PREVENTIVA)
    descricao: str = ""
    oficina: str = ""
    valor: float = 0.0
    status: StatusManutencao = field(default=StatusManutencao.ABERTA)
    created_at: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""

    def validar(self) -> None:
        """Valida regras estruturais da manutenção."""
        from ..exceptions import RegraNegocioError

        if not self.veiculo_id:
            raise RegraNegocioError("Manutenção exige veículo")
        if not self.descricao:
            raise RegraNegocioError("Descrição da manutenção é obrigatória")

    def concluir(self, data_saida: date | None = None) -> None:
        """Conclui a manutenção."""
        from ..exceptions import RegraNegocioError

        if self.status == StatusManutencao.CONCLUIDA:
            raise RegraNegocioError("Manutenção já concluída")
        self.status = StatusManutencao.CONCLUIDA
        self.data_saida = data_saida or date.today()


class StatusRota(Enum):
    """Situação da rota/deslocamento."""

    PLANEJADA = "planejada"
    EM_ANDAMENTO = "em_andamento"
    CONCLUIDA = "concluida"
    CANCELADA = "cancelada"


@dataclass
class Rota:
    """Deslocamento de veículo entre origem e destino."""

    id: str = field(default_factory=lambda: str(uuid4()))
    veiculo_id: str = ""
    data: date | None = None
    origem: str = ""
    destino: str = ""
    km_inicio: float = 0.0
    km_fim: float = 0.0
    distancia_km: float = 0.0
    descricao: str = ""
    status: StatusRota = field(default=StatusRota.PLANEJADA)
    created_at: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""

    def validar(self) -> None:
        """Valida regras estruturais da rota."""
        from ..exceptions import RegraNegocioError

        if not self.veiculo_id:
            raise RegraNegocioError("Rota exige veículo")
        if not self.origem or not self.destino:
            raise RegraNegocioError("Origem e destino são obrigatórios")
        if self.km_fim < self.km_inicio:
            raise RegraNegocioError("Quilometragem final não pode ser menor que a inicial")

    def calcular_distancia(self) -> None:
        """Calcula a distância percorrida."""
        self.distancia_km = round(max(self.km_fim - self.km_inicio, 0.0), 2)

    def concluir(self) -> None:
        """Conclui a rota."""
        from ..exceptions import RegraNegocioError

        if self.status != StatusRota.PLANEJADA:
            raise RegraNegocioError("Apenas rotas planejadas podem ser concluídas")
        self.calcular_distancia()
        self.status = StatusRota.CONCLUIDA


__all__ = [
    "Abastecimento",
    "TipoManutencao",
    "StatusManutencao",
    "Manutencao",
    "StatusRota",
    "Rota",
]