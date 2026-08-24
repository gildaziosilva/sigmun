"""Caso de uso: Atualizar Processo Documental."""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.atualizar_processo_documental_command import (
    AtualizarProcessoDocumentalCommand,
)
from src.modules.sigmun_compras.domain.entities.processo_documental import (
    ProcessoDocumental,
)
from src.modules.sigmun_compras.domain.events.processo_documental_events import (
    ProcessoDocumentalAtualizadoEvent,
)
from src.modules.sigmun_compras.domain.exceptions import (
    ProcessoDocumentalDuplicadoError,
    ProcessoDocumentalNaoEncontradoError,
)
from src.modules.sigmun_compras.domain.repositories.processo_documental_repository import (
    ProcessoDocumentalRepository,
)

logger = logging.getLogger(__name__)


class AtualizarProcessoDocumentalUseCase:
    """Orquestra a atualização de um processo documental."""

    def __init__(self, repository: ProcessoDocumentalRepository) -> None:
        self._repository = repository

    def execute(
        self, command: AtualizarProcessoDocumentalCommand
    ) -> ProcessoDocumental:
        logger.info("Atualizando processo documental – id=%s", command.processo_id)

        if all(
            v is None
            for v in (command.numero, command.ano, command.assunto, command.descricao)
        ):
            raise ValueError("Informe ao menos um campo para atualização")

        processo = self._repository.get_by_id(command.processo_id)
        if processo is None or processo.foi_excluido():
            raise ProcessoDocumentalNaoEncontradoError(
                f"Processo documental {command.processo_id} não encontrado"
            )

        # Unicidade do par (numero, ano) quando algum dos dois mudar.
        novo_numero = command.numero if command.numero is not None else processo.numero
        novo_ano = command.ano if command.ano is not None else processo.ano
        par_alterado = (novo_numero, novo_ano) != (processo.numero, processo.ano)
        if par_alterado and self._repository.exists_numero_ano(
            novo_numero, novo_ano, excluir_id=processo.id
        ):
            raise ProcessoDocumentalDuplicadoError(
                f"Já existe processo documental numero={novo_numero} "
                f"ano={novo_ano}"
            )

        processo.atualizar_dados(
            numero=command.numero,
            ano=command.ano,
            assunto=command.assunto,
            descricao=command.descricao,
            usuario_id=command.usuario_id,
        )

        processo_atualizado = self._repository.update(processo)

        evento = ProcessoDocumentalAtualizadoEvent(
            processo_id=processo_atualizado.id,
            numero=processo_atualizado.numero,
            ano=processo_atualizado.ano,
            updated_at=processo_atualizado.updated_at,
        )
        logger.info("Processo documental atualizado: %s", evento)

        return processo_atualizado
