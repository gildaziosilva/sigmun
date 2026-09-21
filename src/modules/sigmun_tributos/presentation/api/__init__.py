"""Agregador de rotas do DOM-TRI."""

from .contribuintes_imoveis_endpoints import router as router_contribuintes_imoveis
from .divida_certidao_endpoints import router as router_divida_certidao
from .lancamentos_endpoints import router as router_lancamentos

routers = [
    router_contribuintes_imoveis,
    router_lancamentos,
    router_divida_certidao,
]
__all__ = [
    "routers",
    "router_contribuintes_imoveis",
    "router_lancamentos",
    "router_divida_certidao",
]
