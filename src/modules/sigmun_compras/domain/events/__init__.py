"""Eventos de domínio Gestão de Compras e Contratações."""

from src.modules.sigmun_compras.domain.events.compra_events import (
    CompraAtualizadaEvent,
    CompraCriadaEvent,
    CompraSituacaoAlteradaEvent,
)
from src.modules.sigmun_compras.domain.events.contrato_events import (
    ContratoAtualizadoEvent,
    ContratoCriadoEvent,
    ContratoSituacaoAlteradaEvent,
)
from src.modules.sigmun_compras.domain.events.fornecedor_events import (
    FornecedorAtualizadoEvent,
    FornecedorCriadoEvent,
    FornecedorInativadoEvent,
)
from src.modules.sigmun_compras.domain.events.item_compra_events import (
    ItemCompraAtualizadoEvent,
    ItemCompraCriadoEvent,
    ItemCompraRemovidoEvent,
)
from src.modules.sigmun_compras.domain.events.processo_documental_events import (
    ProcessoDocumentalAbertoEvent,
    ProcessoDocumentalAtualizadoEvent,
)

__all__ = [
    "FornecedorCriadoEvent",
    "FornecedorInativadoEvent",
    "FornecedorAtualizadoEvent",
    "ItemCompraCriadoEvent",
    "ItemCompraAtualizadoEvent",
    "ItemCompraRemovidoEvent",
    "CompraCriadaEvent",
    "CompraAtualizadaEvent",
    "CompraSituacaoAlteradaEvent",
    "ContratoCriadoEvent",
    "ContratoAtualizadoEvent",
    "ContratoSituacaoAlteradaEvent",
    "ProcessoDocumentalAbertoEvent",
    "ProcessoDocumentalAtualizadoEvent",
]


