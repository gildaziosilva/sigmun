"""Agregador dos casos de uso do DOM-IMO — Cadastro Imobiliário.

A implementação está separada por agregado (`use_cases_imovel`,
`use_cases_avaliacao`); este módulo consolida a superfície pública.
"""

from .use_cases_avaliacao import (
    AvaliarImovelInput,
    AvaliarImovelUseCase,
    CancelarAvaliacaoUseCase,
    ConcluirAvaliacaoUseCase,
    RegistrarCaracteristicaInput,
    RegistrarCaracteristicaUseCase,
    RegistrarGeometriaInput,
    RegistrarGeometriaUseCase,
    ocupacao_do_imovel,
)
from .use_cases_imovel import (
    AlterarSituacaoImovelUseCase,
    AtualizarImovelInput,
    AtualizarImovelUseCase,
    CadastrarImovelInput,
    CadastrarImovelUseCase,
    ExcluirImovelUseCase,
    RemoverProprietarioUseCase,
    VincularProprietarioInput,
    VincularProprietarioUseCase,
)

__all__ = [
    "CadastrarImovelInput",
    "CadastrarImovelUseCase",
    "AtualizarImovelInput",
    "AtualizarImovelUseCase",
    "AlterarSituacaoImovelUseCase",
    "ExcluirImovelUseCase",
    "VincularProprietarioInput",
    "VincularProprietarioUseCase",
    "RemoverProprietarioUseCase",
    "AvaliarImovelInput",
    "AvaliarImovelUseCase",
    "ConcluirAvaliacaoUseCase",
    "CancelarAvaliacaoUseCase",
    "RegistrarCaracteristicaInput",
    "RegistrarCaracteristicaUseCase",
    "RegistrarGeometriaInput",
    "RegistrarGeometriaUseCase",
    "ocupacao_do_imovel",
]
