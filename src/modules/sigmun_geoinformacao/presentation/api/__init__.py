"""Agregador de rotas do DOM-GEO — Geoinformação Municipal.

Importa os módulos de endpoints para que as rotas sejam registradas no router
único do domínio e expõe os conversores reutilizados pelos testes.
"""

from . import endpoints_camada, endpoints_servico
from .deps import to_camada, to_feature, to_mapa, to_servico, to_vinculo
from .router import NAO_ENCONTRADOS
from .router import router as router_geo

routers = [router_geo]

__all__ = [
    "routers",
    "router_geo",
    "NAO_ENCONTRADOS",
    "to_camada",
    "to_mapa",
    "to_vinculo",
    "to_feature",
    "to_servico",
    "endpoints_camada",
    "endpoints_servico",
]
