"""Value objects do domínio de Cadastro Único Municipal."""

from src.modules.sigmun_cadastro.domain.value_objects.cnpj import CNPJ
from src.modules.sigmun_cadastro.domain.value_objects.cpf import CPF

__all__ = ["CPF", "CNPJ"]
