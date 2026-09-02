"""Queries do Cadastro Único Municipal (DOM-CUM)."""

from src.modules.sigmun_cadastro.application.queries.pessoa_queries import (
    ConsultarPessoaQuery,
    ListarPessoasQuery,
)
from src.modules.sigmun_cadastro.application.queries.unidade_queries import (
    ConsultarUnidadeQuery,
    ListarUnidadesQuery,
)

__all__ = [
    "ConsultarPessoaQuery",
    "ListarPessoasQuery",
    "ConsultarUnidadeQuery",
    "ListarUnidadesQuery",
]
