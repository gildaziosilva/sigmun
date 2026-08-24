"""Consultas do domínio Gestão de Compras e Contratações."""

from src.modules.sigmun_compras.application.queries.consultar_fornecedor_query import (
    ConsultarFornecedorQuery,
)
from src.modules.sigmun_compras.application.queries.consultar_item_compra_query import (
    ConsultarItemCompraQuery,
)
from src.modules.sigmun_compras.application.queries.listar_fornecedores_query import (
    ListarFornecedoresQuery,
)
from src.modules.sigmun_compras.application.queries.listar_itens_compra_query import (
    ListarItensCompraQuery,
)

__all__ = [
    "ConsultarFornecedorQuery",
    "ListarFornecedoresQuery",
    "ConsultarItemCompraQuery",
    "ListarItensCompraQuery",
]


