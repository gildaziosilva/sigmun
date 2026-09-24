"""Agregador de rotas do DOM-EDU."""
from .endpoints import router as router_edu
routers = [router_edu]
__all__ = ["routers", "router_edu"]
