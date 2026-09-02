"""Caso de uso: Adicionar Endereço a uma Pessoa (DOM-CUM RN-CUM-005)."""

from __future__ import annotations

import logging

from src.modules.sigmun_cadastro.application.commands.pessoa_commands import (
    AdicionarEnderecoCommand,
)
from src.modules.sigmun_cadastro.domain.entities.pessoa import Pessoa
from src.modules.sigmun_cadastro.domain.exceptions import PessoaNaoEncontradoError
from src.modules.sigmun_cadastro.domain.repositories.pessoa_repository import (
    PessoaRepository,
)

logger = logging.getLogger(__name__)


class AdicionarEnderecoUseCase:
    """Adiciona um endereço ao agregado da pessoa (RN-CUM-005).

    Se ``principal``, os demais endereços vigentes deixam de ser
    principais (comportamento do agregado).
    """

    def __init__(self, repository: PessoaRepository) -> None:
        self._repository = repository

    def execute(self, command: AdicionarEnderecoCommand) -> Pessoa:
        pessoa = self._repository.get_by_id(command.pessoa_id)
        if pessoa is None:
            raise PessoaNaoEncontradoError(f"Pessoa {command.pessoa_id} não encontrada")
        endereco = pessoa.adicionar_endereco(
            tipo=command.tipo,
            logradouro=command.logradouro,
            numero=command.numero,
            usuario_id=command.usuario_id,
            complemento=command.complemento,
            bairro=command.bairro,
            cep=command.cep,
            cidade=command.cidade,
            estado=command.estado,
            pais=command.pais,
            principal=command.principal,
        )
        salvo = self._repository.save(pessoa)
        logger.info(
            "Endereço %s adicionado à pessoa %s", endereco.id, command.pessoa_id
        )
        return salvo


__all__ = ["AdicionarEnderecoUseCase"]
