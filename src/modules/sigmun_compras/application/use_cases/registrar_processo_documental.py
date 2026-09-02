"""Caso de uso: Abrir Processo Documental.

Baseado em:
  - UC-COMPRAS-013 – Abrir Processo de Contratação
  - RN-COMPRAS-025 – Processo Único
  - RN-COMPRAS-028 – Responsabilidade
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.criar_processo_documental_command import (
    CriarProcessoDocumentalCommand,
)
from src.modules.sigmun_compras.domain.entities.processo_documental import (
    ProcessoDocumental,
)
from src.modules.sigmun_compras.domain.events.processo_documental_events import (
    ProcessoDocumentalAbertoEvent,
)
from src.modules.sigmun_compras.domain.exceptions import (
    ProcessoDocumentalDuplicadoError,
    UnidadeNaoEncontradaError,
)
from src.modules.sigmun_compras.domain.repositories.processo_documental_repository import (
    ProcessoDocumentalRepository,
)

logger = logging.getLogger(__name__)


class RegistrarProcessoDocumentalUseCase:
    """Orquestra a abertura de um novo processo documental."""

    def __init__(self, repository: ProcessoDocumentalRepository) -> None:
        self._repository = repository

    def execute(self, command: CriarProcessoDocumentalCommand) -> ProcessoDocumental:
        logger.info(
            "Abrindo processo documental – numero=%s ano=%s",
            command.numero,
            command.ano,
        )

        if not self._repository.exists_unidade(command.unidade_id):
            raise UnidadeNaoEncontradaError(
                f"Unidade administrativa {command.unidade_id} não encontrada"
            )

        # Unicidade cadastral do par (numero, ano) — espelha a constraint
        # uq_processos_documentais_numero_ano.
        if self._repository.exists_numero_ano(command.numero, command.ano):
            raise ProcessoDocumentalDuplicadoError(
                f"Já existe processo documental numero={command.numero} "
                f"ano={command.ano}"
            )

        processo = ProcessoDocumental(
            unidade_id=command.unidade_id,
            numero=command.numero,
            ano=command.ano,
            assunto=command.assunto,
            descricao=command.descricao,
            created_by=command.usuario_id,
        )

        processo_salvo = self._repository.save(processo)

        evento = ProcessoDocumentalAbertoEvent(
            processo_id=processo_salvo.id,
            numero=processo_salvo.numero,
            ano=processo_salvo.ano,
            unidade_id=processo_salvo.unidade_id,
            created_at=processo_salvo.created_at,
        )
        logger.info("Processo documental aberto: %s", evento)

        return processo_salvo
