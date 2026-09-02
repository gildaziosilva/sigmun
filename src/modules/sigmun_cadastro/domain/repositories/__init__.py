"""Contratos de repositório do domínio de Cadastro Único Municipal."""

from src.modules.sigmun_cadastro.domain.repositories.pessoa_repository import (
    PessoaRepository,
)
from src.modules.sigmun_cadastro.domain.repositories.unidade_administrativa_repository import (
    UnidadeAdministrativaRepository,
)

__all__ = ["PessoaRepository", "UnidadeAdministrativaRepository"]
