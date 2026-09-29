"""Agregador dos casos de uso do DOM-GEO — Geoinformação Municipal.

A implementação está separada por agregado (`use_cases_camada`,
`use_cases_mapa`, `use_cases_feature`, `use_cases_servico`) para manter
arquivos pequenos; este módulo consolida a superfície pública.
"""

from .use_cases_camada import (
    AtivarCamadaUseCase,
    AtualizarCamadaInput,
    AtualizarCamadaUseCase,
    CadastrarCamadaInput,
    CadastrarCamadaUseCase,
    DesativarCamadaUseCase,
    ExcluirCamadaUseCase,
)
from .use_cases_feature import (
    ExcluirFeatureUseCase,
    RegistrarFeatureInput,
    RegistrarFeatureUseCase,
)
from .use_cases_mapa import (
    ArquivarMapaUseCase,
    AtualizarMapaInput,
    AtualizarMapaUseCase,
    CadastrarMapaInput,
    CadastrarMapaUseCase,
    ComporCamadaInput,
    ComporCamadaUseCase,
    ExcluirMapaUseCase,
    PublicarMapaUseCase,
    RemoverComposicaoUseCase,
)
from .use_cases_servico import (
    AtualizarServicoInput,
    AtualizarServicoUseCase,
    CadastrarServicoInput,
    CadastrarServicoUseCase,
    ExcluirServicoUseCase,
    InativarServicoUseCase,
)

__all__ = [
    "CadastrarCamadaInput",
    "CadastrarCamadaUseCase",
    "AtualizarCamadaInput",
    "AtualizarCamadaUseCase",
    "AtivarCamadaUseCase",
    "DesativarCamadaUseCase",
    "ExcluirCamadaUseCase",
    "CadastrarMapaInput",
    "CadastrarMapaUseCase",
    "AtualizarMapaInput",
    "AtualizarMapaUseCase",
    "ComporCamadaInput",
    "ComporCamadaUseCase",
    "RemoverComposicaoUseCase",
    "PublicarMapaUseCase",
    "ArquivarMapaUseCase",
    "ExcluirMapaUseCase",
    "RegistrarFeatureInput",
    "RegistrarFeatureUseCase",
    "ExcluirFeatureUseCase",
    "CadastrarServicoInput",
    "CadastrarServicoUseCase",
    "AtualizarServicoInput",
    "AtualizarServicoUseCase",
    "InativarServicoUseCase",
    "ExcluirServicoUseCase",
]
