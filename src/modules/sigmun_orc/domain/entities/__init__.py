"""Agregador de entidades do DOM-ORC."""

from .dotacao import (
    ESTADOS_TERMINAIS_DOTACAO,
    TRANSICOES_DOTACAO,
    Dotacao,
    StatusDotacao,
)
from .ldo import ESTADOS_TERMINAIS_LDO, LDO, TRANSICOES_LDO, StatusLDO
from .loa import ESTADOS_TERMINAIS_LOA, LOA, TRANSICOES_LOA, StatusLOA
from .ppa import ESTADOS_TERMINAIS_PPA, PPA, TRANSICOES_PPA, StatusPPA
from .reserva import (
    ESTADOS_TERMINAIS_RESERVA,
    TRANSICOES_RESERVA,
    ReservaSaldo,
    StatusReserva,
)

__all__ = [
    "PPA",
    "StatusPPA",
    "TRANSICOES_PPA",
    "ESTADOS_TERMINAIS_PPA",
    "LDO",
    "StatusLDO",
    "TRANSICOES_LDO",
    "ESTADOS_TERMINAIS_LDO",
    "LOA",
    "StatusLOA",
    "TRANSICOES_LOA",
    "ESTADOS_TERMINAIS_LOA",
    "Dotacao",
    "StatusDotacao",
    "TRANSICOES_DOTACAO",
    "ESTADOS_TERMINAIS_DOTACAO",
    "ReservaSaldo",
    "StatusReserva",
    "TRANSICOES_RESERVA",
    "ESTADOS_TERMINAIS_RESERVA",
]
