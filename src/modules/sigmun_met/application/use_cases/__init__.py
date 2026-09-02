"""Casos de uso para gerenciamento de Metadados Corporativos."""

import logging

from src.modules.sigmun_met.application.use_cases.classificacao_use_cases import (
    AtualizarClassificacaoUseCase,
    BuscarClassificacaoUseCase,
    CriarClassificacaoUseCase,
    DeletarClassificacaoUseCase,
)
from src.modules.sigmun_met.application.use_cases.metadado_use_cases import (
    AtivarMetadadoUseCase,
    AtualizarMetadadoUseCase,
    BuscarMetadadoUseCase,
    CriarMetadadoUseCase,
    DeletarMetadadoUseCase,
    DesativarMetadadoUseCase,
)
from src.modules.sigmun_met.application.use_cases.taxonomia_use_cases import (
    AtualizarTaxonomiaUseCase,
    BuscarTaxonomiaUseCase,
    CriarTaxonomiaUseCase,
    DeletarTaxonomiaUseCase,
)
from src.modules.sigmun_met.application.use_cases.termo_use_cases import (
    AtualizarTermoUseCase,
    BuscarTermoUseCase,
    CriarTermoUseCase,
    DeletarTermoUseCase,
)
from src.modules.sigmun_met.application.use_cases.valor_metadado_use_cases import (
    AtribuirValorMetadadoUseCase,
    BuscarValorMetadadoUseCase,
    RemoverValorMetadadoUseCase,
    ValidarValorMetadadoUseCase,
)

logger = logging.getLogger(__name__)

__all__ = [
    # Metadados
    "CriarMetadadoUseCase",
    "AtualizarMetadadoUseCase",
    "BuscarMetadadoUseCase",
    "AtivarMetadadoUseCase",
    "DesativarMetadadoUseCase",
    "DeletarMetadadoUseCase",
    # Valores de Metadado
    "AtribuirValorMetadadoUseCase",
    "BuscarValorMetadadoUseCase",
    "RemoverValorMetadadoUseCase",
    "ValidarValorMetadadoUseCase",
    # Classificações
    "CriarClassificacaoUseCase",
    "AtualizarClassificacaoUseCase",
    "BuscarClassificacaoUseCase",
    "DeletarClassificacaoUseCase",
    # Taxonomias
    "CriarTaxonomiaUseCase",
    "AtualizarTaxonomiaUseCase",
    "BuscarTaxonomiaUseCase",
    "DeletarTaxonomiaUseCase",
    # Termos de Taxonomia
    "CriarTermoUseCase",
    "AtualizarTermoUseCase",
    "BuscarTermoUseCase",
    "DeletarTermoUseCase",
]
