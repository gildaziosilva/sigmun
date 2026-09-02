"""Entidades do domínio Gestão de Compras e Contratações."""

from src.modules.sigmun_compras.domain.entities.compra import (
    ESTADOS_FECHADOS,
    TRANSICOES_VALIDAS,
    Compra,
    SituacaoCompra,
)
from src.modules.sigmun_compras.domain.entities.contrato import (
    ESTADOS_TERMINAIS,
    Contrato,
    SituacaoContrato,
)
from src.modules.sigmun_compras.domain.entities.contrato import (
    TRANSICOES_VALIDAS as TRANSICOES_VALIDAS_CONTRATO,
)
from src.modules.sigmun_compras.domain.entities.fornecedor import (
    Fornecedor,
    SituacaoFornecedor,
)
from src.modules.sigmun_compras.domain.entities.item_compra import ItemCompra
from src.modules.sigmun_compras.domain.entities.processo_documental import ProcessoDocumental
from src.modules.sigmun_compras.domain.entities.registro_auditoria import (
    CategoriaEventoAuditoria,
    RegistroAuditoria,
    ResultadoEventoAuditoria,
)

__all__ = [
    "Compra",
    "SituacaoCompra",
    "TRANSICOES_VALIDAS",
    "ESTADOS_FECHADOS",
    "Contrato",
    "SituacaoContrato",
    "TRANSICOES_VALIDAS_CONTRATO",
    "ESTADOS_TERMINAIS",
    "Fornecedor",
    "SituacaoFornecedor",
    "ItemCompra",
    "ProcessoDocumental",
    "RegistroAuditoria",
    "CategoriaEventoAuditoria",
    "ResultadoEventoAuditoria",
]


