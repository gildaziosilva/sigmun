"""Agregador de rotas do DOM-ORC."""

from .dotacao_endpoints import router as router_dotacao
from .planejamento_endpoints import router as router_planejamento

routers = [router_planejamento, router_dotacao]
__all__ = ["routers", "router_planejamento", "router_dotacao"]
