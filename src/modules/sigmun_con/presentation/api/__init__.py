"""Agregador de rotas do DOM-CON."""

from .contabil_endpoints import router as router_contabil
from .execucao_endpoints import router as router_execucao

routers = [router_execucao, router_contabil]
__all__ = ["routers", "router_execucao", "router_contabil"]
