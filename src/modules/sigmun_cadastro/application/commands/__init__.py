"""Commands do Cadastro Único Municipal (DOM-CUM)."""

from src.modules.sigmun_cadastro.application.commands.pessoa_commands import (
    AdicionarContatoCommand,
    AdicionarDocumentoCommand,
    AdicionarEnderecoCommand,
    AlterarCategoriaPessoaCommand,
    AtualizarPessoaFisicaCommand,
    AtualizarPessoaJuridicaCommand,
    CriarPessoaCommand,
    ExcluirPessoaCommand,
)
from src.modules.sigmun_cadastro.application.commands.unidade_commands import (
    AtualizarUnidadeCommand,
    CriarUnidadeCommand,
    ExcluirUnidadeCommand,
)

__all__ = [
    "CriarPessoaCommand",
    "AtualizarPessoaFisicaCommand",
    "AtualizarPessoaJuridicaCommand",
    "AlterarCategoriaPessoaCommand",
    "ExcluirPessoaCommand",
    "AdicionarEnderecoCommand",
    "AdicionarDocumentoCommand",
    "AdicionarContatoCommand",
    "CriarUnidadeCommand",
    "AtualizarUnidadeCommand",
    "ExcluirUnidadeCommand",
]
