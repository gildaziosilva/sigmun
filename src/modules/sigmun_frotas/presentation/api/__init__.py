"""Agregador de rotas do DOM-FRO."""

from .endpoints import router as router_fro

routers = [router_fro]
__all__ = ["routers", "router_fro"]
