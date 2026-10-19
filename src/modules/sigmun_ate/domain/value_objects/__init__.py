"""Objetos de valor do domínio de Atendimento ao Cidadão (DOM-ATE)."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class CodigoServico:
    """Código de serviço de atendimento."""

    valor: str

    def __post_init__(self):
        if not self.valor or not self.valor.strip():
            raise ValueError("Código de serviço não pode ser vazio")
        if len(self.valor) > 20:
            raise ValueError("Código de serviço deve ter no máximo 20 caracteres")


@dataclass(frozen=True)
class NumeroSenha:
    """Número da senha de atendimento."""

    valor: str

    def __post_init__(self):
        if not self.valor or not self.valor.strip():
            raise ValueError("Número da senha não pode ser vazio")
        if len(self.valor) > 10:
            raise ValueError("Número da senha deve ter no máximo 10 caracteres")


@dataclass(frozen=True)
class Prioridade:
    """Prioridade de atendimento."""

    valor: int

    def __post_init__(self):
        if not 1 <= self.valor <= 4:
            raise ValueError("Prioridade deve estar entre 1 (baixa) e 4 (urgente)")


@dataclass(frozen=True)
class NotaAvaliacao:
    """Nota de avaliação de atendimento (1 a 5)."""

    valor: int

    def __post_init__(self):
        if not 1 <= self.valor <= 5:
            raise ValueError("Nota deve estar entre 1 e 5")


@dataclass
class PeriodoAtendimento:
    """Período de funcionamento de uma unidade."""

    abertura: datetime
    fechamento: datetime

    def __post_init__(self):
        if self.abertura >= self.fechamento:
            raise ValueError("Horário de abertura deve ser anterior ao de fechamento")

    def esta_aberto(self, momento: datetime | None = None) -> bool:
        """Verifica se a unidade está aberta no momento dado."""
        if momento is None:
            momento = datetime.utcnow()
        return self.abertura <= momento <= self.fechamento


@dataclass
class TempoEspera:
    """Tempo estimado de espera."""

    minutos: int

    def __post_init__(self):
        if self.minutos < 0:
            raise ValueError("Tempo de espera não pode ser negativo")

    @property
    def esta_dentro_sla(self) -> bool:
        """Verifica se está dentro do SLA (padrão: 30 min)."""
        return self.minutos <= 30

    def formatado(self) -> str:
        """Retorna tempo formatado (ex: '15 min' ou '1h 30min')."""
        if self.minutos < 60:
            return f"{self.minutos} min"
        horas = self.minutos // 60
        mins = self.minutos % 60
        if mins == 0:
            return f"{horas}h"
        return f"{horas}h {mins}min"


__all__ = [
    "CodigoServico",
    "NumeroSenha",
    "Prioridade",
    "NotaAvaliacao",
    "PeriodoAtendimento",
    "TempoEspera",
]
