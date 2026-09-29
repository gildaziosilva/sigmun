"""Agregador de rotas do DOM-TEL — Gestão Territorial.

Importa os módulos de endpoints para que as rotas sejam registradas no router
único do domínio e expõe os mapeadores reutilizados pelos testes.
"""

from . import endpoints_geo, endpoints_planta, endpoints_territoriais
from .endpoints_geo import to_georreferencia
from .endpoints_planta import to_planta
from .endpoints_territoriais import to_bairro, to_logradouro
from .router import router as router_tel

routers = [router_tel]

__all__ = [
    "routers",
    "router_tel",
    "to_bairro",
    "to_logradouro",
    "to_planta",
    "to_georreferencia",
    "endpoints_territoriais",
    "endpoints_planta",
    "endpoints_geo",
]
