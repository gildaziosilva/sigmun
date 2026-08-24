"""Consultas do domínio Gestão de Compras e Contratações."""

from src.modules.sigmun_compras.application.queries.consultar_fornecedor_query import (
    ConsultarFornecedorQuery,
)
from src.modules.sigmun_compras.application.queries.listar_fornecedores_query import (
    ListarFornecedoresQuery,
)

__all__ = ["ConsultarFornecedorQuery", "ListarFornecedoresQuery"]


