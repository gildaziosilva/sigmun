"""Caso de uso: Atualizar Contrato.

Baseado em:
  - RN-COMPRAS-036 a 039
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.atualizar_contrato_command import (
    AtualizarContratoCommand,
)
from src.modules.sigmun_compras.domain.entities.contrato import Contrato
from src.modules.sigmun_compras.domain.events.contrato_events import (
    ContratoAtualizadoEvent,
)
from src.modules.sigmun_compras.domain.exceptions import (
    ContratoDuplicadoError,
    ContratoNaoEncontradoError,
)
from src.modules.sigmun_compras.domain.repositories.contrato_repository import (
    ContratoRepository,
)

logger = logging.getLogger(__name__)


class AtualizarContratoUseCase:
    """Orquestra a atualização de um contrato."""

    def __init__(self, repository: ContratoRepository) -> None:
        self._repository = repository

    def execute(self, command: AtualizarContratoCommand) -> Contrato:
        logger.info("Atualizando contrato – id=%s", command.contrato_id)

        if all(
            v is None
            for v in (
                command.numero,
                command.data_inicio,
                command.data_fim,
                command.valor,
                command.objeto,
            )
        ):
            raise ValueError("Informe ao menos um campo para atualização")

        contrato = self._repository.get_by_id(command.contrato_id)
        if contrato is None or contrato.foi_excluido():
            raise ContratoNaoEncontradoError(
                f"Contrato {command.contrato_id} não encontrado"
            )

        # RN-COMPRAS-036: unicidade quando o numero mudar.
        if (
            command.numero is not None
            and command.numero.strip() != contrato.numero
            and self._repository.exists_numero(command.numero, excluir_id=contrato.id)
        ):
            raise ContratoDuplicadoError(
                f"Já existe contrato com numero={command.numero}"
            )

        contrato.atualizar_dados(
            numero=command.numero,
            data_inicio=command.data_inicio,
            data_fim=command.data_fim,
            valor=command.valor,
            objeto=command.objeto,
            usuario_id=command.usuario_id,
        )

        contrato_atualizado = self._repository.update(contrato)

        evento = ContratoAtualizadoEvent(
            contrato_id=contrato_atualizado.id,
            numero=contrato_atualizado.numero,
            valor=contrato_atualizado.valor,
            updated_at=contrato_atualizado.updated_at,
        )
        logger.info("Contrato atualizado: %s", evento)

        return contrato_atualizado
