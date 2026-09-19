"""Agregador de rotas do DOM-PES."""

from .cargos_endpoints import router as router_cargos
from .ferias_freq_endpoints import router as router_ferias_freq
from .folha_endpoints import router as router_folha
from .lotacoes_endpoints import router as router_lotacoes
from .servidores_endpoints import router as router_servidores

routers = [
    router_cargos,
    router_servidores,
    router_lotacoes,
    router_folha,
    router_ferias_freq,
]
__all__ = [
    "routers",
    "router_cargos",
    "router_servidores",
    "router_lotacoes",
    "router_folha",
    "router_ferias_freq",
]
