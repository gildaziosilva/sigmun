"""Repositórios do domínio Gestão de Compras e Contratações."""

from src.modules.sigmun_compras.domain.repositories.compra_repository import (
    CompraRepository,
)
from src.modules.sigmun_compras.domain.repositories.fornecedor_repository import (
    FornecedorRepository,
)
from src.modules.sigmun_compras.domain.repositories.item_compra_repository import (
    ItemCompraRepository,
)
from src.modules.sigmun_compras.domain.repositories.processo_documental_repository import (
    ProcessoDocumentalRepository,
)

__all__ = [
    "FornecedorRepository",
    "ItemCompraRepository",
    "CompraRepository",
    "ProcessoDocumentalRepository",
]


