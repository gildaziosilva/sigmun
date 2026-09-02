"""Casos de uso: Atualizar Pessoa (DOM-CUM).

Três operações: atualização de dados físicos (PF), jurídicos (PJ) e
alteração de categoria (RN-CUM-007: não operar sobre excluída).
"""

from __future__ import annotations

import logging

from src.modules.sigmun_cadastro.application.commands.pessoa_commands import (
    AlterarCategoriaPessoaCommand,
    AtualizarPessoaFisicaCommand,
    AtualizarPessoaJuridicaCommand,
)
from src.modules.sigmun_cadastro.domain.entities.pessoa import Pessoa
from src.modules.sigmun_cadastro.domain.events.pessoa_events import PessoaAtualizadaEvent
from src.modules.sigmun_cadastro.domain.exceptions import (
    PessoaExcluidaError,
    PessoaNaoEncontradoError,
)
from src.modules.sigmun_cadastro.domain.repositories.pessoa_repository import (
    PessoaRepository,
)
from uuid import uuid4

logger = logging.getLogger(__name__)


class AtualizarPessoaFisicaUseCase:
    """Atualiza os dados da extensão física de uma pessoa (PATCH parcial)."""

    def __init__(self, repository: PessoaRepository) -> None:
        self._repository = repository

    def execute(self, command: AtualizarPessoaFisicaCommand) -> Pessoa:
        pessoa = self._repository.get_by_id(command.pessoa_id)
        if pessoa is None:
            raise PessoaNaoEncontradoError(f"Pessoa {command.pessoa_id} não encontrada")
        try:
            pessoa.atualizar_dados_fisicos(
                usuario_id=command.usuario_id,
                nome=command.nome,
                data_nascimento=command.data_nascimento,
                sexo=command.sexo,
                estado_civil=command.estado_civil,
                mae=command.mae,
                pai=command.pai,
            )
        except ValueError as exc:
            raise PessoaExcluidaError(str(exc)) from exc
        salvo = self._repository.save(pessoa)
        logger.info(
            "Pessoa física atualizada: %s (%s)",
            PessoaAtualizadaEvent(
                event_id=uuid4(), pessoa_id=salvo.id, occurred_at=salvo.updated_at
            ),
        )
        return salvo


class AtualizarPessoaJuridicaUseCase:
    """Atualiza os dados da extensão jurídica de uma pessoa (PATCH parcial)."""

    def __init__(self, repository: PessoaRepository) -> None:
        self._repository = repository

    def execute(self, command: AtualizarPessoaJuridicaCommand) -> Pessoa:
        pessoa = self._repository.get_by_id(command.pessoa_id)
        if pessoa is None:
            raise PessoaNaoEncontradoError(f"Pessoa {command.pessoa_id} não encontrada")
        try:
            pessoa.atualizar_dados_juridicos(
                usuario_id=command.usuario_id,
                razao_social=command.razao_social,
                nome_fantasia=command.nome_fantasia,
                cnae_principal=command.cnae_principal,
                capital=command.capital,
            )
        except ValueError as exc:
            raise PessoaExcluidaError(str(exc)) from exc
        return self._repository.save(pessoa)


class AlterarCategoriaPessoaUseCase:
    """Altera a categoria cadastral da pessoa."""

    def __init__(self, repository: PessoaRepository) -> None:
        self._repository = repository

    def execute(self, command: AlterarCategoriaPessoaCommand) -> Pessoa:
        pessoa = self._repository.get_by_id(command.pessoa_id)
        if pessoa is None:
            raise PessoaNaoEncontradoError(f"Pessoa {command.pessoa_id} não encontrada")
        try:
            pessoa.alterar_categoria(command.categoria, usuario_id=command.usuario_id)
        except ValueError as exc:
            raise PessoaExcluidaError(str(exc)) from exc
        return self._repository.save(pessoa)


__all__ = [
    "AtualizarPessoaFisicaUseCase",
    "AtualizarPessoaJuridicaUseCase",
    "AlterarCategoriaPessoaUseCase",
]
