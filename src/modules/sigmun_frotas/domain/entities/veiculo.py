"""Entidade Veiculo — veículo da frota municipal (DOM-FRO).

RN-FRO-001: a placa do veículo é única no cadastro.
RN-FRO-002: veículos em manutenção têm status ``manutencao``; concluída a
    manutenção retornam a ``ativo``.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class TipoVeiculo(Enum):
    """Classificação do veículo."""

    LEVE = "leve"
    PESADO = "pesado"
    MOTOCICLETA = "motocicleta"
    ONIBUS = "onibus"
    TRATOR = "trator"


class Combustivel(Enum):
    """Tipo de combustível."""

    GASOLINA = "gasolina"
    ALCOOL = "alcool"
    FLEX = "flex"
    DIESEL = "diesel"
    ELEETRICO = "eletrico"
    GAS = "gas"


class StatusVeiculo(Enum):
    """Situação operacional do veículo."""

    ATIVO = "ativo"
    MANUTENCAO = "manutencao"
    INATIVO = "inativo"
    BAIXADO = "baixado"


@dataclass
class Veiculo:
    """Veículo integrante da frota municipal."""

    id: str = field(default_factory=lambda: str(uuid4()))
    placa: str = ""
    chassi: str = ""
    renavam: str = ""
    marca: str = ""
    modelo: str = ""
    ano_fabricacao: int = 0
    ano_modelo: int = 0
    tipo: TipoVeiculo = field(default=TipoVeiculo.LEVE)
    combustivel: Combustivel = field(default=Combustivel.FLEX)
    capacidade: float = 0.0
    odometro_atual: float = 0.0
    status: StatusVeiculo = field(default=StatusVeiculo.ATIVO)
    unidade_id: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    def validar(self) -> None:
        """Valida regras estruturais do veículo."""
        from ..exceptions import RegraNegocioError

        if not self.placa:
            raise RegraNegocioError("Placa do veículo é obrigatória (RN-FRO-001)")
        if not self.marca or not self.modelo:
            raise RegraNegocioError("Marca e modelo do veículo são obrigatórios")

    def atualizar_odometro(self, km: float) -> None:
        """Atualiza o odômetro (nunca regride)."""
        from ..exceptions import RegraNegocioError

        if km < self.odometro_atual:
            raise RegraNegocioError("Odômetro informado é inferior ao registrado")
        self.odometro_atual = km
        self.updated_at = datetime.utcnow()

    def entrar_em_manutencao(self) -> None:
        """Marca o veículo como em manutenção (RN-FRO-002)."""
        from ..exceptions import RegraNegocioError

        if self.status != StatusVeiculo.ATIVO:
            raise RegraNegocioError(
                f"Veículo só entra em manutenção se ativo (atual: {self.status.value})"
            )
        self.status = StatusVeiculo.MANUTENCAO
        self.updated_at = datetime.utcnow()

    def concluir_manutencao(self) -> None:
        """Retorna o veículo à condição ativa (RN-FRO-002)."""
        from ..exceptions import RegraNegocioError

        if self.status != StatusVeiculo.MANUTENCAO:
            raise RegraNegocioError(
                "Veículo não está em manutenção para concluir"
            )
        self.status = StatusVeiculo.ATIVO
        self.updated_at = datetime.utcnow()

    def baixar(self) -> None:
        """Baixa definitiva do veículo."""
        from ..exceptions import RegraNegocioError

        if self.status == StatusVeiculo.BAIXADO:
            raise RegraNegocioError("Veículo já baixado")
        self.status = StatusVeiculo.BAIXADO
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca o veículo como excluído (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()


__all__ = ["TipoVeiculo", "Combustivel", "StatusVeiculo", "Veiculo"]