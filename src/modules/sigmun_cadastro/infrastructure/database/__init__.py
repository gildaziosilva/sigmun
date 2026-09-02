"""Camada de persistência do módulo de Cadastro (DOM-CUM)."""

from src.modules.sigmun_cadastro.infrastructure.database.models import (
    CadastroBase,
    ContatoModel,
    DocumentoModel,
    EnderecoModel,
    PessoaFisicaModel,
    PessoaJuridicaModel,
    PessoaModel,
    UnidadeAdministrativaModel,
)

__all__ = [
    "CadastroBase",
    "PessoaModel",
    "PessoaFisicaModel",
    "PessoaJuridicaModel",
    "EnderecoModel",
    "DocumentoModel",
    "ContatoModel",
    "UnidadeAdministrativaModel",
]
