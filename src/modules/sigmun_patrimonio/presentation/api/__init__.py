"""Agregador de rotas do DOM-PAT."""

from .endpoints import router as router_pat

routers = [router_pat]
__all__ = ["routers", "router_pat"]
