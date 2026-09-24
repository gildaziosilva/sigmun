"""Agregador de rotas do DOM-SAU."""
from .endpoints import router as router_sau
routers = [router_sau]
__all__ = ["routers", "router_sau"]
