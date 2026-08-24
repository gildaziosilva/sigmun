"""Casos de uso do domínio Gestão de Compras e Contratações."""

from src.modules.sigmun_compras.application.use_cases.atualizar_fornecedor import (
    AtualizarFornecedorUseCase,
)
from src.modules.sigmun_compras.application.use_cases.consultar_fornecedor import (
    ConsultarFornecedorUseCase,
)
from src.modules.sigmun_compras.application.use_cases.inativar_fornecedor import (
    InativarFornecedorUseCase,
)
from src.modules.sigmun_compras.application.use_cases.listar_fornecedores import (
    ListarFornecedoresUseCase,
)
from src.modules.sigmun_compras.application.use_cases.registrar_fornecedor import (
    RegistrarFornecedorUseCase,
)

__all__ = [
    "RegistrarFornecedorUseCase",
    "ConsultarFornecedorUseCase",
    "ListarFornecedoresUseCase",
    "AtualizarFornecedorUseCase",
    "InativarFornecedorUseCase",
]


