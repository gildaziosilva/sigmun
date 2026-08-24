"""Eventos de domínio Gestão de Compras e Contratações."""

from src.modules.sigmun_compras.domain.events.fornecedor_events import (
    FornecedorAtualizadoEvent,
    FornecedorCriadoEvent,
    FornecedorInativadoEvent,
)

__all__ = ["FornecedorCriadoEvent", "FornecedorInativadoEvent", "FornecedorAtualizadoEvent"]


