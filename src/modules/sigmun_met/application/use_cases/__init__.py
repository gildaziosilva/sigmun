"""Casos de uso para gerenciamento de Metadados.

Nomenclatura PT-BR espelhada no DOM-COM:
Registrar* (criação), Consultar*/Listar* (leitura), Excluir* (remoção).

Aliases Criar*/Buscar*/Deletar* mantidos por compatibilidade.
"""

import logging

from src.modules.sigmun_met.application.use_cases.classificacao_use_cases import (
    AtualizarClassificacaoUseCase,
    BuscarClassificacaoUseCase,
    ConsultarClassificacaoUseCase,
    CriarClassificacaoUseCase,
    DeletarClassificacaoUseCase,
    ExcluirClassificacaoUseCase,
    RegistrarClassificacaoUseCase,
)
from src.modules.sigmun_met.application.use_cases.metadado_use_cases import (
    AlterarSituacaoMetadadoUseCase,
    AtivarMetadadoUseCase,
    AtualizarMetadadoUseCase,
    BuscarMetadadoUseCase,
    ConsultarMetadadoUseCase,
    CriarMetadadoUseCase,
    DeletarMetadadoUseCase,
    DesativarMetadadoUseCase,
    ExcluirMetadadoUseCase,
    ListarMetadadosUseCase,
    RegistrarMetadadoUseCase,
)
from src.modules.sigmun_met.application.use_cases.taxonomia_use_cases import (
    AtualizarTaxonomiaUseCase,
    BuscarTaxonomiaUseCase,
    ConsultarTaxonomiaUseCase,
    CriarTaxonomiaUseCase,
    DeletarTaxonomiaUseCase,
    ExcluirTaxonomiaUseCase,
    ListarTaxonomiasUseCase,
    RegistrarTaxonomiaUseCase,
)
from src.modules.sigmun_met.application.use_cases.termo_use_cases import (
    AtualizarTermoUseCase,
    BuscarTermoUseCase,
    ConsultarTermoUseCase,
    CriarTermoUseCase,
    DeletarTermoUseCase,
    ExcluirTermoUseCase,
    ListarTermosUseCase,
    RegistrarTermoUseCase,
)
from src.modules.sigmun_met.application.use_cases.valor_metadado_use_cases import (
    AtribuirValorMetadadoUseCase,
    BuscarValorMetadadoUseCase,
    ConsultarValorMetadadoUseCase,
    ListarValoresMetadadoUseCase,
    RegistrarValorMetadadoUseCase,
    RemoverValorMetadadoUseCase,
    ValidarValorMetadadoUseCase,
)

logger = logging.getLogger(__name__)

__all__ = [
    # Metadados
    "RegistrarMetadadoUseCase",
    "CriarMetadadoUseCase",
    "AtualizarMetadadoUseCase",
    "ConsultarMetadadoUseCase",
    "BuscarMetadadoUseCase",
    "ListarMetadadosUseCase",
    "AtivarMetadadoUseCase",
    "DesativarMetadadoUseCase",
    "AlterarSituacaoMetadadoUseCase",
    "ExcluirMetadadoUseCase",
    "DeletarMetadadoUseCase",
    # Valores de Metadado
    "RegistrarValorMetadadoUseCase",
    "AtribuirValorMetadadoUseCase",
    "ConsultarValorMetadadoUseCase",
    "BuscarValorMetadadoUseCase",
    "ListarValoresMetadadoUseCase",
    "RemoverValorMetadadoUseCase",
    "ValidarValorMetadadoUseCase",
    # Classificações
    "RegistrarClassificacaoUseCase",
    "CriarClassificacaoUseCase",
    "AtualizarClassificacaoUseCase",
    "ConsultarClassificacaoUseCase",
    "BuscarClassificacaoUseCase",
    "ExcluirClassificacaoUseCase",
    "DeletarClassificacaoUseCase",
    # Taxonomias
    "RegistrarTaxonomiaUseCase",
    "CriarTaxonomiaUseCase",
    "AtualizarTaxonomiaUseCase",
    "ConsultarTaxonomiaUseCase",
    "BuscarTaxonomiaUseCase",
    "ListarTaxonomiasUseCase",
    "ExcluirTaxonomiaUseCase",
    "DeletarTaxonomiaUseCase",
    # Termos de Taxonomia
    "RegistrarTermoUseCase",
    "CriarTermoUseCase",
    "AtualizarTermoUseCase",
    "ConsultarTermoUseCase",
    "BuscarTermoUseCase",
    "ListarTermosUseCase",
    "ExcluirTermoUseCase",
    "DeletarTermoUseCase",
]
