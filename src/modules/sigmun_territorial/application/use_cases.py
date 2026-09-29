"""Agregador dos casos de uso do DOM-TEL — Gestão Territorial.

A implementação está separada por agregado (`use_cases_bairro`,
`use_cases_logradouro`, `use_cases_planta`, `use_cases_geo`) para manter
arquivos pequenos; este módulo consolida a superfície pública.
"""

from .use_cases_bairro import (
    AtualizarBairroInput,
    AtualizarBairroUseCase,
    CadastrarBairroInput,
    CadastrarBairroUseCase,
    ExcluirBairroUseCase,
)
from .use_cases_geo import (
    ExcluirGeorreferenciaUseCase,
    RegistrarGeorreferenciaInput,
    RegistrarGeorreferenciaUseCase,
)
from .use_cases_logradouro import (
    AtualizarLogradouroInput,
    AtualizarLogradouroUseCase,
    CadastrarLogradouroInput,
    CadastrarLogradouroUseCase,
    ExcluirLogradouroUseCase,
)
from .use_cases_planta import (
    AtivarPlantaValoresUseCase,
    AtualizarPlantaValoresInput,
    AtualizarPlantaValoresUseCase,
    CadastrarPlantaValoresInput,
    CadastrarPlantaValoresUseCase,
    RevogarPlantaValoresUseCase,
)

__all__ = [
    "CadastrarBairroInput",
    "CadastrarBairroUseCase",
    "AtualizarBairroInput",
    "AtualizarBairroUseCase",
    "ExcluirBairroUseCase",
    "CadastrarLogradouroInput",
    "CadastrarLogradouroUseCase",
    "AtualizarLogradouroInput",
    "AtualizarLogradouroUseCase",
    "ExcluirLogradouroUseCase",
    "CadastrarPlantaValoresInput",
    "CadastrarPlantaValoresUseCase",
    "AtualizarPlantaValoresInput",
    "AtualizarPlantaValoresUseCase",
    "AtivarPlantaValoresUseCase",
    "RevogarPlantaValoresUseCase",
    "RegistrarGeorreferenciaInput",
    "RegistrarGeorreferenciaUseCase",
    "ExcluirGeorreferenciaUseCase",
]
