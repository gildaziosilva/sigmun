"""Repositórios concretos (infraestrutura) do domínio Gestão de Compras."""

from .sqlalchemy_compra_repository import SqlAlchemyCompraRepository
from .sqlalchemy_contrato_repository import SqlAlchemyContratoRepository
from .sqlalchemy_fornecedor_repository import SqlAlchemyFornecedorRepository
from .sqlalchemy_item_compra_repository import SqlAlchemyItemCompraRepository
from .sqlalchemy_processo_documental_repository import (
    SqlAlchemyProcessoDocumentalRepository,
)
from .sqlalchemy_trilha_auditoria_repository import (
    SqlAlchemyTrilhaAuditoriaRepository,
)

__all__ = [
    "SqlAlchemyFornecedorRepository",
    "SqlAlchemyItemCompraRepository",
    "SqlAlchemyCompraRepository",
    "SqlAlchemyProcessoDocumentalRepository",
    "SqlAlchemyContratoRepository",
    "SqlAlchemyTrilhaAuditoriaRepository",
]


