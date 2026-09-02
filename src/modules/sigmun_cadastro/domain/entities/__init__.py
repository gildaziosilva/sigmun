"""Entidades do domínio de Cadastro Único Municipal."""

from src.modules.sigmun_cadastro.domain.entities.contato import Contato, TipoContato
from src.modules.sigmun_cadastro.domain.entities.documento import Documento, TipoDocumento
from src.modules.sigmun_cadastro.domain.entities.endereco import Endereco, TipoEndereco
from src.modules.sigmun_cadastro.domain.entities.pessoa import (
    CategoriaPessoa,
    DadosFisicos,
    DadosJuridicos,
    Pessoa,
    Sexo,
    TipoPessoa,
)
from src.modules.sigmun_cadastro.domain.entities.unidade_administrativa import (
    UnidadeAdministrativa,
)

__all__ = [
    "Pessoa",
    "TipoPessoa",
    "CategoriaPessoa",
    "Sexo",
    "DadosFisicos",
    "DadosJuridicos",
    "Endereco",
    "TipoEndereco",
    "Documento",
    "TipoDocumento",
    "Contato",
    "TipoContato",
    "UnidadeAdministrativa",
]
