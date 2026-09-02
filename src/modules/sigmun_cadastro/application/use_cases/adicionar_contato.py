"""Caso de uso: Adicionar Contato a uma Pessoa (DOM-CUM RN-CUM-006)."""

from __future__ import annotations

import logging

from src.modules.sigmun_cadastro.application.commands.pessoa_commands import (
    AdicionarContatoCommand,
)
from src.modules.sigmun_cadastro.domain.entities.pessoa import Pessoa
from src.modules.sigmun_cadastro.domain.exceptions import PessoaNaoEncontradoError
from src.modules.sigmun_cadastro.domain.repositories.pessoa_repository import (
    PessoaRepository,
)

logger = logging.getLogger(__name__)


class AdicionarContatoUseCase:
    """Adiciona um contato (tel/e-mail/redes/whatsapp) ao agregado."""

    def __init__(self, repository: PessoaRepository) -> None:
        self._repository = repository

    def execute(self, command: AdicionarContatoCommand) -> Pessoa:
        pessoa = self._repository.get_by_id(command.pessoa_id)
        if pessoa is None:
            raise PessoaNaoEncontradoError(f"Pessoa {command.pessoa_id} não encontrada")
        pessoa.adicionar_contato(
            tipo=command.tipo,
            valor=command.valor,
            usuario_id=command.usuario_id,
            principal=command.principal,
        )
        salvo = self._repository.save(pessoa)
        logger.info(
            "Contato %s adicionado à pessoa %s", command.tipo.value, command.pessoa_id
        )
        return salvo


__all__ = ["AdicionarContatoUseCase"]
