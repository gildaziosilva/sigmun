"""Caso de uso: Atualizar Fornecedor.

Baseado em:
  - RN-COMPRAS-033 – Dados Cadastrais
  - RN-COMPRAS-031 – Unicidade Cadastral (não duplicar)
  - SRV-COMPRAS-007 – Gestão de Fornecedores
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.atualizar_fornecedor_command import (
    AtualizarFornecedorCommand,
)
from src.modules.sigmun_compras.domain.entities.fornecedor import Fornecedor
from src.modules.sigmun_compras.domain.events.fornecedor_events import (
    FornecedorAtualizadoEvent,
)
from src.modules.sigmun_compras.domain.exceptions import (
    FornecedorNaoEncontradoError,
)
from src.modules.sigmun_compras.domain.repositories.fornecedor_repository import (
    FornecedorRepository,
)

logger = logging.getLogger(__name__)


class AtualizarFornecedorUseCase:
    """Orquestra a atualização de dados de um fornecedor."""

    def __init__(self, repository: FornecedorRepository) -> None:
        self._repository = repository

    def execute(self, command: AtualizarFornecedorCommand) -> Fornecedor:
        logger.info("Atualizando fornecedor – id=%s", command.fornecedor_id)

        fornecedor = self._repository.get_by_id(command.fornecedor_id)
        if fornecedor is None or fornecedor.foi_excluido():
            raise FornecedorNaoEncontradoError(
                f"Fornecedor {command.fornecedor_id} não encontrado"
            )

        fornecedor.atualizar_situacao(command.situacao_cadastro, command.usuario_id)

        fornecedor_atualizado = self._repository.update(fornecedor)

        evento = FornecedorAtualizadoEvent(
            fornecedor_id=fornecedor_atualizado.id,
            pessoa_juridica_id=fornecedor_atualizado.pessoa_juridica_id,
            situacao_cadastro=fornecedor_atualizado.situacao_cadastro.value,
            updated_at=fornecedor_atualizado.updated_at,
        )
        logger.info("Fornecedor atualizado: %s", evento)

        return fornecedor_atualizado
