"""Caso de uso: Alterar situação processual de uma Compra.

Baseado em:
  - RN-COMPRAS-026 – Sequenciamento
  - RN-COMPRAS-027 – Pendências
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.alterar_situacao_compra_command import (
    AlterarSituacaoCompraCommand,
)
from src.modules.sigmun_compras.domain.entities.compra import Compra
from src.modules.sigmun_compras.domain.events.compra_events import (
    CompraSituacaoAlteradaEvent,
)
from src.modules.sigmun_compras.domain.exceptions import CompraNaoEncontradaError
from src.modules.sigmun_compras.domain.repositories.compra_repository import (
    CompraRepository,
)

logger = logging.getLogger(__name__)


class AlterarSituacaoCompraUseCase:
    """Orquestra a transição de situação processual de uma compra."""

    def __init__(self, repository: CompraRepository) -> None:
        self._repository = repository

    def execute(self, command: AlterarSituacaoCompraCommand) -> Compra:
        logger.info(
            "Alterando situação da compra – id=%s nova=%s",
            command.compra_id,
            command.nova_situacao,
        )

        compra = self._repository.get_by_id(command.compra_id)
        if compra is None or compra.foi_excluido():
            raise CompraNaoEncontradaError(
                f"Compra {command.compra_id} não encontrada"
            )

        situacao_anterior = compra.situacao

        # RN-026/027: valida sequência processual (ValueError se inválida)
        compra.alterar_situacao(command.nova_situacao, command.usuario_id)

        compra_atualizada = self._repository.update(compra)

        evento = CompraSituacaoAlteradaEvent(
            compra_id=compra_atualizada.id,
            situacao_anterior=situacao_anterior.value,
            situacao_nova=compra_atualizada.situacao.value,
            updated_at=compra_atualizada.updated_at,
        )
        logger.info("Situação da compra alterada: %s", evento)

        return compra_atualizada
