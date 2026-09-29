"""Agregador dos casos de uso do DOM-OBR — Obras e Infraestrutura.

A implementação está separada por agregado (`use_cases_obra`,
`use_cases_medicao`, `use_cases_despesa`, `use_cases_acompanhamento`) para
manter arquivos pequenos; este módulo consolida a superfície pública.
"""

from .use_cases_acompanhamento import (
    AtualizarEtapaUseCase,
    CadastrarEtapaInput,
    CadastrarEtapaUseCase,
    ConcluirEtapaUseCase,
    RegistrarVistoriaInput,
    RegistrarVistoriaUseCase,
)
from .use_cases_despesa import (
    ExcluirDespesaUseCase,
    RegistrarDespesaInput,
    RegistrarDespesaUseCase,
)
from .use_cases_medicao import (
    AprovarMedicaoUseCase,
    CancelarMedicaoUseCase,
    GlosarMedicaoUseCase,
    RegistrarMedicaoInput,
    RegistrarMedicaoUseCase,
    recalcular_avanco,
)
from .use_cases_obra import (
    AtualizarObraInput,
    AtualizarObraUseCase,
    CadastrarObraInput,
    CadastrarObraUseCase,
    CancelarObraUseCase,
    ConcluirObraUseCase,
    ExcluirObraUseCase,
    IniciarExecucaoObraUseCase,
    SuspenderObraUseCase,
)

__all__ = [
    "CadastrarObraInput",
    "CadastrarObraUseCase",
    "AtualizarObraInput",
    "AtualizarObraUseCase",
    "IniciarExecucaoObraUseCase",
    "ConcluirObraUseCase",
    "SuspenderObraUseCase",
    "CancelarObraUseCase",
    "ExcluirObraUseCase",
    "RegistrarMedicaoInput",
    "RegistrarMedicaoUseCase",
    "AprovarMedicaoUseCase",
    "GlosarMedicaoUseCase",
    "CancelarMedicaoUseCase",
    "RegistrarDespesaInput",
    "RegistrarDespesaUseCase",
    "ExcluirDespesaUseCase",
    "CadastrarEtapaInput",
    "CadastrarEtapaUseCase",
    "AtualizarEtapaUseCase",
    "ConcluirEtapaUseCase",
    "RegistrarVistoriaInput",
    "RegistrarVistoriaUseCase",
    "recalcular_avanco",
]
