"""Agregador de rotas do DOM-OBR — Obras e Infraestrutura.

Importa os módulos de endpoints para que as rotas sejam registradas no router
único do domínio e expõe os conversores reutilizados pelos testes.
"""

from . import endpoints_acompanhamento, endpoints_obra
from .deps import to_despesa, to_etapa, to_medicao, to_obra, to_vistoria
from .router import NAO_ENCONTRADOS
from .router import router as router_obr

routers = [router_obr]

__all__ = [
    "routers",
    "router_obr",
    "NAO_ENCONTRADOS",
    "to_obra",
    "to_medicao",
    "to_despesa",
    "to_etapa",
    "to_vistoria",
    "endpoints_obra",
    "endpoints_acompanhamento",
]
