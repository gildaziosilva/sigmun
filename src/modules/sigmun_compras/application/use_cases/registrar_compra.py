"""Caso de uso: Registrar Compra (processo de compras).

Baseado em:
  - UC-COMPRAS-022 – Formalizar Contratação
  - ENT-COMPRAS-003 – Processo de Contratação
  - RN-COMPRAS-025 – Processo Único
  - RN-COMPRAS-030 – Identificação do Fornecedor
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.criar_compra_command import (
    CriarCompraCommand,
)
from src.modules.sigmun_compras.domain.entities.compra import Compra
from src.modules.sigmun_compras.domain.events.compra_events import CompraCriadaEvent
from src.modules.sigmun_compras.domain.exceptions import (
    FornecedorNaoEncontradoError,
    ProcessoDocumentalNaoEncontradoError,
    UnidadeNaoEncontradaError,
)
from src.modules.sigmun_compras.domain.repositories.compra_repository import (
    CompraRepository,
)

logger = logging.getLogger(__name__)


class RegistrarCompraUseCase:
    """Orquestra o registro de uma nova compra, validando os vínculos."""

    def __init__(self, repository: CompraRepository) -> None:
        self._repository = repository

    def execute(self, command: CriarCompraCommand) -> Compra:
        logger.info(
            "Registrando compra – processo=%s fornecedor=%s unidade=%s",
            command.processo_documental_id,
            command.fornecedor_id,
            command.unidade_id,
        )

        # RN-COMPRAS-025: vínculo obrigatório ao processo administrativo
        if not self._repository.exists_processo_documental(command.processo_documental_id):
            raise ProcessoDocumentalNaoEncontradoError(
                f"Processo documental {command.processo_documental_id} não encontrado"
            )

        # RN-COMPRAS-030: fornecedor deve existir e estar ativo
        if not self._repository.exists_fornecedor_ativo(command.fornecedor_id):
            raise FornecedorNaoEncontradoError(
                f"Fornecedor {command.fornecedor_id} não encontrado ou inativo"
            )

        if not self._repository.exists_unidade(command.unidade_id):
            raise UnidadeNaoEncontradaError(
                f"Unidade administrativa {command.unidade_id} não encontrada"
            )

        compra = Compra(
            processo_documental_id=command.processo_documental_id,
            fornecedor_id=command.fornecedor_id,
            unidade_id=command.unidade_id,
            numero=command.numero,
            data=command.data,
            valor_total=command.valor_total,
            situacao=command.situacao,
            created_by=command.usuario_id,
        )

        compra_salva = self._repository.save(compra)

        evento = CompraCriadaEvent(
            compra_id=compra_salva.id,
            numero=compra_salva.numero,
            processo_documental_id=compra_salva.processo_documental_id,
            fornecedor_id=compra_salva.fornecedor_id,
            unidade_id=compra_salva.unidade_id,
            situacao=compra_salva.situacao.value,
            data=compra_salva.data,
            created_at=compra_salva.created_at,
        )
        logger.info("Compra registrada: %s", evento)

        return compra_salva
