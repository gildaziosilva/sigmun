"""Casos de uso do Cadastro Único Municipal (DOM-CUM)."""

from src.modules.sigmun_cadastro.application.use_cases.atualizar_pessoa import (
    AlterarCategoriaPessoaUseCase,
    AtualizarPessoaFisicaUseCase,
    AtualizarPessoaJuridicaUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.atualizar_unidade import (
    AtualizarUnidadeUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.consultar_pessoa import (
    ConsultarPessoaUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.consultar_unidade import (
    ConsultarUnidadeUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.excluir_pessoa import (
    ExcluirPessoaUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.excluir_unidade import (
    ExcluirUnidadeUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.listar_pessoas import (
    ListarPessoasUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.listar_unidades import (
    ListarUnidadesUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.registrar_pessoa import (
    RegistrarPessoaUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.registrar_unidade import (
    RegistrarUnidadeUseCase,
)

__all__ = [
    "RegistrarPessoaUseCase",
    "ConsultarPessoaUseCase",
    "ListarPessoasUseCase",
    "AtualizarPessoaFisicaUseCase",
    "AtualizarPessoaJuridicaUseCase",
    "AlterarCategoriaPessoaUseCase",
    "ExcluirPessoaUseCase",
    "RegistrarUnidadeUseCase",
    "ConsultarUnidadeUseCase",
    "ListarUnidadesUseCase",
    "AtualizarUnidadeUseCase",
    "ExcluirUnidadeUseCase",
]
