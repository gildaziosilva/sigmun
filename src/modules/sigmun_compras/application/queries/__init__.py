"""Consultas do domínio Gestão de Compras e Contratações."""

from src.modules.sigmun_compras.application.queries.consultar_compra_query import (
    ConsultarCompraQuery,
)
from src.modules.sigmun_compras.application.queries.consultar_fornecedor_query import (
    ConsultarFornecedorQuery,
)
from src.modules.sigmun_compras.application.queries.consultar_item_compra_query import (
    ConsultarItemCompraQuery,
)
from src.modules.sigmun_compras.application.queries.consultar_processo_documental_query import (
    ConsultarProcessoDocumentalQuery,
)
from src.modules.sigmun_compras.application.queries.listar_compras_query import (
    ListarComprasQuery,
)
from src.modules.sigmun_compras.application.queries.listar_fornecedores_query import (
    ListarFornecedoresQuery,
)
from src.modules.sigmun_compras.application.queries.listar_itens_compra_query import (
    ListarItensCompraQuery,
)
from src.modules.sigmun_compras.application.queries.listar_processos_documentais_query import (
    ListarProcessosDocumentaisQuery,
)

__all__ = [
    "ConsultarFornecedorQuery",
    "ListarFornecedoresQuery",
    "ConsultarItemCompraQuery",
    "ListarItensCompraQuery",
    "ConsultarCompraQuery",
    "ListarComprasQuery",
    "ConsultarProcessoDocumentalQuery",
    "ListarProcessosDocumentaisQuery",
]

