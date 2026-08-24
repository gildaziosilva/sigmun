"""Caso de uso: Inativar Fornecedor.

Baseado em:
  - RN-COMPRAS-030 – Identificação do Fornecedor
  - RN-COMPRAS-031 – Unicidade Cadastral
  - RN-COMPRAS-032 – Histórico (soft-delete preserva histórico)
  - RN-COMPRAS-033 – Dados Cadastrais (preserva histórico de auditoria)
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.inativar_fornecedor_command import (
    InativarFornecedorCommand,
)
from src.modules.sigmun_compras.domain.entities.fornecedor import Fornecedor
from src.modules.sigmun_compras.domain.events.fornecedor_events import (
    FornecedorInativadoEvent,
)
from src.modules.sigmun_compras.domain.exceptions import (
    FornecedorNaoEncontradoError,
)
from src.modules.sigmun_compras.domain.repositories.fornecedor_repository import (
    FornecedorRepository,
)

logger = logging.getLogger(__name__)


class InativarFornecedorUseCase:
    """Orquestra a inativação (soft-delete) de um fornecedor."""

    def __init__(self, repository: FornecedorRepository) -> None:
        self._repository = repository

    def execute(self, command: InativarFornecedorCommand) -> Fornecedor:
        logger.info("Inativando fornecedor – id=%s", command.fornecedor_id)

        fornecedor = self._repository.get_by_id(command.fornecedor_id)
        if fornecedor is None or fornecedor.foi_excluido():
            raise FornecedorNaoEncontradoError(
                f"Fornecedor {command.fornecedor_id} não encontrado"
            )

        fornecedor.inativar(command.usuario_id)

        # O soft-delete é registrado via repository.delete
        self._repository.delete(command.fornecedor_id, command.usuario_id)

        evento = FornecedorInativadoEvent(
            fornecedor_id=fornecedor.id,
            pessoa_juridica_id=fornecedor.pessoa_juridica_id,
            updated_at=fornecedor.updated_at,
        )
        logger.info("Fornecedor inativado: %s", evento)

        return fornecedor
