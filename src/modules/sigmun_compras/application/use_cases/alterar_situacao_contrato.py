"""Caso de uso: Alterar situação do Contrato."""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.alterar_situacao_contrato_command import (
    AlterarSituacaoContratoCommand,
)
from src.modules.sigmun_compras.domain.entities.contrato import Contrato
from src.modules.sigmun_compras.domain.events.contrato_events import (
    ContratoSituacaoAlteradaEvent,
)
from src.modules.sigmun_compras.domain.exceptions import (
    ContratoNaoEncontradoError,
)
from src.modules.sigmun_compras.domain.repositories.contrato_repository import (
    ContratoRepository,
)

logger = logging.getLogger(__name__)


class AlterarSituacaoContratoUseCase:
    """Orquestra a transição de situação de um contrato."""

    def __init__(self, repository: ContratoRepository) -> None:
        self._repository = repository

    def execute(self, command: AlterarSituacaoContratoCommand) -> Contrato:
        logger.info(
            "Alterando situação do contrato – id=%s nova=%s",
            command.contrato_id,
            command.nova_situacao,
        )

        contrato = self._repository.get_by_id(command.contrato_id)
        if contrato is None or contrato.foi_excluido():
            raise ContratoNaoEncontradoError(
                f"Contrato {command.contrato_id} não encontrado"
            )

        situacao_anterior = contrato.situacao

        # Valida a transição (ValueError se inválida).
        contrato.alterar_situacao(command.nova_situacao, command.usuario_id)

        contrato_atualizado = self._repository.update(contrato)

        evento = ContratoSituacaoAlteradaEvent(
            contrato_id=contrato_atualizado.id,
            situacao_anterior=situacao_anterior.value,
            situacao_nova=contrato_atualizado.situacao.value,
            updated_at=contrato_atualizado.updated_at,
        )
        logger.info("Situação do contrato alterada: %s", evento)

        return contrato_atualizado
