"""Caso de uso: Registrar Fornecedor.

Baseado em:
  - UC-COMPRAS-019 – Cadastrar Fornecedor
  - HU-COMPRAS-019 – Cadastrar Fornecedor
  - RF-COMPRAS-033 – Cadastrar Fornecedor (P0)
  - RN-COMPRAS-030 – Identificação do Fornecedor
  - RN-COMPRAS-031 – Unicidade Cadastral
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.criar_fornecedor_command import (
    CriarFornecedorCommand,
)
from src.modules.sigmun_compras.domain.entities.fornecedor import (
    Fornecedor,
)
from src.modules.sigmun_compras.domain.events.fornecedor_events import FornecedorCriadoEvent
from src.modules.sigmun_compras.domain.exceptions import (
    FornecedorJaCadastradoError,
)
from src.modules.sigmun_compras.domain.repositories.fornecedor_repository import (
    FornecedorRepository,
)

logger = logging.getLogger(__name__)


class RegistrarFornecedorUseCase:
    """Orquestra o registro de um novo fornecedor."""

    def __init__(self, repository: FornecedorRepository) -> None:
        self._repository = repository

    def execute(self, command: CriarFornecedorCommand) -> Fornecedor:
        logger.info(
            "Registrando fornecedor – pessoa_juridica_id=%s",
            command.pessoa_juridica_id,
        )

        # RN-COMPRAS-030: Identificação suficiente
        if command.pessoa_juridica_id is None:
            raise ValueError("pessoa_juridica_id é obrigatório (RN-COMPRAS-030)")

        # RN-COMPRAS-031: Unicidade Cadastral
        if self._repository.exists_pessoa_juridica(command.pessoa_juridica_id):
            raise FornecedorJaCadastradoError(
                f"Já existe um fornecedor vinculado à pessoa jurídica "
                f"{command.pessoa_juridica_id} (RN-COMPRAS-031)"
            )

        fornecedor = Fornecedor(
            pessoa_juridica_id=command.pessoa_juridica_id,
            situacao_cadastro=command.situacao_cadastro,
            created_by=command.usuario_id,
        )

        fornecedor_salvo = self._repository.save(fornecedor)

        # Evento de domínio (RN-COMPRAS-033: auditoria)
        evento = FornecedorCriadoEvent(
            fornecedor_id=fornecedor_salvo.id,
            pessoa_juridica_id=fornecedor_salvo.pessoa_juridica_id,
            situacao_cadastro=fornecedor_salvo.situacao_cadastro.value,
            created_at=fornecedor_salvo.created_at,
        )
        logger.info("Fornecedor registrado: %s", evento)

        return fornecedor_salvo
