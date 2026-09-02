"""Caso de uso: Registrar Contrato.

Baseado em:
  - UC-COMPRAS-024 – Registrar Contrato
  - RN-COMPRAS-036 – Identificação Única
  - RN-COMPRAS-038 – Objeto/Processo Contratual
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.criar_contrato_command import (
    CriarContratoCommand,
)
from src.modules.sigmun_compras.domain.entities.contrato import Contrato
from src.modules.sigmun_compras.domain.events.contrato_events import (
    ContratoCriadoEvent,
)
from src.modules.sigmun_compras.domain.exceptions import (
    ContratoDuplicadoError,
    FornecedorNaoEncontradoError,
    ProcessoDocumentalNaoEncontradoError,
    UnidadeNaoEncontradaError,
)
from src.modules.sigmun_compras.domain.repositories.contrato_repository import (
    ContratoRepository,
)

logger = logging.getLogger(__name__)


class RegistrarContratoUseCase:
    """Orquestra o registro de um novo contrato, validando os vínculos."""

    def __init__(self, repository: ContratoRepository) -> None:
        self._repository = repository

    def execute(self, command: CriarContratoCommand) -> Contrato:
        logger.info("Registrando contrato – numero=%s", command.numero)

        # RN-COMPRAS-038: vínculo obrigatório ao processo contratado.
        if not self._repository.exists_processo_documental(
            command.processo_documental_id
        ):
            raise ProcessoDocumentalNaoEncontradoError(
                f"Processo documental {command.processo_documental_id} não encontrado"
            )

        if not self._repository.exists_fornecedor_ativo(command.fornecedor_id):
            raise FornecedorNaoEncontradoError(
                f"Fornecedor {command.fornecedor_id} não encontrado ou inativo"
            )

        if not self._repository.exists_unidade(command.unidade_id):
            raise UnidadeNaoEncontradaError(
                f"Unidade administrativa {command.unidade_id} não encontrada"
            )

        # RN-COMPRAS-036: identificação única.
        if self._repository.exists_numero(command.numero):
            raise ContratoDuplicadoError(
                f"Já existe contrato com numero={command.numero}"
            )

        contrato = Contrato(
            processo_documental_id=command.processo_documental_id,
            fornecedor_id=command.fornecedor_id,
            unidade_id=command.unidade_id,
            licitacao_master_id=command.licitacao_master_id,
            numero=command.numero,
            data_inicio=command.data_inicio,
            data_fim=command.data_fim,
            valor=command.valor,
            objeto=command.objeto,
            situacao=command.situacao,
            created_by=command.usuario_id,
        )

        contrato_salvo = self._repository.save(contrato)

        evento = ContratoCriadoEvent(
            contrato_id=contrato_salvo.id,
            numero=contrato_salvo.numero,
            processo_documental_id=contrato_salvo.processo_documental_id,
            fornecedor_id=contrato_salvo.fornecedor_id,
            unidade_id=contrato_salvo.unidade_id,
            situacao=contrato_salvo.situacao.value,
            created_at=contrato_salvo.created_at,
        )
        logger.info("Contrato registrado: %s", evento)

        return contrato_salvo
