"""Agregador de rotas do DOM-IMO — Cadastro Imobiliário.

Importa os módulos de endpoints para que as rotas sejam registradas no router
único do domínio e expõe os mapeadores reutilizados pelos testes.
"""

from . import endpoints_avaliacoes, endpoints_imoveis
from .endpoints_avaliacoes import to_avaliacao, to_caracteristica, to_geometria
from .endpoints_imoveis import to_imovel, to_proprietario
from .router import router as router_imo

routers = [router_imo]

__all__ = [
    "routers",
    "router_imo",
    "to_imovel",
    "to_proprietario",
    "to_avaliacao",
    "to_caracteristica",
    "to_geometria",
    "endpoints_imoveis",
    "endpoints_avaliacoes",
]
