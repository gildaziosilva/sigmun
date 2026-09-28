"""Agregador de rotas do DOM-ASS."""
from .endpoints import router as router_ass
routers = [router_ass]
__all__ = ["routers", "router_ass"]

