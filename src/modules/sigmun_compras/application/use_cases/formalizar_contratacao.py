"""Caso de uso: Formalizar Contratação (integração Compra -> Contrato).

Baseado em:
  - UC-COMPRAS-022 – Formalizar Contratação
  - RN-COMPRAS-026 – Sequência processual (HOMOLOGADO -> CONTRATADO)
  - RN-COMPRAS-036 – Identificação única do contrato
  - RN-COMPRAS-038 – Objeto/Processo contratual

Esta é a integração central do domínio Compras com o subdomínio de
Contratos: compõe os repositórios de Compra e de Contrato sem acoplar a
persistência entre os domínios.
"""

from __future__ import annotations

import logging

from src.modules.sigmun_compras.application.commands.formalizar_contratacao_command import (
    FormalizarContratacaoCommand,
)
from src.modules.sigmun_compras.domain.entities.compra import SituacaoCompra
from src.modules.sigmun_compras.domain.entities.contrato import (
    Contrato,
    SituacaoContrato,
)
from src.modules.sigmun_compras.domain.events.contrato_events import (
    ContratoCriadoEvent,
)
from src.modules.sigmun_compras.domain.exceptions import (
    CompraNaoEncontradaError,
    ContratoDuplicadoError,
    FornecedorNaoEncontradoError,
    ProcessoDocumentalNaoEncontradoError,
    UnidadeNaoEncontradaError,
)
from src.modules.sigmun_compras.domain.repositories.compra_repository import (
    CompraRepository,
)
from src.modules.sigmun_compras.domain.repositories.contrato_repository import (
    ContratoRepository,
)

logger = logging.getLogger(__name__)


class FormalizarContratacaoUseCase:
    """Orquestra a formalização do contrato a partir de uma compra homologada."""

    SITUACOES_ELEGIVEIS = {
        SituacaoCompra.HOMOLOGADO,
        SituacaoCompra.CONTRATADO,
    }

    def __init__(
        self,
        contratos: ContratoRepository,
        compras: CompraRepository,
    ) -> None:
        self._contratos = contratos
        self._compras = compras

    def execute(self, command: FormalizarContratacaoCommand) -> Contrato:
        logger.info(
            "Formalizando contratação – compra_id=%s numero=%s",
            command.compra_id,
            command.numero,
        )

        compra = self._compras.get_by_id(command.compra_id)
        if compra is None or compra.foi_excluido():
            raise CompraNaoEncontradaError(
                f"Compra {command.compra_id} não encontrada"
            )

        # RN-COMPRAS-026: só formaliza compra homologada (ou já contratada).
        if compra.situacao not in self.SITUACOES_ELEGIVEIS:
            raise ValueError(
                "Compra precisa estar HOMOLOGADA para formalizar o contrato "
                "(RN-COMPRAS-026). Situação atual: "
                f"{compra.situacao.value}"
            )

        # Revalida vínculos com os domínios core (integração entre domínios).
        if not self._contratos.exists_processo_documental(
            compra.processo_documental_id
        ):
            raise ProcessoDocumentalNaoEncontradoError(
                f"Processo documental {compra.processo_documental_id} não encontrado"
            )
        if not self._contratos.exists_fornecedor_ativo(compra.fornecedor_id):
            raise FornecedorNaoEncontradoError(
                f"Fornecedor {compra.fornecedor_id} não encontrado ou inativo"
            )
        if not self._contratos.exists_unidade(compra.unidade_id):
            raise UnidadeNaoEncontradaError(
                f"Unidade administrativa {compra.unidade_id} não encontrada"
            )

        # RN-COMPRAS-036: identificação única do número de contrato.
        if self._contratos.exists_numero(command.numero):
            raise ContratoDuplicadoError(
                f"Já existe contrato com numero={command.numero}"
            )

        # Avança a compra para CONTRATADO quando ainda estava HOMOLOGADA.
        avancou_compra = False
        if compra.situacao == SituacaoCompra.HOMOLOGADO:
            compra.alterar_situacao(SituacaoCompra.CONTRATADO, command.usuario_id)
            avancou_compra = True

        contrato = Contrato(
            processo_documental_id=compra.processo_documental_id,
            fornecedor_id=compra.fornecedor_id,
            unidade_id=compra.unidade_id,
            compra_id=compra.id,
            numero=command.numero,
            data_inicio=command.data_inicio,
            data_fim=command.data_fim,
            valor=command.valor,
            objeto=command.objeto,
            situacao=SituacaoContrato.EM_ELABORACAO,
            created_by=command.usuario_id,
        )

        # Assinatura na formalização avança o contrato para ASSINADO.
        if command.data_assinatura is not None:
            if command.usuario_id is None:
                raise ValueError("Data de assinatura exige usuário autenticado")
            contrato.alterar_situacao(SituacaoContrato.ASSINADO, command.usuario_id)

        contrato_salvo = self._contratos.save(contrato)
        if avancou_compra:
            self._compras.update(compra)

        evento = ContratoCriadoEvent(
            contrato_id=contrato_salvo.id,
            numero=contrato_salvo.numero,
            processo_documental_id=contrato_salvo.processo_documental_id,
            fornecedor_id=contrato_salvo.fornecedor_id,
            unidade_id=contrato_salvo.unidade_id,
            situacao=contrato_salvo.situacao.value,
            created_at=contrato_salvo.created_at,
        )
        logger.info("Contratação formalizada: %s", evento)

        return contrato_salvo
